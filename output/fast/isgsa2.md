---
title: "isgsa2"
source_url: https://fast.faa.gov/docs/isgsa2.doc
source_type: doc
converted: 2026-10-27
---
# isgsa2

**Federal Aviation Administration**

**Preliminary Information System Security (ISS)**

**Assessment Template**

**January 2024**

**TEMPLATE TABLE OF CONTENTS**

General Template Guidance ……………..…    iii

Instructions for Completing the Template ……. iv

Title Page ……………………….……………   1

Assessment Table of Contents …………….…    2

**General Template Guidance**

This ISGSA assessment template has been designed to be used in conjunction with the ISGSA for conducting the Preliminary Information System Security Assessment in support of the Acquisition Management System (AMS) concept and requirements definition (CRD).

This template does not include Sensitive Unclassified Information (SUI), however, the assessment report based on this template will contain threat information of a prospective capability and may lead to threat information of a prospective system. Therefore, the preparers of the assessment report must determine if the report needs to be marked as SUI in accordance with the most up-to-date FAA Order 1600.75 “Protecting SUI” and in consultation with the sponsoring organization Security Servicing Element (SSE), if necessary.

Subject to review by ANG-B and ASAG approval to ensure compliance with the ISGSA, a Line of Business or Staff Office (LOB/SO) Authorizing Official (AO) may tailor this ISGSA assessment template to suit the LOB/SO specific needs. However, if the LOB/AO tailoring requires modification of the ISGSA, the LOB/SO tailoring and ISGSA modification will require ASAG review and AEB approval. LOB/SO investment initiatives must use the corresponding LOB/SO tailored template, if one exists. Note that any retailoring of LOB/SO tailored templates is also subject to this review process. 

The ISGSA assessment templates and the approved LOB/SO tailored templates can be found at:

 HYPERLINK "https://fast.faa.gov/EMP\_Information\_Security.cfm" https://fast.faa.gov/EMP\_Information\_Security.cfm

**Instructions for completing the template**

This template uses the following conventions:

Text in sharp brackets < > is to be replaced with investment initiative specific information.

Plain text is actual assessment text that should be used as is.

Technical terms within the assessment will be italicized and bold-faced to indicate the term is defined in the glossary (Appendix A).

Text enclosed in square brackets [ ] denotes editorial notes and must be deleted from the assessment report.

Text in italics that is preceded by the tag *“Instruction:”* is instructional information and will not be part of the assessment report.

**TITLE PAGE**

**Preliminary Information Systems Security Risk Assessment for <Investment Initiative****Name>**

<date>

**Focal Point**

*Name:*

*Organizational Code:*

*Phone Number:*

*Email address:*

Federal Aviation Administration

800 Independence Avenue SW

Washington, DC 20591

**TABLE OF CONTENTS**

**TOC \O "1-3" \H \Z \U** **HYPERLINK \L "\_TOC152165274"** 1.0 introduction **PAGEREF \_TOC152165274 \H 4**

 **HYPERLINK \L "\_TOC152165275"** 2.0 Prospective capability description **PAGEREF \_TOC152165275 \H 5**

 HYPERLINK \L "\_TOC152165276" 2.1 Prospective Capability Purpose  PAGEREF \_TOC152165276 \H 9

 HYPERLINK \L "\_TOC152165277" 2.2 Service Environment  PAGEREF \_TOC152165277 \H 9

 HYPERLINK \L "\_TOC152165278" 2.3 Capability Users, Operators and Potential Threats  PAGEREF \_TOC152165278 \H 10

 HYPERLINK \L "\_TOC152165279" 2.4 Information Security Policies and Proactive Compliance  PAGEREF \_TOC152165279 \H 11

 **HYPERLINK \L "\_TOC152165280"** 3.0 investment initiative security categorization **PAGEREF \_TOC152165280 \H 13**

 HYPERLINK \L "\_TOC152165281" 3.1 Identification of Information Types  PAGEREF \_TOC152165281 \H 14

 HYPERLINK \l "\_Toc152165282" 3.1.1 Mission-Based Information Types  PAGEREF \_Toc152165282 \h 14

 HYPERLINK \l "\_Toc152165283" 3.1.2 Management and Support Information Types  PAGEREF \_Toc152165283 \h 16

 HYPERLINK \l "\_Toc152165284" 3.1.3 Other Information Types  PAGEREF \_Toc152165284 \h 16

 HYPERLINK \l "\_Toc152165285" 3.1.4 Sensitive Unclassified Information (SUI) other than Sensitive Flight Data  PAGEREF \_Toc152165285 \h 16

 HYPERLINK \l "\_Toc152165286" 3.1.5 Records Management Office Input  PAGEREF \_Toc152165286 \h 17

 HYPERLINK \L "\_TOC152165287" 3.2 Initial Investment Initiative Security Category  PAGEREF \_TOC152165287 \H 17

 HYPERLINK \L "\_TOC152165288" 3.3 Investment Initiative Security Category  PAGEREF \_TOC152165288 \H 20

 **HYPERLINK \L "\_TOC152165289"** 4.0 PRELIMINARY INFORMATION SYSTEM SECURITY REQUIREMENTS **PAGEREF \_TOC152165289 \H 21**

 HYPERLINK \L "\_TOC152165290" 4.1 Investment Initiative Security Category Impact Level and Baseline Security Control  PAGEREF \_TOC152165290 \H 21

 HYPERLINK \L "\_TOC152165291" 4.2 Tailoring of the Baseline Security Controls  PAGEREF \_TOC152165291 \H 21

 HYPERLINK \l "\_Toc152165292" 4.2.1 Controls Allocated to Common Control Providers and Cloud Service Providers  PAGEREF \_Toc152165292 \h 24

 HYPERLINK \l "\_Toc152165293" 4.2.2 Supplementing Control Baselines  PAGEREF \_Toc152165293 \h 25

 HYPERLINK \l "\_Toc152165294" 4.2.3 Applying Scoping Considerations  PAGEREF \_Toc152165294 \h 25

 HYPERLINK \l "\_Toc152165295" 4.2.4 Selecting Compensating Controls If Needed  PAGEREF \_Toc152165295 \h 27

 HYPERLINK \l "\_Toc152165296" 4.2.5 Assigning Security Control Parameter Values  PAGEREF \_Toc152165296 \h 27

 HYPERLINK \l "\_Toc152165297" 4.2.6 Controls to Protect Sensitive Flight Data (SFD)  PAGEREF \_Toc152165297 \h 27

 HYPERLINK \l "\_Toc152165298" 4.2.7 Controls to Protect Sensitive Unclassified Information (SUI) other than SFD  PAGEREF \_Toc152165298 \h 28

 HYPERLINK \L "\_TOC152165299" 4.3 Information System Security Requirements for the pPRD  PAGEREF \_TOC152165299 \H 28

 **HYPERLINK \L "\_TOC152165300"** 5.0 FACTORS FOR ROUGH ISS COST ESTIMATE **PAGEREF \_TOC152165300 \H 29**

 HYPERLINK \L "\_TOC152165301" 5.1 Investment Initiative Security Category  PAGEREF \_TOC152165301 \H 29

 HYPERLINK \L "\_TOC152165302" 5.2 Single or Multiple Facility Deployment  PAGEREF \_TOC152165302 \H 29

 HYPERLINK \L "\_TOC152165303" 5.3 Reliability, Maintainability and Availability (RMA) Requirements  PAGEREF \_TOC152165303 \H 29

 HYPERLINK \L "\_TOC152165304" 5.4 Prospective Capability Complexity  PAGEREF \_TOC152165304 \H 29

 HYPERLINK \L "\_TOC152165305" 5.5 Custom-Made Components  PAGEREF \_TOC152165305 \H 29

 HYPERLINK \L "\_TOC152165306" 5.6 Comparable Systems  PAGEREF \_TOC152165306 \H 29

 HYPERLINK \L "\_TOC152165307" 5.7 Availability of Enterprise ISS Capabilities  PAGEREF \_TOC152165307 \H 30

 HYPERLINK \L "\_TOC152165308" 5.8 Service  PAGEREF \_TOC152165308 \H 30

 **HYPERLINK \L "\_TOC152165309"** 6.0 factors for rough iss benefit estimate **PAGEREF \_TOC152165309 \H 30**

 HYPERLINK \L "\_TOC152165310" 6.1 Service Volume  PAGEREF \_TOC152165310 \H 30

 HYPERLINK \L "\_TOC152165311" 6.2 Service Dollar Value  PAGEREF \_TOC152165311 \H 30

 **HYPERLINK \L "\_TOC152165312"** Appendix A. Glossary **PAGEREF \_TOC152165312 \H 31**

 **HYPERLINK \L "\_TOC152165313"** Appendix B. INVESTMENT INITIATIVE SECURITY CATEGORY TABLE **PAGEREF \_TOC152165313 \H 33**

 **HYPERLINK \L "\_TOC152165314"** Appendix C. Information System security requirements for <THE system name> preliminary PROGRAM requirements document **PAGEREF \_TOC152165314 \H 34**

 **HYPERLINK \L "\_TOC152165315"** Appendix D. Acronyms **PAGEREF \_TOC152165315 \H 35**

