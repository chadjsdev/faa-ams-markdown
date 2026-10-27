---
title: "isgsa3"
source_url: https://fast.faa.gov/docs/isgsa3.doc
source_type: doc
converted: 2026-10-27
---
# isgsa3

**Federal Aviation Administration**

**Initial Information System Security (ISS) Assessment Template**

**January 2024**

**TEMPLATE TABLE OF CONTENTS**

General Template Guidance ….………..….…    iii

Instructions for Completing the Template ……..  iv

Title Page ……………………….……………..   1

Assessment Table of Contents ……….…….…    2

**General Template Guidance**

This ISGSA assessment template has been designed to be used in conjunction with the ISGSA for conducting the Initial Information System Security Assessment in support of the Acquisition Management System (AMS) initial investment analysis.

This template does not include Sensitive Unclassified Information (SUI), however, the assessment report based on this template will contain threat information of a prospective capability and may lead to threat information of a prospective system. Therefore, the preparers of the assessment report must determine if the report needs to be marked as SUI in accordance with the most up-to-date FAA Order 1600.75 “Protecting SUI” and in consultation with the sponsoring organization Security Servicing Element (SSE), if necessary. 

Subject to review by ANG-B to ensure compliance with the ISGSA, a Line of Business or Staff Office (LOB/SO) Authorizing Official (AO) may tailor this ISGSA assessment template to suit the LOB/SO specific needs. However, if the LOB/AO tailoring requires modification of the ISGSA, the LOB/SO tailoring and ISGSA modification will require ASAG review and AEB approval. LOB/SO investment initiatives must use the corresponding LOB/SO tailored template, if one exists. Note that any retailoring of LOB/SO tailored templates is also subject to this review process. 

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

**Initial Information Systems Security Assessment for <Investment Initiative Name>**

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

