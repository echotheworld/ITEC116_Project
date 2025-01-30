# Laboratory Activity #5: Cloud API Deployment

## 📚 Overview
This project demonstrates the deployment of a FastAPI application to Render, a cloud platform service. It builds upon Laboratory Activity #4, taking the locally developed API and making it accessible worldwide through cloud deployment.

## 🌐 Live API
- **Base URL**: [https://itec116-feolino.onrender.com](https://itec116-feolino.onrender.com)
- **API Documentation**: [https://itec116-feolino.onrender.com/docs](https://itec116-feolino.onrender.com/docs)

## 🎯 Objectives
- Deploy FastAPI application to Render cloud platform
- Configure environment variables in cloud environment
- Implement secure API deployment practices
- Ensure API accessibility and functionality in production

## 🛠 Technical Requirements
- Python 3.7+
- FastAPI
- Render account
- Git repository
- requirements.txt file

## 🚀 Deployment Steps

### 1. Prepare Your Repository
```bash
# Ensure your repository has these files
requirements.txt
main.py
.gitignore
```

### 2. Configure Render
1. Create a new Web Service
2. Connect your GitHub repository
3. Configure the service:
   - Name: `itec116-<surname>`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `fastapi run main.py`

### 3. Set Environment Variables
1. Navigate to Environment in Render dashboard
2. Add your API key:
   ```
   API_KEY=your_api_key_here
   ```

## 📡 API Access

### Base Endpoint
```http
GET https://itec116-<surname>.onrender.com/
```

### Swagger Documentation
```http
GET https://itec116-<surname>.onrender.com/docs
```

### API Versions
1. Version 1 (No Authentication)
```http
GET https://itec116-<surname>.onrender.com/apiv1/
```

2. Version 2 (With Authentication)
```http
GET https://itec116-<surname>.onrender.com/apiv2/
```

## 🔒 Security Considerations
- API Key must be set in Render environment variables
- Never commit sensitive information to repository
- Use HTTPS for all API calls
- Implement proper CORS policies

## 🧪 Testing Deployed API
1. Verify base URL accessibility
2. Test API endpoints through Swagger UI
3. Validate authentication with API key
4. Check environment variable configuration
5. Monitor application logs in Render dashboard

## 💡 Implementation Details
- Cloud platform: Render
- Automatic deployments from Git
- Environment variable management
- Production-grade server configuration
- Secure HTTPS endpoints

## ⚙️ Technical Architecture
The deployment utilizes:
- Render's Web Service platform
- Git-based deployment
- Environment variable management
- Automatic HTTPS/SSL
- Production-ready server configuration

## 🔍 Monitoring and Maintenance
- Monitor application logs
- Track API performance
- Monitor error rates
- Check resource usage
- Review security alerts

## 👨‍💻 Development Best Practices
- Use version control
- Implement CI/CD
- Secure environment variables
- Regular monitoring
- Proper documentation

## 🚨 Troubleshooting
1. Check Render logs for deployment issues
2. Verify environment variables
3. Ensure requirements.txt is complete
4. Validate API key configuration
5. Check application startup logs

## 📝 License
This project is created as part of ITEC116 coursework.

---

<div align="center">
Made with ❤️ for ITEC116 Laboratory Activity 5
</div> 