**1.0 INTRODUCTION**

***Instruction:*** *Section 1 has two mutually exclusive alternatives.*

***Alternative 1:******Instruction for investments with no information service or system component***

*If the service shortfall is of such a nature that an information service component is clearly ruled out (for example, the service need is mowing the lawns of a given FAA facility) then use the introductory paragraph below this instruction, and complete processing the template up to Section 3 and the corresponding table for Appendix B. The resulting table in Appendix B should be blank, otherwise the investment initiative is required to complete the entire assessment; i.e., use alternative 2 below. Please note that “not being connected to a network”, “the system is isolated”, or “the system is stand alone” are not valid reasons for seeking assessment exception because isolated systems are subject to threats introduced by vectors other than a network, e.g. the supply chain threat, auxiliary detachable storage devices, and insider threat.*

*In selecting this alternative, be aware of extrinsic information service needs and how the shortfall is framed. For example, the same mechanical transport shortfall may be worded in the following two ways: (1) There is a shortfall of slow speed vehicles to distribute mail at a given FAA facility or (2) There is shortfall in the transport of mail at a given FAA facility. The first wording explicitly expresses that there is a need to acquire slow speed vehicles and most likely rules out any information service need, while the second is more open to extrinsic information service needs such as a command and control to operate an automated mechanical mail transport.*

The shortfall associated with this <investment initiative name> has been determined that it does not have any intrinsic or extrinsic information service needs and as such, it does not require a full information system security assessment. The documentation that demonstrates that the shortfall does not have any intrinsic or extrinsic information is provided in Sections 2, 3.1, and Appendix B.

***Alternative 2: Instruction for investments with an information service or system component***

*As explained in section 1.4 of the ISGSA, ISGSA information security assessments apply to capability or service shortfalls with an information service component. The main objective of the* ***Preliminary Information System Security Assessment*** *is to assess the potential security impact of the information types underlying the service need. If the investment initiative performed the previous assessment, i.e., the* ***ISS Risk Factors Assessment****, then this assessment is nothing more than an update based on firmer data discovered during concept and requirements definition.*

*Use the introductory paragraph provided below. Include the text in curly brackets if this assessment is an update of the* ***ISS Risk Factors*** Assessment; *otherwise delete it.*

The objective of this assessment is to determine the <investment initiative name> ISS requirements for the security section of the preliminary Program Requirements Document (PRD) based on the ***security******category*** and information ***security******threats*** to the prospective capability. The assessment is based on {the preliminary information developed in the **ISS Risk Factors Assessment** and} the most up-to-date information developed during CRD; i.e., the final shortfall analysis, functional analysis, and solution concept of operations. This assessment will also provide the factors for the rough security cost estimate of the legacy case and each solution alternative, as well as factors for monetizing security benefits from closing the capability shortfall.

Section 2 {is an update of the ISS Risk Factors Assessment Section 2, and it} provides the description for the prospective capability suitable to obtain the information that the capability will generate, store, process, or transmit, and the threats it will potentially face. 

Section 3 {is an update of the ISS Risk Factors Assessment Section 3, and it} provides the <investment initiative name> category impact prepared following the Federal Information Processing Standard (FIPS) 199 “Standards for Security Categorization of Federal Information and Information Systems”  and guidance in NIST Special Publication (SP) NIST SP 800-60 Volume I “Guide for Mapping Types of Information and Information Systems to Security Categories” and NIST SP 800-60 Volume II “Appendices to Guide for Mapping Types of Information and Information Systems to Security Categories.”

Section 4 identifies the ***security control baseline*** based on the results of the investment initiative security categorization in Section 3. This section also develops <the investment initiative name> preliminary ISS requirements based on two ***tailoring*** actions on the selected security baseline: (1) identification of requirements that may be addressed by enterprise level ISS capabilities, also known as common controls, and (2) inclusion of supplementary controls to address known threats in the capability environment, but not addressed by the security control baseline.

Section 5 identifies the most relevant factors and associated quantitative data to obtain a rough cost estimate of the information security costs in the legacy case and each solution alternative.

Section 6 identifies the most relevant factors and associated quantitative data for monetizing the incremental benefits from closing the capability shortfall with the pPRD security requirements in place rather than without them.

**2.0 PROSPECTIVE CAPABILITY DESCRIPTION**

***Instruction:***

*Provide a description of the prospective capability. If the investment initiative was described in the previous assessment, i.e., the* ***ISS Risk Factors Assessment****, then this section is nothing more than an update based on additional and more reliable data discovered during concept and requirements definition.*

*Use the introductory paragraph provided below.*

The prospective capability description developed in this section is from the point of view of information security. The description includes the purpose of the prospective capability, the environment in which it will operate (the service environment), and the anticipated users and potential threats. This section also identifies FAA enterprise-level and lower level policies applicable to the capability, and related actions that investment initiative sponsors can take to get the capability in an early compliance track. The information from this section will be used in Section 3 to identify the information types that the capability will generate, collect, store, process, or exchange with other capabilities. 

A summary of the characteristics and status of the system underlying the prospective capability is provided by the following table.

*Instruction:*

*Include the following table modified as needed to convey a summary of the characteristics and status of the prospective capability.*

