---
title: "isgsa4"
source_url: https://fast.faa.gov/docs/isgsa4.doc
source_type: doc
converted: 2026-10-27
---
# isgsa4

**Federal Aviation Administration**

**Final Information System Security (ISS)**

**Assessment Template**

**January 2024**

**TEMPLATE TABLE OF CONTENTS**

General Template Guidance ….………….…    iii

Instructions for Completing the Template …...……. iv

Title Page ……………………….……………   1

Assessment Table of Contents …………….…   2

**General Template Guidance**

This ISGSA assessment template has been designed to be used in conjunction with the ISGSA for conducting the final information system security assessment in support of the Acquisition Management System (AMS) final investment analysis.

This template does not include Sensitive Unclassified Information (SUI), however, the assessment report based on this template will contain threat information of a prospective capability and may lead to threat information of a prospective system. Therefore, preparers of the assessment report must determine if the report needs to be marked as SUI in accordance with the most up-to-date FAA Order 1600.75 “Protecting SUI” and in consultation with the sponsoring organization Security Servicing Element (SSE), if necessary.

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

**Final Information Systems Security Assessment for <Investment Initiative Name>**

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

**TOC \O "1-3" \H \Z \U** **HYPERLINK \L "\_TOC152150046"** 1.0 introduction **PAGEREF \_TOC152150046 \H 4**

 **HYPERLINK \L "\_TOC152150047"** 2.0 PROSPECTIVE CAPABILITY description **PAGEREF \_TOC152150047 \H 4**

 HYPERLINK \L "\_TOC152150048" 2.1 Prospective Capability Purpose  PAGEREF \_TOC152150048 \H 5

 HYPERLINK \L "\_TOC152150049" 2.2 Service Environment  PAGEREF \_TOC152150049 \H 5

 HYPERLINK \L "\_TOC152150050" 2.3 Users, Operators, and Potential Threats  PAGEREF \_TOC152150050 \H 5

 HYPERLINK \L "\_TOC152150051" 2.4 Information Security Policies and Proactive Compliance  PAGEREF \_TOC152150051 \H 5

 **HYPERLINK \L "\_TOC152150052"** 3.0 investment initiative security categorization **PAGEREF \_TOC152150052 \H 6**

 HYPERLINK \L "\_TOC152150053" 3.1 Identification of Information Types  PAGEREF \_TOC152150053 \H 6

 HYPERLINK \l "\_Toc152150054" 3.1.1 Mission-Based Information Types  PAGEREF \_Toc152150054 \h 6

 HYPERLINK \l "\_Toc152150055" 3.1.2 Management and Support Information Types  PAGEREF \_Toc152150055 \h 6

 HYPERLINK \l "\_Toc152150056" 3.1.3 Other Information Types  PAGEREF \_Toc152150056 \h 6

 HYPERLINK \l "\_Toc152150057" 3.1.4 Sensitive Unclassified Information (SUI) other than SFD  PAGEREF \_Toc152150057 \h 6

 HYPERLINK \l "\_Toc152150058" 3.1.5 Records Management Office Input  PAGEREF \_Toc152150058 \h 6

 HYPERLINK \L "\_TOC152150059" 3.2 Initial Investment Initiative Security Category  PAGEREF \_TOC152150059 \H 6

 HYPERLINK \L "\_TOC152150060" 3.3 Investment Initiative Security Category  PAGEREF \_TOC152150060 \H 6

 **HYPERLINK \L "\_TOC152150061"** 4.0 FINAL INFORMATION SYSTEM SECURITY REQUIREMENTS **PAGEREF \_TOC152150061 \H 7**

 HYPERLINK \L "\_TOC152150062" 4.1 Investment Initiative Security Category Impact Level and Baseline Security Control  PAGEREF \_TOC152150062 \H 7

 HYPERLINK \L "\_TOC152150063" 4.2 Tailoring Completion of the Baseline Security Control  PAGEREF \_TOC152150063 \H 7

 HYPERLINK \l "\_Toc152150064" 4.2.1 Controls Allocated to Common Control Providers and Cloud Service Providers  PAGEREF \_Toc152150064 \h 7

 HYPERLINK \l "\_Toc152150065" 4.2.2 Supplementary Controls  PAGEREF \_Toc152150065 \h 7

 HYPERLINK \l "\_Toc152150066" 4.2.3 Applying Scoping Considerations  PAGEREF \_Toc152150066 \h 7

 HYPERLINK \l "\_Toc152150067" 4.2.4 Selecting Compensating Controls If Needed  PAGEREF \_Toc152150067 \h 8

 HYPERLINK \l "\_Toc152150068" 4.2.5 Assigning Security Control Parameter Values  PAGEREF \_Toc152150068 \h 8

 HYPERLINK \l "\_Toc152150069" 4.2.6 Controls to protect Sensitive Flight Data (SFD)  PAGEREF \_Toc152150069 \h 8

 HYPERLINK \l "\_Toc152150070" 4.2.7 Controls to protect Sensitive Unclassified Information (SUI) other than SFD  PAGEREF \_Toc152150070 \h 8

 HYPERLINK \L "\_TOC152150071" 4.3 Information System Security Requirements for the fPRD  PAGEREF \_TOC152150071 \H 8

 **HYPERLINK \L "\_TOC152150072"** 5.0 FACTORS FOR ROUGH ISS COST ESTIMATE **PAGEREF \_TOC152150072 \H 9**

 HYPERLINK \L "\_TOC152150073" 5.1 Investment Initiative Security Category  PAGEREF \_TOC152150073 \H 9

 HYPERLINK \L "\_TOC152150074" 5.2 Single or Multiple Facility Deployment  PAGEREF \_TOC152150074 \H 9

 HYPERLINK \L "\_TOC152150075" 5.3 Reliability, Maintainability, and Availability Requirements  PAGEREF \_TOC152150075 \H 9

 HYPERLINK \L "\_TOC152150076" 5.4 Prospective Capability Complexity  PAGEREF \_TOC152150076 \H 9

 HYPERLINK \L "\_TOC152150077" 5.5 Custom-Made Components  PAGEREF \_TOC152150077 \H 9

 HYPERLINK \L "\_TOC152150078" 5.6 Comparable Systems  PAGEREF \_TOC152150078 \H 9

 HYPERLINK \L "\_TOC152150079" 5.7 Availability of Enterprise ISS Capabilities  PAGEREF \_TOC152150079 \H 9

 HYPERLINK \L "\_TOC152150080" 5.8 Service  PAGEREF \_TOC152150080 \H 9

 **HYPERLINK \L "\_TOC152150081"** 6.0 Factors for rough ISS Benefit estimate **PAGEREF \_TOC152150081 \H 9**

 HYPERLINK \L "\_TOC152150082" 6.1 Service Volume  PAGEREF \_TOC152150082 \H 9

 HYPERLINK \L "\_TOC152150083" 6.2 Service Dollar Value  PAGEREF \_TOC152150083 \H 9

 **HYPERLINK \L "\_TOC152150084"** APPENDIX A. GLOSSARY **PAGEREF \_TOC152150084 \H 10**

 **HYPERLINK \L "\_TOC152150085"** APPENDIX B. INVESTMENT INITIATIVE SECURITY CATEGORY TABLE **PAGEREF \_TOC152150085 \H 12**

 **HYPERLINK \L "\_TOC152150086"** APPENDIX C. Information System security requirements for <the INVESTMENT INITIATIVE Name> final program requirements document **PAGEREF \_TOC152150086 \H 13**

 **HYPERLINK \L "\_TOC152150087"** APPENDIX D. ACROnyms **PAGEREF \_TOC152150087 \H 14**

