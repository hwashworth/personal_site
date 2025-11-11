# Hunter Ashworth's Personal Portfolio

This repository contains the source code for my personal portfolio website, `hwashworth.com`.

The site itself is a live, deployed project demonstrating a complete, automated CI/CD pipeline.

**Live URL:** [https://hwashworth.com](https://hwashworth.com)

---

## Project Overview

This is a simple Python/Flask web application that serves as my professional portfolio. The main purpose of this project is to serve as a real-world example of an automated deployment pipeline, bridging the gap between development (the code) and operations (the infrastructure).

## CI/CD Pipeline & Technologies

This project demonstrates a full "Git-to-production" workflow.

* **Application:** The website is a lightweight **Python** app using the **Flask** framework.
* **Source Control:** All code is hosted on **GitHub**.
* **CI/CD:** A **GitHub Actions** workflow is configured to trigger on every `git push` to the `main` branch.
* **Deployment:** The GitHub Actions workflow automatically packages and deploys the new version of the application to **AWS Elastic Beanstalk**.
* **DNS:** **AWS Route 53** manages the custom domain name.
* **Security:** The site is secured with HTTPS, using a free certificate from **AWS Certificate Manager (ACM)**.



---

## How to Run Locally

1.  Clone this repository:
    ```bash
    git clone [https://github.com/hwashworth/personal_site.git](https://github.com/hwashworth/personal_site.git)
    cd personal_site
    ```

2.  Create and activate a Python virtual environment:
    ```bash
    # On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    
    # On Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4.  Run the Flask application:
    ```bash
    flask run
    ```
    The application will be available at `http://127.0.0.1:5000`.