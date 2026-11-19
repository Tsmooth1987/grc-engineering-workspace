

Section 3: Python for GRC Engineering

Chapter 7: Why Python for GRC?
As a GRC professional, your expertise lies in governance, risk management, and compliance. Not necessarily in software engineering. Yet in modern cloud environments, the ability to automate controls and reports can mean the difference between scrambling through quarterly audits and operating a proactive, continuously assured compliance program. 
That’s why we chose Python: it combines a gentle learning curve with the power to tackle complex AWS integrations and data transformations.
Python’s readability is one of its greatest strengths. Unlike many programming languages that require a strict syntax of brackets, semicolons, or explicit type declarations, Python uses plain‑English keywords and indentation to structure code. For example, a simple for loop in Python looks like:
for record in findings:
    process_record(record)

This readability makes Python constructs, the building blocks of code such as loops, conditional statements (if/else), and function definitions, immediately understandable, even for those new to programming. Later in this chapter, we’ll explain each of these constructs with concrete examples and show how they map to the compliance logic you need.
Beyond readability, Python’s ecosystem includes a vast collection of third‑party libraries and modules that offer pre‑built functionality for almost every task you can imagine. A library is simply a bundle of pre‑written code you can import into your own scripts. For instance:
boto3 is the official AWS SDK for Python. It provides ready‑made classes and methods to call AWS APIs without you having to handle low‑level HTTP requests or authentication details.
pandas is a data‑analysis library that lets you manipulate tables and time series with just a few methods, rather than writing custom parsing code.
logging, part of Python’s standard library, makes it easy to record what your scripts do. Which is an essential capability for audit‑quality evidence.
We will also introduce you to concepts such as virtual environments, which isolate each project’s dependencies, and dependency management via files like requirements.txt. These practices ensure that your automation code remains stable and reproducible over time.
Perhaps most importantly, Python supports rapid prototyping. You can write a script on your laptop to extract CloudTrail events in a few hours, test it locally, and then package it for deployment as an AWS Lambda function the next day. This flexibility lets you validate your ideas quickly, gather feedback from auditors or stakeholders, and iterate on your compliance checks without long development cycles.
Finally, Python is a common lingua franca across DevOps, SecOps, and Audit teams. Because Python code is so widely understood, engineers and compliance professionals can collaborate on the same codebase. This cross‑functional collaboration helps ensure that your compliance scripts evolve in lockstep with infrastructure changes and policy updates.
In the sections that follow, we will unpack each of these ideas in turn. Defining key terms, walking through setup steps, and writing our first simple scripts. By the end of this chapter, you will not only understand why Python is the ideal choice for GRC automation but also feel confident writing and running your first Python code.
After working through Section 3, I highly recommend exploring a Python course on YouTube, Udemy, LinkedIn Learning or any other learning platform to dive much deeper into the concepts we cover in the next three chapters. 
Setting Up Your Python Environment
Before writing any code, you need a stable development environment that will make your life easier and your code more reliable. We'll start by setting up your development workspace, then use it to install Python and configure your project environment. In this section we'll cover:
Choosing and installing an IDE (Integrated Development Environment)
Installing Python 3.11 or later using your IDE's terminal
Creating and activating a virtual environment
Managing dependencies with requirements.txt
Choose and Install Your IDE
An Integrated Development Environment (IDE) is your command center for writing code. Think of it as Microsoft Word for programmers but instead of just editing text, it helps you write code, run programs, debug issues, manage files, and integrate with version control systems like Git. A good IDE will highlight syntax errors before you run your code, suggest completions as you type, and provide built-in terminals so you don't have to constantly switch between applications.
Here are three excellent options for Python GRC work:
VS Code (Recommended for beginners)
Free, lightweight, and works on Windows, Mac, and Linux
Excellent Python support with extensions
Built-in terminal, Git integration, and debugging tools
Download from: code.visualstudio.com
PyCharm Community Edition
Powerful IDE specifically designed for Python development
Advanced refactoring tools, integrated test runner, and smart code completion
Professional version adds database tools and web framework support
Download from: jetbrains.com/pycharm
AI-Assisted Editors (Cursor or Windsurf)
Modern editors with built-in AI assistance
Get code completions, explanations, and help writing boilerplate code
Great for learning as the AI can explain what code does
Download Cursor from: cursor.sh or Windsurf from: codeium.com/windsurf
Install your chosen IDE and take a few minutes to familiarize yourself with the interface. Most importantly, locate the integrated terminal. This is where you'll run all the commands in the following sections.
 In VS Code, open it with View > Terminal. 
In PyCharm, it's typically at the bottom of the screen or accessible via View > Tool Windows > Terminal`.
Install Python 3.11+ Using Your IDE's Terminal
Now we'll use your IDE's terminal to install Python. Most modern systems come with Python pre-installed, but often in older versions. We want Python 3.11 or later for performance improvements and new language features.
Open your IDE's terminal and follow the instructions for your operating system:
Windows: Download and install from python.org, then verify in your terminal:



python --version
# If that doesn't work, try:
python3 --version

Note: During installation from python.org, check "Add Python to PATH"
macOS:
# Install via Homebrew (install Homebrew first from brew.sh if needed):
brew install python@3.11
# Verify installation:
python3.11 --version

You should see output like Python 3.11.x confirming your installation.
Create and Activate a Virtual Environment
A virtual environment is like a private workspace for your project. It keeps your project's Python packages separate from other projects and your system Python, preventing version conflicts and dependency issues.
Create the virtual environment: From your project directory in the IDE terminal:
python3.11 -m venv .venv

This creates a .venv/ folder containing a private Python installation for your project.
Activate the virtual environment:
macOS/Linux:
source .venv/bin/activate

Windows (PowerShell):
.\.venv\Scripts\Activate.ps1

Windows (Command Prompt):
.\.venv\Scripts\activate.bat

You should see (.venv) appear at the beginning of your terminal prompt, indicating you're now using the virtual environment's Python.
Upgrade pip:
pip install --upgrade pip

Configure Your IDE to Use the Virtual Environment
Tell your IDE to use your project's Python interpreter:
VS Code: Press Ctrl+Shift+P, type "Python: Select Interpreter", and choose the one in your .venv folder
PyCharm: Go to File > Settings > Project > Python Interpreter and select the .venv interpreter
Most IDEs will automatically detect and suggest using the virtual environment
Manage Dependencies with requirements.txt
As you install libraries for your GRC projects, record them in a requirements.txt file. This ensures anyone can recreate your exact environment.
Install packages for GRC work:
pip install boto3 pandas pytest requests

Record your dependencies:
pip freeze > requirements.txt

This creates a file like:
boto3==1.31.0
pandas==2.0.1
pytest==7.3.1
requests==2.28.2

Recreate the environment later: On a new machine or when sharing your project:
python3.11 -m venv .venv
source .venv/bin/activate  # or Windows equivalent
pip install --upgrade pip
pip install -r requirements.txt

Final IDE Configuration
Configure your IDE for productive Python development:
Enable auto-formatting: Install and configure black for consistent code style
Set up linting: Use flake8 or pylint to catch common errors
Configure Git integration: Most IDEs have built-in Git support
Install helpful extensions: For VS Code, install the Python extension pack
With your IDE configured, Python installed, a virtual environment activated, and dependencies managed through requirements.txt, you're ready to start building GRC automation tools. Your development environment will now provide syntax highlighting, error detection, and integrated debugging. This will make your coding experience much more productive than working with basic text editors and separate terminals.

Core Language Concepts
In this section we introduce the fundamental building blocks of Python: variables, data types, input/output, control flow, and functions. Mastering these concepts will allow you to translate compliance requirements: 
“loop through each finding,” 
“if encryption is disabled, log an error,” 
“call this API for each resource”
All into working code.
Variables and Data Types
A variable is simply a name bound to a value. Python infers the type automatically, so you do not need to declare types explicitly.
# String
bucket_name = "example-bucket"

# Integer
port = 22

# Float
threshold = 0.75

# Boolean
is_encrypted = False

Common built‑in data types include:
int for whole numbers
float for decimal numbers
str for text
bool for True/False flags
NoneType for “no value” (represented by None)
You can inspect a variable’s type at runtime:
print(type(bucket_name))  # <class 'str'>
print(type(port))         # <class 'int'>


Basic Input and Output
For simple scripts, you can read from standard input or files, and write to the console.
Console output uses print():
print("Processing bucket:", bucket_name)

Reading from a file:
with open("resources.txt", "r") as f:
    lines = f.readlines()
    # lines is now a list of strings

Writing to a file:
with open("report.csv", "w") as f:
    f.write("bucket_name,is_encrypted\n")
    f.write(f"{bucket_name},{is_encrypted}\n")

Later, we’ll replace this simple manual file input/output with pandas for robust CSV and Excel handling.
Control Flow: Making Decisions and Repeating Work
Python uses indentation rather than braces to denote code blocks. Control flow constructs let you direct execution based on conditions or iterate over collections.
if / elif / else
if is_encrypted:
    print("Bucket is secure")
elif port == 22:
    print("SSH port open, consider restricting access")
else:
    print("No immediate issues detected")

Loops
for loops iterate over sequences (lists, tuples, sets, dictionaries):
findings = ["F1", "F2", "F3"]
for finding in findings:
    print("Review finding", finding)

# Print Output
Review finding F1
Review finding F2
Review finding F3



When iterating dictionaries, use .items() for key/value pairs:
tags = {"Owner": "Alice", "Env": "Prod"}
for key, value in tags.items():
    print(f"{key} = {value}")

# Print Output
Owner = Alice
Env = Prod



while loops repeat until a condition becomes false:
counter = 0
while counter < 5:
    print("Counter is", counter)
    counter += 1
# Print Output
Counter is 0
Counter is 1
Counter is 2
Counter is 3
Counter is 4

# Note that the while loop stops at 4 because when counter reaches 5, the condition counter < 5 becomes false and the loop exits.



Use break to exit a loop early and continue to skip to the next iteration.
Defining and Using Functions
Functions group reusable logic, making code easier to test and maintain. In Python, define a function with def, specify parameters, and use return to produce outputs.

def check_encryption(bucket):
    """
    Returns True if bucket is encrypted, False otherwise.
    """
    # Placeholder for actual AWS call
    encrypted = False  # pretend we queried AWS here
    return encrypted

# Call the function
if not check_encryption(bucket_name):
    print(f"Bucket {bucket_name} is not encrypted")

Functions can accept multiple arguments and return multiple values:
def parse_event(event):
    resource = event.get("detail", {}).get("resource")
    status   = event.get("detail", {}).get("status")
    return resource, status

resource_id, status = parse_event(sample_event)


Organizing Code into Modules
As your scripts grow, you will want to split code into multiple files (modules). Suppose you have common routines in utils.py:
# utils.py
def load_json(path):
    import json
    with open(path) as f:
        return json.load(f)

You can then import and use it elsewhere:
# main.py
from utils import load_json
config = load_json("config.json")
print(config)

Use a __main__.py or command‑line parsing libraries (like argparse) to make your script executable.
Putting It All Together: A Simple Compliance Script
Below is a minimal example that reads a JSON file of S3 buckets, checks encryption, and writes a report:
import json

# Function to load bucket data from a JSON file
def load_buckets(path):
    """
    Reads a JSON file containing a list of bucket configurations
    and returns it as a Python list of dictionaries.
    """
    with open(path) as f:
        return json.load(f)

# Function to check whether a bucket has server-side encryption enabled
def check_encryption(bucket):
    """
    Examines the bucket dictionary for the 'ServerSideEncryptionConfiguration' key.
    If that key exists (and is non-null), we consider the bucket encrypted.
    Returns True if encrypted, False otherwise.
    """
    return bucket.get("ServerSideEncryptionConfiguration") is not None

# Main entry point of the script
def main():
    # Load the list of buckets from an input JSON file
    buckets = load_buckets("buckets.json")

    # Open (or create) a CSV file to record encryption status
    with open("encryption_report.csv", "w") as report:
        # Write the header row for the CSV
        report.write("Bucket,Encrypted\n")

        # Iterate over each bucket configuration
        for b in buckets:
            name      = b["Name"]                # Bucket name
            encrypted = check_encryption(b)      # Boolean result of our check

            # Write a line in the CSV: bucket name and True/False
            report.write(f"{name},{encrypted}\n")

            # If the bucket is not encrypted, print a console warning
            # This provides immediate feedback when running the script manually
            if not encrypted:
                print(f"Warning: {name} is not encrypted")

# This conditional ensures that main() only runs when the script is executed directly,
# and not when imported as a module in another script or test suite.
if __name__ == "__main__":
    main()

Explanation of key sections:
Imports: We import Python’s built‑in json module for parsing JSON files into native dictionaries and lists.
load_buckets Function: Encapsulates file reading and JSON parsing. By keeping it here, you can later swap in an AWS S3 read or an API call without changing the rest of the script.
check_encryption Function: Encapsulates the logic that determines compliance (in this case, the presence of a specific configuration). This makes it reusable and easier to test.
main Function: Manages the overall workflow:
Loads input data
Opens a report file and writes headers
Loops through each bucket, applying the compliance check
Records results to CSV and prints warnings
if __name__ == "__main__": Standard Python idiom to allow this script to be both executable and importable.
In this chapter, you gained the foundational Python skills needed to begin automating your GRC workflows:
Why Python for GRC? You saw how Python’s readability, extensive libraries, and rapid‑prototyping capabilities make it an ideal choice for compliance automation.
Environment Setup: You learned to install Python 3.11, create isolated virtual environments, manage dependencies with requirements.txt, and choose an editor to streamline your development.
Core Language Concepts: You mastered variables, data types, input/output, control flow, and functions, and saw how these constructs translate compliance requirements into code.
Modular Design: You discovered how to organize scripts into reusable modules, making your automation code clearer, more maintainable, and easier to test.
End‑to‑End Example: You walked through a simple compliance script that loads JSON, checks encryption settings, writes a CSV report, and provides console warnings—all with detailed comments to explain each step.
With these building blocks in place, you are now ready to integrate Python with AWS more deeply. In the next chapter, we will explore the AWS SDK for Python (boto3), fetch real compliance data from services like Security Hub and AWS Config, and transform that data into spreadsheets and audit artifacts. Your GRC automation toolkit is just getting started. 
Let’s keep building.
Chapter 8: Python, AWS, and Spreadsheets
Automating AWS interactions from Python begins with boto3, the AWS Software Development Kit (SDK) for Python. Rather than constructing raw HTTP requests and handling signatures, you call familiar Python methods. In this section we will cover:
Configuring AWS credentials, including CLI profiles
The difference between client and resource interfaces
Pagination patterns for large result sets
Configuring AWS Credentials
Before any API call succeeds, boto3 must discover valid AWS credentials and a default region. There are multiple ways to supply this information; AWS has great documentation on the preferred order of precedence (https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).
Shared Credentials File
The most common mechanism is the shared credentials file, typically located at ~/.aws/credentials (Linux/macOS) or %USERPROFILE%\.aws\credentials (Windows). It looks like this:
[default]
aws_access_key_id=AKIA...EXAMPLE
aws_secret_access_key=wJalrXUtnFEMI/^^^^K7MDENG/bPxRfiCYEXAMPLEKEY

[grc-engineer]
aws_access_key_id     = AKIA...OTHER
aws_secret_access_key = abcdef1234567890example

Your config file (~/.aws/config) defines the default region and output format:
[default]
region = us-east-1
output = json

[profile grc-engineer]
region = us-west-2

Here, grc-engineer is a named profile. You can reference it in code or via environment variables.
Environment Variables
You can set these directly in your shell:
export AWS_ACCESS_KEY_ID=AKIA...EXAMPLE
export AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
export AWS_DEFAULT_REGION=us-east-1
export AWS_PROFILE=grc-engineer

Using AWS_PROFILE tells both the AWS CLI and boto3 which named profile to load by default.
Using CLI Profiles in Code
To explicitly select a profile within your Python script, create a Session:
import boto3

# Use the 'grc-engineer' profile and override region
session = boto3.Session(profile_name="grc-engineer", region_name="us-west-2")

# Now create service clients from this session
securityhub = session.client("securityhub")
aws_config  = session.client("config")
cloudtrail  = session.client("cloudtrail")

If you do not specify a session, boto3 falls back to the default profile or environment‑provided credentials.
Client vs. Resource Interfaces
boto3 offers two principal interfaces:
Client
Low‑level, direct mapping to AWS service APIs
Returns Python dictionaries and lists exactly as the JSON response
You manage pagination, request parameters, and response parsing
Resource
Higher‑level, object‑oriented interface
Provides Python classes (for example, ec2.Instance) with methods like .start() or .stop()
Automatically handles pagination for many operations
For compliance work, where you want explicit control over filtering, parameters, and pagination we typically prefer the client interface. It exposes every API operation and makes dependencies clear.
# Low‑level client example
securityhub = boto3.client("securityhub")
response    = securityhub.get_findings(Filters={...})

Later, if you need to drill down into specific objects (for example, tagging an EC2 instance), you can create a resource:
ec2 = boto3.resource("ec2", region_name="us-west-2")
instance = ec2.Instance("i-0123456789abcdef0")
instance.create_tags(Tags=[{"Key": "Owner", "Value": "Alice"}])


Handling Paginated Responses
Many AWS API calls return large result sets in pages. You must iterate through each page to retrieve all data. There are two main patterns:
Using a Paginator: boto3 clients include built‑in paginator objects:
paginator = securityhub.get_paginator("get_findings")
all_findings = []
for page in paginator.paginate(
    Filters={...},
    PaginationConfig={"PageSize": 50}
):
    all_findings.extend(page["Findings"])

Here, paginate() handles making successive API calls and collecting NextToken values.
Manual Loop with NextToken
Alternatively, you can manage pagination yourself:
findings = []
next_token = None