**INTRODUCTION**

***Instruction:*** *Section 1 has two mutually exclusive alternatives*

***Alternative 1:*** *Instruction for investments with no information service or system component*

*If the service shortfall is of such a nature that an information service component is clearly ruled out (for example, the service need is mowing the lawns of a given FAA facility), then use the introductory paragraph below this instruction, complete processing the template up to Section 3, and the corresponding table for Appendix B. The resulting table in Appendix B should be blank, otherwise the investment initiative is required to complete the entire assessment. Please note that “not being connected to a network”, “the system is isolated”, or “the system is stand alone” are not valid reasons for seeking assessment exception because isolated systems are subject to threats introduced by vectors other than a network, e.g. the supply chain threat, auxiliary detachable storage devices, and insider threat.*

*In selecting this alternative be aware of extrinsic information service needs and how the shortfall is agreed to be framed. For example, the same mechanical transport shortfall may be worded in the following two ways: (1) There is a shortfall of slow-speed vehicles to distribute mail at a given FAA facility or (2) There is shortfall in the transport of mail at a given FAA facility. The first wording explicitly expresses that there is a need to acquire slow-speed vehicles and most likely rules out any information service need, while the second is more open to extrinsic information service needs such as a command and control to operate an automated mechanical mail transport.*

The shortfall associated with this <investment initiative name> has been determined that it does not have any intrinsic or extrinsic information service needs and as such it does not require a full information system security assessment. The documentation that demonstrates that the shortfall does not have any intrinsic or extrinsic information is provided in Sections 2, 3.1, and Appendix B. 