|  |  |
| --- | --- |
| System name | [System Name] |
| System acronym | [Acronym] |
| System owner | [System Owner Name] |
| Organization responsible for this system | [System Owner Organization Code] |
| AMS Milestone & Date | [AMS Milestone & Date] |
| Investment Type | Check the Investment Types that apply:  **FORMCHECKBOX** Single System  **FORMCHECKBOX** Portfolio   **FORMCHECKBOX** New system  **FORMCHECKBOX** Tech Refresh / Sustainment  **FORMCHECKBOX** This will replace an existing system |
| Name of Portfolio, if investment is a component of a portfolio | [It is not part of a portfolio] or [Name of Portfolio] |
| System FIPS 199 Security Categorization  SC system = {(confidentiality, *impact*), (integrity, *impact*), (availability, *impact*)} | [SC = {(confidentiality, *Impact*), (integrity, *Impact*), (availability, *Impact*)} |
| Has the Enterprise Infrastructure Service (EIS) assessment been completed? | **FORMCHECKBOX** Yes, [date]  **FORMCHECKBOX** No |
| Operational status of the System | Check the operational status that applies:   FORMCHECKBOX    Operational    FORMCHECKBOX    Development |
| System type | Check the System type that applies:   FORMCHECKBOX   General Support System (GSS)   FORMCHECKBOX   Major Application (MA)    FORMCHECKBOX   Industrial Control System (ICS)   FORMCHECKBOX   FAA Cloud Provider (FCS)   FCS Cloud Vendor Name:                            FORMCHECKBOX   IaaS  FORMCHECKBOX   SaaS  FORMCHECKBOX   PaaS   FORMCHECKBOX   Other Cloud Provider  Name of Cloud Vendor:   FORMCHECKBOX   IaaS  FORMCHECKBOX   SaaS  FORMCHECKBOX   PaaS  Hosted at FAA Data Center  FORMCHECKBOX   WJHTC  FORMCHECKBOX   SLA Available  FORMCHECKBOX   MMAC  FORMCHECKBOX   SLA Available |
| List the Systems to which the Investment Currently or Plans on Connecting | System Connections: |
| Does the system process, contain, or transmit Sensitive Flight Data (SFD) | FORMCHECKBOX   Yes   FORMCHECKBOX   No |
| Contractor System | Check Contractor System identification that applies:   FORMCHECKBOX   Yes   FORMCHECKBOX   No |
| Type of Communications Gateway between Operating Environments (e.g., NAS Enterprise Security Gateway (NESG), Remote Management Access Gateway (RMAG), Vendor Security Enclave (VSE), etc.) | System is connected to Approved Gateway:   FORMCHECKBOX   Yes   FORMCHECKBOX   NESG   FORMCHECKBOX   RMAG   FORMCHECKBOX   VSE     FORMCHECKBOX   No, Identify/Describe Other: |
| External/Public Facing | Assets are External/Public Facing (Public DMZ):   FORMCHECKBOX   Yes   FORMCHECKBOX   No |
| Personal Identity Verification (PIV) | Check PIV status box that applies:  ☐  PIV-enabled [Include brief description of user type or device that is PIV-enabled, e.g. all System Users, including Administrators]:  ☐ Integrated Windows Authentication (IWA)  ☐ MyAccess Solution  ☐ Not PIV-enabled [Include brief description of user type or device that is not PIV-enabled, e.g. if GSS, Non-Windows/Active Directory (AD) devices]  ☐ Not Applicable  ☐ Partial Implementation |
| Foreign Users outside of the United States   \*NOTE:  Section 3.3 of this document further describes the need to verify if the System is available to foreign users outside of the United States | Check foreign user identification that applies:  ☐ Yes  ☐ No |
| Social Security Number (SSN) Collection | Check SSN collection identification that applies:  ☐ Yes.  Check all that apply below  ☐ Social Security Number (SSN)  ☐ Airman Certification Number  ☐ Pseudo SSN  ☐ Partial SSN  ☐ No |
| If the System is deployed, how many sites?  Include all sites that are part of the System authorization boundary, including Operational and Second Level Support facilities. |  |

**2.1 Prospective Capability Purpose**

*Instruction:*

*Describe the prospective capability purpose. The questions this section should answer include:*

*What customer needs will the capability satisfy?*

*Is the purpose of the capability to support (1) safe and efficient air traffic management,, or (2) air traffic flow management, or (3) maintenance and repair of air traffic systems, or (4) training for air traffic management, or, (5) personnel services and management, or (6) facilities operations management, or (7) system engineering for FAA acquisitions, or (8) communications and public relations, or, (9) other FAA endeavor?*

**2.2 Service Environment**

*Instruction:*

*If information included in this assessment includes Sensitive Unclassified Information (SUI) mark the document with the label SUI as indicated in the General Template Guidance on page iii above.*

*Describe the environment in which the prospective capability will be operated and supported. Questions that this section should answer include:*

*Will the capability operate in a manned or unmanned facility?*

*Will the capability operate in an air traffic facility or an administrative facility?*

*Is the capability part of pre-flight operations, airport ground operations, terminal, en route, traffic flow operations or other environment?*

*Will the capability operate entirely within the FAA or will it interoperate with non-FAA systems? Will interoperations be mediated by a courier service such as FEDEX or by a telecommunications transport?*

*Will the capability operate entirely within the National Airspace System (NAS) or will it have to interoperate with Mission Support systems?*

*Will the capability be provided by a service provider, and if so, will the capability be dedicated to the FAA, or will the FAA be a subscriber sharing the capability with other subscribers?*

*Instruction:*

*Describe or enumerate the(prospective) system authorization boundary, i.e., the system components to be protected by the controls selected in the assessment. The description must include the (prospective) system diagram and a narrative specifying that either:*

*the system is part of a larger system supporting the same function, or*

*the system is a component of a “portfolio” investment, or*

*the system is self-contained.*

*Instruction:*

*Include the following table modified as needed to provide details of proposed and current external system connections:*

**Connecting System NameSystem OwnerExternal to FAA?ProtocolData DirectionData TypeISA/MOU required?***NOP*

 *AFN* | *No* | *SSL* | *Outgoing* | *Radar data* | *Yes* ||  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

**2.3 Capability Users, Operators and Potential Threats**

*Instruction:*

*Provide a list of users, operators, and potential threats or threat sources.*

*Questions to identify the capability users include:*

*What persons and systems are authorized to use the capability?*

*Will the capability be used by FAA employees only, FAA employees and contractors, FAA employees and aircraft operators, or will it be open to the public?*

*Questions to identify system operators include:*

*Will capability maintenance or configuration be performed by FAA technicians or FAA contractors?*

*Will the capability need remote maintenance or configuration?*

*Summarize the user types in tabular format as illustrated below:*

*System User Types*

***User role******Access rights******Assets granted accessTypes of access: Local or remoteUser Type (Federal, Federal Contractor, General Public, or Other)****Internal System User*

 *Read/Write access to all non-Admin modules* | *Desktop environment, and applications* | *Local and remote* | *Federal and Federal contractor* || *System Administrator* | *Read/Write access to all modules* | *Servers, system software, system utilities, and desktop environment* | *Local and remote* | *Federal* |
| *Non-FAA End User* | *Read only access to documentation module* | *Brokered access to specific documentation access* | *Remote* | *Federal and General public* |

*Questions to characterize the security threat profile include:*

*Who may be the unauthorized persons or entities with the motivation, means, and opportunity to access and misuse the capability?*

*Who may be the unauthorized persons or entities with the motivation, means, and opportunity to access and misuse the capability’s maintenance or configuration?*

*In addition to probing the prospective capability with the questions above, the preparers of this assessment may find threat information relevant to the prospective capability by reviewing the capability environment in conjunction with a review of the sample threat sources and sample threat events in Table D-2“Taxonomy of Threat Sources” and Table E-2 “*Representative Examples – Adversarial Threat Events*” in appendices D and E of the NIST SP 800-30 “Guide for Conducting Risk Assessments.*

**2.4 Information Security Policies and Proactive Compliance**

*Instruction:*

*This section should identify the most up-to-date agency-wide and line of business (LOB) or staff office (SO) information system security policies applicable to the investment initiative. This assumes that the solution will be an information service, which implies an underlying system. This section should not be a simple list of policies, but it should also identify the investment initiative sponsor actions that would help put the prospective capability on an early security policy compliance track*.  

*Two examples of enterprise-level policies and corresponding actions include:*

***Policy****: FAA Order 1370.121B: Information Security and Privacy Policy*

***Action****: Identify the information system security officers and their potential acquisition roles, including the information system owner, authorizing official), the LOB/SO information system security lead and others.*

***Policy****: FAA Order JO 1370.114:  Implementation of FAA Telecommunications Infrastructure Services and Information Systems Requirements in the NAS*

***Action:*** *If the investment initiative prospective capability will require telecommunications, networking or gateway services, initiative sponsors must arrange subject-matter expertise to comply with this policy.*

*For NAS systems, look for applicable policies in the Air Traffic Organization (ATO) ISS website:*

*https://my.faa.gov/org/linebusiness/ato/operations/naseo/ATO\_Cybersecurity\_Group/issp/iss\_review.html*

*For FAA systems in general, look for applicable policies in the link for Orders and Notices for Information System Security in the FAA employee (MyFAA) website:*

*https://employees.faa.gov/tools\_resources/orders\_notices/*

**3.0 INVESTMENT INITIATIVE SECURITY CATEGORIZATION**

*Instruction:*