while True:
    params = {"Filters": {...}, "MaxResults": 50}
    if next_token:
        params["NextToken"] = next_token

    response = securityhub.get_findings(params)
    findings.extend(response["Findings"])

    next_token = response.get("NextToken")
    if not next_token:
        break

Manual pagination gives you precise control but requires more code. Paginators are generally preferred for clarity and reliability.
Quick Example: Listing High‑Severity Security Hub Findings
Putting these elements together, here is a self‑contained script that:
Uses the grc-engineer CLI profile
Fetches all FAILED findings with HIGH severity
Prints their IDs and titles
import boto3

def get_high_severity_failures(profile="grc-engineer", region="us-east-1"):
    # Establish a session using a named CLI profile
    session   = boto3.Session(profile_name=profile, region_name=region)
    securityhub = session.client("securityhub")

    paginator = securityh.get_paginator("get_findings")
    failures  = []

    for page in paginator.paginate(
        Filters={
            "SeverityLabel":     [{"Value": "HIGH",   "Comparison": "EQUALS"}],
            "ComplianceStatus": [{"Value": "FAILED", "Comparison": "EQUALS"}]
        }
    ):
        failures.extend(page["Findings"])

    return failures

if __name__ == "__main__":
    results = get_high_severity_failures()
    print(f"Found {len(results)} high‑severity failed findings\n")
    for f in results:
        print(f"{f['Id']}: {f['Title']}")

Session Setup: Respects the grc-engineer profile.
Paginator: Ensures you retrieve every matching finding, regardless of volume.
Filters: Narrow results to the events that matter for your compliance check.
With credentials, profile selection, client/resource distinctions, and pagination covered, you have all the tools to retrieve real‑world compliance data from AWS. Next, we will transform that raw JSON into structured tables using pandas.
Fetching Compliance Data from AWS
With boto3 configured, you can retrieve live data from the three core AWS services that power event‑driven GRC:
AWS Security Hub for consolidated security and compliance findings
AWS Config for resource configuration evaluations
AWS CloudTrail for user activity and API call history
Each subsection below provides reusable functions you can drop into your scripts.
Security Hub Findings
Security Hub aggregates findings from AWS services and partner tools into the Amazon Security Finding Format (ASFF). To pull all "FAILED" findings of a given severity:
import boto3
from botocore.exceptions import ClientError, NoCredentialsError

def create_aws_session(profile_name=None, region_name='us-east-1'):
    """
    Create an AWS session with optional profile and region.
    
    AWS sessions encapsulate your credentials and configuration,
    allowing you to make API calls to AWS services. This function
    creates a session and tests it to ensure credentials are valid.
    
    Args:
        profile_name: AWS CLI profile name (None for default profile)
        region_name: AWS region to connect to (defaults to us-east-1)
    
    Returns:
        boto3.Session object if successful, None if failed
    """
    try:
        if profile_name:
            session = boto3.Session(profile_name=profile_name, region_name=region_name)
        else:
            session = boto3.Session(region_name=region_name)
        
        # Test the session by calling AWS STS (Security Token Service)
        # This verifies our credentials work without doing anything destructive
        session.client('sts').get_caller_identity()
        return session
    
    except NoCredentialsError:
        print("AWS credentials not found. Please configure your credentials.")
        return None
    except ClientError as e:
        print(f"Error creating AWS session: {e}")
        return None

def fetch_securityhub_failures(session, severity_labels):
    """
    Returns a list of Security Hub findings with ComplianceStatus=FAILED
    and SeverityLabel matching the specified severity levels.
    
    Security Hub uses the Amazon Security Finding Format (ASFF) to standardize
    security findings from multiple sources (Config, GuardDuty, Inspector, etc.).
    This function specifically looks for compliance failures - resources that
    violate security standards or best practices.
    
    Args:
        session: boto3.Session object with valid AWS credentials
        severity_labels: List of severity levels to filter on (e.g., ["HIGH", "CRITICAL"])
    
    Returns:
        List of Security Hub finding dictionaries in ASFF format
    """
    client = session.client("securityhub")
    
    # Use pagination to handle large numbers of findings
    # Security Hub can return thousands of findings, so we need to page through results
    paginator = client.get_paginator("get_findings")
    
    # Build filters using Security Hub's filter syntax
    # Filters use a specific structure: [{"Value": "...", "Comparison": "EQUALS"}]
    filters = {
        # Only get findings where compliance has failed
        "ComplianceStatus": [{"Value": "FAILED", "Comparison": "EQUALS"}],
        
        # Filter by severity levels (HIGH, CRITICAL, etc.)
        # This list comprehension creates a filter for each severity level
        "SeverityLabel": [
            {"Value": lbl, "Comparison": "EQUALS"} for lbl in severity_labels
        ]
    }
    
    findings = []
    try:
        # Paginate through all results to ensure we don't miss any findings
        # Each page can contain up to 100 findings by default
        for page in paginator.paginate(Filters=filters):
            findings.extend(page["Findings"])
    except ClientError as e:
        print(f"Error fetching Security Hub findings: {e}")
        return []
    
    return findings

Key points to understand:
Security Hub is your compliance dashboard: It aggregates findings from multiple AWS security services into one place using a standardized format (ASFF)
Pagination is essential: Large AWS accounts can have thousands of security findings. Always use paginators to ensure you get all results
Filter syntax matters: Security Hub uses a specific filter format. Each filter needs a "Value" and "Comparison" operator
ComplianceStatus vs. WorkflowStatus: ComplianceStatus tells you if a resource violates a rule, while WorkflowStatus tracks remediation progress
Cost consideration: Security Hub charges per finding ingested, but querying existing findings doesn't incur additional charges
Config Rule Evaluations
AWS Config evaluates resources against managed or custom rules and records whether each resource is COMPLIANT or NON_COMPLIANT. To list all non‑compliant resources for a specific rule:
def fetch_config_noncompliance(session, rule_name):
    """
    Returns a list of evaluation results where ComplianceType=NON_COMPLIANT
    for the specified Config rule.
    
    AWS Config continuously monitors your resources and evaluates them against
    compliance rules. Each evaluation produces a result: COMPLIANT, NON_COMPLIANT,
    or NOT_APPLICABLE. This function retrieves only the violations.
    
    Args:
        session: boto3.Session object with valid AWS credentials
        rule_name: Name of the Config rule to query (e.g., "s3-bucket-server-side-encryption-enabled")
    
    Returns:
        List of evaluation result dictionaries containing non-compliant resources
    """
    client = session.client("config")
    
    # Use pagination for Config rule evaluations
    # Each rule can evaluate hundreds or thousands of resources
    paginator = client.get_paginator("get_compliance_details_by_config_rule")

    results = []
    try:
        # Page through all evaluation results for this specific rule
        for page in paginator.paginate(ConfigRuleName=rule_name):
            # Each page contains an "EvaluationResults" array
            for evaluation in page["EvaluationResults"]:
                # Filter for non-compliant resources only
                # ComplianceType can be: COMPLIANT, NON_COMPLIANT, NOT_APPLICABLE, INSUFFICIENT_DATA
                if evaluation["ComplianceType"] == "NON_COMPLIANT":
                    # Add resource details to help with remediation
                    results.append({
                        'ResourceType': evaluation['EvaluationResultIdentifier']['EvaluationResultQualifier']['ResourceType'],
                        'ResourceId': evaluation['EvaluationResultIdentifier']['EvaluationResultQualifier']['ResourceId'],
                        'ComplianceType': evaluation['ComplianceType'],
                        'ConfigRuleName': evaluation['EvaluationResultIdentifier']['EvaluationResultQualifier']['ConfigRuleName'],
                        'ResultRecordedTime': evaluation['ResultRecordedTime'],
                        'Annotation': evaluation.get('Annotation', 'No details provided')
                    })
    except ClientError as e:
        print(f"Error fetching Config compliance details for rule {rule_name}: {e}")
        return []

    return results

Key points to understand:
Config rules vs. Security Hub findings: Config rules evaluate specific resource configurations, while Security Hub aggregates broader security findings
Rule names are exact matches: Config rule names must match exactly, including case and hyphens (e.g., "s3-bucket-server-side-encryption-enabled")
Evaluation timing: Config evaluates rules when resources change or on a schedule. Results may not be real-time
Resource identification: Each evaluation result includes the resource type and ID, essential for remediation
Annotation field: Often contains specific details about why a resource failed the rule
CloudTrail Event History
CloudTrail provides an audit log of every AWS API call. To extract events matching certain attributes (e.g., IAM actions or console logins):
from datetime import datetime, timedelta
def fetch_cloudtrail_events(session, lookup_attributes,
                            start_time=None, end_time=None):
    """
    Returns a list of CloudTrail events matching lookup_attributes
    within the specified time range.
    
    CloudTrail records every API call made in your AWS account, creating
    an audit trail for security analysis and compliance. This function
    queries the event history using specific attributes like event names,
    usernames, or resource names.
    
    Args:
        session: boto3.Session object with valid AWS credentials
        lookup_attributes: List of attribute filters in format:
                          [{"AttributeKey": "EventName", "AttributeValue": "CreateUser"}]
        start_time: datetime object for search start (defaults to 24 hours ago)
        end_time: datetime object for search end (defaults to now)
    
    Returns:
        List of CloudTrail event dictionaries
    
    Note: CloudTrail event history is only available for 90 days through this API.
    For longer retention, you need CloudTrail logs stored in S3.
    """
    client = session.client("cloudtrail")
    
    # CloudTrail can return massive amounts of data, so pagination is critical
    paginator = client.get_paginator("lookup_events")

    # Default to the past 24 hours if not specified
    # CloudTrail times are in UTC, so we use utcnow() for consistency
    if end_time is None:
        end_time = datetime.utcnow()
    if start_time is None:
        start_time = end_time - timedelta(days=1)

    events = []
    try:
        # Page through CloudTrail events
        # Be careful with large time ranges - they can return thousands of events
        for page in paginator.paginate(
            LookupAttributes=lookup_attributes,
            StartTime=start_time,
            EndTime=end_time
        ):
            # Each event contains detailed information about the API call
            for event in page["Events"]:
                # Enrich the event data with parsed information for easier analysis
                enriched_event = {
                    'EventTime': event['EventTime'],
                    'EventName': event['EventName'],
                    'Username': event.get('Username', 'Unknown'),
                    'UserIdentityType': event.get('UserIdentity', {}).get('type', 'Unknown'),
                    'SourceIPAddress': event.get('SourceIPAddress', 'Unknown'),
                    'UserAgent': event.get('UserAgent', 'Unknown'),
                    'Resources': [r.get('ResourceName', 'Unknown') for r in event.get('Resources', [])],
                    'CloudTrailEvent': event.get('CloudTrailEvent', '{}')  # Full JSON for detailed analysis
                }
                events.append(enriched_event)
                
    except ClientError as e:
        print(f"Error fetching CloudTrail events: {e}")
        return []

    return events

Key points to understand:
CloudTrail event history limitations: Only stores 90 days of events. For longer retention, enable CloudTrail logging to S3
Lookup attributes are powerful filters: You can search by EventName, Username, ResourceName, and more. Each attribute filter is an AND operation
Time ranges affect performance and cost: Larger time ranges return more data and take longer to process. Start small and expand as needed
UserIdentity complexity: AWS events can come from IAM users, roles, federated users, or AWS services. The UserIdentity field reveals the source
SourceIPAddress for security analysis: Helps identify unusual access patterns or potential security incidents
Putting It Together
You can combine these three fetch functions in a single script to get a comprehensive security overview:
import boto3
from datetime import datetime, timedelta
def comprehensive_security_audit(profile_name="default"):
    """
    Perform a comprehensive security audit using multiple AWS services.
    
    This function demonstrates how to combine Security Hub, Config, and CloudTrail
    to get a complete picture of your security posture and recent activity.
    """
    # Initialize AWS session
    session = create_aws_session(profile_name=profile_name)
    if not session:
        print("Failed to create AWS session. Check your credentials.")
        return
    
    print("=== Starting Comprehensive Security Audit ===\n")
    
    # 1. Fetch high-severity Security Hub failures
    print("1. Checking Security Hub for critical security findings...")
    findings = fetch_securityhub_failures(session, ["HIGH", "CRITICAL"])
    print(f"   Found {len(findings)} high/critical Security Hub failures")
    
    # Show sample finding details for context
    if findings:
        sample_finding = findings[0]
        print(f"   Sample finding: {sample_finding.get('Title', 'No title')}")
        print(f"   Resource: {sample_finding.get('Resources', [{}])[0].get('Id', 'Unknown')}")
    
    # 2. Check Config compliance for common security rules
    print("\n2. Checking AWS Config compliance...")
    
    # Common security-related Config rules to check
    security_rules = [
        "s3-bucket-server-side-encryption-enabled",
        "s3-bucket-public-access-prohibited",
        "root-access-key-check",
        "iam-user-mfa-enabled"
    ]
    
    total_violations = 0
    for rule in security_rules:
        try:
            noncompliant = fetch_config_noncompliance(session, rule)
            total_violations += len(noncompliant)
            print(f"   {rule}: {len(noncompliant)} violations")
        except Exception as e:
            print(f"   {rule}: Error checking rule - {e}")
    
    print(f"   Total Config violations: {total_violations}")
    
    # 3. Check recent suspicious CloudTrail activity
    print("\n3. Analyzing recent CloudTrail activity...")
    
    # Look for potentially suspicious activities in the last 24 hours
    suspicious_activities = [
        {"AttributeKey": "EventName", "AttributeValue": "CreateUser"},      # New user creation
        {"AttributeKey": "EventName", "AttributeValue": "AttachUserPolicy"}, # Policy changes
        {"AttributeKey": "EventName", "AttributeValue": "CreateRole"},       # New role creation
        {"AttributeKey": "EventName", "AttributeValue": "ConsoleLogin"}      # Console logins
    ]
    
    for activity in suspicious_activities:
        events = fetch_cloudtrail_events(session, [activity])
        event_name = activity["AttributeValue"]
        print(f"   {event_name} events in last 24h: {len(events)}")
        
        # Show details for high-risk events
        if event_name in ["CreateUser", "AttachUserPolicy"] and events:
            print(f"     Recent {event_name} by: {events[0].get('Username', 'Unknown')}")
    
    # 4. Generate summary and recommendations
    print("\n=== Security Audit Summary ===")
    print(f"Security Hub Critical/High Findings: {len(findings)}")
    print(f"Config Rule Violations: {total_violations}")
    print(f"Recent IAM Activity: Review CloudTrail events above")
    
    if len(findings) > 0 or total_violations > 0:
        print("\n⚠️  ATTENTION REQUIRED:")
        if len(findings) > 0:
            print("   • Review and remediate Security Hub findings")
        if total_violations > 0:
            print("   • Address Config rule violations")
        print("   • Monitor CloudTrail for unusual activity patterns")
    else:
        print("\n✅ No critical security issues detected in this audit")

def main():
    """
    Main function to run the comprehensive security audit.
    Modify the profile_name to match your AWS CLI profile.
    """
    comprehensive_security_audit(profile_name="grc-engineer")

if __name__ == "__main__":
    main()

Key integration points:
Correlation is key: Security findings from different sources often relate to the same underlying issues. Look for patterns across services
Timing matters: Config evaluations may lag behind actual resource changes. CloudTrail shows real-time activity
Error handling in production: Always wrap API calls in try/catch blocks. AWS services can have temporary outages or rate limits
Resource limits: Each service has different pagination limits and query restrictions. Design your scripts to handle large datasets gracefully
Cost awareness: CloudTrail queries and Security Hub can incur costs with heavy usage. Start with focused queries and expand as needed
In the next section, we'll transform these raw JSON lists into structured tables using pandas, preparing for export to CSV or Excel for stakeholder reporting and audit evidence.
Transforming JSON to Tabular Data with pandas
Raw JSON from AWS APIs is often nested and inconsistent, making it hard to analyze or export directly. The pandas library shines at flattening and normalizing these structures into two‑dimensional tables, called DataFrames, which can then be easily filtered, aggregated, and written to CSV or Excel.
Installing and Importing pandas
First, ensure pandas is in your requirements.txt:
pip install pandas openpyxl xlsxwriter
pip freeze > requirements.txt

In your script:
import pandas as pd
import json
from datetime import datetime, timedelta

Normalizing Nested JSON
AWS Security Hub findings, for example, contain nested dictionaries under keys like "Severity", "Resources", or "ProductFields". Use pd.json_normalize to flatten these into columns:
def findings_to_dataframe(findings: list[dict]) -> pd.DataFrame:
    """
    Converts a list of Security Hub findings into a flat DataFrame.
    
    Security Hub findings are deeply nested JSON objects with arrays of resources,
    nested severity information, and complex metadata. This function flattens
    the structure into a tabular format suitable for analysis and reporting.
    
    Args:
        findings: List of Security Hub finding dictionaries from AWS API
        
    Returns:
        pandas.DataFrame with flattened columns and one row per finding
        
    Example:
        Raw finding: {"Id": "abc", "Severity": {"Label": "HIGH"}, "Title": "Issue"}
        Result: DataFrame with columns ["Id", "Severity_Label", "Title"]
    """
    if not findings:
        # Return empty DataFrame with expected columns to prevent downstream errors
        return pd.DataFrame(columns=['Id', 'Title', 'CreatedAt', 'Severity_Label'])
    
    try:
        # json_normalize is pandas' most powerful tool for flattening nested data
        # It converts nested dictionaries into flat column names using separator
        df = pd.json_normalize(
            data=findings,               # The list of dictionaries to flatten
            record_path=None,           # None means we're not exploding any arrays yet
            meta=["Id", "Title", "CreatedAt", "UpdatedAt", "Description"],  # Top-level fields to preserve
            meta_prefix="",             # Don't add prefixes to meta fields
            record_prefix="",           # Don't add prefixes to record fields  
            sep="_"                     # Nested keys like Severity.Label become Severity_Label
        )

        # Clean up common nested fields that are important for reporting
        column_mappings = {
            "Severity.Label": "Severity",
            "Workflow.Status": "WorkflowStatus", 
            "Compliance.Status": "ComplianceStatus",
            "ProductArn": "ProductName"  # ARNs are long, extract readable names later
        }
        
        # Apply column renaming for better readability
        for old_col, new_col in column_mappings.items():
            if old_col in df.columns:
                df = df.rename(columns={old_col: new_col})
        
        # Convert string timestamps to datetime objects for better sorting/filtering
        datetime_columns = ['CreatedAt', 'UpdatedAt', 'FirstObservedAt', 'LastObservedAt']
        for col in datetime_columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='coerce')  # coerce handles invalid dates
                
        return df
        
    except Exception as e:
        print(f"Error processing findings to DataFrame: {e}")
        # Return empty DataFrame rather than crashing
        return pd.DataFrame()

