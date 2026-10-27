---
title: "isgsa1"
source_url: https://fast.faa.gov/docs/isgsa1.doc
source_type: doc
converted: 2026-10-27
---
# isgsa1

**Federal Aviation Administration**

**Information System Security (ISS) Risk Factors**

**Assessment Template**

**January 2024**

**TEMPLATE TABLE OF CONTENTS**

General Template Guidance ……………..…    iii

Instructions for Completing the Template ……. iv

Title Page ……………………….……………   1

Assessment Table of Contents …………….…    2

**General Template Guidance**

This ISGSA assessment template has been designed to be used in conjunction with the Information Security Guidance for System Acquisitions (ISGSA) for conducting the Information System Security (ISS) risk factors assessment in support of FAA acquisitions during the Acquisition Management System (AMS) service analysis.

This template does not include Sensitive Unclassified Information (SUI). However, the assessment report based on this template will contain threat information of a prospective capability and may lead to threat information of a prospective system. Therefore, the preparers of the assessment report must determine if the report needs to be marked as SUI in accordance with the most up-to-date FAA Order 1600.75 “Protecting SUI” and in consultation with the sponsoring organization Security Servicing Element (SSE), if necessary.

Subject to review by the NAS Systems Engineering and Integration Directorate (ANG-B) to ensure compliance with the ISGSA, a Line of Business or Staff Office (LOB/SO) Authorizing Official (AO) may tailor this ISGSA assessment template to suit the LOB/SO specific needs. However, if the LOB/AO tailoring requires modification of the ISGSA, the LOB/SO tailoring and ISGSA modification will require the Acquisition Systems Advisory Group (ASAG) review and the Acquisition Executive Board (AEB) approval. LOB/SO investment initiatives must use the corresponding LOB/SO tailored template, if one exists. Note that any retailoring of LOB/SO tailored templates is also subject to this review process.

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

**Information Systems Security Risk Factors Assessment for**

**<Investment initiative Name>**

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

**TOC \O "1-3" \H \Z \U** **HYPERLINK \L "\_TOC152165054"** 1.0 introduction **PAGEREF \_TOC152165054 \H 3**

 **HYPERLINK \L "\_TOC152165055"** 2.0 Preliminary prospective CAPABILITY description **PAGEREF \_TOC152165055 \H 4**

 HYPERLINK \L "\_TOC152165056" 2.1 Prospective Capability Purpose  PAGEREF \_TOC152165056 \H 8

 HYPERLINK \L "\_TOC152165057" 2.2 Service Environment  PAGEREF \_TOC152165057 \H 8

 HYPERLINK \L "\_TOC152165058" 2.3 Capability Users, Operators and Potential Threats  PAGEREF \_TOC152165058 \H 9

 HYPERLINK \L "\_TOC152165059" 2.4 Information Security Policies and Proactive Compliance  PAGEREF \_TOC152165059 \H 10

 **HYPERLINK \L "\_TOC152165060"** 3.0 provisional investment initiative security categorization **PAGEREF \_TOC152165060 \H 12**

 HYPERLINK \L "\_TOC152165061" 3.1 Identification of Information Types  PAGEREF \_TOC152165061 \H 12

 HYPERLINK \l "\_Toc152165062" 3.1.1 Mission-Based Information Types  PAGEREF \_Toc152165062 \h 13

 HYPERLINK \l "\_Toc152165063" 3.1.2 Management and Support Information Types  PAGEREF \_Toc152165063 \h 15

 HYPERLINK \l "\_Toc152165064" 3.1.3 Other Information Types  PAGEREF \_Toc152165064 \h 15

 HYPERLINK \l "\_Toc152165065" 3.1.4 Sensitive Unclassified Information other than Sensitive Flight Data  PAGEREF \_Toc152165065 \h 15

 HYPERLINK \L "\_TOC152165066" 3.2 Provisional Investment Initiative Security Category  PAGEREF \_TOC152165066 \H 17

 **HYPERLINK \L "\_TOC152165067"** APPENDIX A. GLOSSARY **PAGEREF \_TOC152165067 \H 19**

 **HYPERLINK \L "\_TOC152165068"** APPENDIX B. investment initiative Provisional SECURITY CATEGORY TABLE **PAGEREF \_TOC152165068 \H 21**

 **HYPERLINK \L "\_TOC152165069"** APPENDIX C. ACRONYMS **PAGEREF \_TOC152165069 \H 22**