**TOC \O "1-3" \H \Z \U** **HYPERLINK \L "\_TOC118789736"** 1.0 introduction **PAGEREF \_TOC118789736 \H 4**

 **HYPERLINK \L "\_TOC118789737"** 2.0 prospective capability description **PAGEREF \_TOC118789737 \H 5**

 HYPERLINK \L "\_TOC118789738" 2.1 Prospective Capability Purpose  PAGEREF \_TOC118789738 \H 5

 HYPERLINK \L "\_TOC118789739" 2.2 Service Environment  PAGEREF \_TOC118789739 \H 5

 HYPERLINK \L "\_TOC118789740" 2.3 Capability Users, Operators, and Potential Threats  PAGEREF \_TOC118789740 \H 5

 HYPERLINK \L "\_TOC118789741" 2.4 Information Security Policies and Proactive Compliance  PAGEREF \_TOC118789741 \H 5

 **HYPERLINK \L "\_TOC118789742"** 3.0 investment initiative security categorization **PAGEREF \_TOC118789742 \H 5**

 HYPERLINK \L "\_TOC118789743" 3.1 Identification of Information Types  PAGEREF \_TOC118789743 \H 6

 HYPERLINK \l "\_Toc118789744" 3.1.1 Mission-Based Information Types  PAGEREF \_Toc118789744 \h 6

 HYPERLINK \l "\_Toc118789745" 3.1.2 Management and Support Information Types  PAGEREF \_Toc118789745 \h 6

 HYPERLINK \l "\_Toc118789746" 3.1.3 Other Information Types  PAGEREF \_Toc118789746 \h 6

 HYPERLINK \l "\_Toc118789747" 3.1.4 Sensitive Unclassified Information (SUI) other than Sensitive Flight Data  PAGEREF \_Toc118789747 \h 6

 HYPERLINK \l "\_Toc118789748" 3.1.5 Records Management Office Input  PAGEREF \_Toc118789748 \h 6

 HYPERLINK \L "\_TOC118789749" 3.2 Initial Investment Initiative Security Category  PAGEREF \_TOC118789749 \H 7

 HYPERLINK \L "\_TOC118789750" 3.3 Investment Initiative Security Category  PAGEREF \_TOC118789750 \H 7

 **HYPERLINK \L "\_TOC118789751"** 4.0 initial INFORMATION SYSTEM SECURITY REQUIREMENTS **PAGEREF \_TOC118789751 \H 8**

 HYPERLINK \L "\_TOC118789752" 4.1 Investment Initiative Security Category Impact Level and Baseline Security Control  PAGEREF \_TOC118789752 \H 8

 HYPERLINK \L "\_TOC118789753" 4.2 Tailoring Completion of the Baseline Security Control  PAGEREF \_TOC118789753 \H 8

 HYPERLINK \l "\_Toc118789754" 4.2.1 Controls Allocated to Common Control Providers and Cloud Service Providers  PAGEREF \_Toc118789754 \h 9

 HYPERLINK \l "\_Toc118789755" 4.2.2 Supplementary Controls  PAGEREF \_Toc118789755 \h 9

 HYPERLINK \l "\_Toc118789756" 4.2.3 Applying Scoping Considerations  PAGEREF \_Toc118789756 \h 9

 HYPERLINK \l "\_Toc118789757" 4.2.4 Selecting Compensating Controls If Needed  PAGEREF \_Toc118789757 \h 9

 HYPERLINK \l "\_Toc118789758" 4.2.5 Assigning Security Control Parameter Values  PAGEREF \_Toc118789758 \h 9

 HYPERLINK \l "\_Toc118789759" 4.2.6 Controls to protect Sensitive Flight Data (SFD)  PAGEREF \_Toc118789759 \h 10

 HYPERLINK \l "\_Toc118789760" 4.2.7 Controls to protect Sensitive Unclassified Information (SUI) other than SFD  PAGEREF \_Toc118789760 \h 10

 HYPERLINK \L "\_TOC118789761" 4.3 Information System Security Requirements for the iPRD  PAGEREF \_TOC118789761 \H 10

 **HYPERLINK \L "\_TOC118789762"** 5.0 FACTORS FOR ROUGH ISS COST ESTIMATE **PAGEREF \_TOC118789762 \H 10**

 HYPERLINK \L "\_TOC118789763" 5.1 Investment Initiative Security Category  PAGEREF \_TOC118789763 \H 10

 HYPERLINK \L "\_TOC118789764" 5.2 Single or Multiple Facility Deployment  PAGEREF \_TOC118789764 \H 10

 HYPERLINK \L "\_TOC118789765" 5.3 Reliability, Maintainability and Availability Requirements  PAGEREF \_TOC118789765 \H 10

 HYPERLINK \L "\_TOC118789766" 5.4 Prospective Capability Complexity  PAGEREF \_TOC118789766 \H 10

 HYPERLINK \L "\_TOC118789767" 5.5 Custom-Made Components  PAGEREF \_TOC118789767 \H 10

 HYPERLINK \L "\_TOC118789768" 5.6 Comparable Systems  PAGEREF \_TOC118789768 \H 10

 HYPERLINK \L "\_TOC118789769" 5.7 Availability of Enterprise ISS Capabilities  PAGEREF \_TOC118789769 \H 10

 HYPERLINK \L "\_TOC118789770" 5.8 Service  PAGEREF \_TOC118789770 \H 10

 **HYPERLINK \L "\_TOC118789771"** 6.0 Factors for rough order of magnitude ISS Benefit estimate **PAGEREF \_TOC118789771 \H 10**

 HYPERLINK \L "\_TOC118789772" 6.1 Service Volume  PAGEREF \_TOC118789772 \H 11

 HYPERLINK \L "\_TOC118789773" 6.2 Service Dollar Value  PAGEREF \_TOC118789773 \H 11

 **HYPERLINK \L "\_TOC118789774"** APPENDIX A. GLOSSARY **PAGEREF \_TOC118789774 \H 12**

 **HYPERLINK \L "\_TOC118789775"** APPENDIX B. investment initiative SECURITY CATEGORY TABLE **PAGEREF \_TOC118789775 \H 14**

 **HYPERLINK \L "\_TOC118789776"** APPENDIX C. Information System security requirements for <THE INVESTMENT INITIATIVE Name> initial program requirements document **PAGEREF \_TOC118789776 \H 15**

 **HYPERLINK \L "\_TOC118789777"** APPENDIX D. ACronyms **PAGEREF \_TOC118789777 \H 16**

**INTRODUCTION**

***Instruction:*** *Section 1 has two mutually exclusive alternatives.*

***Alternative 1: Instruction for investments with no information service or system component***

*If the service shortfall is of such a nature that an information service component is clearly ruled out (for example, the service need is mowing the lawns of a given FAA facility), then use the introductory paragraph below this instruction and complete processing the template up to Section 3, and the corresponding table for Appendix B. The resulting table in Appendix B should be blank, otherwise the investment initiative is required to complete the entire assessment; i.e., use alternative 2 below. Please note that “not being connected to a network”, “the system is isolated”, or “the system is stand alone” are not valid reasons for seeking assessment exception because isolated systems are subject to threats introduced by vectors other than a network, e.g. the supply chain threat, auxiliary detachable storage devices, and insider threat.*