Key points to understand:
json_normalize is your best friend: It's specifically designed to handle nested JSON structures that AWS APIs commonly return
Column naming strategy: Use consistent, readable column names. AWS field names can be verbose or unclear
Handle empty data gracefully: Always check for empty inputs to prevent downstream errors in reports
Datetime conversion is critical: String timestamps can't be sorted or filtered properly. Convert them early
Handling Lists of Resources
Some AWS payloads include arrays of sub‑objects—for example, a finding's "Resources" list. You can expand each element into its own row:
def expand_resources(df: pd.DataFrame) -> pd.DataFrame:
    """
    Expands Security Hub findings that contain multiple resources into separate rows.
    
    Many Security Hub findings apply to multiple AWS resources (e.g., a misconfigured
    security group affecting multiple EC2 instances). This function creates one row
    per resource, making it easier to analyze resource-specific compliance issues.
    
    Args:
        df: DataFrame from findings_to_dataframe() containing Resources column
        
    Returns:
        DataFrame with one row per finding-resource combination
        
    Example:
        Input: 1 finding affecting 3 S3 buckets
        Output: 3 rows, each with the same finding data but different resource details
    """
    # Defensive programming: check if Resources column exists
    if "Resources" not in df.columns:
        print("Warning: No 'Resources' column found. Returning original DataFrame.")
        return df
    
    if df.empty:
        return df
    
    try:
        # explode() creates a new row for each element in the Resources list
        # This transforms one finding with multiple resources into multiple rows
        exploded = df.explode("Resources")
        
        # Remove rows where Resources is null (some findings may have empty resource lists)
        exploded = exploded.dropna(subset=["Resources"])
        
        if exploded.empty:
            print("Warning: No valid resources found after explosion.")
            return df
        
        # Normalize the nested resource dictionaries into flat columns
        # Each resource contains Id, Type, Region, Tags, etc.
        resources_df = pd.json_normalize(
            exploded["Resources"],
            sep="_"  # Resource.Id becomes Resource_Id, etc.
        )
        
        # Add descriptive prefixes to avoid column name conflicts
        resources_df.columns = ["Resource_" + col for col in resources_df.columns]
        
        # Drop the original Resources column (now expanded) and join the new resource columns
        result = exploded.drop(columns=["Resources"]).reset_index(drop=True).join(resources_df)
        
        print(f"Expanded {len(df)} findings into {len(result)} finding-resource combinations")
        return result
        
    except Exception as e:
        print(f"Error expanding resources: {e}")
        return df

Key points to understand:
One-to-many relationships: Security findings often affect multiple resources. Expanding creates clearer resource-level reporting
Data volume impact: Expanding can significantly increase row count. A single finding with 50 resources becomes 50 rows
Resource identification: Each expanded row contains specific resource details needed for remediation (Resource ID, Type, Region)
Null handling: Always handle cases where resources might be missing or malformed
Merging Multiple DataFrames
You may wish to join Security Hub findings with their corresponding Config evaluations or CloudTrail events. For example, if both DataFrames share a "ResourceId" column:
def merge_findings_and_config(df_findings: pd.DataFrame, 
                              df_config: pd.DataFrame) -> pd.DataFrame:
    """
    Merges Security Hub findings with AWS Config compliance data on matching resources.
    
    This creates a comprehensive view showing both security findings and configuration
    compliance status for the same resources. Useful for understanding the relationship
    between security issues and configuration violations.
    
    Args:
        df_findings: DataFrame from expand_resources() with Resource_Id column
        df_config: DataFrame from fetch_config_noncompliance() with ResourceId column
        
    Returns:
        DataFrame containing matched records with both security and config data
    """
    if df_findings.empty or df_config.empty:
        print("Warning: One or both DataFrames are empty. Cannot merge.")
        return pd.DataFrame()
    
    try:
        # Ensure we have the columns we need for merging
        finding_resource_col = "Resource_Id"
        config_resource_col = "ResourceId"
        
        if finding_resource_col not in df_findings.columns:
            print(f"Error: '{finding_resource_col}' not found in findings DataFrame")
            return df_findings
            
        if config_resource_col not in df_config.columns:
            print(f"Error: '{config_resource_col}' not found in config DataFrame")
            return df_findings
        
        # Inner join to get only resources that appear in both datasets
        # This shows resources with both security findings AND config violations
        merged = df_findings.merge(
            df_config,
            left_on=finding_resource_col,      # Resource_Id from Security Hub
            right_on=config_resource_col,      # ResourceId from Config
            how="inner",                       # Only keep matching records
            suffixes=("_SecurityHub", "_Config")  # Disambiguate overlapping column names
        )
        
        print(f"Merged {len(df_findings)} findings with {len(df_config)} config violations")
        print(f"Found {len(merged)} resources with both security findings and config violations")
        
        # Add a correlation flag to highlight resources with multiple issue types
        merged["MultipleIssueTypes"] = True
        
        return merged
        
    except Exception as e:
        print(f"Error merging DataFrames: {e}")
        return df_findings

