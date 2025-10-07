from flask import Flask, render_template, request, jsonify
from cno_product_advisor import CNOProductAdvisor
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('advisor.html')

@app.route('/submit_consultation', methods=['POST'])
def submit_consultation():
    try:
        data = request.json
        
        # Create advisor instance
        advisor = CNOProductAdvisor()
        
        # Set user responses from form data
        advisor.user_responses = {
            'age_range': data.get('age_range'),
            'employment_status': data.get('employment_status'),
            'coverage_interests': data.get('coverage_interests', []),
            'has_dependents': data.get('has_dependents'),
            'coverage_channel': data.get('coverage_channel'),
            'priority': data.get('priority')
        }
        
        # Analyze and get recommendations
        advisor.analyze_responses()
        
        # Format recommendations for UI
        recommendations = []
        for brand, score in advisor.recommended_brands:
            brand_data = advisor.products[brand]
            user_coverage = advisor.user_responses.get('coverage_interests', [])
            
            # Get relevant products
            relevant_products = []
            for category in brand_data['categories']:
                if (category in user_coverage or 
                    (category == 'life' and 'life' in user_coverage) or
                    (category == 'health' and 'health' in user_coverage) or
                    (category == 'supplemental' and 'supplemental' in user_coverage) or
                    (category == 'retirement' and 'retirement' in user_coverage) or
                    (category == 'employee_benefits' and 'employee_benefits' in user_coverage)):
                    relevant_products = brand_data['products']
                    break
            
            if not relevant_products and score >= 3:
                relevant_products = brand_data['products']
            
            recommendations.append({
                'brand': brand,
                'score': score,
                'products': relevant_products
            })
        
        return jsonify({
            'success': True,
            'recommendations': recommendations
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)