*If the investment initiative was described in the previous assessment, i.e., the* ***ISS Risk Factors Assessment****, then this section is an update and extension based on additional data discovered during the CRD**, e.g., the (final) shortfall analysis report, functional analysis and solution CONOPS.*

*Instruction:*

*The collection and processing of information to determine the investment initiative security category will be facilitated and documented by a table with the format below. Once the table is completed, it will constitute Appendix B of the assessment.*

|  |
| --- |
| **Investment Initiative Security Category** |

**Name and brief description of Information typeConfidentialityRationaleIntegrityRationaleAvailabilityRationale****High water marks for confidentiality, integrity, and availability****High water markblankHigh water markblankHigh water markblank****Investment Initiative Security Category**

 **The highest of the three high water marks** |

*Use the introductory paragraph provided below.*

In this section, the security category for <the investment initiative name> will be determined by following NIST SP 800-60 Rev 1 guidance for the determination of the security impact defined in the FIPS-200 mandatory standard. The investment initiative security category is obtained in three steps. The first step (Section 3.1) identifies all anticipated information types that are collected, stored, exchanged, or otherwise processed by the prospective capability. The second step (Section 3.2) determines the security impact level of each identified information type and the initial investment initiative security category.  In the third step (Section 3.3), the impact levels of individual information types are reviewed and adjusted to obtain the overall investment initiative security category.

**3.1 Identification of Information Types**

*Instruction:*

*Following the guidelines in Section 4.1 of the NIST SP 800-60 and the description of the capability purpose in Section 2.1 of this template, preparers of this assessment make an inventory of all the information types the prospective capability is anticipated of collecting, storing, exchanging, or otherwise processing organized in three categories: mission-based information types, management and support information types, and other required information types*. *Use the introductory paragraph provided below.*

This section will identify prospective capability information types and document them in the first column of the table in Appendix B. In order to assure an exhaustive search, information types will be searched within three categories:

Information that directly support FAA missions (Section 3.1.1)

Management and support information, namely information that indirectly supports the FAA mission, e.g., to manage resources (Section 3.1.2)

Other information, e.g., information types arising from legislative and executive information requirements such as personally identifiable information (PII).

**3.1.1 Mission-Based Information Types**

*Instruction:*

*List in Appendix B the mission-based information types of the prospective capability with a brief description that includes whether the information is stored or processed by the capability or exchanged with other systems.*

*According to SP 800-60, mission-based information types are by definition specific to individual departments and agencies or to specific sets of departments and agencies. For the FAA, mission-based information types must include information used in the provision of safe and efficient air traffic management and air traffic flow management. Preparers of this assessment should also consult Table 4: Mission-Based Information Types and Delivery Mechanisms in SP 800-60 to elicit other possible mission-based information types in <the investment initiative name>. It is anticipated that the mission-based information types assembled by assessment preparers will have finer granularity than the entries in Table 4 and will map to the Table 4 information types “Air Transport,” “Border & Transportation Security” and “Work Force Management.” The finer information types correspond to what NIST SP 800-60 refers to as sub-functions necessary to conduct agency business and in turn accomplish the agency’s mission. A useful reference for detailed NAS information types is the NAS Enterprise Architecture SV-6 Mid-Term* *Systems/ Services Data Exchange Matrix Version 4.0 which identifies the following information types: Aeronautical Information, Airspace Management Information, Airspace Security Information, Collaboration Information, Control Information, Flight Information, Maintenance Information, NAS Status Information, Notices to Airmen, Processed Surveillance Information, Raw Surveillance Information, Speed and Position Information, Traffic Flow Information, Weather Information, Weather Radar Data, Weather Sensor Data.* 

*Investment initiatives for prospective services or systems that generate, receive, transfer, or otherwise process flight information must identify this information type as described in Section 3.1.1.1 below.*

The mission-based information types collected, stored, or exchanged with other capabilities or otherwise processed by the prospective capability are documented in the first column of the Investment Initiative Security table in Appendix B along with a brief description. Mission-based information types include information used in the provision of safe and efficient air traffic management and air traffic flow management.

**3.1.1.1   Flight information type and Sensitive Flight Data (SFD)**

*Instruction:*

*Use just one of the following options.*

*Option 1**Instruction:*

*If the prospective system of the investment initiative does not generate, receive, transfer, or otherwise process flight information, use the following paragraph, and move to the next section.*

The prospective system of this investment initiative does not generate, receive, transfer, or otherwise process flight information. Accordingly, the table in appendix B does not include the “Flight information” type.

*Option 2 Instruction:*

*If the prospective system of this investment initiative does generate, receive, transfer, or otherwise process flight information, the preparers of the assessment must consult with the NAS Data Release Board (NDRB) of the ATO Systems Operations Security (AJR-2)* ***to make a determination if all, some, or none of the flight information in question includes Sensitive Flight Information, formally called Sensitive Flight Data by AJR-2.*** *Sensitive Flight Data (SFD) is defined in FAA Order 1370.121B, and it is reproduced in Appendix A of this template. According to the results of this consultation with the NDRB, Appendix B must include the “Flight Information” type, or the “Sensitive Flight Data” information type, or both. In the event that the assessment preparers are not able to contact the NDRB, the assessment preparers will not include in Appendix B the “Flight Information” type, but rather they will list all their flight information as “Sensitive Flight Data” information type.*

*Use just one of the following statements.*

<This investment **consulted with the NDRB and determined the prospective system of this investment** includes flight information, none of which is Sensitive Flight Data (SFD). Accordingly, Appendix B lists only “Flight Information” among the mission-based information types.>

<This investment **consulted with the NDRB and determined the prospective system of this investment** includes flight information, all of which fits the definition of Sensitive Flight Data (SFD). Accordingly, Appendix B lists “Sensitive Flight Data” among the mission-based information types, but does not list “Flight Information”.>

<This investment **consulted with the NDRB and determined the prospective system of this investment** includes flight information, some of which is Sensitive Flight Data (SFD) and some is ordinary Flight Information. Accordingly, Appendix B lists both “Sensitive Flight Data” and “Flight Information” among the mission-based information types.>

<The prospective system of this investment **contains flight information but the investment was not able to** **consult with the NDRB** and obtain a ruling of whether such flight information does or does not include Sensitive Flight Data. Accordingly, per NDRB directive, Appendix B lists ONLY “Sensitive Flight Data” among the mission-based information types and does not include “Flight Information”**.**>

**3.1.2 Management and Support Information Types**

*Instruction:*

*List in Appendix B the prospective capability management and support information types with a brief description that includes whether the information is stored or processed by the capability or exchanged with other systems.*

*Management and Support Information Types include information that is not employed directly to provide mission-based services, but are primarily intended to support delivery of services or to manage resources.*

*Use Table 5 “Service Delivery Support Functions and Information Types” and Table 6 “Government Resource Management Functions and Information Types” from SP 800-60 Sections 4.1.2 and 4.1.3 to identify <investment initiative name> management and support information types. Examples of management and support information types from SP 800-60 include: “C.5.3.8 System and Network Monitoring”, “C.2.8.9 Personal Identity and Authentication”, “C.2.4.2 Continuity of Operations”, “C.2.4.1 Contingency Planning” and “C.3.5.3 System Maintenance”.*

The management and support information types collected, stored, or exchanged with other capabilities or otherwise processed by the prospective capability are documented in the first column of the Investment Initiative Security table in Appendix B along with a brief description. Management and support information types include information that is not employed directly to provide direct mission-based services, but are primarily intended to support delivery of services or to manage resources. 

**3.1.3 Other Information Types**

*Instruction:*

*List in Appendix B the prospective capability information types other than mission-based or management support with a brief description that includes whether the information is stored or processed by the capability, or exchanged with other systems.*

*Identify other information types not included in SP 800-60 tables 4, 5, and 6 following guidelines in SP 800-60 Sections 4.1.3 and 4.1.4, such as information types arising from legislative and executive information requirements.* 

This category of information types includes *PII and* information types arising from legislative and executive information requirements. Information types in this residual category are documented in the first column of the Investment Initiative Security table in Appendix B along with a brief description. The PII documented in Appendix B will be input to the Privacy Threshold Assessment (PTA).