def advanced_correlation_analysis(df_security: pd.DataFrame, 
                                  df_config: pd.DataFrame,
                                  df_cloudtrail: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """
    Performs advanced correlation analysis across multiple AWS security data sources.
    
    Creates multiple views of the data to identify patterns and relationships:
    - Resources with multiple types of violations
    - Timeline correlation between config changes and security findings
    - High-risk resources (multiple violations + recent activity)
    
    Returns:
        Dictionary of DataFrames with different analytical views
    """
    results = {}
    
    # 1. Resources with both security findings and config violations
    if not df_security.empty and not df_config.empty:
        results["MultipleViolations"] = merge_findings_and_config(df_security, df_config)
    
    # 2. Recent activity correlation (resources changed recently + have security issues)
    if not df_security.empty and not df_cloudtrail.empty:
        # Merge security findings with recent CloudTrail activity
        recent_activity = df_security.merge(
            df_cloudtrail,
            left_on="Resource_Id",
            right_on="ResourceName", 
            how="inner",
            suffixes=("_Finding", "_Activity")
        )
        results["RecentActivityWithFindings"] = recent_activity
    
    # 3. High-risk resource summary
    if "MultipleViolations" in results:
        high_risk = results["MultipleViolations"].groupby("Resource_Id").agg({
            "Severity": "max",  # Highest severity finding
            "ComplianceType": "count",  # Number of config violations
            "CreatedAt": "min"  # First finding date
        }).reset_index()
        results["HighRiskSummary"] = high_risk
    
    return results

Key points to understand:
Join strategies matter: Inner joins show only overlapping data, outer joins preserve all records. Choose based on your analysis needs
Column naming conflicts: Use suffixes to distinguish between columns with the same name from different sources
Data quality affects joins: Inconsistent resource naming between services can prevent successful merges
Correlation insights: Merged data often reveals patterns not visible in individual datasets
Adding Calculated Columns
You can derive new columns for reporting, timestamps, severity scores, or business logic flags:
def add_business_logic_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Enhances the DataFrame with calculated columns for business analysis and reporting.
    
    Adds derived fields that help with prioritization, SLA tracking, and executive
    reporting. These columns transform raw security data into actionable business metrics.
    
    Args:
        df: DataFrame with security findings data
        
    Returns:
        Enhanced DataFrame with additional calculated columns
    """
    if df.empty:
        return df
        
    df = df.copy()  # Avoid modifying the original DataFrame
    
    try:
        # 1. Convert CreatedAt strings to datetime objects for time-based analysis
        if "CreatedAt" in df.columns:
            df["CreatedAt"] = pd.to_datetime(df["CreatedAt"], errors='coerce')
        
        # 2. Create numeric severity levels for sorting and aggregation
        # Higher numbers = more severe, easier for mathematical operations
        severity_map = {
            "INFORMATIONAL": 0,
            "LOW": 1, 
            "MEDIUM": 2, 
            "HIGH": 3, 
            "CRITICAL": 4
        }
        
        if "Severity" in df.columns:
            df["SeverityLevel"] = df["Severity"].map(severity_map).fillna(0).astype(int)
            
            # Create severity category for executive reporting
            df["SeverityCategory"] = df["SeverityLevel"].apply(
                lambda x: "Critical/High" if x >= 3 else "Medium" if x == 2 else "Low/Info"
            )
        
        # 3. Time-based flags for SLA tracking and prioritization
        if "CreatedAt" in df.columns:
            now = pd.Timestamp.utcnow()
            
            # Flag recent findings (last 7 days) - these need immediate attention
            df["IsRecent"] = df["CreatedAt"] >= (now - pd.Timedelta(days=7))
            
            # Calculate age in days for SLA tracking
            df["AgeDays"] = (now - df["CreatedAt"]).dt.days
            
            # SLA violation flags based on severity (example business rules)
            df["SLAViolation"] = False
            if "SeverityLevel" in df.columns:
                # Critical: 1 day, High: 7 days, Medium: 30 days
                sla_days = df["SeverityLevel"].map({4: 1, 3: 7, 2: 30, 1: 90, 0: 365})
                df["SLAViolation"] = df["AgeDays"] > sla_days
        
        # 4. Business impact scoring (combine severity + resource type + compliance status)
        impact_factors = []
        
        if "SeverityLevel" in df.columns:
            impact_factors.append(df["SeverityLevel"] * 2)  # Severity is most important
            
        if "Resource_Type" in df.columns:
            # Higher impact for critical resource types
            resource_weights = {
                "AWS::IAM::Role": 3,
                "AWS::IAM::User": 3, 
                "AWS::S3::Bucket": 2,
                "AWS::EC2::Instance": 2,
                "AWS::RDS::DBInstance": 2
            }
            resource_impact = df["Resource_Type"].map(resource_weights).fillna(1)
            impact_factors.append(resource_impact)
        
        if "ComplianceStatus" in df.columns:
            compliance_impact = df["ComplianceStatus"].map({"FAILED": 2, "WARNING": 1}).fillna(0)
            impact_factors.append(compliance_impact)
        
        # Calculate overall business impact score
        if impact_factors:
            df["BusinessImpactScore"] = sum(impact_factors)
            
            # Create business impact categories for executive dashboards
            df["BusinessImpact"] = pd.cut(
                df["BusinessImpactScore"], 
                bins=[0, 3, 6, 12, float('inf')],
                labels=["Low", "Medium", "High", "Critical"],
                include_lowest=True
            )
        
        # 5. Resource ownership and accountability columns
        if "Resource_Tags" in df.columns:
            # Extract common business tags for accountability
            df["Owner"] = df["Resource_Tags"].apply(
                lambda tags: extract_tag_value(tags, ["Owner", "owner", "Team", "team"])
            )
            df["Environment"] = df["Resource_Tags"].apply(
                lambda tags: extract_tag_value(tags, ["Environment", "Env", "Stage"])
            )
            df["CostCenter"] = df["Resource_Tags"].apply(
                lambda tags: extract_tag_value(tags, ["CostCenter", "BU", "Department"])
            )
        
        print(f"Added business logic columns. DataFrame now has {len(df.columns)} columns.")
        return df
        
    except Exception as e:
        print(f"Error adding business logic columns: {e}")
        return df

def extract_tag_value(tags_dict: dict, possible_keys: list[str]) -> str:
    """
    Helper function to extract tag values using multiple possible key names.
    AWS tags are case-sensitive and inconsistently named across organizations.
    """
    if not isinstance(tags_dict, dict):
        return "Unknown"
    
    for key in possible_keys:
        if key in tags_dict:
            return str(tags_dict[key])
    
    return "Unknown"

Key points to understand:
Business context matters: Raw severity levels don't always match business priorities. Add your organization's logic
SLA tracking enables accountability: Automatic SLA violation detection helps with escalation and reporting
Scoring algorithms drive prioritization: Combine multiple factors (severity + resource type + age) for better triage
Tag extraction is crucial: AWS resource tags contain ownership and business context needed for accountability
Previewing the Result
Before exporting, inspect the DataFrame to ensure it looks correct:
def preview_dataframe_analysis(df: pd.DataFrame, name: str = "DataFrame") -> None:
    """
    Comprehensive preview of DataFrame structure and content for quality assurance.
    
    Provides detailed information about the DataFrame to catch data quality issues
    before generating reports. Essential for validating data transformations.
    """
    if df.empty:
        print(f"⚠️  {name} is empty!")
        return
    
    print(f"\n=== {name} Analysis ===")
    
    # Basic structure information
    print(f"Dimensions: {df.shape[0]:,} rows × {df.shape[1]} columns")
    print(f"Memory usage: {df.memory_usage(deep=True).sum() / 10242:.1f} MB")
    
    # Column information with data types and null counts
    print(f"\nColumn Information:")
    info_df = pd.DataFrame({
        'Column': df.columns,
        'DataType': df.dtypes.values,
        'NonNull': df.count().values,
        'NullCount': df.isnull().sum().values,
        'NullPct': (df.isnull().sum() / len(df) * 100).round(1).values
    })
    print(info_df.to_string(index=False))
    
    # Sample data
    print(f"\nFirst 3 rows:")
    print(df.head(3).to_string())
    
    # Key metrics for security data
    if "Severity" in df.columns:
        print(f"\nSeverity Distribution:")
        print(df["Severity"].value_counts().to_string())
    
    if "Resource_Type" in df.columns:
        print(f"\nTop 5 Resource Types:")
        print(df["Resource_Type"].value_counts().head().to_string())
    
    if "CreatedAt" in df.columns:
        print(f"\nTime Range:")
        print(f"  Earliest: {df['CreatedAt'].min()}")
        print(f"  Latest: {df['CreatedAt'].max()}")
        print(f"  Span: {(df['CreatedAt'].max() - df['CreatedAt'].min()).days} days")

# Usage example
df = findings_to_dataframe(findings)
df = expand_resources(df)
df = add_business_logic_columns(df)
preview_dataframe_analysis(df, "Security Hub Findings")

This interactive step helps catch schema mismatches or missing fields early and ensures your data transformations worked correctly.
Exporting to CSV and Excel
Once you have a clean pandas.DataFrame of your compliance data, exporting to CSV or Excel is straightforward. In this section, we'll cover writing formatted files that auditors and executives can easily consume.
Writing to CSV
A CSV (comma‐separated values) file is the simplest, most portable report format. Use DataFrame.to_csv():
def export_to_csv(df: pd.DataFrame, path: str, include_metadata: bool = True) -> None:
    """
    Exports DataFrame to CSV with proper formatting for auditor consumption.
    
    CSV files are universally readable and work well for large datasets.
    This function adds metadata and ensures proper formatting for compliance reports.
    
    Args:
        df: DataFrame to export
        path: Output file path
        include_metadata: Whether to include a metadata header
    """
    if df.empty:
        print(f"Warning: DataFrame is empty. Creating empty CSV at {path}")
        df.to_csv(path, index=False)
        return
    
    try:
        # Create the export directory if it doesn't exist
        import os
        os.makedirs(os.path.dirname(path) if os.path.dirname(path) else '.', exist_ok=True)
        
        if include_metadata:
            # Write metadata header for audit trail
            with open(path, 'w', encoding='utf-8') as f:
                f.write(f"# Security Compliance Report\n")
                f.write(f"# Generated: {datetime.now().isoformat()}\n")
                f.write(f"# Record Count: {len(df):,}\n")
                f.write(f"# Column Count: {len(df.columns)}\n")
                f.write("#\n")
            
            # Append the actual data
            df.to_csv(path, mode='a', index=False, encoding='utf-8')
        else:
            df.to_csv(path, index=False, encoding='utf-8')
        
        # Report file size for reference
        file_size = os.path.getsize(path) / 1024  # KB
        print(f"✅ Exported {len(df):,} rows to {path} ({file_size:.1f} KB)")
        
    except Exception as e:
        print(f"❌ Error exporting to CSV: {e}")

def export_filtered_csv(df: pd.DataFrame, base_path: str) -> dict[str, str]:
    """
    Exports multiple filtered views of the data as separate CSV files.
    
    Creates different files for different stakeholder needs:
    - Executive summary (high/critical only)
    - Operations team (all actionable items)
    - Audit team (complete dataset)
    
    Returns:
        Dictionary mapping view names to file paths
    """
    exports = {}
    
    try:
        # Executive view: Only high and critical severity
        if "SeverityLevel" in df.columns:
            executive_df = df[df["SeverityLevel"] >= 3].copy()
            exec_path = base_path.replace('.csv', '_executive.csv')
            export_to_csv(executive_df, exec_path)
            exports["Executive"] = exec_path
        
        # Operations view: All items requiring action
        if "WorkflowStatus" in df.columns:
            ops_df = df[df["WorkflowStatus"].isin(["NEW", "NOTIFIED"])].copy()
            ops_path = base_path.replace('.csv', '_operations.csv')
            export_to_csv(ops_df, ops_path)
            exports["Operations"] = ops_path
        
        # Audit view: Complete dataset with all columns
        audit_path = base_path.replace('.csv', '_audit.csv')
        export_to_csv(df, audit_path)
        exports["Audit"] = audit_path
        
        return exports
        
    except Exception as e:
        print(f"Error creating filtered exports: {e}")
        return {}

Key parameters and considerations:
index=False: Omits the DataFrame's integer index column (usually not needed in reports)
encoding='utf-8': Ensures international characters display correctly
Metadata headers: Help auditors understand when and how the report was generated
File size awareness: Large CSV files (>100MB) may be difficult for stakeholders to open
Generating an Excel Workbook
Excel workbooks can contain multiple sheets, each holding a different slice of data. Use a context‐managed ExcelWriter:
def export_to_excel(dataframes: dict[str, pd.DataFrame], path: str, 
                   include_summary: bool = True) -> None:
    """
    Exports multiple DataFrames to a comprehensive Excel workbook.
    
    Creates a professional audit-ready Excel file with multiple sheets,
    formatting, and summary analysis. Ideal for stakeholder presentations
    and audit evidence packages.
    
    Args:
        dataframes: Dictionary mapping sheet names to DataFrames
        path: Output Excel file path
        include_summary: Whether to auto-generate summary sheets
    """
    if not dataframes:
        print("Warning: No DataFrames provided for Excel export")
        return
    
    try:
        # Create output directory
        import os
        os.makedirs(os.path.dirname(path) if os.path.dirname(path) else '.', exist_ok=True)
        
        with pd.ExcelWriter(path, engine="openpyxl") as writer:
            # Write each DataFrame to its own sheet
            for sheet_name, df in dataframes.items():
                if df.empty:
                    print(f"Warning: {sheet_name} sheet is empty")
                    continue
                    
                # Clean sheet name (Excel has character restrictions)
                clean_sheet_name = clean_excel_sheet_name(sheet_name)
                
                # Write the data
                df.to_excel(writer, sheet_name=clean_sheet_name, index=False, startrow=1)
                
                # Add header information
                worksheet = writer.sheets[clean_sheet_name]
                worksheet['A1'] = f"{sheet_name} - Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}"
                
                # Auto-adjust column widths for readability
                auto_adjust_column_widths(writer, clean_sheet_name)
                
                print(f"  ✅ Added sheet '{clean_sheet_name}' with {len(df):,} rows")
            
            # Generate summary sheets if requested
            if include_summary and dataframes:
                create_executive_summary_sheet(writer, dataframes)
                create_detailed_summary_sheets(writer, dataframes)
        
        # Report final file size
        file_size = os.path.getsize(path) / 10242  # MB
        print(f"✅ Excel workbook saved to {path} ({file_size:.1f} MB)")
        
    except Exception as e:
        print(f"❌ Error creating Excel workbook: {e}")

def clean_excel_sheet_name(name: str) -> str:
    """
    Cleans sheet names to comply with Excel's naming restrictions.
    Excel sheet names cannot exceed 31 characters and cannot contain: / \ ? * [ ]
    """
    # Remove invalid characters
    invalid_chars = ['/', '\\', '?', '*', '[', ']', ':']
    for char in invalid_chars:
        name = name.replace(char, '_')
    
    # Truncate to 31 characters
    if len(name) > 31:
        name = name[:28] + "..."
    
    return name

def auto_adjust_column_widths(writer: pd.ExcelWriter, sheet_name: str) -> None:
    """
    Automatically adjusts column widths based on content length.
    Makes the Excel file more readable without manual formatting.
    """
    try:
        from openpyxl.utils import get_column_letter
        
        worksheet = writer.sheets[sheet_name]
        
        for idx, column in enumerate(worksheet.columns, start=1):
            # Calculate max length in this column
            max_length = 0
            column_letter = get_column_letter(idx)
            
            for cell in column:
                if cell.value:
                    max_length = max(max_length, len(str(cell.value)))
            
            # Set width with some padding, but cap at reasonable maximum
            adjusted_width = min(max_length + 2, 50)
            worksheet.column_dimensions[column_letter].width = adjusted_width
            
    except Exception as e:
        print(f"Warning: Could not adjust column widths for {sheet_name}: {e}")



Adding Summary Sheets with Analytics
You can programmatically build summary analysis sheets that executives and auditors find valuable:
def create_executive_summary_sheet(writer: pd.ExcelWriter, 
                                  dataframes: dict[str, pd.DataFrame]) -> None:
    """
    Creates an executive-level summary sheet with key metrics and trends.
    
    Provides high-level insights that executives need for decision-making:
    - Overall risk posture
    - Trend analysis
    - Priority areas for attention
    """
    try:
        summary_data = []
        
        for sheet_name, df in dataframes.items():
            if df.empty:
                continue
                
            # Calculate key metrics for each dataset
            metrics = {
                'Data Source': sheet_name,
                'Total Issues': len(df),
                'Critical/High': len(df[df.get('SeverityLevel', pd.Series([0])) >= 3]) if 'SeverityLevel' in df.columns else 'N/A',
                'SLA Violations': len(df[df.get('SLAViolation', pd.Series([False]))]) if 'SLAViolation' in df.columns else 'N/A',
                'Recent Issues (7d)': len(df[df.get('IsRecent', pd.Series([False]))]) if 'IsRecent' in df.columns else 'N/A'
            }
            
            summary_data.append(metrics)
        
        # Create summary DataFrame
        summary_df = pd.DataFrame(summary_data)
        
        # Add overall totals row
        if not summary_df.empty:
            totals = {
                'Data Source': 'TOTAL',
                'Total Issues': summary_df['Total Issues'].sum(),
                'Critical/High': summary_df['Critical/High'].sum() if summary_df['Critical/High'].dtype in ['int64', 'float64'] else 'N/A',
                'SLA Violations': summary_df['SLA Violations'].sum() if summary_df['SLA Violations'].dtype in ['int64', 'float64'] else 'N/A',
                'Recent Issues (7d)': summary_df['Recent Issues (7d)'].sum() if summary_df['Recent Issues (7d)'].dtype in ['int64', 'float64'] else 'N/A'
            }
            summary_df = pd.concat([summary_df, pd.DataFrame([totals])], ignore_index=True)
        
        # Write to Excel
        summary_df.to_excel(writer, sheet_name="Executive_Summary", index=False, startrow=2)
        
        # Add title and context
        worksheet = writer.sheets["Executive_Summary"]
        worksheet['A1'] = f"Executive Security Summary - {datetime.now().strftime('%Y-%m-%d')}"
        worksheet['A2'] = "Key metrics across all security data sources"
        
        auto_adjust_column_widths(writer, "Executive_Summary")
        print("  ✅ Added Executive Summary sheet")
        
    except Exception as e:
        print(f"Warning: Could not create executive summary: {e}")

def create_detailed_summary_sheets(writer: pd.ExcelWriter, 
                                  dataframes: dict[str, pd.DataFrame]) -> None:
    """
    Creates detailed analysis sheets for operational teams.
    
    Provides operational insights like:
    - Severity distributions
    - Resource type breakdowns  
    - Trend analysis over time
    """
    try:
        # Combine all security findings for cross-cutting analysis
        all_findings = []
        for name, df in dataframes.items():
            if not df.empty and 'Severity' in df.columns:
                df_copy = df.copy()
                df_copy['Source'] = name
                all_findings.append(df_copy)
        
        if not all_findings:
            return
            
        combined_df = pd.concat(all_findings, ignore_index=True)
        
        # 1. Severity distribution across all sources
        if 'Severity' in combined_df.columns:
            severity_summary = combined_df.groupby(['Source', 'Severity']).size().unstack(fill_value=0)
            severity_summary.to_excel(writer, sheet_name="Severity_Analysis")
            auto_adjust_column_widths(writer, "Severity_Analysis")
            
        # 2. Resource type analysis
        if 'Resource_Type' in combined_df.columns:
            resource_summary = combined_df['Resource_Type'].value_counts().head(20)
            resource_df = pd.DataFrame({
                'Resource Type': resource_summary.index,
                'Issue Count': resource_summary.values
            })
            resource_df.to_excel(writer, sheet_name="Resource_Analysis", index=False)
            auto_adjust_column_widths(writer, "Resource_Analysis")
            
        # 3. Time-based trend analysis
        if 'CreatedAt' in combined_df.columns:
            combined_df['Date'] = combined_df['CreatedAt'].dt.date
            trend_summary = combined_df.groupby(['Date', 'Severity']).size().unstack(fill_value=0)
            trend_summary.to_excel(writer, sheet_name="Trend_Analysis")
            auto_adjust_column_widths(writer, "Trend_Analysis")
            
        print("  ✅ Added detailed analysis sheets")
        
    except Exception as e:
        print(f"Warning: Could not create detailed summaries: {e}")

# Complete workflow example
def create_comprehensive_report(df_security: pd.DataFrame, 
                               df_config: pd.DataFrame,
                               df_cloudtrail: pd.DataFrame,
                               output_path: str) -> None:
    """
    Creates a comprehensive security report with multiple formats and views.
    """
    # Prepare all datasets
    datasets = {
        "Security_Hub_Findings": df_security,
        "Config_Violations": df_config, 
        "CloudTrail_Events": df_cloudtrail
    }
    
    # Export to Excel with summary sheets
    excel_path = output_path.replace('.xlsx', '_comprehensive.xlsx')
    export_to_excel(datasets, excel_path, include_summary=True)
    
    # Export filtered CSV views
    csv_base = output_path.replace('.xlsx', '.csv')
    csv_exports = export_filtered_csv(df_security, csv_base)
    
    print(f"\n📊 Report Generation Complete:")
    print(f"  📈 Excel Report: {excel_path}")
    for view, path in csv_exports.items():
        print(f"  📋 {view} CSV: {path}")

Key points to understand:
Multiple sheets enable organization: Different stakeholders need different views of the same data
Summary sheets add value: Raw data is less useful than analyzed insights for decision-makers
Auto-formatting improves usability: Proper column widths and headers make reports more professional
Error handling preserves workflow: Failed formatting shouldn't prevent report generation
Ingesting Spreadsheets Back into Python
Auditors or other teams may provide spreadsheets (CSV or Excel) containing manual evidence, remediation logs, or control mappings. Python's pandas makes it easy to read these files, validate their schema, and process the contents for automated ingestion or analysis.
Reading CSV and Excel Files
def load_csv(path: str, required_columns: list[str] = None, 
             encoding: str = 'utf-8') -> pd.DataFrame:
    """
    Reads a CSV file into a DataFrame with comprehensive validation and error handling.
    
    CSV files from auditors often have encoding issues, missing columns, or
    inconsistent formats. This function handles common problems gracefully.
    
    Args:
        path: Path to CSV file
        required_columns: List of column names that must be present
        encoding: File encoding (try 'utf-8', 'latin-1', or 'cp1252' for Windows files)
        
    Returns:
        DataFrame with validated structure
        
    Raises:
        ValueError: If required columns are missing
        FileNotFoundError: If file doesn't exist
    """
    try:
        # Try primary encoding first
        df = pd.read_csv(path, encoding=encoding)
        
    except UnicodeDecodeError:
        # Fall back to common Windows encoding
        print(f"UTF-8 encoding failed, trying latin-1 for {path}")
        try:
            df = pd.read_csv(path, encoding='latin-1')
        except UnicodeDecodeError:
            print(f"Latin-1 encoding failed, trying cp1252 for {path}")
            df = pd.read_csv(path, encoding='cp1252')
    
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file not found: {path}")
    
    except Exception as e:
        raise ValueError(f"Error reading CSV file {path}: {e}")
    
    # Validate file structure
    if df.empty:
        raise ValueError(f"CSV file is empty: {path}")
    
    # Clean up common issues in auditor-provided files
    df = clean_auditor_data(df)
    
    # Validate required columns
    if required_columns:
        missing = set(required_columns) - set(df.columns)
        if missing:
            available_cols = list(df.columns)
            raise ValueError(
                f"Missing required columns in {path}: {missing}\n"
                f"Available columns: {available_cols}"
            )
    
    print(f"✅ Loaded {len(df):,} rows from {path}")
    return df

def load_excel(path: str, sheet_name: str = 0, required_columns: list[str] = None,
               header_row: int = 0) -> pd.DataFrame:
    """
    Reads an Excel sheet into a DataFrame with advanced error handling.
    
    Excel files from auditors often have title rows, merged cells, or data
    starting at non-standard locations. This function handles these issues.
    
    Args:
        path: Path to Excel file
        sheet_name: Sheet name or index (0 for first sheet)
        required_columns: List of column names that must be present
        header_row: Row number containing column headers (0-indexed)
        
    Returns:
        DataFrame with validated structure
    """
    try:
        # Read Excel file with specified header row
        df = pd.read_excel(path, sheet_name=sheet_name, header=header_row)
        
        # Handle cases where Excel has title rows above the actual data
        if df.empty or df.columns[0].startswith('Unnamed'):
            print(f"Attempting to find header row in {path}")
            # Try a few different header positions
            for row in range(1, min(5, len(df))):
                test_df = pd.read_excel(path, sheet_name=sheet_name, header=row)
                if not test_df.empty and not test_df.columns[0].startswith('Unnamed'):
                    df = test_df
                    print(f"Found headers at row {row}")
                    break
        
    except FileNotFoundError:
        raise FileNotFoundError(f"Excel file not found: {path}")
    
    except Exception as e:
        raise ValueError(f"Error reading Excel file {path}, sheet '{sheet_name}': {e}")
    
    if df.empty:
        raise ValueError(f"Excel sheet is empty: {path}[{sheet_name}]")
    
    # Clean up the data
    df = clean_auditor_data(df)
    
    # Validate required columns
    if required_columns:
        missing = set(required_columns) - set(df.columns)
        if missing:
            available_sheets = get_excel_sheet_names(path)
            available_cols = list(df.columns)
            raise ValueError(
                f"Missing required columns in {path}[{sheet_name}]: {missing}\n"
                f"Available columns: {available_cols}\n"
                f"Available sheets: {available_sheets}"
            )
    
    print(f"✅ Loaded {len(df):,} rows from {path}[{sheet_name}]")
    return df

def clean_auditor_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans common issues in auditor-provided spreadsheets.
    
    Auditors often work with Excel in ways that create data quality issues:
    - Extra spaces in column names and values
    - Inconsistent date formats
    - Mixed case text that should be standardized
    """
    df = df.copy()
    
    # Clean column names: remove spaces, standardize case
    df.columns = df.columns.str.strip().str.replace(' ', '_')
    
    # Clean string columns: remove leading/trailing spaces
    string_columns = df.select_dtypes(include=['object']).columns
    for col in string_columns:
        df[col] = df[col].astype(str).str.strip()
        # Replace empty strings with NaN for better handling
        df[col] = df[col].replace('', pd.NA)
    
    # Remove completely empty rows and columns
    df = df.dropna(how='all').dropna(axis=1, how='all')
    
    return df

def get_excel_sheet_names(path: str) -> list[str]:
    """Helper function to list all sheet names in an Excel file."""
    try:
        xl_file = pd.ExcelFile(path)
        return xl_file.sheet_names
    except Exception:
        return []

Data Cleansing and Type Casting
After loading, ensure each column has the correct data type and handle missing values:
def cleanse_manual_evidence(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and validates manual evidence DataFrame for automated processing.
    
    Manual evidence files from auditors need standardization before they can
    be ingested into AWS services or processed by automation scripts.
    
    Args:
        df: Raw DataFrame from auditor spreadsheet
        
    Returns:
        Cleaned DataFrame ready for automated processing
    """
    df = df.copy()
    
    try:
        # 1. Standardize date columns
        date_columns = ['ReviewDate', 'CompletionDate', 'DueDate', 'SubmissionDate']
        for col in date_columns:
            if col in df.columns:
                # Handle various date formats that auditors might use
                df[col] = pd.to_datetime(df[col], errors='coerce', 
                                       format=None, dayfirst=False)
                
                # Flag records with invalid dates for manual review
                invalid_dates = df[col].isna()
                if invalid_dates.any():
                    print(f"Warning: {invalid_dates.sum()} invalid dates in column '{col}'")
        
        # 2. Standardize text fields
        text_standardization = {
            'Status': {'complete': 'COMPLETE', 'completed': 'COMPLETE', 
                      'pending': 'PENDING', 'in progress': 'IN_PROGRESS'},
            'Severity': {'high': 'HIGH', 'medium': 'MEDIUM', 'low': 'LOW', 
                        'critical': 'CRITICAL'},
            'ComplianceStatus': {'compliant': 'COMPLIANT', 'non-compliant': 'NON_COMPLIANT',
                               'not applicable': 'NOT_APPLICABLE'}
        }
        
        for col, mapping in text_standardization.items():
            if col in df.columns:
                # Convert to lowercase for matching, then map to standard values
                df[col] = df[col].str.lower().map(mapping).fillna(df[col])
        
        # 3. Clean and validate required business fields
        if 'ControlId' in df.columns:
            # Remove any non-alphanumeric characters from control IDs
            df['ControlId'] = df['ControlId'].astype(str).str.replace(r'[^A-Za-z0-9\-\.]', '', regex=True)
        
        if 'EvidenceFile' in df.columns:
            # Validate evidence file references
            df['EvidenceFile'] = df['EvidenceFile'].astype(str).str.strip()
            # Flag missing evidence files
            missing_evidence = (df['EvidenceFile'].isna()) | (df['EvidenceFile'] == '')
            if missing_evidence.any():
                print(f"Warning: {missing_evidence.sum()} records missing evidence file references")
        
        # 4. Validate reviewer information
        if 'Reviewer' in df.columns:
            df['Reviewer'] = df['Reviewer'].astype(str).str.strip()
            # Extract email addresses if present
            email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
            df['ReviewerEmail'] = df['Reviewer'].str.extract(f'({email_pattern})')
        
        # 5. Add data quality flags
        required_fields = ['ControlId', 'EvidenceFile', 'Reviewer', 'ReviewDate']
        available_required = [col for col in required_fields if col in df.columns]
        
        df['DataQualityScore'] = 0
        for col in available_required:
            # Increase quality score for each non-null required field
            df['DataQualityScore'] += (~df[col].isna()).astype(int)
        
        # Flag high-quality records (all required fields present)
        df['HighQuality'] = df['DataQualityScore'] == len(available_required)
        
        # 6. Remove completely invalid records
        # Keep only records with at least ControlId and either evidence or reviewer
        essential_data = (~df['ControlId'].isna()) if 'ControlId' in df.columns else pd.Series([True] * len(df))
        
        if 'EvidenceFile' in df.columns and 'Reviewer' in df.columns:
            has_evidence_or_reviewer = (~df['EvidenceFile'].isna()) | (~df['Reviewer'].isna())
            valid_records = essential_data & has_evidence_or_reviewer
        else:
            valid_records = essential_data
        
        invalid_count = (~valid_records).sum()
        if invalid_count > 0:
            print(f"Removing {invalid_count} records with insufficient data")
            df = df[valid_records].reset_index(drop=True)
        
        print(f"✅ Data cleansing complete. {len(df)} records ready for processing")
        print(f"   High quality records: {df['HighQuality'].sum()}/{len(df)}")
        
        return df
        
    except Exception as e:
        print(f"Error during data cleansing: {e}")
        return df

def validate_evidence_schema(df: pd.DataFrame, schema_requirements: dict) -> tuple[bool, list[str]]:
    """
    Validates that the evidence DataFrame meets specific schema requirements.
    
    Args:
        df: DataFrame to validate
        schema_requirements: Dict with column names as keys and requirements as values
                           e.g., {'ControlId': 'required', 'ReviewDate': 'datetime'}
        
    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []
    
    for column, requirement in schema_requirements.items():
        if column not in df.columns:
            if requirement == 'required':
                errors.append(f"Required column '{column}' is missing")
            continue
        
        if requirement == 'required':
            null_count = df[column].isna().sum()
            if null_count > 0:
                errors.append(f"Column '{column}' has {null_count} null values")
        
        elif requirement == 'datetime':
            try:
                pd.to_datetime(df[column], errors='raise')
            except Exception:
                errors.append(f"Column '{column}' contains invalid datetime values")
        
        elif requirement == 'email':
            email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            invalid_emails = ~df[column].str.match(email_pattern, na=False)
            if invalid_emails.any():
                errors.append(f"Column '{column}' contains {invalid_emails.sum()} invalid email addresses")
    
    return len(errors) == 0, errors

Converting Rows to JSON Payloads
To feed manual evidence into AWS APIs, convert each row into the required JSON structure:
def manual_evidence_to_aws_payloads(df: pd.DataFrame, 
                                   assessment_id: str,
                                   control_set_mapping: dict = None) -> list[dict]:
    """
    Transforms manual evidence DataFrame into AWS Audit Manager API payloads.
    
    Converts cleaned auditor spreadsheets into the specific JSON format required
    by AWS Audit Manager's batchImportEvidenceToAssessmentControl API.
    
    Args:
        df: Cleaned DataFrame from cleanse_manual_evidence()
        assessment_id: AWS Audit Manager assessment ID
        control_set_mapping: Optional mapping of ControlId to AWS control set IDs
        
    Returns:
        List of API payload dictionaries ready for batch import
    """
    payloads = []
    
    try:
        for index, row in df.iterrows():
            # Skip low-quality records
            if not row.get('HighQuality', True):
                print(f"Skipping row {index}: Low data quality")
                continue
            
            # Map to AWS control set if mapping provided
            control_id = str(row['ControlId'])
            control_set_id = control_set_mapping.get(control_id, control_id) if control_set_mapping else control_id
            
            # Build the evidence payload
            evidence_data = {
                "dataSource": "MANUAL",
                "eventSource": "Manual Evidence Upload",
                "eventName": f"ManualEvidence_{control_id}",
                "evidenceByType": "Evidence",
                "resourcesIncluded": []
            }
            
            # Add text response with reviewer information
            review_info = []
            if pd.notna(row.get('Reviewer')):
                review_info.append(f"Reviewed by: {row['Reviewer']}")
            if pd.notna(row.get('ReviewDate')):
                review_info.append(f"Review Date: {row['ReviewDate'].strftime('%Y-%m-%d')}")
            if pd.notna(row.get('EvidenceFile')):
                review_info.append(f"Evidence File: {row['EvidenceFile']}")
            if pd.notna(row.get('Comments')):
                review_info.append(f"Comments: {row['Comments']}")
            
            evidence_data["textResponse"] = " | ".join(review_info)
            
            # Add compliance assessment if available
            if pd.notna(row.get('ComplianceStatus')):
                evidence_data["complianceCheck"] = {
                    "status": row['ComplianceStatus'],
                    "checkDate": row.get('ReviewDate', datetime.now()).isoformat()
                }
            
            # Build the complete payload
            payload = {
                "assessmentId": assessment_id,
                "controlSetId": control_set_id,
                "controlId": control_id,
                "evidenceFolderId": f"manual_evidence_{control_id}_{index}",
                "evidence": evidence_data
            }
            
            payloads.append(payload)
            
        print(f"✅ Generated {len(payloads)} AWS API payloads from {len(df)} evidence records")
        return payloads
        
    except Exception as e:
        print(f"Error generating AWS payloads: {e}")
        return []

def batch_upload_evidence_to_aws(payloads: list[dict], session: boto3.Session,
                                 batch_size: int = 50) -> dict:
    """
    Uploads manual evidence payloads to AWS Audit Manager in batches.
    
    AWS API limits and rate limiting require careful batch processing.
    This function handles retries and provides detailed upload results.
    
    Args:
        payloads: List of evidence payloads from manual_evidence_to_aws_payloads()
        session: Authenticated boto3 session
        batch_size: Number of evidence items per batch (AWS limit is 50)
        
    Returns:
        Dictionary with upload results and any errors
    """
    from botocore.exceptions import ClientError
    import time
    
    client = session.client('auditmanager')
    results = {
        'successful_uploads': 0,
        'failed_uploads': 0,
        'errors': []
    }
    
    # Process in batches to respect AWS API limits
    for i in range(0, len(payloads), batch_size):
        batch = payloads[i:i + batch_size]
        
        try:
            # Call AWS Audit Manager batch import API
            response = client.batch_import_evidence_to_assessment_control(
                assessmentId=batch[0]['assessmentId'],  # All should have same assessment ID
                controlSetId=batch[0]['controlSetId'],
                controlId=batch[0]['controlId'],
                manualEvidence=[payload['evidence'] for payload in batch]
            )
            
            results['successful_uploads'] += len(batch)
            print(f"✅ Uploaded batch {i//batch_size + 1}: {len(batch)} evidence items")
            
            # Respect API rate limits
            time.sleep(1)
            
        except ClientError as e:
            error_code = e.response['Error']['Code']
            error_msg = e.response['Error']['Message']
            
            results['failed_uploads'] += len(batch)
            results['errors'].append({
                'batch_start': i,
                'batch_size': len(batch),
                'error_code': error_code,
                'error_message': error_msg
            })
            
            print(f"❌ Failed to upload batch {i//batch_size + 1}: {error_code} - {error_msg}")
            
        except Exception as e:
            results['failed_uploads'] += len(batch)
            results['errors'].append({
                'batch_start': i,
                'batch_size': len(batch),
                'error_code': 'UNKNOWN',
                'error_message': str(e)
            })
            
            print(f"❌ Unexpected error in batch {i//batch_size + 1}: {e}")
    
    return results

Handling Large Spreadsheets
If your Excel files have thousands of rows, consider reading in chunks to reduce memory usage:
def process_large_spreadsheet(path: str, chunk_size: int = 5000,
                             processing_function: callable = None) -> list:
    """
    Processes large CSV files in chunks to manage memory usage.
    
    Large auditor spreadsheets (>100k rows) can consume significant memory.
    This function processes them in manageable chunks.
    
    Args:
        path: Path to large CSV file
        chunk_size: Number of rows to process at once
        processing_function: Function to apply to each chunk
        
    Returns:
        List of results from processing each chunk
    """
    results = []
    chunk_count = 0
    
    try:
        # Use pandas chunking capability for memory efficiency
        for chunk in pd.read_csv(path, chunksize=chunk_size):
            chunk_count += 1
            print(f"Processing chunk {chunk_count} ({len(chunk)} rows)")
            
            # Clean the chunk
            clean_chunk = clean_auditor_data(chunk)
            
            # Apply custom processing if provided
            if processing_function:
                result = processing_function(clean_chunk)
                results.append(result)
            else:
                results.append(clean_chunk)
            
            # Memory cleanup
            del chunk, clean_chunk
            
        print(f"✅ Processed {chunk_count} chunks from {path}")
        return results
        
    except Exception as e:
        print(f"Error processing large spreadsheet: {e}")
        return results

def consolidate_processed_chunks(chunk_results: list, 
                               output_format: str = 'dataframe') -> pd.DataFrame:
    """
    Consolidates results from chunk processing into a single output.
    
    Args:
        chunk_results: List of DataFrames or other results from chunk processing
        output_format: 'dataframe' to combine into single DataFrame, 'separate' to keep separate
        
    Returns:
        Consolidated DataFrame or list of results
    """
    if output_format == 'dataframe' and all(isinstance(chunk, pd.DataFrame) for chunk in chunk_results):
        combined = pd.concat(chunk_results, ignore_index=True)
        print(f"✅ Consolidated {len(chunk_results)} chunks into {len(combined)} total rows")
        return combined
    
    return chunk_results

# Complete workflow example
def process_auditor_evidence_workflow(file_path: str, assessment_id: str, 
                                    aws_session: boto3.Session) -> dict:
    """
    Complete workflow for processing auditor-provided evidence files.
    
    Handles the full lifecycle from raw auditor spreadsheet to AWS Audit Manager.
    """
    try:
        # 1. Load the evidence file
        print("Step 1: Loading evidence file...")
        required_columns = ['ControlId', 'EvidenceFile', 'Reviewer', 'ReviewDate']
        
        if file_path.endswith('.csv'):
            df = load_csv(file_path, required_columns)
        else:
            df = load_excel(file_path, required_columns=required_columns)
        
        # 2. Clean and validate the data
        print("Step 2: Cleaning and validating data...")
        df_clean = cleanse_manual_evidence(df)
        
        # 3. Validate schema requirements
        schema_requirements = {
            'ControlId': 'required',
            'ReviewDate': 'datetime',
            'ReviewerEmail': 'email'
        }
        is_valid, errors = validate_evidence_schema(df_clean, schema_requirements)
        
        if not is_valid:
            print("⚠️  Schema validation warnings:")
            for error in errors:
                print(f"  - {error}")
        
        # 4. Convert to AWS payloads
        print("Step 3: Converting to AWS API format...")
        payloads = manual_evidence_to_aws_payloads(df_clean, assessment_id)
        
        # 5. Upload to AWS (if payloads were generated successfully)
        upload_results = {}
        if payloads:
            print("Step 4: Uploading to AWS Audit Manager...")
            upload_results = batch_upload_evidence_to_aws(payloads, aws_session)
        
        # 6. Generate summary report
        workflow_results = {
            'input_file': file_path,
            'records_loaded': len(df),
            'records_cleaned': len(df_clean),
            'high_quality_records': df_clean['HighQuality'].sum() if 'HighQuality' in df_clean.columns else 0,
            'payloads_generated': len(payloads),
            'upload_results': upload_results,
            'validation_errors': errors
        }
        
        print(f"\n📋 Workflow Summary:")
        print(f"  Input records: {workflow_results['records_loaded']:,}")
        print(f"  Cleaned records: {workflow_results['records_cleaned']:,}")
        print(f"  High quality: {workflow_results['high_quality_records']:,}")
        print(f"  AWS uploads: {upload_results.get('successful_uploads', 0):,}")
        
        return workflow_results
        
    except Exception as e:
        print(f"❌ Workflow failed: {e}")
        return {'error': str(e)}

Key points to understand:
File encoding issues are common: Auditor files often come from Windows systems with different character encoding
Schema validation prevents downstream errors: Always validate structure before processing thousands of records
Data quality scoring helps prioritization: Not all auditor data is perfect; focus automation on high-quality records first
Batch processing respects API limits: AWS services have rate limits; process in appropriately sized batches
Error handling preserves workflow: One bad record shouldn't prevent processing the entire spreadsheet
Key Takeaways
This chapter covered the complete data pipeline for GRC automation: fetching data from AWS security services, transforming it into analysis-ready formats, and exporting comprehensive reports for stakeholders. Here are the essential concepts to master:
Data Acquisition Mastery
Pagination is non-negotiable in enterprise AWS environments. Security Hub findings, Config evaluations, and CloudTrail events can number in the hundreds of thousands. Always use paginators to ensure complete data collection, and design your scripts to handle large volumes gracefully.
Error handling determines production readiness. AWS services experience temporary outages, rate limiting, and permission issues. Robust error handling with retry logic and graceful degradation separates professional automation from fragile scripts that break when you need them most.
Service-specific quirks require attention. Each AWS service has unique characteristics: Security Hub's complex nested JSON, Config's resource-specific evaluation results, and CloudTrail's massive event volumes. Understanding these differences helps you write more efficient and reliable code.
Data Transformation Excellence
pandas.json_normalize is your most powerful tool for handling AWS API responses. Master its parameters (record_path, meta, sep) to efficiently flatten complex nested structures into analysis-ready tables.
Business logic transforms raw data into actionable insights. Converting severity labels to numeric scores, calculating SLA violations, and deriving business impact metrics make your reports valuable to executives and operational teams, not just technical staff.
Data correlation reveals hidden patterns. Merging Security Hub findings with Config violations and CloudTrail activity provides comprehensive security insights that individual services cannot deliver alone. This correlation often reveals root causes and helps prioritize remediation efforts.
Export Strategy for Stakeholder Success
Different audiences need different formats. Technical teams can work with comprehensive CSV exports, but executives need summary sheets with key metrics. Design your exports to serve multiple stakeholder needs simultaneously.
Summary sheets add disproportionate value. Raw security data is overwhelming; analyzed insights drive action. Automatically generated summary tables showing severity distributions, trend analysis, and compliance metrics help stakeholders make informed decisions quickly.
Professional formatting matters for adoption. Auto-adjusted column widths, consistent naming conventions, and metadata headers make your reports look professional and trustworthy. These details significantly impact how stakeholders perceive and use your automation.
Ingestion and Integration Capabilities
Auditor data requires significant cleaning. Spreadsheets from external auditors typically need extensive preprocessing: encoding fixes, column standardization, date parsing, and data quality validation. Build robust cleaning pipelines that handle common issues automatically.
Schema validation prevents downstream failures. Always validate incoming data structure before processing. Clear error messages about missing columns or invalid formats help auditors fix their submissions rather than guessing what went wrong.
Batch processing respects API constraints. AWS services have rate limits and batch size restrictions. Design your upload processes to work within these constraints while providing clear progress feedback and error handling.
Production Readiness Considerations
Memory management becomes critical at scale. Large organizations generate millions of security events. Use chunked processing for large datasets and implement proper cleanup to prevent memory exhaustion in long-running scripts.
Monitoring and observability enable reliability. Add comprehensive logging, progress indicators, and result summaries to your scripts. When automation runs in production environments, operators need visibility into what happened and why.
Configuration management supports multiple environments. Hard-coded values limit reusability. Use configuration files or environment variables for AWS profiles, file paths, and business logic parameters so your scripts work across development, staging, and production environments.
Strategic Impact
Automation enables continuous compliance rather than point-in-time snapshots. Monthly automated reports provide better security posture visibility than quarterly manual reviews, and they're significantly cheaper to produce.
Data standardization facilitates integration. Consistent column naming, date formats, and categorical values across all your exports make it easier to build dashboards, integrate with other tools, and perform historical analysis.
Stakeholder-specific outputs drive adoption. The most technically perfect automation fails if stakeholders don't find it useful. Design exports that answer specific questions your auditors, executives, and operational teams actually have, not just what the APIs make available.
The techniques in this chapter form the foundation for scalable GRC automation.
Chapter 9: The FAFO Case Study From Meeting-Heavy SOC 2 Audits to a Self-Documenting Cloud
"You're the new Director of GRC. We can't buy an off-the-shelf platform, but we must pass SOC 2 again without hijacking Engineering time." — VP of Engineering, FAFO, Inc.
Chapters 4 through 8 taught you the building blocks:
AWS Config, Security Hub, CloudTrail, and Audit Manager for continuous evidence collection
Service Control Policies (SCPs) and Infrastructure as Code for secure baselines
Event-driven Lambdas to catch and fix problems quickly
Python + boto3 to tie everything together in auditable code
Now we combine these pieces into one real-world story that shows how these technologies transform painful audits into smooth, automated processes.
The Scenario 
You just joined FAFO, Inc., a fast-growing SaaS company running on AWS Organizations with multiple AWS accounts. Last year's SOC 2 Type II audit almost killed their product roadmap:
Metric
2024 Audit Cost
Prep meetings (pre-audit, on-site, follow-up)
15 sessions
Engineer hours diverted from product work
≈380 hours
Findings that could have been auto-detected
23 of 31

Leadership hired you to cut that burden in half, but there's no budget for a commercial GRC platform. Your only tools are:
Native AWS services (Security Hub, Config, Audit Manager, EventBridge, Lambda, S3)
Open-source scripts (Python, boto3, GitLab CI/CD)
A helpful but busy Security Operations team that already runs GuardDuty, Security Hub, and centralized logging
This chapter concentrates on SOC 2 families that work best with automation:
Logical & Physical Access (CC 6)
Change Management (CC 7)
System Operations (CC 8)
Availability (A-series)
Confidentiality (C-series)
Twenty-eight controls, one cloud platform, zero extra licenses. Let's see how a modern GRC engineer turns last year's audit pain into a self-documenting, event-driven compliance system.
The foundation of automated SOC 2 compliance lies in leveraging AWS's built-in security standards as your evidence source. Instead of manually documenting security configurations, you'll enable automated checks that continuously validate compliance and generate auditable evidence. We will be focusing on two built-in security standards. 
AWS Foundational Security Best Practices (FSBP)
Written by internal AWS security engineers based on real customer incident data
Covers common misconfigurations leading to most customer-side security breaches (open S3 buckets, weak IAM policies, unencrypted volumes, etc.)
Updated several times per year with each control including specific remediation steps within the Security Hub finding
Provides immediate, actionable guidance that auditors value for their practicality
CIS AWS Foundations Benchmark v1.4
Published by the Center for Internet Security (CIS), an independent nonprofit maintaining security best-practice guides for various platforms
Slightly stricter than FSBP in areas such as CloudTrail log validation, root-account protections, and network port exposure
Widely adopted by auditors as a de facto baseline, allowing SOC 2 control mappings to CIS checks to streamline evidence discussions
Carries significant credibility with external auditors due to CIS's reputation for rigorous security standards
Security Hub implements both benchmarks as standards. Enabling a standard activates each individual check as a Security Hub control that produces pass/fail findings every 12 hours or faster for some services. Those findings automatically stream to EventBridge and, in our design, flow directly into Audit Manager for evidence collection.
The Critical Difference Reminder: Security Hub vs. Config
AWS Config overlaps with but is not identical to Security Hub:
Security Hub provides the latest result each time a check runs. Showing current compliance state.
AWS Config maintains a timeline of every compliance state change. Showing compliance history and duration of violations.
Auditors need both perspectives. Security Hub identifies when a control failed (point-in-time compliance). Config indicates how long it remained failed (compliance duration for SLA tracking). Enabling corresponding Config managed rules for each Security Hub control provides this historical view without requiring custom Lambda code or complex data correlation.
Step 1: Enable, then prune systematically
FSBP plus CIS totals more than 200 individual controls. Activating every check without strategic triage will overwhelm your Security Operations team with noise and discourage ongoing engagement. At FAFO, we developed this systematic approach:
Initial activation: Enable the entire standard in the Security account's administrator region
Baseline assessment: Run all checks for one full business day to collect representative data
Export and analyze: Export all FAILED findings to CSV and sort by control ID for systematic review
Map to requirements: Compare the complete findings list to your 28 target SOC 2 criteria
Strategic pruning: Disable every control that does not support at least one SOC 2 criterion or critical internal security policy
Disabling a control in Security Hub is accomplished through the BatchUpdateStandardsControlAssociations API call. 
This immediately stops new findings for that control, significantly reducing operational noise while maintaining focus on audit-relevant security posture.
# Disable non-relevant Security Hub controls using AWS CLI
aws securityhub batch-update-standards-control-associations \
  --standards-control-association-updates '[
    {
      "StandardsControlArn": "arn:aws:securityhub:us-east-1:123456789012:control/aws-foundational-security-best-practices/v/1.0.0/EC2.2", 
      "AssociationStatus": "DISABLED",
      "UpdatedReason": "Control does not apply to current environment. Classic ELBs not in use. Disabled to reduce false positives and focus on relevant security controls."
    }
  ]'

To identify which controls to disable, first retrieve all available control ARNs:
# List all controls in a standard to identify candidates for disabling
aws securityhub describe-standards-controls \
  --standards-subscription-arn arn:aws:securityhub:us-east-1:123456789012:subscription/aws-foundational-security-best-practices/v/1.0.0

Step 2: Mirror the final set in AWS Config
Each Security Hub control references an underlying Config rule that provides the compliance evaluation logic. After pruning Security Hub controls, ensure the corresponding Config rules are enabled in your organization-wide conformance pack. This synchronization ensures consistent evidence collection between Security Hub (current state) and Config (historical timeline).
Step 3: Capture and document the rationale
Auditors will inquire why certain controls, such as ELB.5 – Classic Load Balancer Listener Security, are disabled. Proactively store concise, business-relevant justifications as Management Response manual evidence within your SOC 2 assessment in Audit Manager.
Example rationale that auditors appreciate:
"Control ELB.5 (Classic Load Balancer Listener Security) disabled because FAFO migrated all load balancers to Application Load Balancers (ALB) in Q2 2024. No Classic ELBs remain in production. Control disabled to prevent false positive findings and focus monitoring on relevant infrastructure."
This approach keeps the rationale directly adjacent to evidence, streamlining audit fieldwork and eliminating the need to search through emails or documentation during audit interviews.
Mapping of the Automatable SOC 2 Controls
This comprehensive mapping demonstrates how AWS-native services can provide evidence for the majority of SOC 2 technical controls:
SOC 2 Criterion
Sample Control Title
AWS Evidence Source
Benchmark/Rule ID
Evidence Type
CC 6.1.2
Multi-Factor Authentication
Security Hub findings IAM.2 (root MFA) and IAM.3 (user MFA)
FSBP
Automated
CC 6.1.4
Firewalls/Security Groups
Config rule vpc-default-security-group-closed and Security Hub EC2.2
CIS
Automated
CC 6.1.6
TLS Encryption in Transit
Security Hub ELB.1, CloudFront.1, API Gateway controls
FSBP
Automated
CC 6.1.7
Database Encryption
Security Hub RDS.3, Config rds-storage-encrypted
FSBP
Automated
CC 6.1.10
Data Encryption at Rest
Security Hub S3.2, EBS.2; Config encrypted-volumes
FSBP
Automated
CC 6.6.2
Security Monitoring
GuardDuty integrated into Security Hub; findings feed Audit Manager
GuardDuty
Automated
CC 6.6.3
Intrusion Detection/Prevention
WAF logging rule wafv2-web-acl-log-enabled; Security Hub WAFV2.1
FSBP
Automated
CC 7.2
DAST Scanning
GitLab DAST Pipeline results converted to ASFF format
Git Integration
Semi-automated
CC 8.1.5
Automated Code Scanning
GitLab SAST results converted to ASFF format
Git Integration
Semi-automated
CC 9.1.3
Database High Availability
Config rule rds-multi-az-support
FSBP
Automated
A 1.1.2
Autoscaling Enabled
Config rule autoscaling-group-elb-healthcheck
FSBP
Automated
A 1.2.1
Backup Configuration
Config rule backup-plan-min-frequency-and-min-retention
FSBP
Automated

Note: This table shows 12 of the 28 controls for brevity. The complete mapping spreadsheet is available in the book's GitHub repository.
Key insights from this mapping:
Real-time evidence: Most automated controls provide evidence within 12 hours of configuration changes
Auditor credibility: AWS-managed rules carry higher auditor confidence than custom implementations
Remediation guidance: Each finding includes specific remediation steps, reducing follow-up questions
Any SOC 2 criteria remaining unaddressed after this systematic mapping become either manual procedures (documented in Audit Manager) or stretch goals for the next compliance automation iteration.
Setting Up AWS Audit Manager: Creating Your Custom SOC 2 Framework
Before you can automate evidence collection, you need to set up AWS Audit Manager with a custom SOC 2 framework that maps to your specific control requirements. This is a one-time setup process that creates the foundation for all your automated compliance work.
Why Create a Custom Framework?
While AWS Audit Manager includes pre-built frameworks for common standards, creating a custom SOC 2 framework gives you several advantages:
Precise control mapping: Map each control exactly to the AWS services and data sources you've enabled
Tailored evidence collection: Focus evidence gathering on your specific environment and requirements
Clear audit trail: Document exactly how each control is validated and what evidence supports it
Streamlined assessments: Include only the controls relevant to your organization's scope
Step 1: Access AWS Audit Manager and Create Your Framework
Navigate to the AWS Audit Manager console in your primary region (us-east-1 for FAFO). If this is your first time using Audit Manager, you'll need to enable the service and set up basic configuration.
Enable Audit Manager:
Go to AWS Audit Manager in the console
Click "Get started" and complete the initial setup
Choose your evidence bucket (or let AWS create one)
Enable data collection from Security Hub, Config, and CloudTrail
Create a New Custom Framework:
Navigate to "Framework library" in the left sidebar
Click "Create custom framework"
Choose "Create a completely custom framework"
Step 2: Configure Framework Details
Fill in the basic framework information:
Framework Name: FAFO SOC 2 Type II Custom Framework
Description: Custom SOC 2 framework tailored for FAFO's AWS environment with automated evidence collection from Security Hub, Config, and GitLab CI/CD integration.
Industry: Technology
Compliance Type: SOC 2 Type II
Step 3: Create Control Sets and Individual Controls
You'll organize your 28 controls into logical control sets that match SOC 2 structure. Here are examples of how to set up key controls:
Control Set: CC6 - Logical and Physical Access Controls
Click "Add control set" and enter:
Control Set Name: CC6 - Logical and Physical Access Controls
Description: Controls related to logical and physical access restrictions
Example Control CC6.1.2 - Multi-Factor Authentication
Click "Add control" within the CC6 control set:
Control Name: CC6.1.2 - Multi-Factor Authentication
Description: The entity requires multi-factor authentication for all user access to systems and data.
Control Objective: Ensure all user accounts require multi-factor authentication to access AWS resources and applications.
Test Procedures:
Verify AWS root account has MFA enabled via Security Hub finding IAM.2
Confirm all IAM users have MFA enabled via Security Hub finding IAM.3
Validate Service Control Policies prevent console access without MFA
Testing Frequency: Continuous (automated daily via Security Hub)
Example Control CC6.1.10 - Data Encryption at Rest
Control Name: CC6.1.10 - Data Encryption at Rest
Description: The entity encrypts data at rest to protect sensitive information from unauthorized access.
Control Objective: Ensure all data stored in AWS services is encrypted using appropriate encryption standards.
Test Procedures:
Verify S3 buckets have server-side encryption enabled via Security Hub finding S3.4
Confirm EBS volumes are encrypted via Security Hub finding EBS.1
Review encryption compliance via Config rule encrypted-volumes
Testing Frequency: Continuous (automated daily via Security Hub and Config)
Note: The complete control definitions for all 28 controls are available in the GitHub repository at https://github.com/ajy0127/thegrcengineeringbook with detailed test procedures, evidence sources, and configuration examples.
Step 4: Configure Automated Data Sources
For each control that uses AWS-native services, you'll configure the automated data sources to pull from the specific FSBP and CIS controls you enabled in Security Hub. Here are examples:
For Control CC6.1.2 - Multi-Factor Authentication:
Primary Data Source - AWS Security Hub (FSBP):
Data Source Type: AWS Security Hub
Source Name: FSBP IAM Controls
Source Description: Automated MFA compliance checks from AWS Foundational Security Best Practices
Keywords: IAM.2, IAM.3
Frequency: Daily
Secondary Data Source - AWS Config:
Data Source Type: AWS Config
Source Name: IAM MFA Config Rules
Source Description: Historical compliance tracking for MFA requirements
Keywords: iam-user-mfa-enabled, root-access-key-check
Frequency: Daily
For Control CC6.1.10 - Data Encryption at Rest:
Primary Data Source - AWS Security Hub (FSBP):
Data Source Type: AWS Security Hub
Source Name: FSBP Data at Rest Encryption
Source Description: Data encryption compliance from AWS Foundational Security Best Practices
Keywords: S3.4, EBS.1, RDS.3
Frequency: Daily
Secondary Data Source - AWS Config:
Data Source Type: AWS Config
Source Name: Encryption Config Rules
Source Description: Historical encryption compliance tracking
Keywords: encrypted-volumes, s3-bucket-server-side-encryption-enabled
Frequency: Daily
Important Configuration Notes:
Keyword Matching: The keywords you enter must exactly match the finding types generated by Security Hub. Use the Control IDs from FSBP (like IAM.2, S3.4) and CIS (like EC2.2) that you enabled earlier.
Data Source Priority: List AWS Security Hub as the primary source for automated controls, and AWS Config as secondary for historical tracking.
Complete Configuration: The full data source configuration for all 28 controls is provided in the GitHub repository with exact keywords, descriptions, and frequency settings.
Step 5: Create Your SOC 2 Assessment
Once your custom framework is complete, create an assessment:
Navigate to Assessments:
Go to "Assessments" in the left sidebar
Click "Create assessment"
Configure Assessment Details:
Assessment Name: FAFO SOC 2 Type II Assessment 2025
Description: Annual SOC 2 Type II assessment using automated evidence collection
Assessment Owner: [Your email]
Assessment Roles: Add relevant stakeholders
Framework: FAFO SOC 2 Type II Custom Framework (select your custom framework)
Set Assessment Scope:
Include all relevant AWS accounts in your organization
Set assessment period (typically 12 months for SOC 2 Type II)
Configure evidence collection start date
Complete Assessment Creation:
Review settings and create the assessment
Copy the Assessment ID - you'll need this for your Lambda reporting function and GitLab integration
The Assessment ID will look like: 12345678-abcd-efgh-ijkl-1234567890ab
Step 6: Verify Evidence Collection
After creating your assessment, wait 24-48 hours for initial evidence collection, then verify everything is working:
Navigate to your assessment and check that evidence folders are being created
Verify that Security Hub findings are populating in the relevant controls
Confirm that Config rule evaluations are appearing as evidence
Test that the data source keywords are matching findings correctly
What You've Accomplished
With your custom framework and assessment configured, you now have:
A SOC 2 framework tailored specifically to your AWS environment
Automated evidence collection from Security Hub and Config for 24+ controls
A foundation ready for GitLab integration and automated reporting
An Assessment ID that ties everything together for your Lambda functions
The next sections will show you how to integrate GitLab security scanning and build automated weekly reports using this Assessment ID.
Git Integration: Closing the Gap on Application Security
While Security Hub and AWS Config provide comprehensive coverage for infrastructure and AWS-managed services, a critical layer cannot be ignored: the application code itself. Most SOC 2 audits extend deeply into your Software Development Lifecycle (SDLC) practices, requiring evidence of vulnerability scanning, code security reviews, and continuous security testing.
FAFO relies on GitLab CI/CD pipelines where the DevSecOps team already performs automated Static Application Security Testing (SAST) and Dynamic Application Security Testing (DAST) for vulnerabilities. The strategic challenge becomes integrating those application-layer security scans seamlessly into the same evidence repository (Audit Manager) as your AWS infrastructure checks.
Why Git Integration is Mission-Critical
SOC 2 auditors expect consistency and completeness across your organization's security practices. They look for evidence that security is embedded throughout your development process, not just in your infrastructure. Integrating GitLab security findings into Audit Manager delivers several critical audit advantages:
Unified evidence trail: Auditors access both infrastructure and application security evidence from a single, authoritative source rather than juggling multiple tools and reports
Continuous validation: Every code commit triggers security scans that automatically feed into your compliance evidence stream, proving ongoing rather than point-in-time security testing
Engineering time protection: Eliminates the burden on Engineering and Security teams to manually document, export, or explain application security findings during audit fieldwork
Evidence freshness: Application security evidence stays current, automatically, with timestamps and traceability that auditors can verify independently
AWS Security Hub consumes security findings via a standardized JSON schema called the Amazon Security Finding Format (ASFF). This format structures security findings so Security Hub can ingest them, normalize their severity ratings, link them to AWS resources, and route them automatically to Audit Manager for compliance evidence.
Your GitLab SAST and DAST reports are already in JSON format, but they use GitLab's proprietary schema. The integration strategy transforms your existing DevSecOps pipeline:
Extract existing scan results: Capture SAST and DAST JSON reports from your current GitLab pipelines
Transform to AWS standard: Convert GitLab JSON schema to ASFF format using Python transformation scripts
Import to Security Hub: Send ASFF-formatted findings into Security Hub using the AWS SDK
Automatic routing: Allow Security Hub to auto-route application security findings into Audit Manager alongside infrastructure evidence
This approach leverages your engineering and security teams existing GitLab investment while creating audit-grade evidence traceability without disrupting current development workflows.
Implementing the Integration in Your GitLab Pipeline
Step 1: Extract GitLab security scan results
Your existing GitLab CI/CD pipeline already generates SAST and DAST reports as JSON artifacts. These typically write to standardized filenames like gl-sast-report.json and gl-dast-report.json. 
Step 2: Transform GitLab JSON into ASFF format
Create a Python script (gitlab_to_asff.py) that handles the schema transformation, severity mapping, and AWS integration. This script runs after GitLab completes security scans but before the deployment stage.
import json
import boto3
import datetime

def load_gitlab_findings(filename):
    """Load GitLab security scan results from JSON report file."""
    try:
        with open(filename, 'r') as f:
            gitlab_report = json.load(f)
        return gitlab_report.get('vulnerabilities', [])
    except FileNotFoundError:
        print(f"No {filename} found, skipping...")
        return []

def transform_to_asff(finding, product_name, region, aws_account):
    """Transform GitLab finding to ASFF format for Security Hub."""
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    
    # Map GitLab severity to AWS Security Hub severity
    severity_map = {
        "Critical": "CRITICAL",
        "High": "HIGH", 
        "Medium": "MEDIUM",
        "Low": "LOW",
        "Info": "INFORMATIONAL"
    }
    
    return {
        "SchemaVersion": "2018-10-08",
        "Id": f"{product_name}-{finding.get('id', 'unknown')}",
        "ProductArn": f"arn:aws:securityhub:{region}:{aws_account}:product/{aws_account}/default",
        "GeneratorId": f"{product_name}-Scanner",
        "AwsAccountId": aws_account,
        "Types": ["Software and Configuration Checks/Vulnerabilities"],
        "CreatedAt": now,
        "UpdatedAt": now,
        "Severity": {
            "Label": severity_map.get(finding.get('severity', 'Unknown'), "INFORMATIONAL")
        },
        "Title": finding.get('name', f"{product_name} Security Finding"),
        "Description": finding.get('description', 'Security vulnerability detected'),
        "Resources": [{
            "Type": "Other",
            "Id": finding.get('location', {}).get('file', 'Unknown file')
        }],
        "Remediation": {
            "Recommendation": {
                "Text": finding.get('solution', 'Review GitLab security report for remediation guidance')
            }
        },
        "RecordState": "ACTIVE",
        "WorkflowState": "NEW"
    }

def send_to_security_hub(asff_findings, region='us-east-1'):
    """Send ASFF findings to AWS Security Hub."""
    if not asff_findings:
        print("No findings to send to Security Hub")
        return
    
    sh_client = boto3.client('securityhub', region_name=region)
    
    # Security Hub accepts max 100 findings per batch
    batch_size = 100
    for i in range(0, len(asff_findings), batch_size):
        batch = asff_findings[i:i + batch_size]
        response = sh_client.batch_import_findings(Findings=batch)
        print(f"Sent batch {i//batch_size + 1}: {response['SuccessCount']} successful, {response['FailureCount']} failed")

if __name__ == "__main__":
    region = 'us-east-1'
    aws_account = '123456789012'  # Replace with your AWS Account ID
    
    # Load and transform SAST findings
    sast_findings = load_gitlab_findings('gl-sast-report.json')
    dast_findings = load_gitlab_findings('gl-dast-report.json')
    
    all_findings_asff = []
    
    for finding in sast_findings:
        all_findings_asff.append(transform_to_asff(finding, "GitLab-SAST", region, aws_account))
    
    for finding in dast_findings:
        all_findings_asff.append(transform_to_asff(finding, "GitLab-DAST", region, aws_account))
    
    if all_findings_asff:
        send_to_security_hub(all_findings_asff, region)
        print(f"Successfully processed {len(all_findings_asff)} security findings")
    else:
        print("No security findings detected in scans")

Step 3: Configure AWS IAM Permissions and GitLab CI/CD Variables
Before your GitLab pipeline can send findings to AWS Security Hub, you need to create an IAM role with minimal permissions and configure GitLab with the necessary credentials.
Create a dedicated IAM role for GitLab integration:
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "SecurityHubImportFindings",
            "Effect": "Allow",
            "Action": [
                "securityhub:BatchImportFindings"
            ],
            "Resource": "*"
        },
        {
            "Sid": "GetCallerIdentityForValidation",
            "Effect": "Allow",
            "Action": [
                "sts:GetCallerIdentity"
            ],
            "Resource": "*"
        }
    ]
}