**INTRODUCTION**

*Instruction:*

*As explained in Section 1.4 of the ISGSA, the ISGSA information security assessments apply to investment initiatives arising from capability or service shortfalls with an information service component.* *A service or capability shortfall is said to have an information service component if it is concerned with generating, sending, receiving, processing or storing information. The main objective of the Information System Security (ISS) Risk Factors Assessment is to assess the potential security impact of the information underlying such an investment initiative. The results of this assessment have a provisional character and will be updated in the Preliminary ISS Assessment because knowledge of the prospective capability information types (for a definition of information type see the ISGSA Glossary) will most likely be limited during service analysis. Depending on whether the service need has an obvious, uncertain, or no information service component, the introductory paragraph will be written in one of three alternative ways.*

*Instruction: Introductory paragraph alternative 1*

*If the information service component in the service shortfall is evident at the outset of the investment initiative, as is the case with shortfalls that may be satisfied by a cloud service, use the introductory paragraph provided below and proceed to process the remaining sections of the template. Otherwise, follow one of the other alternative instructions in this section.*

The objective of this assessment is to determine a provisional <investment initiative name> ***security******category*** and provide a characterization of information ***security******threats*** to the prospective capability, i.e., the capability that will fulfill the service/capability shortfall. This information will give the FAA Enterprise Architecture Board (FEAB) an early indication of the security needs for the <investment initiative name> and will also provide input to the < investment initiative name > cloud suitability assessment. In addition, the preliminary capability description assembled during the assessment will be provided as input to the preparers of the solution concept of operations to be developed in the next acquisition phase: Concept and Requirements Definition (CRD).

Section 2 provides the preliminary description of the prospective capability suitable to get an early idea of the information that the prospective capability will generate, store, process, or exchange, and the threats it will potentially face. 

Section 3 determines the <investment initiative name> provisional security category following National Institute of Standards and Technology (NIST) guidance:

1. Federal Information Processing Standard (FIPS) 199 “Standards for Security Categorization of Federal Information and Information Systems”

2. NIST Special Publication (SP) NIST SP 800-60 Volume I “Guide for Mapping Types of Information and Information Systems to Security Categories,” and 

3. NIST SP 800-60 Volume II “Appendices to Guide for Mapping Types of Information and Information Systems to Security Categories.”

*Instruction: Introductory paragraph alternative 2*

*If it is not clear during service analysis that the service/capability shortfall has an information service component, omit the information risk assessment for this phase. Use the introductory paragraph below and delete the rest of text in the template.*

It is not clear at this point if the service shortfall corresponding to <investment initiative name> has an information service component, and thus the ISS risk factors must be omitted. Should the information service component materialize during the CRD planning phase, the service organization will conduct the Preliminary ISS Assessment at that time.

*Instruction: Introductory paragraph alternative 3*

*If the service shortfall is of such a nature that an information service component is clearly ruled out (for example, the service need is mowing the lawns of a given FAA facility) then use the introductory paragraph below and complete processing the template up to Section 3.1 and the corresponding table for Appendix B. The resulting table in Appendix B should be empty, otherwise the investment initiative is required to complete the entire assessment. Please note that “not being connected to a network”, “the system is isolated”, or “the system is stand alone” are not valid reasons for seeking assessment exception because isolated systems are subject to threats introduced by vectors other than a network, e.g. the supply chain threat, auxiliary detachable storage devices, and insider threat.*