**3.1.4 Sensitive Unclassified Information (SUI) other than Sensitive Flight Data**

 *Instruction:*

*Although it is anticipated that the FAA will adopt the DOT Order 1650.5 Controlled Unclassified Information (CUI) in the future, the current FAA policy for identifying and protecting Sensitive Unclassified Information (SUI) is the 2005 FAA Order 1600.75 as recognized by the 2022 FAA Order 1370.121B Implementing Directive: Protection of Sensitive Unclassified Information (SUI) on Federal and non-Federal Information Systems and Services by External Entities. Use the statement below.*

The current FAA authoritative definition of SUI is provided by FAA Order 1600.75 *Protecting Sensitive Unclassified information*. This definition of SUI is reproduced in Appendix A. 

*Instruction:*

*Examine each of the information types identified in sections 3.1.1, 3.1.2, and 3.1.3, except the Flight Information type, and determine if any meet the definition of SUI. Use just one of the following two options.*

*Option 1 Instruction:*

*The assessment preparers determined that the information types identified in sections 3.1.1, 3.1.2, and 3.1.3 do not include SUI, except perhaps Sensitive Flight Data which is dealt with according to guidance in Section 3.1.1.1 above. Accordingly, include the following statement in the assessment.*

This investment initiative does not include SUI, except perhaps Sensitive Flight Data as documented in Section 3.1.1.1 above.

*Option 2 Instruction:*

*The assessment preparers determined that the information types identified in sections 3.1.1, 3.1.2, and 3.1.3 do include SUI that is not Sensitive Flight Data. Accordingly, include the following statement in the assessment.*

This investment initiative includes SUI information that is not Sensitive Flight Data. These information types are included in the table of information types in Appendix B. Each identified SUI information type name is prefixed with the acronym SUI. 

**3.1.5 Records Management Office Input**

All information types identified in Sections 3.1.1, 3.1.2, 3.1.3 and 3.1.4, i.e., the table in Appendix B with the first column filled in, will be provided to the FAA Office of Records Management with a request for input on (1) data types known to the office and (2) data types that impact PII. The list of data types will also serve as a potential information source for the creation of new records, which would materialize if the investment initiative is eventually implemented.

**3.2 Initial Investment Initiative Security Category**

*Instruction: Use the paragraph below to document the initial investment initiative security category.*

The initial investment initiative security category is <high/moderate/low>. This initial security category has been obtained following the FIPS-199 methodology for categorizing information and information systems. The initial investment initiative security category and intermediate results on which it is based, including the rationale for the potential security impact of each security objective (confidentiality, integrity, and availability) for each information type, is documented in Appendix B. The initial investment initiative and intermediate results on which it is based will be reviewed and adjusted in the next section to obtain the final overall investment initiative security category.

*Instruction for obtaining the initial investment initiative security category:*

*Document all prospective capability information types in the table for Appendix B, as described in Section 3.1*

*For each documented information type, assign impact levels to the information security objectives of confidentiality, integrity, and availability according to the FIPS-199 “Potential Impact Definitions for Security Objectives” table reproduced below after the last bullet of these instructions. Document the rationale under the “Rationale” column of the Appendix B table*.

*In general, mission-based information types are assigned higher impact values than management and support information types, but there are cases when the latter may also get mission-based comparable assignments as is the case with “system management” or “system maintenance” information types.*

*Assignments of “High” impact level will require coordination with and approval from the LOB/SO authorizing official.*

*Impact level assignments must take into account the environment, mission, use, and sharing of information types.*