This policy follows the principle of least privilege by granting only:
securityhub:BatchImportFindings - Required to upload findings to Security Hub
sts:GetCallerIdentity - Allows the script to verify credentials are working
Create an IAM user (or preferably, use OIDC if your GitLab supports it) and attach this policy. Then configure the following variables in your GitLab project's CI/CD settings (Settings → CI/CD → Variables):
Variable Name
Value
Protected
Masked
AWS_ACCESS_KEY_ID
[Your IAM user access key]
✓
✓
AWS_SECRET_ACCESS_KEY
[Your IAM user secret key]
✓
✓
AWS_DEFAULT_REGION
us-east-1
✓


AWS_ACCOUNT_ID
123456789012
✓



Security best practices for credential management:
Use GitLab's protected and masked variable features for AWS credentials
Consider using AWS IAM roles for GitLab runners instead of long-term access keys if your GitLab instance supports OIDC
Rotate access keys regularly and monitor their usage in CloudTrail
Limit the IAM permissions to only securityhub:BatchImportFindings for the integration user
Step 4: Integrate the transformation into your GitLab pipeline
Add a new CI/CD job that executes the Python transformation script after SAST and DAST complete:
# Add this job to your .gitlab-ci.yml after the security_scan stage
send_to_securityhub:
  stage: security_scan
  image: python:3.11-slim
  before_script:
    # Install required dependencies
    - pip install boto3
    # Configure AWS credentials from GitLab CI/CD variables
    - export AWS_ACCESS_KEY_ID="${AWS_ACCESS_KEY_ID}"
    - export AWS_SECRET_ACCESS_KEY="${AWS_SECRET_ACCESS_KEY}"
    - export AWS_DEFAULT_REGION="${AWS_DEFAULT_REGION}"
  script:
    - echo "Transforming GitLab security findings to AWS Security Hub format"
    - python gitlab_to_asff.py
  dependencies:
    - sast
    - dast
  # Allow deployment to continue even if Security Hub import fails
  allow_failure: true
  # Only run on main branches to avoid overwhelming Security Hub
  only:
    - main
    - staging  
    - production


