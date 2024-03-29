### Operating Systems and Lab Environments

- **Kali Linux**: Introduction to Kali Linux, Kali Linux basics and discovery
- **Windows Security**: Exploiting and securing Windows environments and using Windows for penetration testing, including Windows 10 Enterprise and Windows Server 2019.
- **Vulnerable Machines**: Download, and configure vulnerable machines from VulnHub for practicing penetration testing.

### Security Tools

- **Metasploit**: How to use Metasploit for searching, scanning, enumerating and exploiting vulnerabilities.
- **Splunk**: Introduction to using Splunk for log management and SIEM (Security Information and Event Management).
- **Nmap**: Using Nmap for network exploration and security auditing.
- **Nessus**: Setting up Nessus Essential for vulnerability scanning and its basic usage.
- **Wireshark**: Using Wireshark for network traffic analysis.
- **Burp Suite**: Introduction to Burp Suite Community Edition for web application security testing.

### Programming for Security

- **Python in Cybersecurity**: Basic Python programming concepts and scripts for automation and security tools development.
- **Bash Scripting**: Leveraging bash scripting for automation and task management on Linux systems.
- **PowerShell for Security**: Using PowerShell for Windows administration and security tasks.

### Projects

- **Building a Pentesting Lab**: Step-by-step guide on setting up a pentesting lab with Kali Linux and vulnerable machines.
- **Web Application Security**: Projects focused on identifying and exploiting web application vulnerabilities.
- **Automating Security Tasks**: Projects that use scripting in Python, Bash, or PowerShell to automate repetitive security tasks.

### Cybersecurity Frameworks

- **MITRE ATT&CK**: Understanding the MITRE ATT&CK framework and its application in real-world scenarios.
- **NIST Cybersecurity Framework**: A guide to the NIST framework principles and practices for improving cybersecurity.
- **OWASP Top 10**: Overview of the top 10 web application security risks and how to mitigate them.

## File Permissions Reference

In Linux, file permissions control the level of access granted to users and groups for files and directories. Understanding file permissions is crucial for maintaining system security and proper functionality. Here is a quick reference guide to Linux file permissions:

| **NUMBER** | **PERMISSION TYPE** | **SYMBOL** |
|------------|---------------------|------------|
| 0          | No permission       | `---`      |
| 1          | Execute             | `--x`      |
| 2          | Write               | `-w-`      |
| 3          | Write and Execute   | `-wx`      |
| 4          | Read                | `r--`      |
| 5          | Read and Execute    | `r-x`      |
| 6          | Read and Write      | `rw-`      |
| 7          | Read, Execute, and Write | `rwx` |

### Understanding Permissions
- **Read (r)**: The read permission allows a user to read the contents of a file or list the contents of a directory.
- **Write (w)**: The write permission allows a user to modify the contents of a file or add/remove files within a directory.
- **Execute (x)**: The execute permission allows a user to run a file as a program or script. For directories, it allows the user to access the directory's contents.

### Modifying Permissions
To change file or directory permissions, you can use the `chmod` command. Here's a basic example:

```bash
chmod 755 filename
```

### Additional Resources

- **Cheat Sheets**: Quick reference guides for tools like Nmap and Metasploit.
- **Useful Links**: Curated list of resources for deeper exploration of cybersecurity topics.
- **File Permissions in Linux**: Understanding Linux file permissions for securing systems.