*In selecting this alternative be aware of extrinsic information service needs and how the shortfall is agreed to be framed. For example, the same mechanical transport shortfall may be worded in the following two ways: (1) There is a shortfall of slow-speed vehicles to distribute mail at a given FAA facility or (2) There is shortfall in the transport of mail at a given FAA facility. The first wording explicitly expresses that there is a need to acquire slow-speed vehicles and most likely rules out any information service need, while the second is more open to extrinsic information service needs such as a command and control to operate an automated mechanical mail transport.*

The shortfall associated with this <investment initiative name> has been determined that it does not have any intrinsic or extrinsic information service needs and as such it does not require a full information system security assessment. The documentation that demonstrates that the shortfall does not have any intrinsic or extrinsic ***information types*** is provided in Sections 2, 3 and Appendix B. 

**PRELIMINARY PROSPECTIVE CAPABILITY****DESCRIPTION**

*Instruction:*

*Use the paragraph provided below.* 

The prospective capability description developed in this section is from the point of view of information security. The description includes the purpose of the prospective capability, the environment in which it will operate (the service environment), and anticipated users and potential threats. The information from this section will be used in Section 3 to identify the information types that the capability will collect, store, process, or exchange with other capabilities. This section (Section 2) also identifies FAA enterprise-level and lower-level policies applicable to the capability, and related actions that investment initiative sponsors can take to get the capability in an early compliance track.

A summary of the characteristics and status (as much as is known at this stage) of the system underlying the prospective capability is provided by the following table.

*Instruction:*

*Include the following table modified as needed to convey a summary of the characteristics and status of the prospective capability.*

