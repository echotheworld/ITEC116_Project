# Laboratory Activity #5: Deploying API in Cloud ☁️

Final implementation demonstrating cloud deployment of Lab 4's API to Render platform.

## 🎯 Objectives

- Develop and deploy API to a cloud platform

## 📋 Requirements

### Deployment Specifications
- Platform: Render
- Domain Format: `itec116_<surname>.onrender.com`
- API Key Configuration: Must match Lab 4's implementation

### Required Components
- Deployed API from Lab 4
- Environment Variables Configuration
- API Documentation
- Secure Authentication Setup

## 🚀 Deployment Steps

1️⃣ **Prepare Your Repository**
```bash
git clone https://github.com/echotheworld/ITEC116_Project.git
cd ITEC116_Project
cd Lab5
```

2️⃣ **Configure Render**
1. Create a Render account
2. Connect your GitHub repository
3. Create a new Web Service
4. Select the Python environment
5. Configure environment variables:
   - Add your API key (from Lab 4)
   - Set Python version
   - Configure start command

⚠️ **Important**: Never commit sensitive information like API keys to your repository

## 🌐 Access Points

### Base URL
```
https://itec116-feolino.onrender.com/
```

### API Documentation
```
https://itec116-feolino.onrender.com/docs
```

## 🔑 Environment Setup

Configure the following in Render's environment variables:
- `API_KEY`: Your secure API key (same as Lab 4)
- `PYTHON_VERSION`: "3.8" or higher
- `PORT`: "8000"

## 📝 Required Output

1. Deployed API Link
   - Format: `itec116_<surname>.onrender.com`
   - Must be accessible and functional

2. API Key (submitted privately)
   - Must match the key used in Lab 4
   - Must be properly configured in Render

---

<div align="center">
Made with ❤️ for ITEC116 Course
</div> 