***Alternative 2:*** *Instruction**for investments with an information service or system component*

*Use the introductory paragraph provided below.*

The objective of this assessment is to determine the <investment initiative name> ISS requirements for the security section of the final Program Requirements Document (PRD) based on the ***security******category*** and information ***security******threats*** to the prospective capability.

The contents of this assessment are identical to the <the investment initiative name> Initial ISS Assessment except for an update to Section 4 based on the response to a market capability survey. Sections other than Section 4, are reproduced from the Initial ISS Assessment report for sake of completeness.

**PROSPECTIVE CAPABILITY** **DESCRIPTION**

*Instruction:*

*For completeness of the document, carry over in its entirety Section 2 from the Initial ISS Assessment.*

**Prospective Capability Purpose**

**Service Environment**

**Users, Operators, and Potential Threats**

**Information Security Policies and Proactive Compliance**

**INVESTMENT INITIATIVE****SECURITY CATEGORIZATION**

*Instruction:*

*For completeness of the document, carry over in its entirety Section 3 from the Initial ISS Assessment.*

**Identification of Information Types**

**Mission-Based Information Types**

**3.1.1.1 Flight information type and Sensitive Flight Data**

**Management and Support Information Types**

**Other Information Types**

**Sensitive Unclassified Information (SUI) other than SFD**

**Records Management Office Input**

**Initial Investment Initiative Security Category**

**Investment Initiative Security Category**

**FINAL INFORMATION SYSTEM SECURITY REQUIREMENTS**

*Instruction:*

*Use the introductory paragraph provided below**.*

The <investment capability name> final ISS requirements are obtained by updating the < investment capability name> initial ISS requirements based on responses to the request for offers from potential solution providers (market capability survey response). By and large, these updates entail particular requirements that vendors’ responses show are too difficult to achieve or otherwise unfeasible, so they may need to be relaxed and compensated with controls in Section 4.2.4. 

**Investment Initiative Security Category Impact Level and Baseline Security Control**

*Instruction:*

*For completeness of the document, include the “Information System Impact Level and Baseline Security Control” section from the Initial ISS Assessment.*

**Tailoring Completion of the Baseline Security Control**

*Instruction:*

*For completeness of the document, include the “**Tailoring Completion of the Baseline Security* *Control” section from the Initial ISS Assessment.*

**Controls Allocated to Common Control Providers and Cloud Service Providers**

*Instruction:*

*For completeness of the document, include the “**Controls Allocated to Common Control Providers and Cloud Service Providers**” section from the Initial ISS Assessment. Identify common controls that if implemented, it would cause unacceptable system performance and therefore it requires to be substituted by a compensating control in Section 4.2.4*

**4.2.1.1 Common Controls provided by FAA Enterprise capabilities**

**4.2.1.2 Common Controls provided by a Cloud Service Provider**

**Supplementary Controls**

*Instruction:*

*Identify which supplementary requirements are too difficult to achieve or otherwise unfeasible according to vendor responses to the request for offers, and thus need to be relaxed or compensated with controls in Section 4.2.4.*

**Applying Scoping Considerations**