What Auditors Experience: Clear, Consistent Evidence
This Git integration transforms the auditor experience by providing streamlined, highly credible evidence that demonstrates continuous application security practices:
Evidence timeliness and freshness: Security findings upload immediately upon scan completion, with precise timestamps showing when vulnerabilities were detected and when they were resolved
Centralized, unified visibility: All security evidence, both infrastructure (from AWS services) and application (from GitLab), appears together in AWS Audit Manager
Complete audit traceability: Each Security Hub finding includes detailed metadata showing the scan type, repository location, affected files, and remediation guidance
Automated compliance mapping: Findings automatically map to relevant SOC 2 criteria (CC7.2 for DAST, CC8.1.5 for SAST)
Implementation Considerations
AWS IAM permissions: Your GitLab CI/CD runners require specific IAM permissions to import findings into Security Hub. Create a dedicated IAM user with minimal permissions (securityhub:BatchImportFindings)
API rate limiting: AWS Security Hub enforces rate limits. The script handles this by batching findings into groups of 100
Finding validation: Before deploying to production, manually compare a few GitLab findings with their ASFF equivalents in Security Hub to verify accuracy
Volume considerations: Large applications may generate hundreds of findings per scan. Consider filtering low-priority findings before import
At FAFO, this GitLab integration eliminated one of the most painful aspects of SOC 2 audits: manually documenting and explaining application security practices. Auditors now have self-service access to real-time application security evidence, and engineers reclaim time previously spent creating audit artifacts.
Weekly Audit Reports: Automating the Last Mile
Having automated infrastructure evidence through Security Hub and Config, and integrated application-layer vulnerabilities from GitLab, FAFO's GRC team faces one final challenge: 
Packaging this continuous evidence stream into auditor-friendly reports that eliminate manual preparation work.
During previous audit seasons, FAFO's experience looked like this:
Engineers interrupted: Pulled away from sprint reviews and development work to answer audit questions
GRC team scrambling: Manually gathering, formatting, and explaining evidence across multiple AWS services
Auditors frustrated: Chasing teams for updates, clarifications, and inconsistent formatting across evidence types
Your solution eliminates all these pain points through automation. You'll create a "Friday Excel" Lambda function. An automated, weekly reporting system that:
Queries Audit Manager for the latest control evidence across all SOC 2 criteria
Formats evidence into clearly structured Excel workbooks with executive summaries and detailed findings
Delivers reports automatically via S3 storage with optional email notifications
Requires zero human intervention after initial setup
No meetings. No manual evidence gathering. No engineering interruptions. Fully automated audit readiness.
Your goal as FAFO's GRC Director is clear: reduce engineer-hours spent on audits by at least 50% while improving audit quality and auditor satisfaction. This automated reporting Lambda serves as your secret weapon because it addresses the most common auditor frustration:
"Great, you have continuous evidence collection, but how do I access and analyze it efficiently during fieldwork?"
By transforming raw AWS compliance data into structured, professional Excel reports, auditors can:
Verify compliance at a glance without needing AWS console access or technical expertise
Identify non-compliant items quickly with clear remediation guidance included
Track compliance trends over time through consistent weekly snapshots
Work independently without requiring engineering or DevOps support during audit fieldwork
This automation positions you as a strategic partner who enables efficient audits rather than a bottleneck that slows them down.
Lambda Implementation: Comprehensive Report Generation
Here's the complete implementation for your weekly audit reporting system:
"""
FAFO Weekly Audit Report Generator

Automated Lambda function that queries AWS Audit Manager for SOC 2 compliance evidence
and generates professionally formatted Excel reports for external auditors.
"""

