# Sansims Flask Website

A professional 3-page Flask website showcasing the Sansims educational technology project.

## File Structure

```
sansims-website/
│
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
├── static/
│   └── css/
│       └── style.css              # Main stylesheet
│
└── templates/
    ├── base.html                  # Base template with navigation/footer
    ├── home.html                  # Page 1: The Impact Story
    ├── solution.html              # Page 2: The Solution
    └── technology.html            # Page 3: Technology & Traction
```

## Installation

1. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

4. **Open in browser:**
   Navigate to `http://localhost:5000`

## Pages Overview

### Page 1: Home (The Impact Story)
- **Route:** `/`
- **Focus:** Problem statement and economic impact
- **Design:** Gradient background with bold statistics
- **Key Sections:**
  - Hero with device illustration
  - Problem statistics (85% schools lacking labs)
  - Economic comparison (40M vs 2.5M UGX)
  - Mission statement
  - Quick stats banner

### Page 2: Solution (What We Built)
- **Route:** `/solution`
- **Focus:** Technical solution and content pillars
- **Design:** Teal/green accents, card-based layout
- **Key Sections:**
  - Sansim device features
  - Smartphone advantage
  - Three content pillars (AI, Luganda, Simulations)
  - How it works workflow
  - Development timeline

### Page 3: Technology (Credibility & Traction)
- **Route:** `/technology`
- **Focus:** Technical architecture and readiness
- **Design:** Blue accents, structured technical details
- **Key Sections:**
  - Content-first development approach
  - ESP32 architecture benefits
  - Complete technology stack
  - Development milestones (checkmarks)
  - Next steps and impact potential
  - Contact/partnership CTAs

## Design Principles

- **Scandinavian minimalism** with generous white space
- **Mobile-first responsive** design
- **Single accent color** (orange #ff6b35) for CTAs
- **Clean typography** with Inter/system fonts
- **Distinct visual identity** per page
- **Professional photography-ready** layout
- **UGX currency** throughout

## Customization

### Colors
Main accent color is defined in `style.css`:
- Primary: `#ff6b35` (Orange)
- Secondary: `#4299e1` (Blue)
- Success: `#38b2ac` (Teal)

### Content
Edit the HTML files in the `templates/` folder to update content.

### Styling
Modify `static/css/style.css` for design changes.

## Production Deployment

For production, consider:
- Setting `debug=False` in `app.py`
- Using a production WSGI server (Gunicorn, uWSGI)
- Adding environment variables for configuration
- Implementing proper error handling
- Adding analytics tracking
- Optimizing images and assets

## Contact

Primary Developer: Steven Nakibinge  
Email: contact@sansims.org

---

**Mission:** Democratizing programming education for millions of African students previously excluded by infrastructure limitations.