*Instruction:*

*For completeness of the document, include the list of controls that were scoped out in the Initial ISS Assessment. No further scoping out of requirements is expected at this point.*

*For National Airspace System (NAS) systems, any requirements identified for scoping out must be presented to the Air Traffic Organization (ATO) ISS Program Office with justification.*

**Selecting Compensating Controls If Needed**

*Instruction:*

*Find and select controls that may be used to compensate common controls that cannot be implemented as indicated in Section 4.2.1, and system controls that are too difficult to implement or are unfeasible according to the market capability survey.*

**Assigning Security Control Parameter Values**

*Instruction:*

*Identify which requirements developed according to Section 4.2.5 of the Initial ISS Assessment are too difficult to achieve or otherwise unfeasible according to the market capability survey, and thus need to be relaxed and compensated with controls in Section 4.2.4 or in Section 4.2.6.*

*For NAS systems, the baseline security control parameters are located in the appropriate ATO NAS ISS requirements matrices. If the requirements need to be relaxed, justification must be presented to the ATO ISS Program Office as part of the development or collaboration steps of the assessment process described in Section 4.3 of the ISGSA.*

**Controls to protect Sensitive Flight Data (SFD)**

*Instruction:* *For completeness of the document, include the “**Controls to protect Sensitive Flight Data**” section from the Initial ISS Assessment.*

**Controls to protect Sensitive Unclassified Information (SUI) other than SFD**

*Instruction:* *For completeness of the document, include the “**Controls to protect Sensitive Unclassified Information other than SFD**” section from the Initial ISS Assessment.*

**Information System Security Requirements for the fPRD**

The information system security requirements developed following the process described in sections 4.2.1 through 4.2.5 constitute <the investment initiative name> final ISS requirements. They are documented in Appendix C and will become part of the final Program Requirement Document (fPRD).

**FACTORS FOR ROUGH ISS COST ESTIMATE**

*Instruction:*

*For completeness of the document, carry over in its entirety Section 5 from the Initial ISS Assessment.*

**Investment Initiative Security Category**

**Single or Multiple Facility Deployment**

**Reliability, Maintainability, and Availability Requirements**

**Prospective Capability Complexity**

**Custom-Made Components**

**Comparable Systems**

**Availability of Enterprise ISS Capabilities**

**Service**

**FACTORS FOR ROUGH ISS BENEFIT ESTIMATE**

*Instruction:*

*For completeness of the document, carry over in its entirety Section 6 from the Initial ISS Assessment, modified if necessary as noted in the introductory paragraph to Section 1.*

**Service Volume**

**Service Dollar Value**

**APPENDIX A. GLOSSARY**

*Instruction:*

*Assessment preparers may include in this appendix the glossary provided in Appendix 2 of the Information Security Guidance for System Acquisitions. Assessment preparers may also include in this glossary definitions of their own terms. Assessment preparers should also include in this appendix the following definitions of Sensitive Unclassified Information (SUI) and Sensitive Flight Data (SFD).*

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

**APPENDIX B. INVESTMENT INITIATIVE****SECURITY CATEGORY TABLE**

*Instruction:*

*Place in this appendix the security categorization table developed according to the process described in Section 3.*

**APPENDIX C. INFORMATION SYSTEM SECURITY REQUIREMENTS FOR <THE INVESTMENT INITIATIVE****NAME> FINAL PROGRAM REQUIREMENTS DOCUMENT**

*Instruction:*

*The controls (requirements) documented in this appendix will constitute the information security requirements of Section 5.3 of the investment initiative Program Requirements Document.*

**APPENDIX D. ACRONYMS**

*Instruction: Assessment preparers may include in this appendix the acronyms used in this report provided in Appendix 3 of the Information Security Guidance for System Acquisitions. Assessment preparers may also include in this appendix new acronyms used in this report.*

 Technical terms such as *security category* are italicized and boldfaced to indicate that their authoritative definitions are provided in the Glossary of Terms, Appendix 2 of the ISGSA.

**Final ISS Assessment Template**

Final ISS Assessment Template

January 2024  PAGE   \\* MERGEFORMAT 14