*In selecting this alternative be aware of extrinsic information service needs and how the shortfall is agreed to be framed. For example, the same mechanical transport shortfall may be worded in the following two ways: (1) There is a shortfall of slow-speed vehicles to distribute mail at a given FAA facility or (2) There is shortfall in the transport of mail at a given FAA facility. The first wording explicitly expresses that there is a need to acquire slow-speed vehicles and most likely rules out any information service need, while the second is more open to extrinsic information service needs such as a command and control to operate an automated mechanical mail transport.*

The shortfall associated with this <investment initiative name> has been determined that it does not have any intrinsic or extrinsic information service needs and as such it does not require a full information system security assessment. The documentation that demonstrates that the shortfall does not have any intrinsic or extrinsic information is provided in Sections 2, 3.1, and Appendix B.

***Alternative 2: Instruction for investments with an information service or system component***

*Use the introductory paragraph provided below. If the prospective capability description (Section 2) or investment initiative categorization (Section 3) need to be modified, for instance due to splitting the acquisition into segments due to funding constraints or identification of new interfaces, state so in the introduction. Otherwise, keep the paragraph as is.*

The objective of this assessment is to determine the <investment initiative name> ISS requirements for the security section of the initial Program Requirements Document (PRD) based on the ***security******category*** and information ***security******threats*** to the prospective capability.

This assessment updates and extends <the investment initiative name> Preliminary ISS Assessment by completing the tailoring of the selected <FAA Order 1370.121B> <ATO 800-53> baseline of security controls. The main product of the assessment is a set of information security requirements for <the investment initiative name> sufficiently detailed to conduct a market capability survey (part of a screening information request) as stated in Section 4.1.4 of the AMS “Investment Analysis Process Guidance.” This set of security requirements constitutes the ISS component of the initial Program Requirements Document (iPRD).

Section 2, the prospective capability description, and Section 3, the investment initiative security categorization, are carried over without modifications from the Preliminary ISS Assessment.

Section 4 updates and completes the tailoring of the baseline security controls started in the Preliminary ISS Assessment.  

Section 5 updates the identification of the most relevant factors and associated quantitative data for estimating the ISS cost component for each solution alternative proposed by <the investment initiative name> sponsors.

Section 6 updates the most relevant factors and associated quantitative data for monetizing the incremental benefits from closing the capability shortfall with the iPRD security requirements in place rather than without them.

**PROSPECTIVE CAPABILITY DESCRIPTION**

*Instruction:*

*This section is identical to Section 2 of the Preliminary ISS Assessment and thus it should be reproduced below in the interest of having all of the information for this assessment in one place. If the capability**description needs to be modified, for instance due to splitting the acquisition into segments due to funding constraints or identification of new interfaces, make those modifications. Otherwise, keep the reproduction unchanged.*

**Prospective Capability Purpose**

*Instruction:*

*For completeness of the document, include the “Prospective Capability Purpose” from the Preliminary ISS Assessment, modified if necessary as noted in the introductory paragraph to Section 2.*

**Service Environment**

*Instruction:*

*For completeness of the document, include the “Service Environment” section from the Preliminary ISS Assessment, modified if necessary as noted in the introductory paragraph to Section 2.*

**Capability Users, Operators, and Potential Threats**

*Instruction:*

*For completeness of the document, include the “Capability Users, Operators, and Potential Threats” section from the Preliminary ISS Assessment*, *modified if necessary as noted in the introductory paragraph to Section 2.* 

**Information Security Policies and Proactive Compliance**

*Instruction:*

*For completeness of the document, include the “Information Security Policies and Proactive Compliance” section from the Preliminary ISS Assessment, modified if necessary as noted in the introductory paragraph to Section 2.*

**INVESTMENT INITIATIVE SECURITY CATEGORIZATION**

*Instruction:*

*Use the introductory paragraph provided below. If <*theinvestment initiative name> *security categorization needs to be modified,  for instance due to splitting the acquisition into segments due to funding constraints or identification of new interfaces, state so in the introductory paragraph below, otherwise keep the paragraph provided below as is.*

This section is identical to Section 3 of <the investment initiative name> Preliminary ISS Assessment and is reproduced below in the interest of having all of the information for this assessment in one place.

**Identification of Information Types**

*Instruction:*

*For completeness of the document, include the “Identification of Information Types” section from the Preliminary ISS Assessment*, *modified if necessary as noted in the introductory paragraph to Section 3.*

**Mission-Based Information Types**

*Instruction:*

