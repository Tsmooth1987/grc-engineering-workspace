# Your 4-Week Python for GRC Study Plan

**Goal:** Go from zero Python knowledge to writing basic GRC automation scripts.

**Method:** Each week introduces new concepts, building on the last, and ends with a small, practical exercise to reinforce your learning.

### A Quick Note: Your Computer and the AWS Cloud (Like Talking to a Big Robot!)

Think of the **AWS Console** (the website where you click around) as a big TV screen showing you all your toys in the cloud. You can see your S3 buckets, users, and everything else.

The **AWS CLI** (the command line tool) is like a magic remote control. When you type a command, you're telling the big robot in the cloud what to do. When you told it to build an S3 bucket, it did, and you could see the new bucket appear on your TV screen (the Console).

**Python scripts** are like teaching the remote control a new trick. Soon, we'll teach Python how to use the remote control all by itself. When a Python script runs, it will use the same magic remote to talk to the big robot. So, anything your script builds or changes will also show up on your TV screen.

**Everything is connected!** The Console, the CLI, and your Python scripts are just different ways of talking to the same AWS cloud.

---

### Week 1: Python Fundamentals & Environment Setup

*   **Objective:** Get your computer ready for development and learn the absolute basics of Python programming.
*   **Topics:**
    *   **Day 1-2: Setup:** Read "Setting Up Your Python Environment" in `Section3.md`. Install Visual Studio Code (a great, free IDE) and Python 3.11+. Practice running a simple `print("Hello, GRC!")` command.
    *   **Day 3: Variables & Data Types:** Learn about storing information in variables (e.g., `finding_severity = "High"`) and the basic data types: strings, integers, and booleans.
    *   **Day 4-5: Logic & Control Flow:** Understand conditional statements (`if`, `else`) to make decisions in your code.
    *   **Day 6: Weekly Exercise:** Write a script that checks a hypothetical risk score. If the score is above 75, print "High Risk"; otherwise, print "Acceptable Risk."
    *   **Day 7: Rest & Review.**

### Week 2: Core Python Constructs

*   **Objective:** Learn how to handle collections of data and repeat tasks automatically.
*   **Topics:**
    *   **Day 1-2: Lists & Loops:** Learn about Python lists to store multiple items (e.g., a list of compliance findings). Use `for` loops to iterate over them.
    *   **Day 3-4: Dictionaries:** Understand dictionaries for storing key-value data, which is perfect for representing structured data like an AWS resource's tags.
    *   **Day 5: Functions:** Learn to write functions to create reusable blocks of code for common tasks (e.g., a function to process a single compliance finding).
    *   **Day 6: Weekly Exercise:** Create a list of dictionaries, where each dictionary represents a server with a `name` and an `is_patched` status (True/False). Write a script that loops through the list and prints the names of the unpatched servers.
    *   **Day 7: Rest & Review.**

### Week 3: Working with the Outside World

*   **Objective:** Learn how to manage project dependencies and interact with files.
*   **Topics:**
    *   **Day 1-2: Virtual Environments:** Learn why and how to create isolated environments for your projects to manage dependencies cleanly.
    *   **Day 3: Dependency Management:** Understand the purpose of a `requirements.txt` file for ensuring your scripts are reproducible.
    *   **Day 4-5: Reading & Writing Files:** Practice opening, reading from, and writing to text files—an essential skill for generating reports.
    *   **Day 6: Weekly Exercise:** Modify last week's exercise. Instead of printing to the console, write the names of the unpatched servers to a report file named `unpatched_servers.txt`.
    *   **Day 7: Rest & Review.**

### Week 4: Introduction to GRC Libraries

*   **Objective:** Get a taste of the powerful libraries mentioned in the chapter.
*   **Topics:**
    *   **Day 1-2: Introduction to `boto3`:** `boto3` is the AWS SDK. We'll start simple: write a script to list your S3 buckets. This will require setting up AWS credentials on your machine.
    *   **Day 3-4: Introduction to `pandas`:** `pandas` is for data analysis. Learn how to create a simple DataFrame (like a spreadsheet) from the list of servers you created in Week 2 and export it to a CSV file.
    *   **Day 5: Introduction to `logging`:** Learn how to add basic logging to your scripts to record actions and errors, which is crucial for creating auditable evidence.
    *   **Day 6: Weekly Exercise:** Combine everything. Write a script that:
        1.  Uses `boto3` to get a list of 5-10 real S3 buckets from your AWS account.
        2.  Uses `pandas` to put that list into a DataFrame.
        3.  Exports the DataFrame to a `s3_inventory.csv` file.
        4.  Uses the `logging` module to log messages like "Script started," "Fetching S3 buckets," and "Report generated successfully."
    *   **Day 7: Rest & Plan Next Steps!**

---

## Post-Study Projects

After completing the 4-week study plan, you can apply your skills to build these real-world GRC automation tools from scratch.

*   **Project 1: S3 Bucket Auditor**
    *   Audits S3 buckets for versioning and public access block status.
    *   Generates a professional log file and a final CSV report.
    *   *Skills Used: `boto3`, `pandas`, `logging`, File I/O, Error Handling.*

*   **Project 2: IAM MFA Auditor**
    *   Audits IAM users for MFA status.
    *   Demonstrated the full development lifecycle: build, test with live data, and clean up.
    *   *Skills Used: `boto3`, `pandas`, `logging`, AWS CLI.*

*   **Project 3: EC2 Security Group Auditor**
    *   Audits EC2 security groups for risky rules (e.g., SSH open to the world).
    *   Parses complex JSON responses from the AWS API.
    *   *Skills Used: `boto3` (EC2), `pandas`, `logging`, AWS CLI.*

*   **Project 4: IAM Policy Auditor**
    *   Audits custom IAM policies for full administrator access (`Allow`, `*`, `*`).
    *   Performs multi-step API calls and advanced JSON parsing.
    *   *Skills Used: `boto3` (IAM), `pandas`, `logging`, `json`, AWS CLI.*

*   **Project 5: S3 Auto-Remediator**
    *   Enhances the S3 auditor to automatically enable versioning on non-compliant buckets.
    *   Implements a critical `--dry-run` safety feature.
    *   *Skills Used: `boto3` (S3 write operations), `argparse`, professional automation workflow.*

*   **Project 6: GRC Alerter**
    *   Integrates an auditor with AWS Simple Notification Service (SNS) to send email alerts.
    *   Creates a proactive, event-driven security tool.
    *   *Skills Used: `boto3` (SNS), AWS CLI, multi-service integration.*

*   **Project 7: EBS Volume Remediator**
    *   Audits for and automatically deletes old, unattached EBS volumes to reduce costs and attack surface.
    *   Implements a robust `--dry-run` mode for safe operations.
    *   *Skills Used: `boto3` (EC2), `pandas`, `logging`, `argparse`, professional automation workflow.*
