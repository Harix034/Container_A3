# Web Service and Load Balancer

## Summary
This project contains two Docker containers:
1. **Web Service**: 
2. **Load Balancer**

## Setup 

### How to Run
1. download the project.
2. Open a terminal and navigate to the project directory.
3. Run the following command to build and start the containers:
   docker-compose up --build

## Changes in Assignment 3

For Assignment 3, the following changes and improvements were made:
1. **Environment Variable Integration**:
   - Added a `.env` file to define environment variables.
   - Passed the `MESSAGE` variable from the `.env` file to the `web_service` and `load_balancer` containers.
   - The `web_service` now reads the `MESSAGE` variable and returns it when accessed via HTTP.

2. **Echo Service Using BusyBox**:
   - The BusyBox container reads the `MESSAGE` variable and prints it to the console using an echo command.
   - **Reason for Choosing BusyBox**:
     - **Lightweight**: BusyBox is a highly efficient, small-footprint image ideal for simple tasks like environment variable testing.
     - **Ease of Use**: Demonstrates how containers can execute lightweight tasks without requiring complex configurations.

5. **Updated README**:
   - Added detailed instructions on how to set up the project, run it, and modify it as needed.