*For completeness of the document, include the “Mission-Based Information Types” section from the Preliminary ISS Assessment, modified if necessary as noted in the introductory paragraph to Section 3.* 

**3.1.1.1 Flight Information type and Sensitive Flight Data (SFD)**

*Instruction:*

*For completeness of the document, include the “Flight Information Type” section from the Preliminary ISS Assessment, modified if necessary as noted in the introductory paragraph to Section 3.*

**Management and Support Information Types**

*Instruction:*

*For completeness of the document, include the “Management and Support Information Types” section from the Preliminary ISS Assessment, modified if necessary as noted in the introductory paragraph to Section 3.*

**Other Information Types**

*Instruction:*

*For completeness of the document, include the “Other Information Types” section from the Preliminary ISS Assessment, modified if necessary as noted in the introductory paragraph to Section 3.*

**Sensitive Unclassified Information (SUI) other than Sensitive Flight Data**

*For completeness of the document, include the “Sensitive Unclassified Information other than Sensitive Flight Data” section from the Preliminary ISS Assessment, modified if necessary as noted in the introductory paragraph to Section 3.*

**Records Management Office Input**

*Instruction:*

*For completeness of the document, include the “Records Management Office Input” section from the Preliminary ISS Assessment, modified if necessary as noted in the introductory paragraph to Section 3.*

**Initial Investment Initiative Security Category**

*Instruction:*

*For completeness of the document, include the “Initial Investment Initiative Security Category” section from the Preliminary ISS Assessment, modified if necessary as noted in the introductory paragraph to Section 3.*

**Investment Initiative Security Category**

*Instruction:*

*For completeness of the document, include the “Investment Initiative Security Category” section from the Preliminary ISS Assessment, modified if necessary as noted in the introductory paragraph to Section 3.*

**INITIAL INFORMATION SYSTEM SECURITY REQUIREMENTS**

*Instruction:*

*Use the introductory paragraph provided below**.*

The <investment initiative name> initial ISS requirements are obtained by updating and extending the tailoring process started in the preliminary ISS requirements or controls. 

**Investment Initiative Security Category Impact Level and Baseline Security Control**

*Instruction:*

*For completeness of the document, include the “Investment Initiative Security Category Impact Level and Baseline Security Control” section from the Preliminary ISS Assessment, modified if necessary as noted in the introductory paragraph to Section 4.*

**Tailoring Completion of the Baseline Security Control**

*Instruction:*

*The security baselines published in the* *FAA Order 1370.121B: FAA Information Security and Privacy: FAA Implementation of NIST Controls supplemental implementing directive* *and the ATO 800-53 security baselines are already tailored baselines; however, they may still be subject to additional tailoring depending on the prospective system characteristics, including:*

*Environment –Is the system isolated, interfaces other systems within a single security domain, or extends to other security domains;*

*Number of user types –has only one user type, a few, or numerous user types, etc.*

*Nature –Is the system a production, an operational, a training system.*

*Impact of security controls on system performance*

*Threats not addressed by the selected control baseline*

*The NIST SP 800-53B tailoring guidance includes the following five activities:*

*Identifying and designating common controls in initial security control baselines*

*Supplementing baselines with additional security controls and control enhancements if there is reason to believe that <the investment initiative name> will be the target of threats not addressed by the security control baseline*

*Applying scoping considerations to the remaining baseline security controls*

*Selecting compensating security controls, if needed*

*Assigning specific values to organization-defined security control parameters via explicit assignment and selection statements*

*Two additional tailoring activities are needed to ensure the inclusion of controls to protect SFD and non-SFD SUI:*

*Identifying controls to protect Sensitive Flight Data.*

*Identifying controls to protect SUI other than Sensitive Flight Data.*

*The tailoring activities should have been performed in the Preliminary ISS Assessment, and they can be updated in this assessment. Use the paragraph provided below.*

This assessment updates the above tailoring activities performed in the Preliminary ISS Assessment. The resulting requirements are documented in Appendix C.

**Controls Allocated to Common Control Providers and Cloud Service Providers**

*Instruction:*

*Update the “Controls Allocated to Common Control Providers and Cloud Service Providers” section prepared in the Preliminary ISS Assessment with any new information, e.g., inauguration of new controls in an existing ISS enterprise capability or the inauguration of a new ISS enterprise capability.*

**Supplementary Controls**

*Instruction:*

*Update the “Supplementary Controls” section prepared in the Preliminary ISS Assessment with any new information, e.g., new controls required due to the discovery of a new threat not included in the security controls baseline.*

**Applying Scoping Considerations**

*Instruction:*