|  |  |
| --- | --- |
| System name | [System Name] |
| System acronym | [Acronym] |
| System owner | [System Owner Name] |
| Organization responsible for this system | [System Owner Organization Code] |
| AMS Milestone & Date | [ Milestone & Date] |
| Investment Type | Check the Investment Types that apply:  **FORMCHECKBOX** Single System  **FORMCHECKBOX** Portfolio   **FORMCHECKBOX** New system  **FORMCHECKBOX** Tech Refresh / Sustainment  **FORMCHECKBOX** This will replace an existing system |
| Name of Portfolio, if investment is a component of a portfolio | [It is not part of a portfolio] or [Name of Portfolio] |
| System FIPS 199 Security Categorization  SC system = {(confidentiality, *impact*), (integrity, *impact*), (availability, *impact*)} | [SC = {(confidentiality, *Impact*), (integrity, *Impact*), (availability, *Impact*)} |
| System type | Check the System type that applies:   FORMCHECKBOX   General Support System (GSS)   FORMCHECKBOX   Major Application (MA)    FORMCHECKBOX   Industrial Control System (ICS)   FORMCHECKBOX   FAA Cloud Provider (FCS)   FCS Cloud Vendor Name:                            FORMCHECKBOX   IaaS  FORMCHECKBOX   SaaS  FORMCHECKBOX   PaaS   FORMCHECKBOX   Other Cloud Provider  Name of Cloud Vendor:   FORMCHECKBOX   IaaS  FORMCHECKBOX   SaaS  FORMCHECKBOX   PaaS  Hosted at FAA Data Center  FORMCHECKBOX   WJHTC  FORMCHECKBOX   SLA Available  FORMCHECKBOX   MMAC  FORMCHECKBOX   SLA Available |
| List the Systems to which the Investment Currently or Plans on Connecting | System Connections: |
| Does the system process, contain, or transmit Sensitive Flight Data (SFD) | FORMCHECKBOX   Yes   FORMCHECKBOX   No |
| Contractor System | Check Contractor System identification that applies:   FORMCHECKBOX   Yes   FORMCHECKBOX   No |
| Type of Communications Gateway between Operating Environments (e.g., NAS Enterprise Security Gateway (NESG), Remote Management Access Gateway (RMAG), Vendor Security Enclave (VSE),  etc.) | System is connected to Approved Gateway:   FORMCHECKBOX   Yes   FORMCHECKBOX   NESG   FORMCHECKBOX   RMAG   FORMCHECKBOX   VSE     FORMCHECKBOX   No, Identify/Describe Other: |
| External/Public Facing | Assets are External/Public Facing (Public DMZ):   FORMCHECKBOX   Yes   FORMCHECKBOX   No |
| Personal Identity Verification (PIV) | Check PIV status box that applies:  ☐  PIV-enabled [Include brief description of user type or device that is PIV-enabled, e.g. all System Users, including Administrators]:  ☐ Integrated Windows Authentication (IWA)  ☐ MyAccess Solution  ☐  Not PIV-enabled [Include brief description of user type or device that is not PIV-enabled, e.g. if GSS, Non-Windows/Active Directory (AD) devices]  ☐  Not Applicable  ☐  Partial Implementation |
| Foreign Users outside of the United States   \*NOTE:  Section 3.3 of this document further describes the need to verify if the System is available to foreign users outside of the United States | Check foreign user identification that applies:  ☐  Yes  ☐   No |
| Social Security Number (SSN) Collection | Check SSN collection identification that applies:  ☐  Yes.  Check all that apply below  ☐  Social Security Number (SSN)  ☐  Airman Certification Number  ☐  Pseudo SSN  ☐  Partial SSN  ☐  No |

**Prospective Capability****Purpose**

*Instruction:*

*Describe the prospective capability purpose. Questions this section should answer include:*

*What customer needs will the capability satisfy?*

*Is the purpose of the capability to support (1) safe and efficient air traffic management, or (2) air traffic flow management, or (3) maintenance and repair of air traffic systems, or (4) training for air traffic management, or, (5) personnel services and management, or (6) facilities operations management, or (7) system engineering for FAA acquisitions, or (8) communications and public relations, or (9) other FAA endeavor?*

**Service Environment**

*Instruction:*

*If information included in this assessment includes Sensitive Unclassified Information (SUI) mark the document with the label SUI as indicated in the General Template Guidance on page iii above.*

*Describe the environment in which the prospective capability will be operated and supported.*

*Questions this section should answer include:*

*Will the capability operate in a manned or unmanned facility?*

*Will the capability operate in an air traffic facility, an administrative facility, or a Research and Development environment?*

*Is the capability part of pre-flight operations, airport ground operations, terminal, en-route, traffic flow operation, or other environment?*

*Will the capability operate entirely within the FAA, or will it interoperate with non-FAA systems?*

*Will interoperations be mediated by a courier service, such as FEDEX, or by a telecommunications transport?*

*Will the capability operate entirely within the National Airspace System (NAS), or will it have to interoperate with Mission Support systems?*

*Will the capability be provided by a service provider, and if so, will the capability be dedicated to the FAA, or will the FAA be a subscriber sharing the capability with other subscribers**?*

*Instruction:*

*Describe as much as the available information at this stage permits the(prospective) system authorization boundary, i.e., the system components to be protected by the controls selected in the assessment. The description must include the (prospective) system diagram and a narrative specifying that either:*

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

**Capability Users, Operators and Potential Threats**

*Instruction:*

*Provide a list of users, operators, and potential threats or threat sources.*

*Questions to identify the capability users include:*

*What persons and systems will be authorized to use the capability?*

*Will the capability be used by FAA employees only, FAA employees and contractors, FAA employees and aircraft operators, or will it be open to the public?*

*Questions to identify the capability operators include:*

*Will the capability maintenance or configuration be performed by FAA technicians or FAA contractors?*

*Will the capability need remote maintenance or configuration?*

*Summarize the user types in tabular format as illustrated below:*

*System User Types*

***User roleAccess rightsAccess******Types of access: Local or remoteUser Type (Federal, Federal Contractor, General Public, or Other)****Internal System User*

 *Read/Write access to all non-Admin modules* | *Desktop environment, and applications* | *Local and remote* | *Federal and Federal contractor* || *System Administrator* | *Read/Write access to all modules* | *Servers, system software, system utilities, and desktop environment* | *Local and remote* | *Federal* |
| *Non-FAA End User* | *Read only access to documentation module* | *Brokered access to specific documentation access* | *Remote* | *Federal and General public* |

*Questions to characterize the security threat profile include:*

*Who may be the unauthorized persons or entities with the motivation, means, and opportunity to access and misuse the capability?*

*Who may be the unauthorized persons or entities with the motivation, means, and opportunity to access and misuse the capability’s maintenance or configuration?*

*In addition to probing the prospective capability with the questions above, the preparers of this assessment may find threat information relevant to the prospective capability by reviewing the capability environment in conjunction of a review of the sample threat sources and sample threat events in Table D-2“Taxonomy of Threat Sources” and Table E-2 “*Representative Examples – Adversarial Threat Events*” in appendices D and E of the NIST SP 800-30 “Guide for Conducting Risk Assessments.*

**Information Security Policies and Proactive Compliance**

*Instruction:*

*This section should identify the most up-to-date agency-wide and line of business (LOB) or staff office (SO) information system security policies applicable to the investment initiative. This assumes that the solution will be an information service, which implies an underlying system. This section should not be a simple list of policies, but it should also identify the investment initiative sponsor actions that would help put the prospective capability on an early security policy compliance track*. 

*An example of enterprise-level policy and corresponding action include:*

**Policy***: FAA Order 1370.121B: Information Security and Privacy Policy*

**Action***: Identify the information security officers and their potential acquisition roles, including the information system owner, authorizing official, the LOB/SO information system security lead and others.*

*For NAS systems, look for applicable policies in the ATO Information System Security website:*

*https://my.faa.gov/org/linebusiness/ato/operations/naseo/ATO\_Cybersecurity\_Group/issp/iss\_review.html*

*For FAA systems in general, look for applicable policies in the link for Orders and Notices for Information System Security in the FAA employee (MyFAA) website:*

*https://employees.faa.gov/tools\_resources/orders\_notices/*

**PROVISIONAL INVESTMENT INITIATIVE SECURITY CATEGORIZATION**

*Instruction:*

*The collection and processing of information to determine the provisional investment initiative security category will be facilitated and documented by a table with the format below. Once the table is completed, it will constitute Appendix B of the assessment.*

|  |
| --- |
| **Investment Initiative Provisional Security Category** |

**Name and brief description of Information typeConfidentialityRationaleIntegrityRationaleAvailabilityRationale****High water marks for confidentiality, integrity and availability****High water markblankHigh water markblankHigh water markblank****Provisional Investment Initiative Security Category**

 **The highest of the three high water marks** |

*Use the introductory paragraph provided below.*

In this section, a provisional security category for the <investment initiative name> will be determined following FIPS-199 and FIPS-200 mandatory standards and NIST SP 800-60 Rev 1. The provisional security category is obtained in two steps. The first step (Section 3.1) identifies all the anticipated information types that are generated, collected, stored, exchanged, or otherwise processed by the prospective capability, and the second step (Section 3.2) determines a provisional investment initiative category. The provisional investment initiative security category is defined in terms of the potential impacts to organizational operations, assets, or individuals that would result from the loss of the ***confidentiality***, ***integrity*** or ***availability*** of any of the prospective capability information types. 

For the CRD phase, this section will be updated with all prospective capability information types identified in the other CRD studies, and it will be extended with two additional steps to determine the final investment initiative security category impact level.

**Identification of Information Types**

*Instruction:*

*Following the guidelines in Section 4.1of NIST SP 800-60 and the description of the capability purpose in Section 2.1 of this template, the preparers of this assessment will make an inventory of all the information types anticipated that the prospective capability will generate, collect, store, exchange, or otherwise process organized into three categories: mission-based information types, management and support information types, and other required information types*. *Use the introductory paragraph provided below.*

This section will identify prospective capability information types. In order to assure an exhaustive search, information types will be searched within three categories:

Information that directly supports the FAA mission(s) (Section 3.1.1)

Management and support information, namely information that indirectly supports the FAA mission, e.g. to manage resources (Section 3.1.2)

Other information, e.g. information types arising from legislative and executive information requirements such as ***personally identifiable information (PII)***.

**Mission-Based Information Types**

*Instruction:*

*List in Appendix B the prospective capability mission-based information types with a brief description that includes whether the information would be stored or processed by the investment prospective capability or exchanged with other systems.*

*According to SP 800-60, mission-based information types are by definition specific to individual departments and agencies or to specific sets of departments and agencies. For the FAA, mission-based information types must include information used in the provision of safe and efficient air traffic management and air traffic flow management. Preparers of this assessment should also consult Table 4: Mission-Based Information Types and Delivery Mechanisms in SP 800-60 to elicit other possible mission-based information types in <the investment initiative name>. It is anticipated that the mission-based information types assembled by the assessment preparers will have a finer granularity of the entries in Table 4 and will map to the Table 4 information types “Air Transport,” “Border & Transportation Security” and “Work Force Management.” The finer information types correspond to what NIST SP 800-60 refers to as sub-functions necessary to conduct agency business and in turn accomplish the agency’s mission. A useful reference for NAS information types is the NAS Enterprise Architecture SV-6 Mid-Term Systems/ Services Data Exchange Matrix Version 4.0 which identifies the following information types: Aeronautical Information, Airspace Management Information, Airspace Security Information, Collaboration Information, Control Information, Flight Information, Maintenance Information, NAS Status Information, Notices to Airmen, Processed Surveillance Information, Raw Surveillance Information, Speed and Position Information, Traffic Flow Information, Weather Information, Weather Radar Data, Weather Sensor Data.*

*Investment initiatives for prospective services or systems that generate, receive, transfer, or otherwise process flight information must identify this information type as described in Section 3.1.1.1 below.* 

The mission-based information types generated, collected, stored, or exchanged with other capabilities or otherwise processed by the prospective capability are included in the first column of the Investment Initiative Security table in Appendix B along with a brief description. Mission-based information types include information used in the provision of safe and efficient air traffic management and air traffic flow management.

**3.1.1.1   Flight information type and Sensitive Flight Data (SFD)**

*Instruction:*

*Use just one of the following options.*

*Option 1**Instruction:*

*If the prospective system of the investment initiative does not generate, receive, transfer, or otherwise process flight information, use the following paragraph, and move to the next section.*

The prospective system of this investment initiative does not generate, receive, transfer, or otherwise process flight information. Accordingly, the table in Appendix B does not include the “Flight information” type.

*Option 2 Instruction:*

*If the prospective system of this investment initiative does generate, receive, transfer, or otherwise process flight information, the preparers of the assessment must consult with the NAS Data Release Board (NDRB) of the ATO Systems Operations Security (AJR-2)* ***to make a determination if all, some, or none of the flight information in question includes Sensitive Flight Information, formally called Sensitive Flight Data by AJR-2.*** *Sensitive Flight Data (SFD) is defined in FAA Order 1370.121B, and it is reproduced in Appendix A of this template. According to the results of this consultation with the NDRB, Appendix B must include the “Flight Information” type, or the “Sensitive Flight Data” information type, or both. In the event that the assessment preparers are not able to contact the NDRB, the assessment preparers will not include in Appendix B the “Flight Information” type, but rather they will list all their flight information as “Sensitive Flight Data” information type.*

*Use just one of the following statements.*

<This investment **consulted with the NDRB and determined the prospective system of this investment** includes flight information, none of which is Sensitive Flight Data (SFD). Accordingly, Appendix B lists only “Flight Information” among the mission-based information types.>

<This investment **consulted with the NDRB and determined the prospective system of this investment** includes flight information, all of which fits the definition of Sensitive Flight Data (SFD). Accordingly, Appendix B lists “Sensitive Flight Data” among the mission-based information types, but does not list “Flight Information”.>

<This investment **consulted with the NDRB and determined the prospective system of this investment** includes flight information, some of which is Sensitive Flight Data (SFD) and some is ordinary Flight Information. Accordingly, Appendix B lists both “Sensitive Flight Data” and “Flight Information” among the mission-based information types.>

<The prospective system of this investment **contains flight information but the investment was not able to** **consult with the NDRB** and obtain a ruling of whether such flight information does or does not include Sensitive Flight Data. Accordingly, per NDRB directive, Appendix B lists ONLY “Sensitive Flight Data” among the mission-based information types and does not include “Flight Information”**.**>

**Management and Support Information Types**

*Instruction:*

*List in Appendix B the prospective capability management and support information types with a brief description that includes whether the information is generated, stored, processed by the prospective investment capability or exchanged with other systems.*

*Management and Support Information Types include information that is not employed directly to provide direct mission-based services, but are primarily intended to support delivery of services or to manage resources.*

*Use Table 5 “Service Delivery Support Functions and Information Types” and Table 6 “Government Resource Management Functions and Information Types” from SP 800-60 Sections 4.1.2 and 4.1.3 to identify <the investment initiative name> management and support information types. Examples of management and support information types from SP 800-60 include: “C.5.3.8 System and Network Monitoring”, “C.2.8.9 Personal Identity and Authentication”, “C2.4.2 Continuity of Operations”, “C.2.4.1 Contingency Planning” and “C.3.5.3 System Maintenance”.*

The management and support information types collected, stored, or exchanged with other capabilities or otherwise processed by the prospective capability are included in the first column of the Investment Initiative Security table in Appendix B along with a brief description. Management and support information types include information that is not employed directly to provide direct mission-based services, but are primarily intended to support delivery of services or to manage resources.

**Other Information Types**

*Instruction:*

*List in Appendix B the prospective capability information types other than mission-based or management support with a brief description that includes whether the information is generated, stored, processed by the prospective capability, or exchanged with other systems.*

*Identify other information types not included in SP 800-60 tables 4, 5, and 6 following guidelines in SP 800-60 Sections 4.1.3 and 4.1.4, such as information types arising from legislative and executive information requirements.* 

This category of information types includes PII andinformation types arising from legislative and executive information requirements. Information types in this residual category are included in the first column of the Investment Initiative Security table in Appendix B along with a brief description.

**Sensitive Unclassified Information other than Sensitive Flight Data**

*Instruction:*

*Although it is anticipated that the FAA will adopt the DOT Order 1650.5 Controlled Unclassified Information (CUI) in the future, the current FAA policy for identifying and protecting Sensitive Unclassified Information (SUI) is the 2005 FAA Order 1600.75 as recognized by the 2022 FAA Order 1370.121B Implementing Directive: Protection of Sensitive Unclassified Information (SUI) on Federal and non-Federal Information Systems and Services by External Entities. Use the statement below.*

The current FAA authoritative definition of SUI is provided by FAA Order 1600.75 *Protecting Sensitive Unclassified Information*. This definition of SUI is reproduced in Appendix A. 

*Instruction:*

*Examine each of the information types identified in sections 3.1.1, 3.1.2, and 3.1.3, except the Flight Information type, and determine if any meet the definition of SUI. Use just one of the following options.*

*Option 1 Instruction:*

*The assessment preparers determined that the information types identified in sections 3.1.1, 3.1.2, and 3.1.3 do not include SUI, except perhaps Sensitive Flight Data which is dealt with according to guidance in Section 3.1.1.1 above. Accordingly, include the following statement in the assessment.*

This investment initiative does not include SUI, except perhaps Sensitive Flight Data as documented in Section 3.1.1.1 above.

*Option 2 Instruction:*

*The assessment preparers determined that the information types identified in sections 3.1.1, 3.1.2, and 3.1.3 do include SUI information that is not Sensitive Flight Data. Accordingly, include the following statement in the assessment.*

This investment initiative includes SUI that is not Sensitive Flight Data. These information types are included in the table of information types in Appendix B. Each identified SUI information type name is prefixed with the acronym SUI. 

**Provisional Investment Initiative Security Category**

*Instruction: Use the paragraph below to document the provisional investment initiative security category.*

The investment initiative provisional security category is <high/moderate/low>. This provisional security category has been obtained following the FIPS-199 methodology for categorizing information and information systems. The data, intermediate results, and investment initiative provisional security are documented in the table presented in Appendix B.

*Instruction for obtaining the provisional investment initiative security category:*

*Document all prospective capability information types in the table for Appendix B, as described in Section 3.1*

*For each documented information type, assign impact levels to the information security objectives of confidentiality, integrity, and availability according to the FIPS-199 “Potential Impact Definitions for Security Objectives” table reproduced below after the last bullet of these instructions. Document the rationale under the “Rationale” column of the Appendix B table*.

*In general, mission-based information types are assigned higher impact values than management and support information types, but there are cases when the latter may also get mission-based comparable assignments as is the case with “system management” or “system maintenance” information types.*

*Assignments of “High” impact level will require coordination with the LOB/SO authorizing official.*

*The impact level assignments must take into account the environment, mission, use, and sharing of the information types.*

*To determine the provisional investment initiative security category, first find the maximum value “high water mark” for each security objective, i.e., confidentiality, integrity, and availability. The provisional investment initiative security category is the highest of the three high water marks.*

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

**A limited adverse effect** *means that, for example, the loss of confidentiality, integrity or availability might: (i) cause a degradation in mission capability to an extent and duration that the organization is still able to perform its primary functions, but the effectiveness of the functions is noticeably reduced; (ii) result in minor damage to organizational assets; (iii) result in minor financial loss or (iv) result in minor harm to individuals.*

**A serious adverse effect** *means that, for example, the loss of confidentiality, integrity or availability might: (i) cause a significant degradation in mission capability to an extent and duration that the organization is still able to perform its primary functions, but the effectiveness of the functions is significantly reduced; (ii) result in significant damage to organizational assets; (iii) result in significant financial loss; or (iv) result in significant harm to individuals that does not involve loss of life or serious life-threatening injuries.*

**A severe or catastrophic adverse effect** *means that, for example, the loss of confidentiality, integrity or availability might: (i) cause a severe degradation in or loss of mission capability to an extent and duration that the organization is not able to perform one or more of its primary functions; (ii) result in major damage to organizational assets; (iii) result in major financial loss; or (iv) result in severe or catastrophic harm to individuals involving loss of life or serious life-threatening injuries.*

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

**APPENDIX B. INVESTMENT INITIATIVE PROVISIONAL SECURITY CATEGORY TABLE**

*Instruction:*

*Place in this appendix the table developed according to the process described in Section 3.*

**APPENDIX C. ACRONYMS**

*Instruction: Assessment preparers may include in this appendix the acronyms provided in Appendix 3 of the Information Security Guidance for System Acquisitions. Assessment preparers may also include in this appendix new acronyms.*

 Technical terms in the assessment, i.e. outside of the instructional paragraphs, such as the term security category are italicized and boldfaced to indicate that their authoritative definitions are provided in the Glossary of Terms, Appendix 2 of the ISGSA.

**ISS Risk Factors Assessment Template**

ISS Risk Factors Assessment Template

January 2024  PAGE   \\* MERGEFORMAT 16