import json
import boto3
import pandas as pd
from datetime import datetime, timedelta
from io import BytesIO
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AuditReportGenerator:
    """Generates comprehensive SOC 2 audit reports from AWS Audit Manager evidence."""
    
    def __init__(self, region='us-east-1'):
        self.region = region
        self.audit_manager = boto3.client('auditmanager', region_name=region)
        self.s3 = boto3.client('s3', region_name=region)
        self.ses = boto3.client('ses', region_name=region)
        
        # Configuration - these should come from environment variables in production
        self.assessment_id = "12345678-abcd-efgh-ijkl-1234567890ab"  # Your SOC 2 assessment ID
        self.s3_bucket = "fafo-audit-reports"
        self.report_recipients = [
            "auditor@external-firm.com",
            "grc-team@fafo.com", 
            "vp-engineering@fafo.com"
        ]
    
    def fetch_assessment_evidence(self):
        """Retrieve complete assessment evidence from AWS Audit Manager."""
        try:
            logger.info(f"Fetching assessment {self.assessment_id}")
            response = self.audit_manager.get_assessment(assessmentId=self.assessment_id)
            assessment = response['assessment']
            
            control_sets = assessment['framework']['controlSets']
            logger.info(f"Retrieved assessment with {len(control_sets)} control sets")
            
            return assessment
        except Exception as e:
            logger.error(f"Error fetching assessment: {e}")
            raise
    
    def collect_evidence_by_control(self, control_sets):
        """Collect the latest evidence for each SOC 2 control."""
        evidence_records = []
        current_date = datetime.utcnow()
        
        # Look for evidence from the last 7 days
        evidence_cutoff = (current_date - timedelta(days=7)).strftime('%Y-%m-%d')
        
        for control_set in control_sets:
            control_set_id = control_set['id']
            control_set_name = control_set.get('name', f'Control Set {control_set_id}')
            
            logger.info(f"Processing control set: {control_set_name}")
            
            for control in control_set.get('controls', []):
                control_id = control['id']
                control_name = control.get('name', f'Control {control_id}')
                
                try:
                    # Get evidence folders for this control
                    folders_response = self.audit_manager.get_evidence_folders_by_assessment_control(
                        assessmentId=self.assessment_id,
                        controlSetId=control_set_id,
                        controlId=control_id
                    )
                    
                    evidence_folders = folders_response.get('evidenceFolders', [])
                    
                    # Find the most recent evidence folder
                    recent_folder = None
                    for folder in evidence_folders:
                        folder_date = folder.get('date', '')
                        if folder_date >= evidence_cutoff:
                            if not recent_folder or folder_date > recent_folder.get('date', ''):
                                recent_folder = folder
                    
                    if not recent_folder and evidence_folders:
                        # No recent evidence - use the latest available
                        recent_folder = max(evidence_folders, key=lambda x: x.get('date', ''))
                    
                    if recent_folder:
                        # Get evidence items from the folder
                        evidence_items = self._fetch_evidence_items(
                            control_set_id, control_id, recent_folder['id']
                        )
                        
                        for evidence in evidence_items:
                            evidence_record = {
                                'ControlSetName': control_set_name,
                                'ControlId': control_id,
                                'ControlName': control_name,
                                'EvidenceDate': recent_folder.get('date', 'Unknown'),
                                'EvidenceType': evidence.get('dataSource', 'Unknown'),
                                'ComplianceStatus': self._determine_compliance_status(evidence),
                                'Finding': evidence.get('textResponse', ''),
                                'ResourceArn': self._extract_resource_arn(evidence),
                                'Severity': self._extract_severity(evidence)
                            }
                            evidence_records.append(evidence_record)
                    
                    else:
                        # No evidence available - create placeholder
                        evidence_records.append({
                            'ControlSetName': control_set_name,
                            'ControlId': control_id,
                            'ControlName': control_name,
                            'EvidenceDate': 'No Evidence',
                            'EvidenceType': 'Manual Review Required',
                            'ComplianceStatus': 'UNKNOWN',
                            'Finding': 'No automated evidence available',
                            'ResourceArn': 'N/A',
                            'Severity': 'LOW'
                        })
                
                except Exception as e:
                    logger.warning(f"Error processing control {control_id}: {e}")
                    continue
        
        logger.info(f"Collected {len(evidence_records)} evidence records")
        return evidence_records
    
    def _fetch_evidence_items(self, control_set_id, control_id, evidence_folder_id):
        """Fetch individual evidence items from a folder."""
        try:
            response = self.audit_manager.get_evidence_by_evidence_folder(
                assessmentId=self.assessment_id,
                controlSetId=control_set_id,
                evidenceFolderId=evidence_folder_id
            )
            return response.get('evidence', [])
        except Exception as e:
            logger.warning(f"Error fetching evidence items: {e}")
            return []
    
    def _determine_compliance_status(self, evidence):
        """Determine compliance status from evidence data."""
        # Check explicit compliance check result
        compliance_check = evidence.get('complianceCheck', {})
        if compliance_check:
            return compliance_check.get('result', 'UNKNOWN').upper()
        
        # Infer from evidence attributes
        attributes = evidence.get('attributes', {})
        
        if 'findingComplianceStatus' in attributes:
            status = attributes['findingComplianceStatus'].upper()
            if status in ['PASSED', 'FAILED', 'WARNING']:
                return status
        
        return 'UNKNOWN'
    
    def _extract_resource_arn(self, evidence):
        """Extract AWS resource ARN from evidence."""
        resources = evidence.get('resourcesIncluded', [])
        if resources and len(resources) > 0:
            return resources[0].get('arn', 'N/A')
        return 'N/A'
    
    def _extract_severity(self, evidence):
        """Extract severity level from evidence."""
        attributes = evidence.get('attributes', {})
        
        if 'findingSeverity' in attributes:
            return attributes['findingSeverity'].upper()
        
        # Default severity based on compliance status
        compliance_status = self._determine_compliance_status(evidence)
        if compliance_status == 'FAILED':
            return 'MEDIUM'
        elif compliance_status == 'WARNING':
            return 'LOW'
        
        return 'INFORMATIONAL'
    
    def generate_excel_reports(self, evidence_records):
        """Generate comprehensive Excel workbook with multiple sheets."""
        df = pd.DataFrame(evidence_records)
        
        if df.empty:
            logger.warning("No evidence records to process")
            df = pd.DataFrame([{
                'ControlSetName': 'No Evidence',
                'ControlId': 'N/A', 
                'ControlName': 'No Evidence Available',
                'EvidenceDate': datetime.now().strftime('%Y-%m-%d'),
                'ComplianceStatus': 'UNKNOWN'
            }])
        
        # Create Excel workbook
        excel_buffer = BytesIO()
        
        with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
            # Executive Summary Sheet
            self._create_executive_summary_sheet(df, writer)
            
            # Control Status Overview
            self._create_control_status_sheet(df, writer)
            
            # Failed Findings Detail
            self._create_failed_findings_sheet(df, writer)
            
            # Complete Evidence Inventory
            df.to_excel(writer, sheet_name='Evidence Details', index=False)
        
        excel_buffer.seek(0)
        return excel_buffer
    
    def _create_executive_summary_sheet(self, df, writer):
        """Create executive-level summary with key metrics."""
        total_controls = df['ControlId'].nunique()
        passed_controls = df[df['ComplianceStatus'] == 'PASSED']['ControlId'].nunique()
        failed_controls = df[df['ComplianceStatus'] == 'FAILED']['ControlId'].nunique()
        
        compliance_rate = (passed_controls / total_controls * 100) if total_controls > 0 else 0
        
        summary_data = {
            'Metric': [
                'Total SOC 2 Controls Evaluated',
                'Controls Passing',
                'Controls Failing',
                'Overall Compliance Rate (%)',
                'Report Generation Date'
            ],
            'Value': [
                total_controls,
                passed_controls,
                failed_controls,
                f"{compliance_rate:.1f}%",
                datetime.now().strftime('%Y-%m-%d %H:%M UTC')
            ]
        }
        
        summary_df = pd.DataFrame(summary_data)
        summary_df.to_excel(writer, sheet_name='Executive Summary', index=False)
    
    def _create_control_status_sheet(self, df, writer):
        """Create detailed control-by-control status overview."""
        control_status = df.groupby(['ControlSetName', 'ControlId', 'ControlName']).agg({
            'ComplianceStatus': 'first',
            'EvidenceDate': 'max',
            'EvidenceType': 'first'
        }).reset_index()
        
        control_status = control_status.sort_values(['ControlSetName', 'ControlId'])
        control_status.to_excel(writer, sheet_name='Control Status', index=False)
    
    def _create_failed_findings_sheet(self, df, writer):
        """Create detailed sheet for non-compliant findings."""
        failed_findings = df[df['ComplianceStatus'].isin(['FAILED', 'WARNING'])].copy()
        
        if not failed_findings.empty:
            # Sort by severity for prioritization
            severity_order = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3, 'INFORMATIONAL': 4}
            failed_findings['SeveritySort'] = failed_findings['Severity'].map(severity_order)
            failed_findings = failed_findings.sort_values(['SeveritySort', 'EvidenceDate'])
            
            remediation_columns = [
                'ControlSetName', 'ControlId', 'ControlName', 'ComplianceStatus',
                'Severity', 'ResourceArn', 'Finding', 'EvidenceDate'
            ]
            
            failed_findings[remediation_columns].to_excel(writer, sheet_name='Failed Findings', index=False)
        else:
            # No failed findings
            no_failures_df = pd.DataFrame([{
                'Status': 'No Failed Findings',
                'Message': 'All evaluated controls are currently passing',
                'Generated': datetime.now().strftime('%Y-%m-%d %H:%M UTC')
            }])
            no_failures_df.to_excel(writer, sheet_name='Failed Findings', index=False)
    
    def store_report_in_s3(self, excel_buffer):
        """Store the Excel report in S3 with date-based folder structure."""
        current_date = datetime.now()
        date_path = current_date.strftime('%Y/%m/%d')
        filename = f"SOC2_Weekly_Report_{current_date.strftime('%Y%m%d_%H%M')}.xlsx"
        s3_key = f"weekly-reports/{date_path}/{filename}"
        
        try:
            self.s3.put_object(
                Bucket=self.s3_bucket,
                Key=s3_key,
                Body=excel_buffer.getvalue(),
                ContentType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
            
            logger.info(f"Stored report in S3: s3://{self.s3_bucket}/{s3_key}")
            return s3_key
        except Exception as e:
            logger.error(f"Failed to store report in S3: {e}")
            raise
    
    def send_notification(self, s3_key):
        """Send email notification with report download link."""
        try:
            download_url = self.s3.generate_presigned_url(
                'get_object',
                Params={'Bucket': self.s3_bucket, 'Key': s3_key},
                ExpiresIn=604800  # 7 days
            )
            
            subject = f"Weekly SOC 2 Audit Report - {datetime.now().strftime('%Y-%m-%d')}"
            
            body = f"""
Dear Audit Team,

The weekly SOC 2 compliance report has been generated and is ready for review.

Report Details:
- Generated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}
- Assessment: SOC 2 Type II
- Coverage: All enabled controls with latest evidence

Download Link (expires in 7 days):
{download_url}

The report contains four sheets:
1. Executive Summary - High-level compliance metrics
2. Control Status - Status of each SOC 2 control  
3. Failed Findings - Items requiring attention
4. Evidence Details - Complete evidence inventory

This report was generated automatically from AWS Audit Manager evidence.

Best regards,
FAFO GRC Automation System
            """
            
            for recipient in self.report_recipients:
                self.ses.send_email(
                    Source='grc-automation@fafo.com',
                    Destination={'ToAddresses': [recipient]},
                    Message={
                        'Subject': {'Data': subject},
                        'Body': {'Text': {'Data': body}}
                    }
                )
            
            logger.info(f"Sent notifications to {len(self.report_recipients)} recipients")
        except Exception as e:
            logger.error(f"Failed to send notification: {e}")

def lambda_handler(event, context):
    """Main Lambda function handler for automated audit report generation."""
    try:
        logger.info("Starting weekly audit report generation")
        
        generator = AuditReportGenerator()
        
        # Fetch assessment evidence
        assessment = generator.fetch_assessment_evidence()
        control_sets = assessment['framework']['controlSets']
        
        # Collect evidence
        evidence_records = generator.collect_evidence_by_control(control_sets)
        
        # Generate Excel report
        excel_buffer = generator.generate_excel_reports(evidence_records)
        
        # Store in S3
        s3_key = generator.store_report_in_s3(excel_buffer)
        
        # Send notification
        generator.send_notification(s3_key)
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Weekly audit report generated successfully',
                'reportLocation': f"s3://{generator.s3_bucket}/{s3_key}",
                'evidenceRecords': len(evidence_records)
            })
        }
        
    except Exception as e:
        logger.error(f"Failed to generate audit report: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': 'Failed to generate audit report',
                'details': str(e)
            })
        }

