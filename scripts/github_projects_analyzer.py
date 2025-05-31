#!/usr/bin/env python3

import os
import requests
import json
from datetime import datetime

class GitHubProjectsAnalyzer:
    def __init__(self):
        self.github_token = os.getenv('GITHUB_TOKEN')
        self.repo = self.detect_repository()
        self.headers = {
            'Authorization': f'token {self.github_token}',
            'Accept': 'application/vnd.github.v3+json'
        } if self.github_token else {}
    
    def detect_repository(self):
        """Auto-detect repository from git remote"""
        try:
            import subprocess
            result = subprocess.run(['git', 'remote', 'get-url', 'origin'], 
                                  capture_output=True, text=True)
            if result.returncode == 0:
                url = result.stdout.strip()
                # Extract owner/repo from GitHub URL
                if 'github.com' in url:
                    parts = url.replace('.git', '').split('/')
                    return f"{parts[-2]}/{parts[-1]}"
        except:
            pass
        
        # Default fallback
        return 'otpplus/securify'
    
    def analyze_projects(self):
        """Analyze GitHub Projects and Issues for AI task discovery"""
        if not self.github_token:
            print("⚠️ GITHUB_TOKEN not available - using mock analysis")
            return self.create_mock_analysis()
        
        try:
            # Get repository issues
            issues_url = f'https://api.github.com/repos/{self.repo}/issues'
            params = {'state': 'open', 'per_page': 50}
            
            response = requests.get(issues_url, headers=self.headers, params=params)
            
            if response.status_code == 200:
                issues = response.json()
                return self.analyze_issues(issues)
            else:
                print(f"⚠️ GitHub API error: {response.status_code}")
                return self.create_mock_analysis()
                
        except Exception as e:
            print(f"⚠️ GitHub analysis failed: {e}")
            return self.create_mock_analysis()
    
    def analyze_issues(self, issues):
        """Analyze issues for AI readiness"""
        analysis = {
            'timestamp': datetime.now().isoformat(),
            'repository': self.repo,
            'total_issues': len(issues),
            'ai_ready_tasks': [],
            'priority_distribution': {'high': 0, 'medium': 0, 'low': 0},
            'complexity_distribution': {'low': 0, 'medium': 0, 'high': 0, 'unknown': 0}
        }
        
        for issue in issues:
            labels = [label['name'].lower() for label in issue.get('labels', [])]
            
            # Check if AI-ready
            if self.is_ai_ready(issue, labels):
                task = {
                    'issue_number': issue['number'],
                    'title': issue['title'],
                    'labels': labels,
                    'priority': self.extract_priority(labels),
                    'complexity': self.extract_complexity(labels),
                    'readiness_score': self.calculate_readiness_score(issue, labels),
                    'assignee': issue.get('assignee', {}).get('login') if issue.get('assignee') else None,
                    'url': issue['html_url']
                }
                analysis['ai_ready_tasks'].append(task)
            
            # Update distributions
            priority = self.extract_priority(labels)
            analysis['priority_distribution'][priority] += 1
            
            complexity = self.extract_complexity(labels)
            analysis['complexity_distribution'][complexity] += 1
        
        # Sort AI-ready tasks by readiness score
        analysis['ai_ready_tasks'].sort(key=lambda x: x['readiness_score'], reverse=True)
        
        return analysis
    
    def is_ai_ready(self, issue, labels):
        """Determine if issue is ready for AI processing"""
        # Check for blocking conditions
        blocking_labels = ['needs discussion', 'blocked', 'waiting for input']
        if any(label in labels for label in blocking_labels):
            return False
        
        # Check for AI-ready indicators
        ai_ready_labels = ['good first issue', 'help wanted', 'bug', 'ai-agent-ready']
        if any(label in labels for label in ai_ready_labels):
            return True
        
        # Check for clear description
        body = issue.get('body', '') or ''
        if len(body) > 100:
            return True
        
        return False
    
    def extract_priority(self, labels):
        """Extract priority from labels"""
        if any('high priority' in label or 'critical' in label for label in labels):
            return 'high'
        elif any('medium priority' in label for label in labels):
            return 'medium'
        elif any('low priority' in label for label in labels):
            return 'low'
        else:
            return 'medium'  # Default
    
    def extract_complexity(self, labels):
        """Extract complexity from labels"""
        if any('complexity-low' in label for label in labels):
            return 'low'
        elif any('complexity-medium' in label for label in labels):
            return 'medium'
        elif any('complexity-high' in label for label in labels):
            return 'high'
        else:
            return 'unknown'
    
    def calculate_readiness_score(self, issue, labels):
        """Calculate AI readiness score"""
        score = 50  # Base score
        
        # Label bonuses
        if 'good first issue' in labels:
            score += 20
        if 'ai-agent-ready' in labels:
            score += 25
        if 'bug' in labels:
            score += 15
        if 'enhancement' in labels:
            score += 10
        
        # Complexity bonuses (easier = higher score)
        if 'complexity-low' in labels:
            score += 20
        elif 'complexity-medium' in labels:
            score += 10
        
        # Description quality
        body = issue.get('body', '') or ''
        if len(body) > 200:
            score += 15
        
        # Assignee status
        if not issue.get('assignee'):
            score += 10
        
        return min(score, 100)
    
    def create_mock_analysis(self):
        """Create mock analysis when GitHub API is not available"""
        return {
            'timestamp': datetime.now().isoformat(),
            'repository': self.repo,
            'total_issues': 2,
            'ai_ready_tasks': [
                {
                    'issue_number': 154,
                    'title': 'Flipping Securify endpoints',
                    'labels': ['bug', 'high priority', 'internal'],
                    'priority': 'high',
                    'complexity': 'medium',
                    'readiness_score': 85,
                    'assignee': None,
                    'url': f'https://github.com/{self.repo}/issues/154'
                },
                {
                    'issue_number': 151,
                    'title': 'Fake data from demo store for first time install over the dashboard',
                    'labels': ['enhancement', 'high priority'],
                    'priority': 'high',
                    'complexity': 'low',
                    'readiness_score': 90,
                    'assignee': None,
                    'url': f'https://github.com/{self.repo}/issues/151'
                }
            ],
            'priority_distribution': {'high': 2, 'medium': 0, 'low': 0},
            'complexity_distribution': {'low': 1, 'medium': 1, 'high': 0, 'unknown': 0}
        }

if __name__ == '__main__':
    analyzer = GitHubProjectsAnalyzer()
    analysis = analyzer.analyze_projects()
    print(json.dumps(analysis, indent=2))