*To determine the initial investment initiative security category, first find the maximum value (high water mark” for each security objective, i.e. confidentiality, integrity, and availability. The initial (called provisional in the ISS risk factors assessment) investment initiative security category is the highest of the three high water marks.*

FIPS-199 POTENTIAL IMPACT DEFINITIONS FOR SECURITY OBJECTIVES

|  |
| --- |
| **POTENTIAL IMPACT** |
| **Security Objective** | **LOW** | **MODERATE** | **HIGH** |

***Confidentiality***

Preserving authorized restrictions on information access and disclosure, including means for protecting personal privacy and proprietary information. 

|  |
| --- |
| [44 U.S.C., SEC. 3542] The unauthorized disclosure of information could be expected to have a **limited** adverse effect on organizational operations, organizational assets or individuals. The unauthorized disclosure of information could be expected to have a **serious** adverse effect on organizational operations, organizational assets or individuals. The unauthorized disclosure of information could be expected to have a **severe or catastrophic** adverse effect on organizational operations, organizational assets or individuals. |

***Integrity***

Guarding against improper 

information modification 

or destruction, and includes ensuring information non-repudiation and authenticity. 

|  |
| --- |
| [44 U.S.C., SEC. 3542] The unauthorized modification or destruction of information could be expected to have a **limited** adverse effect on organizational operations, organizational assets or individuals. The unauthorized modification or destruction of information could be expected to have a **serious** adverse effect on organizational operations, organizational assets or individuals. The unauthorized modification or destruction of information could be expected to have a **severe or catastrophic** adverse effect on organizational operations, organizational assets or individuals. |

***Availability***

Ensuring timely and reliable access to and use of information. 

|  |
| --- |
| [44 U.S.C., SEC. 3542] The disruption of access to or use of information or an information system could be expected to have a **limited** adverse effect on organizational operations, organizational assets or individuals. The disruption of access to or use of information or an information system could be expected to have a **serious** adverse effect on organizational operations, organizational assets or individuals. The disruption of access to or use of information or an information system could be expected to have a **severe or catastrophic** adverse effect on organizational operations, organizational assets or individuals. |

*In order to help determine the potential impact level, FIPS-199 provides examples of limited, serious, and severe or catastrophic adverse effects, which are reproduced below for ease of reference:*

***A limited adverse effect*** *means that, for example, the loss of confidentiality, integrity, or availability might: (i) cause a degradation in mission capability to an extent and duration that the organization is still able to perform its primary functions, but the effectiveness of the functions is noticeably reduced; (ii) result in minor damage to organizational assets; (iii) result in minor financial loss; or (iv) result in minor harm to individuals.*

***A serious adverse effect*** *means that, for example, the loss of confidentiality, integrity, or availability might: (i) cause a significant degradation in mission capability to an extent and duration that the organization is still able to perform its primary functions, but the effectiveness of the functions is significantly reduced; (ii) result in significant damage to organizational assets; (iii) result in significant financial loss; or (iv) result in significant harm to individuals that does not involve loss of life or serious life-threatening injuries.*

***A severe or catastrophic adverse effect*** *means that, for example, the loss of confidentiality, integrity, or availability might: (i) cause a severe degradation in or loss of mission capability to an extent and duration that the organization is not able to perform one or more of its primary functions; (ii) result in major damage to organizational assets; (iii) result in major financial loss; or (iv) result in severe or catastrophic harm to individuals involving loss of life or serious life-threatening injuries.*

**3.3 Investment Initiative Security Category**

*Instruction: Use the paragraph below to document the investment initiative security category.*

The investment initiative security category is <high/moderate/low>. The investment initiative security category is obtained from the initial investment initiative security category by a process that includes the following adjustments:

Adjust the impact levels of each information type (strikethrough the old values in Appendix B table) as necessary based on the following considerations:

Confidentiality, integrity, and availability factors [800-60 SP Section 4.2.2]

Situational and operational drivers (timing, lifecycle, etc.) [800-60 SP Section 4.3]

Legal or statutory reasons, e.g. privacy [SP 800-60 Section 4.3]

For each information type with an adjusted impact level, add to the rationale field a justification for the adjustments [SP 800-60 Section 4.5]

Update the high water marks (strikethrough old values) to obtain the investment initiative security category.

Submit the Appendix B table, i.e., the security categorization impact levels of the information types and the overall investment security impact level, to the Authorizing Official office for review, adjustments, and approval to ensure uniformity on the LOB/SO application of the categorization criteria subjective judgments.

The resulting investment initiative security category and the intermediate results on which it is based, including the rationale for the security potential impact of each security objective (confidentiality, integrity, and availability) for each information type, are used to update the table in Appendix B.

**4.0 PRELIMINARY INFORMATION SYSTEM SECURITY REQUIREMENTS**

*Instruction:*

*The organization sponsoring the prospective capability must prepare preliminary ISS requirements according to the directions in this section. These directions are based on the mandatory FIPS-200 standard “Minimum Security Requirements for Federal Information Systems”, NIST guidance contained in its Special Publication 800-37 “Guide for Applying the Risk Management Framework to Federal Information Systems”, NIST Special Publication 800-53 Revision 5 “Security and Privacy Controls for Federal Information Systems and Organizations”, and FAA Order 1370.121B.*

*The resulting requirements will be listed in Appendix C and will constitute the ISS requirements section of the pPRD. Use the introductory paragraph provided below.*

The <investment initiative name> preliminary ISS requirements are obtained in three steps. In the first step, a tailored baseline of security controls from the FAA Order 1370.121B or the ATO tailored 800-53 security baselines is chosen based on the investment initiative security category obtained in Section 3. In the second step, the security control baseline is tailored according to the process described in Section 4.2 to generate a set of controls or requirements specific to <investment initiative name>. In the third step, the requirements developed in Section 4.2 are packaged as described in Section 4.3. These controls specifically tailored to <investment initiative> may be further tailored during the Initial Investment Analysis (IIA), if <investment initiative> is required to perform the IIA.

**4.1 Investment Initiative Security Category Impact Level and Baseline Security Control**

*Instruction:* *Use the introductory paragraph provided below.* 

Given that the investment initiative security category impact is <low/moderate/high>, the corresponding <low/moderate/high> baseline of security controls defined in the <FAA Order 1370.121B: FAA Implementation of NIST Controls Implementing Directive > <ATO 800-53 baselines> is chosen as the starting baseline of information security requirements for the investment initiative.  

**4.2 Tailoring of the Baseline Security Controls**

*Instruction:*

*The security baselines published in the* *FAA Order 1370.121B: FAA Information Security and Privacy: FAA Implementation of NIST Controls supplemental implementing directive* *and the ATO 800-53 security baselines are already tailored baselines; however, they may still be subject to additional tailoring depending on the prospective system characteristics, including:*

*Environment –Is the system isolated, interfaces other systems within a single security domain, or extends to other security domains;*

*Number of user types –has only one user type, a few, or numerous user types, etc.*

*Nature –Is the system a production, an operational, or a training system.*

*Impact of security controls on system performance*

*Threats not addressed by the selected control baseline*

*The NIST SP 800-53B tailoring guidance includes the following five activities:*

*Identifying and designating common controls in initial security control baselines*

*Supplementing baselines with additional security controls and control enhancements, if there is reason to believe that <investment initiative name> will be the target of threats not addressed by the security control baseline.*

*Applying scoping considerations to the remaining baseline security controls.*

*Selecting compensating security controls, if needed.*

*Assigning specific values to organization-defined security control parameters via explicit assignment and selection statements.*

*Two additional tailoring activities are needed to ensure the inclusion of controls to protect SFD and non-SFD SUI:*

*Identifying controls to protect Sensitive Flight Data.*

*Identifying controls to protect SUI other than Sensitive Flight Data.*

*Assessment preparers perform the seven tailoring activities which can be revisited and updated at the IID and/or FID investment phase. However, investment initiatives should pay special attention to the first two and the last two activities:*

*The identification and designation of common controls will save time and money to investment initiatives, but investment initiatives must make sure that the common controls are adequate to their performance requirements.*

*Supplementing the investment control baseline with supplementary controls, if there is reason to believe the system will be target of threats not addressed by the baseline. The reason to pay special attention to this tailoring activity is the additional effort and cost that may require implementing such controls.*

*Identifying controls to protect SFD since controls for protecting SFD have been missing in some investments and had to be addressed after implementation.*

*Identifying controls to protect SUI other than Sensitive Flight Data to make sure non-SFD SUI is protected.*

*Use the paragraph provided below.*

As indicated in Section 4.0, the security baselines published in the FAA Order 1370.121B: FAA Implementation of NIST Controls Implementing Directiveand the ATO 800-53 security baselines are already tailored baselines; however, they may still be subject to additional tailoring depending on the prospective system characteristics, including:

Impact of common security controls on system performance

Threats not addressed by the selected control baseline 

Environment –Is the system isolated, interfaces other systems within a single security domain, or extends to other security domains;

Number of user types –has only one user type, a few, or numerous user types, etc.

Nature –Is the system a production, an operational, or a training system.

Identifying controls to protect SFD and non-SFD SUI.

**4.2.1 Controls Allocated to Common Control Providers and Cloud Service Providers**

<The investment initiative name> is allocating a number of their security controls to FAA common control providers and a cloud service provider as specified in Sections 4.2.1.1 and 4.2.1.2 below.

**4.2.1.1 Common Controls provided by FAA Enterprise capabilities**

*Instruction:*

*Investment initiative sponsors identify enterprise-level or LOB/SO-level ISS capabilities (as noted for example in the ATO security requirements matrices for NAS Systems) to tailor for common controls. Examples of enterprise-level ISS capabilities include: the Enterprise Security Gateway, the NAS Cyber Operations (NCO), enterprise-level security awareness and training, and the Cyber Security Management Center**. ATO NAS operating systems (Windows and Linux) baseline configurations also can be considered as long as such consideration does not bias the selection of specific operating system brands.*

Sponsors of <the *investment initiative* name> in consultation with the corresponding LOB/SO security officers have identified enterprise-level and LOB-level ISS capabilities and the corresponding baseline security controls (requirements) they will meet. These enterprise-level capabilities and security controls (requirements) are listed in the table below.

|  |  |
| --- | --- |
| **Enterprise or LOB level ISS Capability** | **Baseline Security Requirements met by the ISS capability** |
|  |  |
|  |  |
|  |  |

**4.2.1.2 Common Controls provided by a Cloud Service Provider**

*Instruction: Choose one of the two mutually exclusive alternatives below.*

*Alternative 1: The implementation solution chosen by the investment initiative includes a Cloud Service Provider. Accordingly use the following text.*

<The investment initiative name> solution implementation includes a cloud service provider. Accordingly, <the investment initiative name> will allocate to the cloud service provider the following list of security controls: 

*Instruction: List the security controls allocated to the cloud service provider.*

*Alternative 2: The implementation solution chosen by the investment initiative does not include a Cloud Service Provider. Accordingly use the following text.*

<The investment initiative name> solution implementation does not include a cloud service provider. Accordingly, <the investment initiative name> will not allocate any controls to a cloud service provider.

**4.2.2 Supplementing Control Baselines**

*Instruction:*

*If there is reason to believe that the prospective capability will be the target of threats not addressed by the security control baseline, prospective capability sponsors will identify supplementary controls from the NIST SP 800-53 Revision 5 catalog to address them. The reason(s) for believing that supplementary controls are necessary to counter those threats must be explained (e.g., intelligence, credible public threats, and previous attacks). Examples of threats not included in the security control baselines are:*

*Threats posed to information capabilities that operate across multiple security domains*

*The advanced persistent threat*

*If there is no need for supplementary controls, then insert a specific statement “There is no need for supplementary controls.”*

**4.2.3 Applying Scoping Considerations**

*Instruction:*

*Eliminate unnecessary security controls from the security control baseline following NIST guidance.*

*NIST SP 800-53B (Section 2.4 pp. 10-12):*

*The application of scoping considerations can eliminate unnecessary security controls from the initial security control baselines and help ensure the service organization selects only those controls needed to provide the appropriate level of protection for the prospective capability—protection based on the mission and business functions being supported by those systems and the environments in which the capability will operate.*

*For NAS systems, no additional scoping is required to the ATO NAS ISS requirement matrices. Questions or concerns must be presented to the ATO ISS Program Office with justification for the elimination of security controls.*

The five ways to identify unnecessary controls and thus eliminate them (scope them out) are given in the following subsections. The baseline requirements for the investment initiative have been reviewed individually and scoped out according to these five ways when appropriate and documented in Appendix C.

**4.2.3.1 Control Allocation and Placement Considerations**

*Instruction:*

*There are instances when a security control applies to a capability but it may not be needed in all its components. If the prospective capability is such a component, then such control may be scoped out. See NIST SP 800-53B page 10 for more details.*

**4.2.3.2 Operational/Environmental-Related Considerations**

*Instruction:*

*Several of the security controls in the baselines are based on the assumption of the existence of certain operational/environmental factors. Where these factors are absent or significantly diverge from baseline assumptions, it is justifiable to tailor the baseline. See examples in NIST SP 800-53B page 11.*

**4.2.3.3 Security Objective-Related Considerations**

*Instruction: Security controls that support only one or two of the confidentiality, integrity, or availability security objectives may be downgraded to the corresponding control in a lower baseline. For example, if an information system is categorized as moderate impact using the high-water mark concept because confidentiality and/or integrity are moderate but availability is low, there are several controls that only support the availability security objective. Those controls potentially could be downgraded to low baseline requirements—that is, it may be inappropriate to implement CP-2 (1) because the control enhancement supports only availability and is selected in the moderate baseline but not in the low baseline. The following security controls and control enhancements are potential candidates for downgrading:*

*- Confidentiality: AC-21, MA-3 (3), MP-3, MP-4, MP-5, MP-5 (4), MP-6 (1), MP-6 (2), PE-4, PE-5, SC-4, SC-8, SC-8 (1)*

*- Integrity: CM-5, CM-5 (1), CM-5 (3), SC-8, SC-8 (1), SI-7, SI-7 (1), SI-7 (5), SI-10*

*- Availability: CP-2 (1), CP-2 (2), CP-2 (3), CP-2 (4), CP-2 (5), CP-2 (8), CP-3 (1), CP-4 (1), CP-4 (2), CP-6, CP-6 (1), CP-6 (2), CP-6 (3), CP-7, CP-7 (1), CP-7 (2), CP-7 (3), CP-7 (4), CP-8, CP-8 (1), CP-8 (2), CP-8 (3), CP-8 (4), CP-9 (1), CP-9 (2), CP-9 (3), CP-9 (5), CP-10 (2), CP-10 (4), MA-6, PE-9, PE-10, PE-11, PE-11 (1), PE-13 (1), PE-13 (2), PE-13 (3), PE-15 (1).*

**4.2.3.4 Technology Considerations**

*Instruction:*

*Security controls that refer to specific technologies (e.g., wireless, cryptography, public key infrastructure) are applicable only if those technologies are employed or are required to be employed within organizational information systems.*

*Security controls that can be explicitly or implicitly supported by automated mechanisms do not require the development of such mechanisms if the mechanisms do not already exist or are not readily available in commercial or government off-the-shelf products. If automated mechanisms are not readily available, cost-effective or technically feasible, compensating security controls, implemented through non-automated mechanisms or procedures, are used to satisfy specified security controls or control enhancements.*

**4.2.3.5 Mission and Business Considerations**

*Instruction:*

*Some security controls may not be applicable (or appropriate) if implementing those controls has the potential to degrade, debilitate, or otherwise hamper critical organizational missions and/or business functions. For example, if the mission requires that an uninterrupted display of mission-critical information be available at an operator console (e.g., air traffic controller console), the implementation of AC-11, Session Lock or SC-10, Network Disconnect may not be appropriate.*

**4.2.4 Selecting Compensating Controls If Needed**

*Instruction:*

*Following NIST SP 800-53B guidance (p. 12), select compensating controls if needed. Compensating controls are alternative security controls employed by organizations in lieu of specific controls in the low, moderate, or high baselines described in Appendix D. These controls provide equivalent or comparable protection for organizational information systems and the information processed, stored, or transmitted by those systems. This may occur, for example, when organizations are unable to effectively implement specific security controls in the baselines, or when due to the specific nature of the information systems or environments of operation (for example authentication of air traffic controllers at their control stations).*

The preparers of this assessment have identified controls that cannot be effectively implemented due to the specific nature of the prospective capability, and they are documented in Appendix C alongside compensating controls. 

**4.2.5 Assigning Security Control Parameter Values**

*Instruction:*

*Following NIST SP 800-53B guidance (p. 13), assign security control parameter values: Security controls and control enhancements containing embedded parameters (i.e., assignment and selection statements) give organizations the flexibility to define certain portions of controls and enhancements to support specific organizational requirements. Use as much as possible parameter assignments from the Department of Transportation Cybersecurity Compendium.*

*For NAS systems, the baseline security control parameters are located in the appropriate ATO NAS ISS requirements matrices as part of the development or collaboration steps of the assessment process described in Section 4.3 of the ISGSA. Use the following paragraph.*

In Appendix C, the parameter value assignments for security controls are provided in brackets for easy identification of the assignments.

**4.2.6 Controls to Protect Sensitive Flight Data (SFD)**

*Instruction:*

*Use just one of the two following options.*

*Option 1 Instruction: If the investment does not include SFD as determined by Section 3.1.1.1 use the paragraph below.*

The information types of this investment do not include SFD.

*Option 2 Instruction: If the investment does include SFD as determined by Section 3.1.1.1 use the paragraph below.*

The information types of this investment include SFD. Accordingly, it must include the SFD protections specified within the FAA Order 1370.121B controls: AC-3(11), CM-12, IR-5, RA-2, RA-3, SA-3(2), SC-28, and AU-13(3). 

Additionally, the assessment must include the following NDRB specific controls:

NDRB review and approval is required prior to any external release of SFD as prescribed by FAA Order 1200.22.

All information security requirements to ensure adequate protection of SFD must be in place prior to NDRB approval of release of SFD.

**4.2.7 Controls to Protect Sensitive Unclassified Information (SUI) other than SFD**

*Instruction:*

*Use just one of the two following alternative options.*

*Option 1 Instruction: The prospective system of this investment does not include SUI except perhaps SFD (see Section 3.1.1.1) as determined by Section 3.1.4; accordingly, use the paragraph below.*

The information types of this investment do not include SUI, except perhaps SFD (see Section 3.1.1.1). Accordingly, Appendix C does not include specific controls to protect Non-SFD SUI.

*Option 2 Instruction: The prospective system of this investment does include SUI that is not SFD (see Section 3.1.1.1) as determined by Section 3.1.4; accordingly, use the paragraph below.*

The information types of this investment include SUI that is not SFD. Accordingly, Appendix C must include the SUI protections specified in the FAA Order 1370.121B Supplemental Implementing Directives: (1) FAA Information Security and Privacy: FAA Implementation of NIST controls and if applicable (2) FAA Information Security and Privacy: Protection of Sensitive Unclassified Information (SUI) on Federal and Non-Federal Information Systems and Services by External Entities. 

**4.3 Information System Security Requirements for the pPRD**

Information security requirements developed following the process described in sections 4.1 and 4.2 constitute <the investment initiative name> preliminary information security requirements. They are documented in Appendix C and become part of the pPRD.

**5.0 FACTORS FOR ROUGH ISS COST ESTIMATE**

*Instruction:*

*In this section, investment initiative sponsors provide the most relevant factors and associated quantitative data for estimating the information security component of the rough cost estimate for each proposed solution alternative to satisfy investment initiative information security requirements. Cost factors listed in Sections 5.1 through 5.6 are only suggested factors*. *Use the introductory paragraph provided below.*

Although the factors and associated data for estimating the information security component of the rough cost estimate for each solution alternative are not part of the Preliminary ISS Assessment, they are a byproduct of the assessment, and they are provided here to inform the Joint Resources Council (JRC) Investment Analysis Readiness Decision (IARD).  

**5.1 Investment Initiative Security Category**

As established in Section 3.3, <the investment initiative name> security category impact level is <level>. The cost of security controls for high security category initiatives will cost more than controls for low security category initiatives because high security category initiatives require enhanced controls, more controls, and higher assurance.

**5.2 Single or Multiple Facility Deployment**

It is anticipated that < the investment initiative name > including backups will have <n> deployments. Solutions with multiple deployments will cost more than single deployment solutions.

**5.3 Reliability, Maintainability and Availability (RMA) Requirements**

It is anticipated that < the investment initiative name> will require <n> nines of availability. The higher the availability required from a solution, the higher is the need for eliminating single points of failure in the security controls, and therefore the higher the cost.

**5.4 Prospective Capability Complexity**

*Instruction:*

*Identify and estimate the measures that may characterize <the prospective capability name> complexity, for example: the number of systems with which it is anticipated to interface or the number of software lines of code.*

**5.5 Custom-Made Components**

<n percent> of the prospective capability components will be custom made. Custom-made components cost more than commodity ready off-the-shelf components.

**5.6 Comparable Systems**

[If an existing system comparable to the prospective capability can be found based on a set of comparison criteria, then the information security cost of the existing system could be used as reference and scaled according to size and other factors.]

The existing <system> is comparable to <the investment initiative name> based on the following factors/rationale: <enumerate factors or provide rationale>.

**5.7 Availability of Enterprise ISS Capabilities**

[Although Enterprise ISS capabilities are not free to “client” systems (they have to pay a share in the first three years), the cost of sharing the common controls provided by the capability should be lower than building the corresponding controls.]

**5.8 Service**

[Controls obtained through a service should in general be lower than building dedicated system controls. In addition, costs may differ by service provider type: cloud, government-owned and government-operated government owned and contractor operated, Contractor owned and contractor operated.]

**6.0 FACTORS FOR ROUGH ISS BENEFIT ESTIMATE**

*Instruction:*

*In this section, assessment preparers provide the most relevant factors and associated quantitative data that may be used for making an estimate of the savings accrued by avoiding the total annual downtime due to staving off denial of service and integrity attacks. Impacts to service safety are not addressed because this assessment does not address safety.*

This section provides the most relevant factors and associated quantitative data that may be used for estimating annual savings accrued by avoiding service downtime due to staving off denial of service and integrity attacks. Assessment preparers do not assess safety benefits because this assessment does not address safety.

**6.1 Service Volume**

*Instruction: Estimate the number of users, transactions, or operations that would be affected by outages of the prospective capability during a year.*

Without security protections, the prospective capability may be interrupted <n> times during the year and in each episode would deny service to <n users/n transactions/ n operations>. 

**6.2 Service Dollar Value**

*Instruction: Estimate the dollar value of the service provided by the prospective capability during one hour of peak service.*

The dollar value of one hour of the service provided by services protected by the prospective security capability is <n dollars>.

**APPENDIX A. GLOSSARY**

*Instruction: Assessment preparers may include in this appendix the glossary provided in Appendix 2 of the Information Security Guidance for System Acquisitions. Assessment preparers may also include in this glossary definitions of their own terms. Assessment preparers should also include in this appendix the following definitions of Sensitive Unclassified Information (SUI) and Sensitive Flight Data (SFD).*

**Sensitive Unclassified Information (SUI):** SUI is information that we must protect from uncontrolled release to persons outside the FAA and indiscriminate dissemination within the FAA. It includes aviation security, homeland security, and protected critical infrastructure information. SUI may include information that may qualify for withholding from the public under the Freedom of Information Act (FOIA). Throughout the Federal government, there are over 50 types of SUI, but within the FAA we generally handle four types: 

a. For Official Use Only (FOUO) information. FOUO is the *primary* designation given to SUI by the Department of Transportation (DOT) and FAA. It consists of information that could adversely affect the national interest, the conduct of Federal programs, or the privacy of individuals if released to unauthorized individuals. As examples, the uncontrolled use of FOUO information may allow someone to:

(1)Circumvent agency laws, regulations, legal standards, or security protective measures or 

(2)Obtain unauthorized access to an information system. 

b. Sensitive Security Information (SSI). SSI is a designation *unique* to the DOT and DOT’s operating administrations and to the Department of Homeland Security (DHS). It applies to information we obtain or develop while conducting *security activities*, including research and development activities. Unauthorized disclosure of SSI would: 

(1)Constitute an unwarranted invasion of privacy (including, but not limited to, information contained in any personnel, medical, or similar file); 

(2)Reveal trade secrets or privileged or confidential information obtained from any person; or 

(3)Be detrimental to transportation safety or security. 

c. Sensitive Homeland Security Information (SHSI). SHSI is a designation *unique* to homeland security information that we share with State and local personnel. The Federal government shares SHSI with State and local personnel who are involved in prevention against, preparation for, or response to terrorism. We protect it because its loss, misuse, unauthorized disclosure or access, or modification can significantly impair the capabilities and efforts of Federal, State, and local personnel to predict, analyze, investigate, deter, prevent, protect against, mitigate the effects of, or recover from acts of terrorism. If our sensitive unclassified information impairs these capabilities, we must designate it SHSI before we share it with State and local personnel to facilitate its proper protection. See also FAA Order 1600.66 Chapter 2, paragraphs 2.c and 3.c. 

d. Protected Critical Infrastructure Information (PCII). PCII is a designation *unique* to critical infrastructure information provided by non-government persons and entities to the DHS. DHS uses the information for security of critical infrastructure and protected systems, analysis, warning, interdependency studies, recovery, reconstitution, or other informational purposes. While only DHS can designate information as PCII, they can share it with other Federal agencies as needed for operational purposes. PCII is defined in 6 CFR Part 29.1. See also Chapter 2, paragraphs 2.d and 3.d. 

**Sensitive Flight Data:** SFD is all flight data related to an individual flight, inclusive of positional, track and identification data (e.g., call sign, aircraft registration number, aircraft type, beacon code, route of flight) about or associated with a sensitive U.S. government mission conducted for the purposes of national defense, homeland security, intelligence, or law enforcement. SFD contains multiple types of Sensitive Unclassified Information (SUI) and must be protected in accordance with requirements contained in FAA Order 1600.75, *Protection of Sensitive Unclassified Information (SUI)*, and FAA Order 1370.121 along with its supplemental implementing directives. 

**APPENDIX B. INVESTMENT INITIATIVE SECURITY CATEGORY TABLE**

*Instruction:*

*Place in this appendix the security categorization table developed according to the process described in Section 3.*

**APPENDIX C. INFORMATION SYSTEM SECURITY REQUIREMENTS FOR <THE SYSTEM NAME> PRELIMINARY PROGRAM REQUIREMENTS DOCUMENT**

*Instruction:*

The controls (requirements) documented in this appendix will constitute the information security requirements of Section 5.3 of the investment initiative Program Requirements Document.

**APPENDIX D. ACRONYMS**

*Instruction: Assessment preparers may include in this appendix the acronyms used in this assessment that are provided in Appendix 3 of the Information Security Guidance for System Acquisitions. Assessment preparers may also include in this appendix new acronyms used in this assessment.*

 Technical terms such as *security category* are italicized and boldfaced to indicate that their authoritative definitions are provided in the Glossary of Terms, Appendix 2 of the ISGSA.

 The terms “controls” and “requirements” are used as equivalent terms because the NIST SP 800-53 controls can be re-stated as requirements as shown in the example below.

**AC-7a 800-53** Control: The system enforces a limit [of 3 consecutive invalid logon attempts] by a user during a [10-minute period.]

**Control re-stated as a requirement**: The system shall enforce a limit of 3 consecutive invalid logon attempts by a user during a 10-minute period.

 The guidance for tailoring the NIST SP 800-53 controls were included in the 800-53 publication up until its revision 4, however, in NIST SP 800-53 Rev 5 that tailoring has been moved to the NIST SP 800-53B publication.

**Preliminary ISS Assessment Template**

Preliminary ISS Assessment Template

January 2024  PAGE   \\* MERGEFORMAT 16