Schedule this Lambda to run every Friday morning using Amazon EventBridge:
# CloudFormation template snippet for Lambda scheduling
WeeklyAuditReportFunction:
  Type: AWS::Serverless::Function
  Properties:
    CodeUri: src/
    Handler: weekly_audit_report.lambda_handler
    Runtime: python3.9
    Timeout: 900  # 15 minutes
    MemorySize: 1024
    Events:
      WeeklySchedule:
        Type: Schedule
        Properties:
          Schedule: cron(0 7 ? * FRI *)  # Every Friday at 7:00 AM UTC

This automated reporting system transforms the auditor experience:
Predictable delivery: Every Friday morning, auditors receive fresh compliance reports with the latest evidence
Executive-friendly format: Excel workbooks include summary metrics that audit partners can review quickly
Detailed findings: Specific information about non-compliant items with remediation guidance
Professional presentation: Consistent formatting and organization that looks trustworthy
Business Impact at FAFO
Implementing this automated reporting system delivered measurable improvements:
Metric
Before Automation
After Automation
Improvement
Weekly report prep time
12 hours (manual)
0 hours (automated)
100% reduction
Engineer audit interruptions
≈25 per audit
0 per audit
100% elimination
Time to deliver evidence
3-5 business days
Same day (Friday)
80% faster
Auditor satisfaction
6.2/10
9.1/10
47% improvement

Your VP of Engineering is thrilled. Audits no longer disrupt product development. Your SOC 2 auditors appreciate clean, accessible evidence. And your GRC career has taken a significant leap forward.
You've built a continuously-assured compliance pipeline using AWS-native tools, dramatically reducing audit overhead and freeing engineers from unnecessary meetings. Your weekly "Friday Excel" reports deliver clear, structured evidence directly to auditor inboxes.
But there's still one missing piece that could make your audits completely hands-free: giving auditors direct, secure access to AWS Audit Manager evidence without requiring human gatekeepers.
If you solve this final challenge, your audit process becomes truly autonomous. Engineers never get interrupted, GRC teams don't scramble to fulfill ad-hoc evidence requests, and auditors can confidently validate evidence without friction or delays.
In most organizations, auditor interactions create bottlenecks:
Auditors make evidence requests: "Can you show me the Security Hub findings for September?"
GRC teams manually respond: Someone logs into AWS, takes screenshots, exports data
Back-and-forth clarifications: "This screenshot is unclear. Can you show me the remediation steps?"
Delays and frustration mount: Audit timelines slip as simple requests take days to fulfill
At FAFO, you've automated nearly everything, yet manual auditor access remains the final bottleneck preventing truly frictionless audits.
AWS Audit Manager integrates natively with AWS Identity and Access Management (IAM), enabling you to create tightly scoped, read-only auditor roles that provide direct console access to compliance evidence without exposing any other AWS resources.
This approach delivers several benefits:
Complete auditor autonomy: Auditors access live evidence 24/7 without requesting anything from your team
Perfect audit trail: AWS CloudTrail logs every auditor action for accountability
Zero security risk: Read-only permissions prevent accidental or intentional changes
Real-time evidence: Auditors see current compliance data, eliminating version control issues
Professional credibility: Direct access demonstrates transparency and builds auditor confidence
IAM Role Implementation: Step-by-Step Security Configuration
Step 1: Create a restrictive IAM policy for Audit Manager read-only access
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AuditManagerReadOnlyAccess",
            "Effect": "Allow",
            "Action": [
                "auditmanager:GetAssessment",
                "auditmanager:GetAssessmentFramework", 
                "auditmanager:GetControl",
                "auditmanager:GetEvidence",
                "auditmanager:GetEvidenceByEvidenceFolder",
                "auditmanager:GetEvidenceFoldersByAssessment",
                "auditmanager:GetEvidenceFoldersByAssessmentControl",
                "auditmanager:ListAssessments",
                "auditmanager:ListAssessmentFrameworks"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestedRegion": ["us-east-1"]
                }
            }
        },
        {
            "Sid": "BasicConsoleAccess",
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "sts:GetCallerIdentity"
            ],
            "Resource": "*"
        },
        {
            "Sid": "DenyAllWriteOperations", 
            "Effect": "Deny",
            "Action": [
                "auditmanager:Create*",
                "auditmanager:Update*", 
                "auditmanager:Delete*",
                "auditmanager:Put*"
            ],
            "Resource": "*"
        }
    ]
}

Key security features:
Explicit read-only permissions with Get* and List* actions only
Regional restrictions limiting access to your assessment regions
Explicit denial of all write operations
Minimal console access for basic AWS navigation
Step 2: Create the dedicated auditor IAM role
{
    "RoleName": "SOC2-Auditor-ReadOnly",
    "AssumeRolePolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "AWS": [
                        "arn:aws:iam::111122223333:root"
                    ]
                },
                "Action": "sts:AssumeRole",
                "Condition": {
                    "StringEquals": {
                        "sts:ExternalId": "FAFO-SOC2-2025-AUDIT"
                    },
                    "Bool": {
                        "aws:MultiFactorAuthPresent": "true"
                    },
                    "DateGreaterThan": {
                        "aws:CurrentTime": "2025-01-01T00:00:00Z"
                    },
                    "DateLessThan": {
                        "aws:CurrentTime": "2025-12-31T23:59:59Z" 
                    }
                }
            }
        ]
    },
    "Description": "Read-only access to AWS Audit Manager for SOC 2 external auditors",
    "MaxSessionDuration": 28800
}

Advanced security controls:
External ID requirement prevents confused deputy attacks
MFA enforcement for all role assumptions
Time-bound access during active audit periods only
Maximum 8-hour sessions prevent indefinite access
Step 3: Provide secure console access guidance
Create clear documentation for auditors:
# FAFO SOC 2 Auditor Access Guide

## Prerequisites
- AWS account with MFA enabled
- External ID: FAFO-SOC2-2025-AUDIT
- Access period: January 1, 2025 - December 31, 2025

## Accessing Audit Manager

1. Log into your AWS account
2. Navigate to "Switch Role" in the top-right menu
3. Enter:
   - Account: [FAFO's AWS Account ID]
   - Role: SOC2-Auditor-ReadOnly  
   - External ID: FAFO-SOC2-2025-AUDIT

## What You Can Access
✅ All SOC 2 assessment data and evidence
✅ Historical compliance trends and timelines  
✅ Detailed findings with remediation guidance

## What You Cannot Access
❌ Any AWS configuration changes
❌ Other AWS services outside Audit Manager
❌ Ability to modify or delete evidence

Enhanced Auditor Experience
This self-service access model transforms auditor experience:
Immediate evidence availability: Auditors access compliance evidence 24/7 without waiting
Interactive exploration: Drill down into specific findings and view historical trends
Real-time validation: See current data that drives your automated reports
Complete transparency: Every auditor action logged in CloudTrail for accountability
Adding Comprehensive Audit Guidance
To maximize self-service value and minimize follow-up questions, embed clear explanations directly in Audit Manager as Management Responses:
def add_audit_guidance(assessment_id):
    """Add management responses to common auditor questions."""
    audit_manager = boto3.client('auditmanager')
    
    guidance_items = {
        'ELB.5': {
            'response': '''
FAFO does not use Classic ELBs in any environment. All load balancing 
is performed using Application Load Balancers (ALB) and Network Load 
Balancers (NLB) which provide enhanced security features.

Migration completed: Q2 2024
Current inventory: 12 ALBs, 3 NLBs, 0 Classic ELBs

Control disabled to prevent false positive findings.
            '''
        },
        'MFA-Implementation': {
            'response': '''
FAFO enforces MFA across all access methods:

AWS Console: MFA required for all IAM users, no exceptions
Programmatic access: Temporary credentials only, no long-term keys
SSO Integration: Okta SSO with MFA for all corporate applications

Enforcement: SCPs prevent console access without MFA
Monitoring: Daily reports on MFA compliance
            '''
        }
    }
    
    for control_id, guidance in guidance_items.items():
        evidence_data = {
            'dataSource': 'MANUAL',
            'eventSource': 'GRC Team - Management Response',
            'eventName': f'Control_{control_id}_Management_Response',
            'evidenceByType': 'Management Response',
            'textResponse': guidance['response']
        }
        
        audit_manager.batch_import_evidence_to_assessment_control(
            assessmentId=assessment_id,
            controlSetId='CC6',
            controlId=control_id,
            manualEvidence=[evidence_data]
        )

This proactive documentation approach:
Reduces interruptions by answering questions upfront
Demonstrates thoughtful compliance program management
Enables faster audit completion
Shows commitment to transparency
Summary and Key Takeaways: Your Blueprint for Compliance Transformation
At the beginning of this chapter, you stepped into the role of Director of GRC at FAFO, Inc., inheriting an audit process that consumed enormous engineering resources, created organizational friction, and delivered questionable value. You were challenged to automate SOC 2 compliance using only AWS-native services and open-source tools.
You succeeded, you fundamentally transformed how FAFO approaches compliance.
Quantifying the FAFO Transformation
The numbers tell a compelling story:
Metric
Before Automation (2024)
After Automation (2025)
Improvement
Total engineer hours per audit
≈380 hours
<50 hours
87% reduction
Audit preparation meetings
15 sessions
2 sessions
87% reduction
Findings requiring manual detection
23 of 31 (74%)
2 of 31 (6%)
91% improvement
Time to produce audit evidence
3-5 business days
Same day
80% faster
Weekly evidence report preparation
12 hours manual work
0 hours
100% elimination
Controls with continuous monitoring
0%
90% of technical controls
Complete coverage
Engineering team audit interruptions
25+ requests per audit
0 requests
100% elimination

Strategic impact beyond the metrics:
Engineering team morale and productivity improved dramatically
GRC team transformed from reactive evidence gatherers to strategic automation architects
Executive confidence in compliance as a competitive advantage rather than cost center
Auditor relationships strengthened through professionalism and efficiency
Scalability foundation that grows with the business without proportional overhead
Your Repeatable Blueprint for Career Success
This chapter we developed a repeatable methodology that positions you as a strategic compliance leader:
Step 1: Strategic Assessment and Opportunity Mapping
Inventory all compliance requirements and map each control to available cloud-native monitoring
Identify automation opportunities by analyzing current manual processes
Assess organizational readiness including infrastructure, team capabilities, and leadership support
Step 2: Foundation Configuration and Tuning
Enable comprehensive AWS security standards (FSBP, CIS Benchmarks) in Security Hub
Configure corresponding Config rules for historical compliance tracking
Systematically prune non-relevant controls to maintain focus
Document all decisions with clear business rationale
Step 3: Application Security Integration and SDLC Evidence
Transform existing CI/CD security scanning into compliance evidence streams
Implement ASFF transformation to unify infrastructure and application security evidence
Automate upload of application security findings to Security Hub
Establish continuous security testing that generates real-time compliance evidence
Step 4: Automated Evidence Collection and Professional Reporting
Deploy event-driven automation for continuous evidence gathering
Create polished reporting systems that transform raw data into executive-friendly summaries
Implement scheduled delivery systems for predictable evidence packages
Build comprehensive remediation tracking
Step 5: Auditor Enablement and Self-Service Access
Establish secure, read-only access roles for external auditors
Implement comprehensive audit trails demonstrating transparency
Embed proactive documentation answering common auditor questions
Create clear procedures enabling efficient, confident auditor work
Core Principles That Enable Success
Your transformation succeeded because you applied key principles:
Continuous automation over periodic manual work: Built systems that maintain audit readiness continuously
Engineering enablement over engineering burden: Protected developer productivity and maintained velocity
Auditor empowerment over auditor management: Provided secure, direct access for independent validation
Evidence quality over evidence quantity: Focused on high-quality, auditable evidence from authoritative sources
Proactive transparency over reactive responses: Embedded comprehensive explanations directly in evidence systems
Strategic platform thinking over tactical tool implementation: Built cohesive, integrated compliance platform
Your FAFO experience revealed critical insights:
AWS-native services provide enterprise-grade compliance capabilities without additional licensing costs
Engineering team buy-in is achievable when automation protects their time and productivity
Auditors prefer direct access to authoritative evidence over manual summaries
Executive support accelerates when compliance becomes measurably efficient and cost-effective
Comprehensive documentation prevents most audit friction and follow-up questions
Automation quality matters more than speed. Thoughtful implementation creates sustainable advantages
Through your work at FAFO, you've established yourself as a compliance innovation leader:
To leadership teams: The GRC director who eliminates compliance friction and enables rapid, secure growth
To engineering organizations: The compliance professional who protects developer productivity and thinks like an engineer
To audit firms: The client who makes engagements efficient and technically sophisticated
To the GRC community: The practitioner who proves modern compliance can be automated and strategically valuable
In your next role, you'll confidently approach compliance automation with proven methodologies:
"I know exactly how to automate SOC 2 compliance using AWS-native services, and I can show you the 87% reduction in engineering overhead we achieved."
"I've built self-service audit experiences that improve auditor satisfaction by 47% while completely eliminating engineering interruptions."
"I can demonstrate how to transform compliance from a cost center into a competitive advantage that enables rapid scaling."
This combination of technical expertise, business impact quantification, and strategic thinking positions you as a rare compliance leader who understands both implementation details and organizational value.
The work at FAFO represents the direction modern compliance programs must take. The traditional model of manual evidence gathering and periodic audit preparation cannot scale with modern development practices and business growth expectations.
Compliance leaders who succeed will be those who understand how to:
Leverage cloud-native capabilities for sophisticated monitoring without significant investment
Integrate compliance into existing workflows rather than creating competing processes
Provide value to audit firms through professional, efficient experiences
Quantify business impact beyond just compliance outcomes
Think architecturally about compliance systems as integrated platforms
Congratulations on fundamentally changing what SOC 2 compliance means at FAFO. You've proven that compliance can be automated, efficient, and strategically valuable using thoughtful engineering and cloud-native technologies. More importantly, you've equipped yourself with a proven blueprint for replicating this success throughout your career. The transformation you led will serve as a model for how modern organizations approach compliance challenges.
In your next role, you'll walk in as the GRC leader who has already solved the automation challenge that most organizations still struggle with. You'll be the strategic partner who enables rapid, secure growth rather than the compliance function that slows it down.
This is the future of GRC engineering, and you're leading the way.
