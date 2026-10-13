# Adversary Emulation Plan: APT29

**Generated:** 2026-10-12  
**Aliases:** APT29, IRON RITUAL, IRON HEMLOCK, NobleBaron, Dark Halo, NOBELIUM, UNC2452, YTTRIUM, The Dukes, Cozy Bear, CozyDuke, SolarStorm, Blue Kitsune, UNC3524, Midnight Blizzard  
**Techniques:** 66

> **Authorized lab use only.** Run only in an isolated environment you own.

## Execution Plan

### 1. T1595.002 — Vulnerability Scanning
**Tactic:** reconnaissance  

Adversaries may scan victims for vulnerabilities that can be used during targeting. Vulnerability scans typically check if the configuration of a target host/application (ex: software and version) potentially aligns with the target of a specific exploit the adversary may seek to use.

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 2. T1586.002 — Email Accounts
**Tactic:** resource-development  

Adversaries may compromise email accounts that can be used during targeting. Adversaries can use compromised email accounts to further their operations, such as leveraging them to conduct [Phishing for Information](https://attack.mitre.org/techniques/T1598), [Phishing](https://attack.mitre.org/techn

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 3. T1583.006 — Web Services
**Tactic:** resource-development  

Adversaries may register for web services that can be used during targeting. A variety of popular websites exist for adversaries to register for a web-based service that can be abused during later stages of the adversary lifecycle, such as during Command and Control ([Web Service](https://attack.mit

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 4. T1587.001 — Malware
**Tactic:** resource-development  

Adversaries may develop malware and malware components that can be used during targeting. Building malicious software can include the development of payloads, droppers, post-compromise tools, backdoors (including backdoored images), packers, C2 protocols, and the creation of infected removable media

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 5. T1588.002 — Tool
**Tactic:** resource-development  

Adversaries may buy, steal, or download software tools that can be used during targeting. Tools can be open or closed source, free or commercial. A tool can be used for malicious purposes by an adversary, but (unlike malware) were not intended to be used for those purposes (ex: [PsExec](https://atta

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 6. T1587.003 — Digital Certificates
**Tactic:** resource-development  

Adversaries may create self-signed SSL/TLS certificates that can be used during targeting. SSL/TLS certificates are designed to instill trust. They include information about the key, information about its owner's identity, and the digital signature of an entity that has verified the certificate's co

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 7. T1586.003 — Cloud Accounts
**Tactic:** resource-development  

Adversaries may compromise cloud accounts that can be used during targeting. Adversaries can use compromised cloud accounts to further their operations, including leveraging cloud storage services such as Dropbox, Microsoft OneDrive, or AWS S3 buckets for [Exfiltration to Cloud Storage](https://atta

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 8. T1199 — Trusted Relationship
**Tactic:** initial-access  

Adversaries may breach or otherwise leverage organizations who have access to intended victims. Access through trusted third party relationship abuses an existing connection that may not be protected or receives less scrutiny than standard mechanisms of gaining access to a network.

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 9. T1566.002 — Spearphishing Link
**Tactic:** initial-access  

Adversaries may send spearphishing emails with a malicious link in an attempt to gain access to victim systems. Spearphishing with a link is a specific variant of spearphishing. It is different from other forms of spearphishing in that it employs the use of links to download malware contained in ema

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 10. T1190 — Exploit Public-Facing Application
**Tactic:** initial-access  

Adversaries may attempt to exploit a weakness in an Internet-facing host or system to initially access a network. The weakness in the system can be a software bug, a temporary glitch, or a misconfiguration.

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 11. T1566.003 — Spearphishing via Service
**Tactic:** initial-access  

Adversaries may send spearphishing messages via third-party services in an attempt to gain access to victim systems. Spearphishing via service is a specific variant of spearphishing. It is different from other forms of spearphishing in that it employs the use of third party services rather than dire

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 12. T1566.001 — Spearphishing Attachment
**Tactic:** initial-access  

Adversaries may send spearphishing emails with a malicious attachment in an attempt to gain access to victim systems. Spearphishing attachment is a specific variant of spearphishing. Spearphishing attachment is different from other forms of spearphishing in that it employs the use of malware attache

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 13. T1203 — Exploitation for Client Execution
**Tactic:** execution  

Adversaries may exploit software vulnerabilities in client applications to execute code. Vulnerabilities can exist in software due to unsecure coding practices that can lead to unanticipated behavior. Adversaries can take advantage of certain vulnerabilities through targeted exploitation for the pur

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 14. T1651 — Cloud Administration Command
**Tactic:** execution  

Adversaries may abuse cloud management services to execute commands within virtual machines. Resources such as AWS Systems Manager, Azure RunCommand, and Runbooks allow users to remotely run scripts in virtual machines by leveraging installed virtual machine agents. (Citation: AWS Systems Manager Ru

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 15. T1059.001 — PowerShell
**Tactic:** execution  

Adversaries may abuse PowerShell commands and scripts for execution. PowerShell is a powerful interactive command-line interface and scripting environment included in the Windows operating system.(Citation: TechNet PowerShell) Adversaries can use PowerShell to perform a number of actions, including 

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 16. T1059.006 — Python
**Tactic:** execution  

Adversaries may abuse Python commands and scripts for execution. Python is a very popular scripting/programming language, with capabilities to perform many functions. Python can be executed interactively from the command-line (via the <code>python.exe</code> interpreter) or via scripts (.py) that ca

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 17. T1204.002 — Malicious File
**Tactic:** execution  

An adversary may rely upon a user opening a malicious file in order to gain execution. Users may be subjected to social engineering to get them to open a file that will lead to code execution. This user action will typically be observed as follow-on behavior from [Spearphishing Attachment](https://a

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 18. T1059.009 — Cloud API
**Tactic:** execution  

Adversaries may abuse cloud APIs to execute malicious commands. APIs available in cloud environments provide various functionalities and are a feature-rich method for programmatic access to nearly all aspects of a tenant. These APIs may be utilized through various methods such as command line interp

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 19. T1047 — Windows Management Instrumentation
**Tactic:** execution  

Adversaries may abuse Windows Management Instrumentation (WMI) to execute malicious commands and payloads. WMI is designed for programmers and is the infrastructure for management data and operations on Windows systems.(Citation: WMI 1-3) WMI is an administration feature that provides a uniform envi

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 20. T1204.001 — Malicious Link
**Tactic:** execution  

An adversary may rely upon a user clicking a malicious link in order to gain execution. Users may be subjected to social engineering to get them to click on a link that will lead to code execution. This user action will typically be observed as follow-on behavior from [Spearphishing Link](https://at

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 21. T1053.005 — Scheduled Task
**Tactic:** execution, persistence, privilege-escalation  

Adversaries may abuse the Windows Task Scheduler to perform task scheduling for initial or recurring execution of malicious code. There are multiple ways to access the Task Scheduler in Windows. The [schtasks](https://attack.mitre.org/software/S0111) utility can be run directly on the command line, 

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 22. T1098.002 — Additional Email Delegate Permissions
**Tactic:** persistence, privilege-escalation  

Adversaries may grant additional permission levels to maintain persistent access to an adversary-controlled email account. 

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 23. T1037.004 — RC Scripts
**Tactic:** persistence, privilege-escalation  

Adversaries may establish persistence by modifying RC scripts, which are executed during a Unix-like system’s startup. These files allow system administrators to map and start custom services at startup for different run levels. RC scripts require root privileges to modify.

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 24. T1547.001 — Registry Run Keys / Startup Folder
**Tactic:** persistence, privilege-escalation  

Adversaries may achieve persistence by adding a program to a startup folder or referencing it with a Registry run key. Adding an entry to the "run keys" in the Registry or startup folder will cause the program referenced to be executed when a user logs in.(Citation: Microsoft Run Key) These programs

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 25. T1136.003 — Cloud Account
**Tactic:** persistence  

Adversaries may create a cloud account to maintain access to victim systems. With a sufficient level of access, such accounts may be used to establish secondary credentialed access that does not require persistent remote access tools to be deployed on the system.(Citation: Microsoft O365 Admin Roles

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 26. T1133 — External Remote Services
**Tactic:** persistence, initial-access  

Adversaries may leverage external-facing remote services to initially access and/or persist within a network. Remote services such as VPNs, Citrix, and other access mechanisms allow users to connect to internal enterprise network resources from external locations. There are often remote service gate

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 27. T1098.005 — Device Registration
**Tactic:** persistence, privilege-escalation  

Adversaries may register a device to an adversary-controlled account. Devices may be registered in a multifactor authentication (MFA) system, which handles authentication to the network, or in a device management system, which handles device access and compliance.

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 28. T1505.003 — Web Shell
**Tactic:** persistence  

Adversaries may backdoor web servers with web shells to establish persistent access to systems. A Web shell is a Web script that is placed on an openly accessible Web server to allow an adversary to access the Web server as a gateway into a network. A Web shell may provide a set of functions to exec

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 29. T1037 — Boot or Logon Initialization Scripts
**Tactic:** persistence, privilege-escalation  

Adversaries may use scripts automatically executed at boot or logon initialization to establish persistence.(Citation: Mandiant APT29 Eye Spy Email Nov 22)(Citation: Anomali Rocke March 2019) Initialization scripts can be used to perform administrative functions, which may often execute other progra

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 30. T1068 — Exploitation for Privilege Escalation
**Tactic:** privilege-escalation  

Adversaries may exploit software vulnerabilities in an attempt to elevate privileges. Exploitation of a software vulnerability occurs when an adversary takes advantage of a programming error in a program, service, or within the operating system software or kernel itself to execute adversary-controll

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 31. T1546.008 — Accessibility Features
**Tactic:** privilege-escalation, persistence  

Adversaries may establish persistence and/or elevate privileges by executing malicious content triggered by accessibility features. Windows contains accessibility features that may be launched with a key combination before a user has logged in (ex: when the user is on the Windows logon screen). An a

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 32. T1548.002 — Bypass User Account Control
**Tactic:** privilege-escalation  

Adversaries may bypass UAC mechanisms to elevate process privileges on system. Windows User Account Control (UAC) allows a program to elevate its privileges (tracked as integrity levels ranging from low to high) to perform a task under administrator-level permissions, possibly by prompting the user 

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 33. T1546.003 — Windows Management Instrumentation Event Subscription
**Tactic:** privilege-escalation, persistence  

Adversaries may establish persistence and elevate privileges by executing malicious content triggered by a Windows Management Instrumentation (WMI) event subscription. WMI can be used to install event filters, providers, consumers, and bindings that execute code when a defined event occurs. Examples

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 34. T1621 — Multi-Factor Authentication Request Generation
**Tactic:** credential-access  

Adversaries may attempt to bypass multi-factor authentication (MFA) mechanisms and gain access to accounts by generating MFA requests sent to users.

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 35. T1649 — Steal or Forge Authentication Certificates
**Tactic:** credential-access  

Adversaries may steal or forge certificates used for authentication to access remote systems or resources. Digital certificates are often used to sign and encrypt messages and/or files. Certificates are also used as authentication material. For example, Entra ID device certificates and Active Direct

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 36. T1003.004 — LSA Secrets
**Tactic:** credential-access  

Adversaries with SYSTEM access to a host may attempt to access Local Security Authority (LSA) secrets, which can contain a variety of different credential materials, such as credentials for service accounts.(Citation: Passcape LSA Secrets)(Citation: Microsoft AD Admin Tier Model)(Citation: Tilbury W

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 37. T1110.001 — Password Guessing
**Tactic:** credential-access  

Adversaries with no prior knowledge of legitimate credentials within the system or environment may guess passwords to attempt access to accounts. Without knowledge of the password for an account, an adversary may opt to systematically guess the password using a repetitive or iterative mechanism. An 

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 38. T1003.002 — Security Account Manager
**Tactic:** credential-access  

Adversaries may attempt to extract credential material from the Security Account Manager (SAM) database either through in-memory techniques or through the Windows Registry where the SAM database is stored. The SAM is a database file that contains local accounts for the host, typically those found wi

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 39. T1110.003 — Password Spraying
**Tactic:** credential-access  

Adversaries may use a single or small list of commonly used passwords against many different accounts to attempt to acquire valid account credentials. Password spraying uses one password (e.g. 'Password01'), or a small list of commonly used passwords, that may match the complexity policy of the doma

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 40. T1528 — Steal Application Access Token
**Tactic:** credential-access  

Adversaries can steal application access tokens as a means of acquiring credentials to access remote systems and resources.

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 41. T1016.001 — Internet Connection Discovery
**Tactic:** discovery  

Adversaries may check for Internet connectivity on compromised systems. This may be performed during automated discovery and can be accomplished in numerous ways such as using [Ping](https://attack.mitre.org/software/S0097), <code>tracert</code>, and GET requests to websites, or performing initial s

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 42. T1087.004 — Cloud Account
**Tactic:** discovery  

Adversaries may attempt to get a listing of cloud accounts. Cloud accounts are those created and configured by an organization for use by users, remote support, services, or for administration of resources within a cloud service provider or SaaS application.

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 43. T1021.007 — Cloud Services
**Tactic:** lateral-movement  

Adversaries may log into accessible cloud services within a compromised environment using [Valid Accounts](https://attack.mitre.org/techniques/T1078) that are synchronized with or federated to on-premises user identities. The adversary may then perform management actions or access cloud-hosted resou

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 44. T1550.003 — Pass the Ticket
**Tactic:** lateral-movement  

Adversaries may “pass the ticket” using stolen Kerberos tickets to move laterally within an environment, bypassing normal system access controls. Pass the ticket (PtT) is a method of authenticating to a system using Kerberos tickets without having access to an account's password. Kerberos authentica

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 45. T1005 — Data from Local System
**Tactic:** collection  

Adversaries may search local system sources, such as file systems, configuration files, local databases, virtual machine files, or process memory, to find files of interest and sensitive data prior to Exfiltration.

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 46. T1114.002 — Remote Email Collection
**Tactic:** collection  

Adversaries may target an Exchange server, Office 365, or Google Workspace to collect sensitive information. Adversaries may leverage a user's credentials and interact directly with the Exchange server to acquire information from within a network. Adversaries may also access externally facing Exchan

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 47. T1105 — Ingress Tool Transfer
**Tactic:** command-and-control  

Adversaries may transfer tools or other files from an external system into a compromised environment. Tools or files may be copied from an external adversary-controlled system to the victim network through the command and control channel or through alternate protocols such as [ftp](https://attack.mi

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 48. T1568 — Dynamic Resolution
**Tactic:** command-and-control  

Adversaries may dynamically establish connections to command and control infrastructure to evade common detections and remediations. This may be achieved by using malware that shares a common algorithm with the infrastructure the adversary uses to receive the malware's communications. These calculat

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 49. T1090.002 — External Proxy
**Tactic:** command-and-control  

Adversaries may use an external proxy to act as an intermediary for network communications to a command and control server to avoid direct connections to their infrastructure. Many tools exist that enable traffic redirection through proxies or port redirection, including [HTRAN](https://attack.mitre

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 50. T1665 — Hide Infrastructure
**Tactic:** command-and-control  

Adversaries may manipulate network traffic in order to hide and evade detection of their C2 infrastructure. This can be accomplished by identifying and filtering traffic from defensive tools,(Citation: TA571) masking malicious domains to obfuscate the true destination from both automated scanning to

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 51. T1090.003 — Multi-hop Proxy
**Tactic:** command-and-control  

Adversaries may chain together multiple proxies to disguise the source of malicious traffic. Typically, a defender will be able to identify the last proxy traffic traversed before it enters their network; the defender may or may not be able to identify any previous proxies before the last-hop proxy.

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 52. T1573 — Encrypted Channel
**Tactic:** command-and-control  

Adversaries may employ an encryption algorithm to conceal command and control traffic rather than relying on any inherent protections provided by a communication protocol. Despite the use of a secure algorithm, these implementations may be vulnerable to reverse engineering if secret keys are encoded

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 53. T1090.004 — Domain Fronting
**Tactic:** command-and-control  

Adversaries may take advantage of routing schemes in Content Delivery Networks (CDNs) and other services which host multiple domains to obfuscate the intended destination of HTTPS traffic or traffic tunneled through HTTPS. (Citation: Fifield Blocking Resistent Communication through domain fronting 2

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 54. T1070.006 — Timestomp
**Tactic:** stealth  

Adversaries may modify file time attributes to hide new files or changes to existing files. Timestomping is a technique that modifies the timestamps of a file (the modify, access, create, and change times), often to mimic files that are in the same folder and blend malicious files with legitimate fi

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 55. T1027.001 — Binary Padding
**Tactic:** stealth  

Adversaries may use binary padding to add junk data and change the on-disk representation of malware. This can be done without affecting the functionality or behavior of a binary, but can increase the size of the binary beyond what some security tools are capable of handling due to file size limitat

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 56. T1218.005 — Mshta
**Tactic:** stealth  

Adversaries may abuse mshta.exe to proxy execution of malicious .hta files and Javascript or VBScript through a trusted Windows utility. There are several examples of different types of threats leveraging mshta.exe during initial compromise and for execution of code (Citation: Cylance Dust Storm) (C

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 57. T1685.002 — Disable or Modify Cloud Log
**Tactic:** defense-impairment  

An adversary may disable or modify cloud logging capabilities and integrations to limit what data is collected on their activities and avoid detection. Cloud environments allow for collection and analysis of audit and application logs that provide insight into what activities a user does within the 

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 58. T1027.002 — Software Packing
**Tactic:** stealth  

Adversaries may perform software packing or virtual machine software protection to conceal their code. Software packing is a method of compressing or encrypting an executable. Packing an executable changes the file signature in an attempt to avoid signature-based detection. Most decompression techni

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 59. T1036.005 — Match Legitimate Resource Name or Location
**Tactic:** stealth  

Adversaries may match or approximate the name or location of legitimate files, Registry keys, or other resources when naming/placing them. This is done for the sake of evading defenses and observation. 

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 60. T1553.005 — Mark-of-the-Web Bypass
**Tactic:** defense-impairment  

Adversaries may abuse specific file formats to subvert Mark-of-the-Web (MOTW) controls. In Windows, when files are downloaded from the Internet, they are tagged with a hidden NTFS Alternate Data Stream (ADS) named <code>Zone.Identifier</code> with a specific value known as the MOTW.(Citation: Micros

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 61. T1556.007 — Hybrid Identity
**Tactic:** defense-impairment, persistence, credential-access  

Adversaries may patch, modify, or otherwise backdoor cloud authentication processes that are tied to on-premises user identities in order to bypass typical authentication mechanisms, access credentials, and enable persistent access to accounts.  

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 62. T1078.004 — Cloud Accounts
**Tactic:** stealth, persistence, privilege-escalation, initial-access  

Valid accounts in cloud environments may allow adversaries to perform actions to achieve Initial Access, Persistence, Privilege Escalation, or Defense Evasion. Cloud accounts are those created and configured by an organization for use by users, remote support, services, or for administration of reso

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 63. T1070.004 — File Deletion
**Tactic:** stealth  

Adversaries may delete files left behind by the actions of their intrusion activity. Malware, tools, or other non-native files dropped or created on a system by an adversary (ex: [Ingress Tool Transfer](https://attack.mitre.org/techniques/T1105)) may leave traces to indicate to what was done within 

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 64. T1078 — Valid Accounts
**Tactic:** stealth, persistence, privilege-escalation, initial-access  

Adversaries may obtain and abuse credentials of existing accounts as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion. Compromised credentials may be used to bypass access controls placed on various resources on systems within the network and may even be used 

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 65. T1078.003 — Local Accounts
**Tactic:** stealth, persistence, privilege-escalation, initial-access  

Adversaries may obtain and abuse credentials of a local account as a means of gaining Initial Access, Persistence, Privilege Escalation, or Defense Evasion. Local accounts are those configured by an organization for use by users, remote support, services, or for administration on a single system or 

- [ ] Emulate in lab
- [ ] Verify telemetry / detection

### 66. T1027.006 — HTML Smuggling
**Tactic:** stealth  

Adversaries may smuggle data and files past content filters by hiding malicious payloads inside of seemingly benign HTML files. HTML documents can store large binary objects known as JavaScript Blobs (immutable data that represents raw bytes) that can later be constructed into file-like objects. Dat

- [ ] Emulate in lab
- [ ] Verify telemetry / detection