*Update the “Scoping Considerations” Section 4.2.3 and subsections prepared in the Preliminary ISS Assessment with any new information.*

**Selecting Compensating Controls If Needed**

*Instruction:*

*Update the “Compensating Controls” section prepared in the Preliminary ISS Assessment with any new information.*

**Assigning Security Control Parameter Values**

*Instruction:*

*Update the “Assigning Security Control Parameter Values” section prepared in the Preliminary ISS Assessment with any new information.*

**Controls to protect Sensitive Flight Data (SFD)**

*Instruction:*

*Update the “Controls to protect Sensitive Flight Data” section prepared in the Preliminary ISS Assessment with any new information.*

**Controls to protect Sensitive Unclassified Information (SUI) other than SFD**

*Instruction:*

*Update the “Controls to protect Sensitive Flight Data” section prepared in the Preliminary ISS Assessment with any new information.*

**Information System Security Requirements for the iPRD**

The information system security requirements developed following the process described in sections 4.2.1 through 4.2.5 constitute <the investment initiative name> initial ISS requirements. They are documented in Appendix C and will become part of the initial Program Requirement Document (iPRD).

**FACTORS FOR ROUGH ISS COST ESTIMATE**

*Instruction:*

*For completeness of the document, include Section 5 from the Preliminary ISS Assessment with any updates arising from new information*. *Use the introductory paragraph provided below.* 

Although the factors and associated data for estimating the information security component of the rough cost estimate of each solution alternative are not part of the Preliminary ISS Assessment, they are a byproduct of the assessment. They are provided as input to the Initial Business Case. 

**Investment Initiative Security Category**

**Single or Multiple Facility Deployment**

**Reliability, Maintainability and Availability Requirements**

**Prospective Capability Complexity**

**Custom-Made Components**

**Comparable Systems**

**Availability of Enterprise ISS Capabilities**

**Service**

**FACTORS FOR ROUGH ORDER OF MAGNITUDE ISS BENEFIT ESTIMATE**

*Instruction: For completeness of the document, include Section 5 from the Preliminary ISS Assessment with any updates arising from new information*. *Use the introductory paragraph provided below.*

This section provides the most relevant factors and associated quantitative data that may allow making an estimate of the annual savings accrued by avoiding service downtime due to staving off denial of service and integrity attacks. Assessment preparers will not assess safety benefits because this assessment does not address safety.

**Service Volume**

*Instruction:*

*Estimate the number of users, transactions, or operations that would be affected by outages of the prospective capability during a year.*

Without security protections, the prospective capability may have to be interrupted <n> times during the year and in each episode would deny service to <n users/n transactions/ n operations>.

**Service Dollar Value**

*Instruction:*

*Estimate the dollar value of the service provided by the prospective capability during one hour of peak service.*

The dollar value of one hour of the service provided by the prospective capability is <n dollars>.

**APPENDIX A. GLOSSARY**

*Instruction: Assessment preparers may include in this appendix the glossary provided in Appendix 2 of the Information Security Guidance for System Acquisitions. Assessment preparers may also include in this glossary definitions of their own terms. . Assessment preparers should also include in this appendix the following definitions of Sensitive Unclassified Information (SUI) and Sensitive Flight Data (SFD).*

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

**APPENDIX C. INFORMATION SYSTEM SECURITY REQUIREMENTS FOR <THE INVESTMENT INITIATIVE NAME> INITIAL PROGRAM REQUIREMENTS DOCUMENT**

*Instruction:*

*The controls (requirements) documented in this appendix will constitute the information security requirements of Section 5.3 of the investment initiative Program Requirements Document.*

**APPENDIX D. ACRONYMS**

Instruction: Assessment preparers may include in this appendix those acronyms provided in Appendix 3 of the Information Security Guidance for System Acquisitions used in this assessment report. Assessment preparers may also include in this appendix new acronyms used in this assessment report.

 Technical terms such as *security category* are italicized and boldfaced to indicate that their authoritative definitions are provided in the Glossary of Terms, Appendix 2 of the ISGSA.

 The terms “controls” and “requirements” are used as equivalent terms because the NIST SP 800-53 controls can be re-stated as requirements as shown in the example below.

**AC-7a 800-53** Control: The system enforces a limit [of 3 consecutive invalid logon attempts] by a user during a [10-minute period].

**Control re-stated as a requirement**: The system must enforce a limit of 3 consecutive invalid logon attempts by a user during a 10-minute period.

**Initial ISS Assessment Template**

Initial ISS Assessment Template

January 2024  PAGE   \\* MERGEFORMAT 16
