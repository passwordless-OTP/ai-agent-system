#!/usr/bin/env python3

import os
import re
import json
from pathlib import Path
from datetime import datetime

class CodebaseEnhancer:
    def __init__(self, workspace_path="."):
        self.workspace = Path(workspace_path)
        self.enhancement_log = []
        self.file_analysis = {}
    
    def enhance_all_files(self):
        """Add comprehensive AI context to all source files"""
        print("🔧 Enhancing codebase with AI context...")
        
        # Enhance PHP files
        php_files = list(self.workspace.glob("app/**/*.php"))
        for i, php_file in enumerate(php_files, 1):
            print(f"  [{i}/{len(php_files)}] {php_file}")
            self.enhance_php_file(php_file)
        
        # Enhance configuration files
        config_files = list(self.workspace.glob("config/*.php"))
        for config_file in config_files:
            self.enhance_config_file(config_file)
        
        # Create AI-specific documentation
        self.create_ai_documentation()
        
        # Generate enhancement report
        self.generate_enhancement_report()
        
        print(f"✅ Enhanced {len(self.enhancement_log)} files")
    
    def enhance_php_file(self, file_path):
        """Add comprehensive AI comments to PHP file"""
        try:
            content = file_path.read_text()
            
            # Skip if already enhanced
            if "AGENT_ENHANCED" in content:
                return
            
            # Analyze file structure
            analysis = self.analyze_php_file(content, file_path)
            self.file_analysis[str(file_path)] = analysis
            
            # Generate comprehensive AI header
            ai_header = self.generate_ai_header(analysis, file_path)
            
            # Insert AI header after <?php
            enhanced_content = re.sub(
                r'^(<\?php\s*)',
                rf'\1\n{ai_header}\n',
                content,
                flags=re.MULTILINE
            )
            
            # Write enhanced version
            file_path.write_text(enhanced_content)
            self.enhancement_log.append(str(file_path))
            
        except Exception as e:
            print(f"  ⚠️ Failed to enhance {file_path}: {e}")
    
    def analyze_php_file(self, content, file_path):
        """Deep analysis of PHP file for AI context"""
        
        # Extract classes
        classes = re.findall(r'class\s+(\w+)', content)
        
        # Extract methods
        methods = re.findall(r'public\s+function\s+(\w+)', content)
        
        # Find dependencies (use statements)
        dependencies = re.findall(r'use\s+([\w\\\\]+)', content)
        
        # Detect patterns
        has_database = bool(re.search(r'(Model|DB::|Eloquent)', content))
        has_api = bool(re.search(r'(Request|Response|Controller)', content))
        has_shopify = bool(re.search(r'(Shopify|Shop::|shopify)', content, re.IGNORECASE))
        has_geolocation = bool(re.search(r'(geoip|country|location|ip)', content, re.IGNORECASE))
        
        return {
            'file_type': self.determine_file_type(file_path),
            'classes': classes,
            'methods': methods,
            'dependencies': dependencies,
            'patterns': {
                'database': has_database,
                'api': has_api,
                'shopify': has_shopify,
                'geolocation': has_geolocation
            },
            'complexity': self.estimate_complexity(content),
            'line_count': len(content.splitlines())
        }
    
    def determine_file_type(self, file_path):
        """Determine the type and role of the PHP file"""
        path_str = str(file_path).lower()
        
        if 'controller' in path_str:
            return {'layer': 'Controller', 'description': 'HTTP request handling and business logic coordination'}
        elif 'model' in path_str:
            return {'layer': 'Model', 'description': 'Data model and database interaction'}
        elif 'helper' in path_str:
            return {'layer': 'Helper', 'description': 'Utility functions and business logic support'}
        elif 'service' in path_str:
            return {'layer': 'Service', 'description': 'Business service and external API integration'}
        elif 'job' in path_str:
            return {'layer': 'Job', 'description': 'Background job processing and queued tasks'}
        elif 'middleware' in path_str:
            return {'layer': 'Middleware', 'description': 'Request/response filtering and processing'}
        elif 'provider' in path_str:
            return {'layer': 'Provider', 'description': 'Service provider and dependency injection'}
        elif 'command' in path_str:
            return {'layer': 'Command', 'description': 'Artisan console command'}
        else:
            return {'layer': 'Utility', 'description': 'General utility and support functions'}
    
    def estimate_complexity(self, content):
        """Estimate code complexity based on various factors"""
        lines = len(content.splitlines())
        
        # Count complexity indicators
        method_count = len(re.findall(r'function\s+\w+', content))
        if_count = len(re.findall(r'\bif\s*\(', content))
        loop_count = len(re.findall(r'\b(for|while|foreach)\s*\(', content))
        try_count = len(re.findall(r'\btry\s*{', content))
        
        complexity_score = (method_count * 2) + if_count + (loop_count * 2) + (try_count * 3)
        
        if lines < 50 and complexity_score < 10:
            return 'Low'
        elif lines < 200 and complexity_score < 30:
            return 'Medium'
        else:
            return 'High'
    
    def generate_ai_header(self, analysis, file_path):
        """Generate comprehensive AI header for file"""
        file_type = analysis['file_type']
        patterns = analysis['patterns']
        
        # Generate pattern descriptions
        pattern_descriptions = []
        if patterns['database']:
            pattern_descriptions.append('Database interactions')
        if patterns['api']:
            pattern_descriptions.append('API endpoint handling')
        if patterns['shopify']:
            pattern_descriptions.append('Shopify integration')
        if patterns['geolocation']:
            pattern_descriptions.append('Geolocation services')
        
        # Find related test files
        test_file = self.find_test_file(file_path)
        
        return f"""// AGENT_ENHANCED: Comprehensive AI context auto-generated
// AGENT_MODULE: {file_type['description']}
// AGENT_LAYER: {file_type['layer']}
// AGENT_COMPLEXITY: {analysis['complexity']} ({analysis['line_count']} lines, {len(analysis['methods'])} methods)
// AGENT_DEPENDENCIES: {', '.join(analysis['dependencies'][:5]) if analysis['dependencies'] else 'None detected'}
// AGENT_PATTERNS: {', '.join(pattern_descriptions) if pattern_descriptions else 'Standard business logic'}
// AGENT_CLASSES: {', '.join(analysis['classes']) if analysis['classes'] else 'No classes'}
// AGENT_PUBLIC_METHODS: {', '.join(analysis['methods'][:5]) if analysis['methods'] else 'No public methods'}
// AGENT_TEST_COVERAGE: {test_file if test_file else 'No test file found'}
// AGENT_RECENT_CHANGES: Enhanced for AI agent context ({self.get_current_date()})
// AGENT_MAINTENANCE_NOTES: Auto-generated AI context - update when major changes occur
// AGENT_INTEGRATION_POINTS: {self.identify_integration_points(analysis)}
// AGENT_SECURITY_CONTEXT: {self.assess_security_relevance(analysis)}
// AGENT_PERFORMANCE_NOTES: {self.assess_performance_relevance(analysis)}"""
    
    def find_test_file(self, source_file):
        """Find corresponding test file"""
        source_path = Path(source_file)
        class_name = source_path.stem
        
        possible_test_paths = [
            f"tests/Feature/{class_name}Test.php",
            f"tests/Unit/{class_name}Test.php",
            f"tests/Feature/Http/Controllers/{class_name}Test.php"
        ]
        
        for test_path in possible_test_paths:
            if Path(test_path).exists():
                return test_path
        
        return "No corresponding test file found"
    
    def identify_integration_points(self, analysis):
        """Identify key integration points"""
        points = []
        
        if analysis['patterns']['shopify']:
            points.append('Shopify API')
        if analysis['patterns']['geolocation']:
            points.append('Geolocation services')
        if analysis['patterns']['database']:
            points.append('Database layer')
        if analysis['patterns']['api']:
            points.append('REST API endpoints')
        
        return ', '.join(points) if points else 'Internal business logic'
    
    def assess_security_relevance(self, analysis):
        """Assess security relevance of the file"""
        if analysis['patterns']['api']:
            return 'High - API endpoints require authentication and input validation'
        elif analysis['patterns']['database']:
            return 'Medium - Database operations require SQL injection protection'
        elif analysis['patterns']['shopify']:
            return 'High - Shopify integration requires webhook validation and secure tokens'
        else:
            return 'Standard - Follow general security practices'
    
    def assess_performance_relevance(self, analysis):
        """Assess performance implications"""
        if analysis['patterns']['database']:
            return 'Database queries should be optimized and use appropriate indexing'
        elif analysis['patterns']['api']:
            return 'API responses should be cached when appropriate'
        elif analysis['patterns']['geolocation']:
            return 'Geolocation lookups should be cached to avoid service limits'
        else:
            return 'Standard performance considerations apply'
    
    def get_current_date(self):
        """Get current date for timestamps"""
        return datetime.now().strftime('%Y-%m-%d')
    
    def enhance_config_file(self, file_path):
        """Add AI context to configuration files"""
        try:
            content = file_path.read_text()
            
            if "AGENT_ENHANCED" in content:
                return
            
            config_header = f"""<?php

// AGENT_ENHANCED: Configuration file with AI context
// AGENT_MODULE: Application configuration for {file_path.stem}
// AGENT_LAYER: Configuration
// AGENT_PURPOSE: System configuration and environment-specific settings
// AGENT_SECURITY_NOTE: Contains sensitive configuration - review before committing
// AGENT_RECENT_CHANGES: Enhanced for AI agent context ({self.get_current_date()})

"""
            
            # Replace opening PHP tag with enhanced header
            enhanced_content = re.sub(r'^<\?php\s*', config_header, content, flags=re.MULTILINE)
            
            file_path.write_text(enhanced_content)
            self.enhancement_log.append(str(file_path))
            
        except Exception as e:
            print(f"  ⚠️ Failed to enhance config {file_path}: {e}")
    
    def create_ai_documentation(self):
        """Create AI-specific documentation structure"""
        ai_docs_dir = Path('.ai-enhanced/docs')
        ai_docs_dir.mkdir(parents=True, exist_ok=True)
        
        # Create AI context map
        context_map = {
            'enhancement_timestamp': self.get_current_date(),
            'total_files_enhanced': len(self.enhancement_log),
            'file_analysis_summary': self.summarize_file_analysis(),
            'ai_navigation_hints': self.generate_navigation_hints()
        }
        
        with open(ai_docs_dir / 'ai_context_map.json', 'w') as f:
            json.dump(context_map, f, indent=2)
        
        # Create human-readable AI guide
        ai_guide = f"""# AI Agent Context Guide

Generated: {self.get_current_date()}

## Enhanced Files Summary
- Total files enhanced: {len(self.enhancement_log)}
- Controllers: {len([f for f in self.enhancement_log if 'Controller' in f])}
- Models: {len([f for f in self.enhancement_log if 'Model' in f])}
- Helpers: {len([f for f in self.enhancement_log if 'Helper' in f])}

## AI Navigation Quick Start
1. Look for `AGENT_MODULE` comments at the top of each file
2. Use `AGENT_DEPENDENCIES` to understand file relationships
3. Check `AGENT_COMPLEXITY` to estimate modification effort
4. Review `AGENT_PATTERNS` to understand functional areas

## Key Integration Points
{self.generate_integration_summary()}

## AI Agent Usage Instructions
1. Start with high-level controllers for API understanding
2. Follow dependency chains through models and helpers
3. Check test coverage before making changes
4. Update AGENT_RECENT_CHANGES when modifying files
"""
        
        with open(ai_docs_dir / 'AI_AGENT_GUIDE.md', 'w') as f:
            f.write(ai_guide)
    
    def summarize_file_analysis(self):
        """Create summary of file analysis"""
        summary = {
            'total_files': len(self.file_analysis),
            'complexity_distribution': {'Low': 0, 'Medium': 0, 'High': 0},
            'pattern_usage': {'database': 0, 'api': 0, 'shopify': 0, 'geolocation': 0},
            'layer_distribution': {}
        }
        
        for file_path, analysis in self.file_analysis.items():
            # Complexity distribution
            summary['complexity_distribution'][analysis['complexity']] += 1
            
            # Pattern usage
            for pattern, used in analysis['patterns'].items():
                if used:
                    summary['pattern_usage'][pattern] += 1
            
            # Layer distribution
            layer = analysis['file_type']['layer']
            summary['layer_distribution'][layer] = summary['layer_distribution'].get(layer, 0) + 1
        
        return summary
    
    def generate_navigation_hints(self):
        """Generate navigation hints for AI agents"""
        hints = []
        
        # Find entry points
        controllers = [f for f in self.file_analysis.keys() if 'Controller' in f]
        if controllers:
            hints.append(f"Start with controllers: {controllers[:3]}")
        
        # Find core models
        models = [f for f in self.file_analysis.keys() if 'Model' in f]
        if models:
            hints.append(f"Core data models: {models[:3]}")
        
        # Find utility helpers
        helpers = [f for f in self.file_analysis.keys() if 'Helper' in f]
        if helpers:
            hints.append(f"Business logic helpers: {helpers[:3]}")
        
        return hints
    
    def generate_integration_summary(self):
        """Generate integration points summary"""
        shopify_files = [f for f, a in self.file_analysis.items() if a['patterns']['shopify']]
        geo_files = [f for f, a in self.file_analysis.items() if a['patterns']['geolocation']]
        api_files = [f for f, a in self.file_analysis.items() if a['patterns']['api']]
        
        summary = []
        if shopify_files:
            summary.append(f"- **Shopify Integration**: {len(shopify_files)} files")
        if geo_files:
            summary.append(f"- **Geolocation Services**: {len(geo_files)} files")
        if api_files:
            summary.append(f"- **API Endpoints**: {len(api_files)} files")
        
        return '\n'.join(summary) if summary else "- Standard Laravel application structure"
    
    def generate_enhancement_report(self):
        """Generate comprehensive enhancement report"""
        report_dir = Path('.ai-enhanced/reports')
        report_dir.mkdir(parents=True, exist_ok=True)
        
        report = {
            'enhancement_date': self.get_current_date(),
            'files_processed': len(self.enhancement_log),
            'analysis_summary': self.summarize_file_analysis(),
            'enhancement_log': self.enhancement_log,
            'next_steps': [
                'Review generated AI comments for accuracy',
                'Update any incorrect AGENT_* annotations',
                'Add specific business context where needed',
                'Ensure test coverage is documented correctly'
            ]
        }
        
        with open(report_dir / 'enhancement_report.json', 'w') as f:
            json.dump(report, f, indent=2)

if __name__ == '__main__':
    enhancer = CodebaseEnhancer()
    enhancer.enhance_all_files()