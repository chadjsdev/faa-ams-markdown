---
title: "programreq"
source_url: https://fast.faa.gov/docs/programreq.docx
source_type: docx
converted: 2026-10-27
---
# programreq

![FAA Logo. Consists of 3 concentric rings with the outermost ring in a thin gold circle. the next inner ring is thick with a blue background. It has the FAA's name in gold with two gold stars seperating Federal Aviation from Administration. The next ring is a thin gold circle. In the middle is a picture of a green globe with gold latitude and longitude lines. on top of this gold is a with cross pointing in 4 directions perpendicular to each other with an eagle wing in the center. At the top point of the cross there is a gold fluer de lis symbol.](data:image/jpeg;base64...)

Program Requirements Document Template

For AMS Acquisitions

Version 2.5 September 2024

**Responsible Organizations:**

ANG-B1 NAS Enterprise Architecture and Requirements Services Division

ADE-200 Enterprise & Portfolio Insight Division

**GENERAL GUIDANCE**

Investment program requirements drive the search for a realistic and affordable solution to implement a desired capability improvement for the Federal Aviation Administration (FAA). Investment program requirements align to the Shortfall Analysis Report (SAR), Solution Concept of Operations (ConOps), Functional Analysis Document (FAD) and Enterprise Architecture (EA) artifacts. The responsible Line of Business (LOB) and designated program management office, along with program stakeholder representatives from external LOBs, develops the Program Requirements Document (PRD) during the various phases of the Acquisition Management System (AMS) lifecycle.

Program requirements define the operational framework and performance requirements an investment program must achieve and are not typically used for contracting agreements. For National Airspace System (NAS) and Mission Support investments, program requirements will define how the program is established to fulfill the identified shortfalls within the agency. For these investments, references to “solution” in this template not only refer to the candidate product(s) but also the program as a whole.

The National Airspace System (NAS) Enterprise Architecture & Requirements Services Division (ANG-B1) and the Enterprise & Portfolio Insight Division (ADE-200) maintain the Program Requirements template.

**PRD Development**

Development of the PRD is an iterative process with each iteration supporting the needs of the associated AMS Phase and Decision Point. There are three iterations of the PRD:

* pPRD - CRD
* iPRD - IIA
* fPRD – FIA

Successive investment phases from Concepts and Requirements Definition (CRD) to Final Investment Analysis (FIA) progressively add more detail and specificity to the program requirements. The preliminary PRD (pPRD) establishes the basis for determining alternative solutions and estimating costs. It is important to identify high-level requirements that drive cost and a statement of work definition. The pPRD contains only high-level requirements derived from the FAD. Refrain from entering requirements into the pPRD that are implementation specific or overly restrictive to the search for solutions.

If there are known constraints to the program, incorporate the constraints as requirements into the PRD even if they are implementation‐specific because the constraints drive cost estimation and further requirements decomposition. For example, if a program is required to be compliant with a given communication standard for regulatory reasons, this implementation‐specific requirement is appropriate for inclusion in the pPRD since the requirement traces to the communication standard. The pPRD also serves as a basis for the alternatives analysis that will occur during Initial Investment Analysis (IIA). Most of these requirements will be functional with a very limited set of performance requirements (e.g., Reliability, Maintainability, and Availability (RMA), Resiliency, Information Systems Security (ISS) and safety).

The initial PRD (iPRD) serves for evaluating alternatives and developing the Statement of Work (SOW) and associated draft specification(s). The iPRD contains requirements that are solution agnostic, contain sufficient information for quality Return on Investment (ROI) assessments and support the IIA phase. The iPRD includes new functional requirements resulting from functions developed during a lower-level decomposition of the functions in the FAD, as well as a much larger set of performance requirements.

The final PRD (fPRD) contains requirements conforming to the selected alternative and may include additional requirements as more information becomes available on the selected solution during Final Investment Analysis. In addition, the fPRD defines the programmatic, functional, and performance requirements for the investment program and establishes the baseline program requirements.

Investments usually develop the System Specification Document (SSD), which contains solution-specific requirements for a program, prior to/shortly after the Final Investment Decision (FID). The system specification(s) derive from the fPRD and directly trace to the requirements in the fPRD. Use the [FAA-STD-067 Preparation of Specifications](http://www.tc.faa.gov/its/worldpac/standards/faa-std-067.pdf) as the guideline and template in developing the program’s SSD.

All requirements in a program's SSD demonstrate traceability to the PRD through a separate traceability matrix that is part of the SSD. Additionally, the program maintains this traceability matrix to reflect ongoing requirement changes to the fPRD, as well as to the SSD. Include traceability in the SSD to allow changes in details of the document without forcing a revision to the PRD, which would require Joint Resource Council (JRC) approval.

It is highly encouraged that investments use Dynamic Object-Oriented Requirements System (DOORS) to create and maintain their PRDs, SSDs and their associated traceability matrix to enable automated traceability between products. For access to DOORS, please contact [ANG-B11 Requirements and Analysis Branch](https://ksn2.faa.gov/nextgen/SysEng/NASEAandRqmts/RA/SitePages/Home.aspx). In order to import program’s Word documents into DOORS, ANG-B1 recommends investments use the Heading style formats within the PRD template. Save the word document in rich text format (rtf). Please use the following heading styles for each level:

* Title of Document— **Title**
* Subtitle- **Subtitle**
* Section 1.0– **Heading 1**
* Section 1.1– **Heading 2**
* Section 1.1.1– **Heading 3**
* Section 1.1.1.1— **Heading 4**
* Requirements, notes, or descriptive text- **Normal (Please do not use Heading styles)**
* Table names– **Table Heading**
* Figure names– **Figure Heading**

**Requirements**

Write all requirements within sections 3.0 to 9.0 as “must” statements. Include all “must” statements in the Verification Requirements Traceability Matrix (VRTM) found in [Appendix 4](#_APPENDIX_4._PROGRAM) Table 8. Annotate all requirements with a document unique requirement identifier.

This document utilizes "must" as the mandatory imperative in requirement statements. Use of "must" as the mandatory imperative complies with Federal Plain Language Guidelines, March 2011 Revision 1, May 2011 and the FAA Plain Language Toolkit accessible from FAA Plan Language Website: <https://www.faa.gov/about/initiatives/plain_language>.

Do not include “will” statements, as these are a statement of intent rather than a requirement. These statements are usually more applicable for [Section 2.0](#_CAPABILITY_DESCRIPTION_AND) of the PRD. Do not include “must” statements in Sections 1.0 or 2.0. Do not write requirements in any portion of the PRD using the word ‘shall’. [FAA Order 1000.36](https://www.faa.gov/documentlibrary/media/order/branding_writing/order1000_36.pdf) requires use of the word ‘must’ even for internal, non-contractual documents.

In sections 3.0 to 9.0, provide as much detailed information as known during an investment’s acquisition lifecycle phase. As you continue through the AMS process, update sections 3.0 to 9.0 with more content through each PRD iteration.

**Product Alignment**

Maintain horizontal and vertical integration with other systems engineering products as described in the [FAA Systems Engineering Manual (SEM).](https://sep.faa.gov/policy_and_guidance/main) Horizontal integration identifies relationships between systems engineering products at the same level. Because requirements derive from the Functional Architecture, please maintain consistency between the functional analysis document and the program requirements document.

Vertical integration describes how data at a lower level is traceable and related to data at a higher level. In the case of requirements, this means that program-level requirements are traceable to and consistent with enterprise-level requirements. Please refer to Table 12 (contained in section 3.3.2.2 Control Requirements) in the SEM for an example of vertical traceability.

Guidance on requirements traceability is available in [Appendix 4](#_APPENDIX_4._PROGRAM) of this template and in the SEM. When citing FAA Orders, handbooks, and standards in Program Requirements Documents, use the latest version. Refer to the [Table of Acquisition Categories and Tailoring](https://fast.faa.gov/docs/acqcattable.doc) in the AMS to determine if a requirements document is necessary.

**Mission Support**

For Mission Support investments that are IT hardware/software dependent, check for the latest Mandatory Design Standards with the Enterprise & Portfolio Insight Division (ADE‐200). Mission Support investments that are operations funded must contact the [Operations Governance Board (OGB)](http://fast.faa.gov/NNOFCA_Operations_Governance_Board.cfm).

**Special Consideration for Enterprise Information**

Within the federal government, there are numerous rules and regulations governing the development and execution of IT policy. These guidelines have been established to better manage strategic plans, enhance IT acquisition practices, justify IT expenditures, measure IT performance, report results to Congress, integrate new technologies, and manage information resources.

The following documents explain Enterprise Information Management:

* [The Clinger-Cohen Act](http://dodcio.defense.gov/Portals/0/Documents/ciodesrefvolone.pdf)
* [Executive Order 13011, Federal Information Technology](https://govinfo.library.unt.edu/npr/library/direct/orders/27aa.html)
* [Office of Management and Budget (OMB) Circular A-130](https://obamawhitehouse.archives.gov/sites/default/files/omb/assets/OMB/circulars/a130/a130revised.pdf)
* [FAA Order 1370.121- FAA Information Security and Privacy Program & Policy](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1030708)

As stated in the [Future of the NAS (2016)](https://www.faa.gov/nextgen/media/futureOfTheNAS.pdf), the collection, integration, and dissemination of data and information through common standards and global interoperability is treated as an integral part of the modernization. To do this, the FAA must manage information in a manner that promotes discovery, access, and consumption by all authorized consumers.  The focus on information management will result in improved operations that avoid inefficient processes such as manual data input and duplicate data entries. Information management improvements will include improved data quality (e.g., accuracy, resolution and, integrity) that is monitored and controlled, the timely distribution of information, and digital exchange and processing mechanisms.

Investments must use enterprise data and information when available rather than develop their own data sources.

**Requirements for Enterprise Data and Information**

Incorporate enterprise data and information requirements into sections for requirements that:

* Support the business case of the program
* Are implemented by the program
* Are implemented by Enterprise Information Management Enterprise Capability (EIM EC) data teams

The need for enterprise data and information requirements varies based on the AMS phase of the program and the applicable PRD.

**Special Consideration for Multi-Segment Investments**

To reduce risk, facilitate investment management, address complex objectives incrementally, and take advantage of any evolution in technology or service need not known or available during implementation of earlier increments or segments, consideration of modular contracting concepts is encouraged. FAA acquisition management policy (Sections 1.2.4.2 and 1.2.6) encourages the approval and implementation of large, complex investment initiatives as smaller sequential increments or segments.

Whenever investment objectives of a complex investment initiative are to be obtained through implementation of sequentially approved and implemented investment increments or segments, the requirements of each increment or segment must be consistent with the requirements of the overall solution within which each increment will operate, and should address the interface requirements associated with succeeding increments or segments.

If the program intends to implement solutions across multiple segments (i.e. Solution Segment 1, Solution Segment 2, etc.), a single PRD must be developed as a baseline for the complete solution investment. There are several benefits to this method. This will provide a consolidated view of program requirements without having to look at multiple requirements documents created for multiple segments. Program managers, systems engineers, and vendors will gain a full understanding of a program's capabilities across the multiple phases in one consolidated view. Additionally, this, will help establish traceability to other single integrated artifacts such as the FAD and architecture products, as the single PRD will contain the full set of capabilities envisioned for the program.

At the final investment decision for the first increment or segment, the Program Requirements Document defines end-state requirements for the overall initiative, as well as the subset of requirements that must be satisfied by the initial increment or segment. When subsequent increments or segments come to the investment decision authority for approval to proceed with implementation, the Program Requirements Document is updated to identify and specify those requirements that will be satisfied by the increment or segment seeking approval.

For multi-segment investments, specify each segment requirement in the PRD as follows:

* *Requirement Number- Requirement text (Segment number)*

Example: 3.1.4.1The program must provide [PR-INS-027] Aeronautical Information to authorized users. (Segment 3)

**Special Consideration for System of Systems**

In a System of Systems (SoS) enterprise environment, system requirements are allocated to another program/system. In this case, it can be necessary to allocate requirements across multiple investments.

Given the complexity and interconnectivity of the SoS within FAA, a program’s success may rely on certain new or modified functionalities being provided by other programs/systems. When developing and managing requirements for an individual system, consider how requirements at the SoS level are affected, including the system of interest along with all interfacing systems. More information on requirements analysis, management, and development within a system of systems can be found in the SEM.

**Requirements for Systems of Systems (NAS Programs)**

Requirements management within a SoS takes on new responsibilities. Previously, the Program Requirements Document (PRD) was used for managing the programmatic, functional, and performance requirements. In the SoS environment, the PRD is now responsible for managing all the requirements that meet the Operational Event/Trace Description (OV-6) of the programs business case defined by the portfolio.

To incorporate this new use, the PRD template has been updated to include sections for requirements that are allocated to/from the program. Most implemented program requirements are allocated by the Enterprise to support the business case of the portfolio. There are instances a program will agree to accept requirements allocated from another system or may need another system to implement some of their requirements. The need for these enterprise requirements varies based on the AMS phase of the program and the applicable PRD.

For the pPRD, Requirements Allocated by the Enterprise need to be considered and included in the applicable sections within the Program Requirements Document template (3.1, 4.2.1, 5.4.2). Requirements allocated to another program or accepted from another program should be included in section 3.1 with footnotes to document the allocated requirements.

For the iPRD, any additional set of identified Requirements Allocated by the Enterprise need to be added to the applicable sections within the requirements template (3.1, 4.2.1, 5.4.2). Although it is unlikely for new requirements to be allocated to another program or accepted from other programs in Initial Investment Analysis (IIA), follow the same process in the pPRD of documenting these requirements.

For the fPRD, all identified Requirements, including any Requirements Allocated by the Enterprise that are applicable to the selected solution will be included in the applicable sections within the Program Requirements Document template (3.1, 4.2.1, 5.4.2).

**Allocated Requirements**

Allocated requirements come from three sources:

* Allocated by the Enterprise
* Allocated from this investment to another program/system (usually in the same portfolio)
* Allocated from another program/system to this investment

For example, requirements allocated by the Enterprise may consist of a common set of display requirements or system administration requirements. Likewise, if a needed capability is not implemented on another program due to lack of maturity or availability, either the Enterprise or that another program may allocate the associated set of requirements to this investment to ensure meeting operational improvement implementation dates. Also, this investment may need another program to run common portfolio software, which requires allocation of the associated requirements. If the allocation of requirements related specifically to new data, these requirements will be included in section 3.2.

**FAA**

**[AXX-####. Office of]**![Description: m](data:image/png;base64...)

[Preliminary/Initial/Final] Program Requirements

For [Program Name]

****Signature Page****

**<PRELIMINARY/INITIAL/FINAL>**

**PROGRAM REQUIREMENTS**

for

[Enter name of investment program]

Version *(#)*

*![Microsoft Office Signature Line...](data:image/x-emf;base64...)*

Approved by Director or Vice President, Service Organization with the mission need *![Microsoft Office Signature Line...](data:image/x-emf;base64...)*

Approved by Director or Vice President, Operating Service Organization(s)

Note: One Service Organization may have both responsibilities *![Microsoft Office Signature Line...](data:image/x-emf;base64...)*

Concurrence by Director, NAS Systems Engineering & Integration Office, ANG-B or Solution Delivery Services, ADE-001

☐ DOORS Module Exists (NAS Investments) *![Microsoft Office Signature Line...](data:image/x-emf;base64...)* Submitted by Appropriate official of the preparing organization

**Table of Contents**

[1 INTRODUCTION 11](#_Toc78274334)

[1.1 Description 11](#_Toc78274335)

[1.2 Scope 12](#_Toc78274336)

[2 CAPABILITY DESCRIPTION AND PROGRAM INFORMATION 12](#_Toc78274337)

[2.1 Operational Concept 12](#_Toc78274338)

[2.2 Quantities and Location 12](#_Toc78274339)

2.3 Constraints 13

2.4 Use of Multiple Segments…………………………………………………………….………………………………………… ……………………..…….13

[3 FUNCTIONAL, INFORMATION AND PERFORMANCE REQUIREMENTS 14](#_Toc78274341)

[3.1 Functional Requirements 14](#_Toc78274342)

[3.2 Data and Information Requirements 15](#_Toc78274343)

[3.3 Performance Requirements 15](#_Toc78274344)

[3.4 Reliability, Maintainability, and Availability (RMA) and Resiliency Requirements 15](#_Toc78274345)

[4 INTEGRATION REQUIREMENTS 17](#_Toc78274346)

[4.1 Physical Integration 17](#_Toc78274347)

[4.1.1 Environmental Requirements 17](#_Toc78274348)

[4.1.2 Land and Facility 17](#_Toc78274349)

[4.1.3 Telecommunications 19](#_Toc78274350)

[4.1.4 Special Considerations 19](#_Toc78274351)

[4.2 Functional Integration 20](#_Toc78274352)

[4.2.1 Interfaces to Other FAA Enterprise Architecture Elements 20](#_Toc78274353)

[4.2.2 Interfaces 20](#_Toc78274354)

[4.2.3 Spectrum Requirements 21](#_Toc78274355)

[4.3 Human Factors 22](#_Toc78274356)

[4.4 Employee Safety and Health 24](#_Toc78274357)

[5 SECURITY AND SAFETY REQUIREMENTS 25](#_Toc78274358)

[5.1 Facility Security 25](#_Toc78274359)

[5.2 Personnel Security 25](#_Toc78274360)

[5.3 Information Systems Security (ISS) 25](#_Toc78274361)

[5.4 System Safety 27](#_Toc78274362)

[5.4.1 Existing Controls 28](#_Toc78274363)

[5.4.2 Safety Requirements 28](#_Toc78274364)

[6 QUALITY AND CONFIGURATION MANAGEMENT REQUIREMENTS 29](#_Toc78274365)

[6.1 Quality Assurance 29](#_Toc78274366)

[6.2 Configuration Management 29](#_Toc78274367)

[7 TEST AND EVALUATION REQUIREMENTS 31](#_Toc78274368)

[7.1 Planning and Test Design Requirements 31](#_Toc78274369)

[7.2 Development Test Requirements 31](#_Toc78274370)

[7.3 Operational Test Requirements 32](#_Toc78274371)

[**7.4** **Site Test Requirements** 32](#_Toc78274372)

[7.5 Reporting Requirements 32](#_Toc78274373)

[7.6 Test Support Requirements 32](#_Toc78274374)

[7.7 Critical Operational Issues 33](#_Toc78274375)

[8 IMPLEMENTATION AND TRANSITION REQUIREMENTS 35](#_Toc78274376)

[9 IN-SERVICE SUPPORT AND MANAGEMENT REQUIREMENTS 36](#_Toc78274377)

[9.1 Integrated Logistics Support 36](#_Toc78274378)

[9.2 Maintenance Planning 37](#_Toc78274379)

[9.2.1 Field Maintenance Support 37](#_Toc78274380)

[9.2.2 Second Level Engineering, Maintenance, and Technical Support 37](#_Toc78274381)

[9.2.3 Depot-Level Support 38](#_Toc78274382)

[9.3 Supply Support 38](#_Toc78274383)

[9.3.1 Site Sparing 38](#_Toc78274384)

[9.3.2 Life Cycle Provisioning/Depot Spares 38](#_Toc78274385)

[9.3.3 Screening 38](#_Toc78274386)

[9.3.4 Warranty 38](#_Toc78274387)

[9.3.5 Asset Management 39](#_Toc78274388)

[9.4 Packaging, Handling, Storage, and Transportation 39](#_Toc78274389)

[9.4.1 Depot Spares 39](#_Toc78274390)

[9.4.2 Barcoding 39](#_Toc78274391)

[9.5 Support Equipment Maintenance 39](#_Toc78274392)

[9.5.1 Tools and Test Equipment 39](#_Toc78274393)

[9.6 Direct-Work Maintenance Staffing 39](#_Toc78274394)

[9.7 Maintenance Support Facilities 39](#_Toc78274395)

[9.8 Training, Training Support, and Personnel Skills 39](#_Toc78274396)

[9.8.1 FAA Academy Training System 40](#_Toc78274397)

[9.9 Technical Data 40](#_Toc78274398)

[9.9.1 Manuals and Instructions 40](#_Toc78274399)

[9.9.2 Drawing and Specifications 40](#_Toc78274400)

[9.9.3 Escrow Package 40](#_Toc78274401)

[9.9.4 Computer Resources Support 40](#_Toc78274402)

[10 APPENDIX 1. CRITICAL PERFORMANCE REQUIREMENTS 41](#_Toc78274403)

[APPENDIX 2. ACRONYMS AND GLOSSARY TERMS 45](#_Toc78274404)

[Acronyms 45](#_Toc78274405)

[Glossary 48](#_Toc78274406)

[APPENDIX 3. REFERENCE DOCUMENTS 60](#_Toc78274407)

[APPENDIX 4. PROGRAM REQUIREMENTS TRACEABILITY AND VERIFICATION 65](#_Toc78274408)

# INTRODUCTION

The introduction including section 1.1 and 1.2 should be no longer than one page.

## Description

Identify the shortfalls addressed by this Program Requirements Document and summarize the service or capability needs. This section is ONLY a synopsis of the shortfalls described in section one of the Shortfall Analysis Report (SAR). Briefly describe how the requested improvements provide enhanced capabilities or services to the Federal Aviation Administration’s (FAA) current capability (if any). For facility initiatives, describe the shortfalls addressed in section one of the SAR and discuss how the proposed facility modernization/replacement efforts improve current facility condition/capabilities.

Specify the EA Roadmap that contains the program.

## Scope

Describe the scope of the requested improvement to a service, facility, or capability. Identify whether the improvement is new to the FAA or whether it is to replace an existing capability. This section is ONLY a synopsis of the scope described in section one of the ConOps. If the improvement requires a revision to an approved final Program Requirements document (fPRD), from an earlier phase or segment of the investment, briefly summarize any substantive changes since the last approval, and explain why the changes are required.

# CAPABILITY DESCRIPTION AND PROGRAM INFORMATION

## Operational Concept

There is a description of the operational concept details in a ConOps document, (completed prior to developing a PRD). This section is ONLY a synopsis of the concepts described in section 4.2 of the ConOps. Provide a link to that approved ConOps when possible.

Provide a brief, high-level discussion of the new capability as well as what the investment will bring to the FAA. Explain how the capability will be used in the operational environment, who the users are, and how they will be affected. For NAS investments, include EA artifacts such as a high-level operational concept diagram (OV-1), systems/services communications description (SV-2) or interface diagrams to illustrate the concept. For Mission Support investments please refer to the [EA Program Manager Guidance](https://my.faa.gov/content/dam/myfaa/org/staffoffices/afn/information/processes/ade/AIT-ASP-004-W2-Non-NAS-EA-PM-Guidance.pdf) document for useful diagram types.

## Quantities and Location

Provide as much location information as possible (e.g., the number of initial units per region, evolving to specific locations during Business Case Analysis). In the iPRD, include as much information as possible to aid the initial investment analysis. In the fPRD, identify the total number of units, sites or scope of services essential enough to meet the mission need.

## Constraints

Identify the projected date by which products or services will achieve initial and full operational capability at the first site. Also, state the trigger or parameter for initial and full operational capability. Identify the projected date all sites will achieve operational capability; that is Operational Readiness Date (ORD). If an interim demonstration or system mock-up is required, discuss the strategy and planned date for finalizing critical design or production decision. Identify schedule constraints associated with any predecessor and successor interfacing or interdependent EA elements required to achieve full operational capability. Identify constraints in the pPRD as much as possible and fully identified in the fPRD. Schedule constraints must conform to information in the EA roadmaps.

Identify any constraints or assumptions that bound the potential solution or limit the scope of the alternatives to achieve operational capability at all sites. Constraints and assumptions can include predefined hardware/software use, information availability and connectivity, dependence on other technologies, database management, facilities, staffing, training, compatibility with legacy systems, etc. Describe the constraints or limitations associated with predecessor or successor interfacing systems, inter-dependent EA elements, or other resource considerations that may affect the alternative solutions. This section is ONLY a synopsis of the constraints or assumptions described in the ConOps section 4.1.

Document constraints and assumptions in the Program Management Plan in order to assess the extent to which these constraints and assumptions raise the Program's exposure to risk (issues or opportunities).

2.4 **Use of Multiple Segments**

Given the FAA encouragement of the implementation of large, complex investment initiatives as smaller sequential increments or segments, describe the viability of meeting the programs’ operational need described in Section 2.1 Operational Concepts utilizing a multi-segmented approach. (See AMS Policy Appendix C for useful segment definition)

**2.4.1.** If a multi-segmented approach is a viable option, provide a detailed description of the segmented approach the investment is taking. Include which capabilities from the operational CONOPS each segment is enabling, the interface requirements associated with succeeding increments or segments and the timeframe for each segment that is planned to be delivered. Also provide a description of how this document will represent and manage those requirements across the lifecycle of the system.

# FUNCTIONAL, INFORMATION AND PERFORMANCE REQUIREMENTS

Refer to the following for guidance on writing requirements:

* [FAA SEM](https://sep.faa.gov/policy_and_guidance/main)
* INCOSE Systems Engineering Handbook Fourth Edition, 2015
* ISO/IEC/IEEE 15288-2015

## Functional Requirements

Functional Requirements are functions that the intended solution must perform to satisfy a mission need or a shortfall. The source of these functional requirements is the FAD. These functions correspond to the “To-Be” business process activities/tasks, the data inputs, and information products or services output. A functional requirement uses the same elements, e.g., required inputs, internal process, and outputs/interfaces to other functions, systems, and users. The attributes of functional requirements include:

1. Derives from functions in the FAD
2. Traces to functions in the FAD
3. Traces to organization strategic goals
4. Traces to enterprise-level services/capabilities
5. These requirements trace to an interface requirement document (IRD), SSD or web service description document (WSDD)

For Concept and Requirements Definition (CRD), the FAD will contain the “As-Is” and “To-Be” business process functions, as well as the system functions from the top-level ‘Provide System Functions’ plus three full levels of decomposition. Therefore, the pPRD, which primarily contains functional requirements, will contain functional requirements for all three full levels of functions in the FAD. Initial Investment Analysis, the FAD will contain two to three additional levels of functions (e.g., to the level necessary for the specification), so the iPRD will contain the additional functional requirements directly traceable to the new functions. In Final Investment Analysis, the fPRD will contain functional requirements for all functions developed in the FAD.

Functional requirements describe “what” the solution must do to satisfy business/enterprise goals and objectives, not “how” it will accomplish them. The “what” includes information exchanged via interfaces with other systems and people.

If the investment program provides no new functionality, indicate that this section does not apply. If the investment program receives an Acquisition Category (ACAT) approval as a Tech Refresh or Non-Material, the functional requirements section does not apply. If the investment program is non-functional in nature, indicate that this section does not apply. If the investment program intends to procure additional quantities of existing FAA equipment or additional quantities of services (i.e. Variable Quantity ACAT type), include the equipment or service acquired in the functional requirements section. It may be necessary to revalidate the existing requirements.

## Data and Information Requirements

This section identifies requirements for new or modified data and information that are external to the solution being described in the PRD.

For pPRD, identify and describe all known data and information sources, elements, characteristics, and formats that the PRD solution will acquire from new or existing external sources. The requirements may be defined in the “To-Be” Business Process Model (BPM), the ConOps or the FAD.

The requirements in the iPRD and fPRD will expand on the new data and information sources, elements, characteristics, and formats described in the pPRD. Many sources are anticipated to be collected, stored and accessed from the FAA Enterprise Capability (EC) Unified Data Layer (UDL), as most NAS and Mission Support data and information will be maintained within the UDL.

## Performance Requirements

Performance requirements quantitatively or qualitatively assert how well the functional requirement needs to perform. As a result, performance requirements trace directly to their parent requirement from section 3.1. Performance requirements may originate from program level needs or from enterprise level capabilities. Performance requirements do the following:

* Define how well the intended system performs, e.g., accuracy, fidelity, operational range, resolution, and response time
* Map to sub-functions

Identify Critical Performance Requirements (CPRs) where and when they first appear and list all CPRs including their requirement value type (Quantitative/Qualitative) in [Appendix 1](#_APPENDIX_1._CRITICAL). Appendix 1 provides guidance on criteria for selecting CPRs.

## Reliability, Maintainability, and Availability (RMA) and Resiliency Requirements

RMA requirements identify inherent availability, Mean-Time-To-Restore (MTTR), and other measures of performance and reliability.

It is important to specify that only high-level RMA values in the preliminary Program Requirements Document (pPRD). Specific RMA values derive from these high-level values as the program develops the iPRD and fPRD. Refer to the [FAA RMA Handbook (RMA-HDBK-006C](http://www.tc.faa.gov/its/worldpac/standards/faa-hdbk-006c.pdf) and its [attachment](http://www.tc.faa.gov/its/worldpac/standards/faa-hdbk-006c-1.pdf)) for guidance, especially concerning the requirements resulting from the desired level of system criticality.

Resiliency supplements a system’s RMA. Key principles for building resiliency into the NAS include redundancy, diversity, response time, and recovery.

Those services classified as safety critical or would have an impact to safety critical services (as defined in RMA- HDBK-006) need to address high-level resiliency requirements in the pPRD. This would include requirements that enhance a NAS system’s overall ability to avoid and mitigate, limit the effect of and recover from system failure scenarios and/or degraded facility conditions, and to systematically attain an acceptable level of service. Further requirements are developed in the iPRD and fPRD.

Refer to Order 6000.36 National Airspace System Service Survivability for additional guidance on Resiliency.

# INTEGRATION REQUIREMENTS

## Physical Integration

Identify physical integration requirements associated with implementing the solution/system in the FAA environment or facility. For Mission Support investments that are IT centric, work with the Data Center Infrastructure & Operations Service, Performance & Planning Group when defining your physical space and integration requirements.

FAA specification [FAA-G-2100H, Electrical Equipment, General Requirements](https://ksn2.faa.gov/nextgen/SysEng/NASEAandRqmts/ISE/SiteAssets/Attachment_6_FAA-G-2100H.pdf) is applicable to many physical integration requirements. Reference the applicable sections of the specification.

### Environmental Requirements

Define requirements for evaluating the environmental impacts of the construction and operation of the new capability in accordance with the National Environmental Policy Act (NEPA). If the deployment of the new capability requires real property transactions, e.g., land or lease acquisition, define requirements for conducting environmental due diligence audits in accordance with [FAA Order 1050.19B - Environmental Due Diligence Audits in the Conduct of FAA Real Property Transactions](http://www.faa.gov/documentLibrary/media/Order/ND/1050.19B.pdf).

The following FAA Orders, specifications and standards may also be applicable to this section:

* [FAA Order 1050.1F, Environmental Impacts: Policies and Procedures](http://www.faa.gov/documentLibrary/media/Order/FAA_Order_1050_1F.pdf)
* [29 CFR 1910, Subpart J, General Environmental Controls](https://www.osha.gov/pls/oshaweb/owasrch.search_form?p_doc_type=STANDARDS&p_toc_level=1&p_keyvalue=1910)

For Mission Support investments, an example of environmental needs you may need to plan for is cooling for large-scale IT installations.

### Land and Facility

If known, include any requirements for land and facilities in the pPRD and iPRD. In the fPRD, identify requirements for real estate, facility space to accommodate systems, auxiliary equipment, resiliency related infrastructure and personnel for end-state operations and during transition to the new capability.

#### Grounding, Bonding, Shielding, Lightning Protection, Cables, Power and HVAC

Define grounding, bonding and shielding, lightning protection, cable and power and Heating Ventilation Air Conditioning (HVAC) requirements during transition to the new capability and for end-state operations. Power includes requirements for essential and/or critical buses, and back-up power sources such as engine generators, uninterruptable power supply (UPS) and batteries.

The following FAA Orders, specifications and standards may be applicable to this section:

* [FAA-STD-019E - Lightning and Surge Protection, Grounding, Bonding and Shielding Requirements for Facilities and Equipment](http://everyspec.com/FAA/FAA-STD/download.php?spec=FAA_STD_019e.2259.pdf)
* [FAA-G-2100H, Electrical Equipment, General Requirements](https://ksn2.faa.gov/nextgen/SysEng/NASEAandRqmts/ISE/SiteAssets/Attachment_6_FAA-G-2100H.pdf)
* [FAA Order 6030.20F- Electrical Power Policy](http://www.faa.gov/documentLibrary/media/Order/6030_20_F%20with%20CHG%201%20incorporated.pdf)
* [FAA Order 6950.2D - Electrical Power Policy Implementation at National Airspace System Facilities](http://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/9882)
* [American National Standards Institute/Institute of Electrical and Electronics Engineers (ANSI/IEEE) Standard 1100-2005, Recommended Practice for Powering and Grounding Electrical Equipment](https://standards.ieee.org/findstds/standard/1100-2005.html)
* [FAA Order 1370.121- FAA Information Security and Privacy Program & Policy, Appendix 2, Paragraph 17.3., and Appendix 12](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1030708)

#### Energy and Water Conservation

Define requirements to achieve compliance with energy and water conservation mandates of the following policy documents:

* [National Energy Conservation Policy Act](https://www1.eere.energy.gov/femp/pdfs/necpa_amended.pdf)
* [The Energy Policy Act of 2005 (EPACT)](http://www.gpo.gov/fdsys/pkg/PLAW-109publ58/pdf/PLAW-109publ58.pdf)
* [The Energy Independence and Security Act of 2007 (EISA)](http://www.gpo.gov/fdsys/pkg/BILLS-110hr6enr/pdf/BILLS-110hr6enr.pdf)
* [Executive Order 13693](https://www.gpo.gov/fdsys/pkg/FR-2015-03-25/pdf/2015-07016.pdf)
* [FAA Order 1053.1B, Energy and Water Management Program for FAA Buildings and Facilities](http://www.faa.gov/documentLibrary/media/Order/1053.1B.pdf)

This section includes consideration of energy and water-use efficiency, use of off-grid power and non-polluting energy sources, and energy consumption from operation of the product.

#### Hazardous Materials

Define the requirements for handling, removal, cleanup, and recycling hazardous materials for transition to the new capability, e.g., installation, and for end-state operations. Be sure to consider disposal of replaced assets that contain silicon or other hazardous material.

The following standards, regulations, and FAA Orders may apply to this section:

* [OSHA Standard 1910.120 subpart H - Hazardous Waste Operations and Emergency Response](https://www.osha.gov/pls/oshaweb/owadisp.show_document?p_table=STANDARDS&p_id=9765)
* [EPA Regulation 40 CFR Part 260 - Hazardous Waste Management System: General](http://www.ecfr.gov/cgi-bin/text-idx?SID=ce1c367b165ba9c97020a904000ccefd&mc=true&node=pt40.28.260&rgn=div5)
* [FAA Order 1050.10D, Prevention, Control, and Abatement of FAA Environmental Pollution](https://employees.faa.gov/tools_resources/orders_notices/index.cfm/go/document.information/documentID/1028586)
* [FAA Order 1050.14B- Polychlorinated Biphenyls (PCBs) in the National Airspace System](http://www.faa.gov/documentLibrary/media/Order/order%201050.14B.pdf)
* [FAA Order 1050.18 - Chlorofluorocarbons and Halon Use at FAA Facilities](http://www.faa.gov/documentLibrary/media/order/energy_orders/1050.18.pdf)
* [FAA Order 1050.20A - Airway Facilities Asbestos Control Program](http://www.faa.gov/documentLibrary/media/Order/1050.20A.pdf)
* [FAA Order 4600.27B - Personal Property Management](http://www.faa.gov/documentLibrary/media/Order/4600.27B.pdf)

### Telecommunications

Define telecommunications requirements for transition to the new capability and end-state operations.

Mission Support investments will always need to consider telecommunications. Where does the information need to go? How do you transfer the information? What FAA data transfer system will be used (i.e., Federal Telecommunications Infrastructure (FTI), System Wide Information Management (SWIM))? What protocols will be required for use? How will resiliency be incorporated? The following FAA Orders and standards may be applicable to this section:

* [FAA Order 1830.10 - Managing New Telecommunications Requirements](http://www.faa.gov/documentLibrary/media/Order/1830.10.pdf)
* [FAA-STD-049 - Fiber Optic Telecommunication System and Equipment](http://www.tc.faa.gov/its/worldpac/standards/faa-std-049.pdf)
* [FAA Order 1370.121- FAA Information Security and Privacy Program & Policy](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1030708)

### Special Considerations

Define unique requirements related to fiber optics, water and sewer, roadway, seismic safety, and access during transition to the new capability and for end-state operations.

## Functional Integration

Define functional integration requirements associated with implementing the new capability in the operational environment, including portfolio allocation requirements. Functional Integration Requirements describe interfaces to other FAA Enterprise Architecture Elements, External Interfaces and Spectrum requirements.

For facility investments, define functional integration requirements associated with implementing the new facility initiative. Describe how the facility initiative will influence legacy FAA systems**.**

Early IRD development ensures that the affected systems agree to the interface requirements. IRD development starts in the early phase of an acquisition and a draft for each interface completed by Initial Investment Decision (IID) for the preferred alternative. The IRD author for each interface is responsible for coordinating with all stakeholders including the Configuration Management and Information Data Services (AJW-261), NAS Systems Engineering and Integration Office (ANG-B) for NAS programs, and/or with the FAA Enterprise Architect (ADE-200) for Mission Support Systems as a part of the approval process. The final IRD for each interface must be complete by Final Investment Decision (FID).

### Interfaces to Other FAA Enterprise Architecture Elements

Identify systems, subsystems, and networks or facilities that will interface with this capability and for which IRD and Interface Control Documents (ICD) are necessary. Include remote maintenance monitoring (referenced in JO 6040.15G) and operational command and control interface requirements as applicable.

Identify software interface requirements, specifications, protocols, and standards that ensure compatibility and interoperability with other fielded systems. The IRD identifies any unique user interface requirements, demonstration needs, and special software certification requirements.

The following FAA orders and standards may be applicable to this section:

* [FAA-STD-025F - Preparation of Interface Documentation](http://www.tc.faa.gov/its/worldpac/standards/faa-std-025f.pdf)
* [JO 6000.53D - Remote Maintenance Monitoring Interface Development and Implementation](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1029689)

For facility investments, discuss the systems, subsystems, and networks impacted by the facility initiative.

### Interfaces

Identify and define requirements for all interfaces between your system and any “user” to which your system interfaces. In this section, a user means an internal system for which a program has control over, an external system for which a user may not have control, facility, or service. The interfaces can take the form of an analog, discrete, general service, or web services type. An IRD in conformance with [FAA STD-025F](http://www.tc.faa.gov/its/worldpac/standards/faa-std-025f.pdf) must accompany each user interface.

### Spectrum Requirements

Define spectrum requirements including certification of radio spectrum availability. Mission Support program spectrum needs will typically be commercial spectrum versus NAS spectrum. Ensure the solution provider understands your program requirements. The following orders may be applicable to this section:

* [FAA Order 6050.32B - Spectrum Management Regulations and Procedures Manual](http://www.faa.gov/documentLibrary/media/Order/6050_32B_WITH_CHG_1_AND_2_INCORPORATED.pdf)
* [FAA Order 6050.19F - Radio Spectrum Planning](https://www.faa.gov/documentLibrary/media/Order/6050_19F.pdf)

## Human Factors

Identify human factors (HF) requirements for all users (e.g., operators, maintainers, trainers, and supervisors) of the product or service. In the pPRD and iPRD, include as much information as possible to aid the initial investment analysis. Human System Integration (HSI) helps to ensure that the system appropriately accommodates and leverages human capabilities and limitations. Common areas addressed by HF-related requirements include:

* Staffing and Selection
* Training and Job Development
* Tasks and Procedures
* Equipment and Facilities

The applicability of these areas and other HF considerations depend on a number of factors, such as the AMS phase, and the novelty and complexity of the product or service. Include consideration of human integration broadly, such as across facilities, job tasks, and teams.

The FAA has HF specialist resources in various organizations that cover primarily [Aviation Safety and Air Traffic](http://www.hf.faa.gov). AMS HF support is typically available to some degree from the Office of NextGen Human Factors Division for initial coordination, or the ATO Program Management Organization Human Factors branch for direct program support.

The following FAA Orders, standards and guidance may be applicable to this section:

* [HF Design Standard](http://hf.tc.faa.gov/hfds)
* [HF Job Aid](http://www.hf.faa.gov/workbenchtools/Tools/HFAcqJobAid2012.pdf)
* [HF Order](http://www.faa.gov/documentLibrary/media/Order/9550.8.pdf)

**HF Requirements for IARD**

A key consideration in the early AMS phases (Service Analysis and Strategic Planning and CRD) prior to IARD is the allocation of functions between humans and systems—for example, an automated tool to replace a function that previously performed manually. At these early stages of the AMS lifecycle, the Shortfall Analysis and ConOps are not solution-specific, and therefore may only drive requirements at the human-system or operational level, versus their human and system component levels. The intent is generally to avoid over constraining the solution space, but the result for HF is boilerplate high-level human-system requirements, whose primary value is to lower-level requirements in later AMS phases.

In order to complement boilerplate high-level human-system requirements, it may be appropriate to consider the following:

* Derive HF requirements from the Preliminary Shortfall Analysis, ConOps, and available program-specific information. This is particularly important when the service need is human-centered.
* Define conditional boilerplate requirements that get into human-system “architecture” solutions. For example, “IF a decision support tool is used, THEN the system must XYZ”. This allows requirements to address HF with meaningful detail, without going so far as to get into specific design solutions. This level of detail will foster consideration of alternatives that cover a breadth of basic human-system architectures, versus prematurely focusing on a narrower set of architectures with mainly a system focus. Because these requirements identified as conditional on future program decisions, they do not over constrain the solution space, and are acceptable at this stage.

**HF Requirements for IID**

As mentioned in the General Guidance section of this document, the iPRD contains requirements conforming to the preferred alternative, but is still not solution-specific, and supports IID. The iPRD includes new functions (if any), and lower-level requirements (as known). At this stage, the human-system function allocation is known based on the alternatives that have been defined. Therefore, the requirements can have the finer granularity to address known human and system components, while still satisfying the higher-level requirements specified in the pPRD. Ensure the level of detail is appropriate for a comparative analysis of the alternatives, from a HF perspective.

**HF Requirements for FID**

Include additional requirements as more information becomes available on the selected solution at IID to support the FID. The fPRD is the foundation for the product specification that ultimately addresses Computer-Human Interface (CHI) formats (colors, graphics, text, menus, etc.). Such CHI detail is what many think of when they consider HF, but are in fact a fraction of overall HF considerations, and derive from previous requirements from the pPRD and iPRD. The primary intent during FID is to define HF requirements in sufficient detail to analyze the preferred alternative that address HF risks and mitigations, and that support estimates of HF costs/activities needed to incorporate HF during Solution Implementation by a vendor.

## Employee Safety and Health

Define requirements related to compliance with federal regulations and mandates, FAA Orders, and national consensus standards as they apply to the physical architecture of the program. These requirements ensure the physical architecture is safe for FAA personnel to install, maintain and operate. Where applicable, consider the following topics:

* electrical safety
* fire life safety
* indoor air quality
* material handling
* personal protective equipment
* lockout/ tag out

The following FAA Orders, standards and guidance may be applicable to this section:

* [FAA Order 3900.19B - FAA Occupational Safety and Health Program](http://www.faa.gov/documentLibrary/media/Order/3900.19B.pdf)
* [FAA-G-2100H, Electrical Equipment, General Requirements](https://ksn2.faa.gov/nextgen/SysEng/NASEAandRqmts/ISE/SiteAssets/Attachment_6_FAA-G-2100H.pdf)

[29 CFR 1910.303, Electrical](https://www.osha.gov/pls/oshaweb/owadisp.show_document?p_table=standards&p_id=9880)

* [NFPA 13, Standard for the Installation of Sprinkler Systems](http://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards?mode=code&code=13)
* [NFPA 70, National Electrical Code](http://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards?mode=code&code=70)
* [NFPA 101, Life Safety Code](http://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards?mode=code&code=101)
* [29 CFR 1910.95, Occupational Noise Exposure](https://www.law.cornell.edu/cfr/text/29/1910.95)
* [29 CFR 1910.145, Specifications for Accident Prevention Signs](https://www.law.cornell.edu/cfr/text/29/1910.145)
* [29 CFR 1910.1001, Asbestos](https://www.law.cornell.edu/cfr/text/29/1910.1001)
* [29 CFR 1910, Subpart E, Means of Egress](https://www.osha.gov/pls/oshaweb/owadisp.show_document?p_id=10113&p_table=standards)
* [29 CFR 1910, Subpart I, Personal Protective Equipment](https://www.law.cornell.edu/cfr/text/29/part-1910/subpart-I)
* [29 CFR 1910, Subpart L, Fire Protection](https://www.law.cornell.edu/cfr/text/29/part-1910/subpart-L)
* [ANSI Z535.4, Product Safety Signs and Labels](http://www.safetysign.com/help/h39/safety-labels)
* [29 CFR Part 1960, Basic Program Elements for Federal Employees Occupational Safety and Health Programs and Related Matters](https://www.law.cornell.edu/cfr/text/29/part-1960)

# SECURITY AND SAFETY REQUIREMENTS

## Facility Security

Identify facility internal and external security requirements. List applicable standards and orders, (e.g., [FAA Order 1600.6E - Facility Security Policy](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/13920), [FAA Order 1600.69C, FAA Facility Security Management Program](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1029860)) along with the local security policy in the pPRD. Include requirements that are more specific as soon as there is more knowledge acquired in the iPRD and fPRD.

## Personnel Security

Identify personnel security requirements. List applicable standards and FAA Orders, (e.g., [FAA Order 1600.1E - Personnel Security Program](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/14801) and [FAA Order 1600.72A, Contractor & Industrial Security Program) in the pPRD.](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/15573)

## Information Systems Security (ISS)

Identify ISS requirements following guidance and templates in the Information Security Guidance for System Acquisitions (ISGSA) as required by FAA acquisition management policy ([AMS Section 4.11](http://fast.faa.gov/docs/acquisitionManagementPolicy/AcquisitionManagementPolicy4.11.pdf)). The [ISGSA guidance and templates](http://fast.faa.gov/EMP_Information_Security.cfm) assist investment initiatives sponsors in complying with [FAA Order 1370.121 – FAA Information Security and Privacy Program & Policy](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1030708) and its underlying government requirements. The table below summarizes the assessment names, their main objectives, the AMS planning phases when they are prepared and the AMS decisions required.

| **ISS Assessment** | **AMS Planning Phase / AMS Decision / Decision Entity** | **Assessment Main Objectives** |
| --- | --- | --- |
| **ISS Risk Factors Assessment** | Service Analysis (SA)  CRD Readiness Decision (CRDRD)  FAA Enterprise Architecture Board (FEAB) | -Determine a provisional investment initiative, security category, i.e., a provisional ranking of the damage that would result if the confidentiality, integrity, or availability of the information capability were lost.  -Characterize the security threat profile, the unauthorized persons or entities with the motivation, means, and opportunity to access and misuse the capability.  -Provide input to the cloud suitability assessment and solution concept of operations. |
| **Preliminary ISS Assessment** | Concept and Requirements Definition (CRD)  Investment Analysis Readiness Decision (IARD)  Joint Resources Council (JRC) | -Determine the final investment initiative, security category, which in turn determines the security requirements baseline from the [<u>National Institute of Standards and Technology Special Publication (NIST SP) 800-53</u>](http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf).  -Provide the security component for the preliminary Program Requirements Document (pPRD) based on an initial tailoring of the NIST SP 800-53 security requirements baseline and attendant risk assessments.  -Provide the factors for a rough ISS cost estimate of alternative solutions and factors for a rough estimate of the annual operational benefits gained by implementing security requirements.  -Provide input to the determination of the investment initiative Acquisition Category (ACAT). |
| **Initial ISS Assessment** | Initial Investment Analysis  Initial Investment Decision (IID)  JRC | - Provide the security component of the initial PRD (iPRD) based on final tailoring of 800-53 controls (with attendant risk assessments) and sufficiently detailed to conduct a market capability survey via a Screening Information Request.  -Update the cost and benefit factors of the preliminary ISS assessment for input to the initial business case. |
| **Final ISS Assessment** | Final Investment Analysis  Final Investment Decision (FID)  JRC | -Finalize the security requirements based on response to market capability survey. |

As explained in Section 1.4 of the ISGSA, the ISGSA applies only to investment initiatives to bridge service or capability shortfalls that include an information service component. In some cases, you can omit or fold the ISS Risk Assessment into the second assessment if the service shortfall-information component is not evident during the Service Analysis planning phase. Section four of the ISGSA describes the stakeholders, assessment tasks, and process for conducting the ISGSA ISS assessments.

You can find information about the ISGSA and templates on the [FAA Information Security](http://fast.faa.gov/EMP_Information_Security.cfm) website.

It is of paramount importance for FAA systems that contain generate, gather, store, disseminate, or process sensitive flight and radar track data associated with the classified and sensitive unclassified US government missions conducted for the purposes of national defense, homeland security, intelligence and law enforcement, to include requirements that comply with [FAA Order 1200.22 (latest version), External Requests for National Airspace System (NAS) Data](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1019774) and the [FAA Order 1600.75 (latest version), Protecting Sensitive Unclassified Information (SUI)](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/14210). Sensitive Flight Data (SFD) is designated For Official Use Only (FOUO) information, which is a category of FAA SUI. SFD can only be shared with authorized entities who have both a valid ‘need to know’ the information in furtherance of a lawful government purpose, and also a duty to protect that same information. SFD must be protected at the Moderate Confidentiality level using controls identified in FAA Order 1370.121. To this end such systems may want to tailor the ATO NIST SP 800-53 requirements AC-21 and CA-03 to explicitly bar unauthorized sharing of such sensitive information. Programs can also refer to the PRD canned requirements when creating sensitive data requirements.

System Operations Security (AJR-2) manages the FAA Sensitive Flight Data (SFD) security program.  The Controlled Unclassified Information (CUI) program is in the process of replacing SUI throughout government.  Per CUI requirements in 32 CFR Part 2002, CUI must be protected at the Moderate Confidentiality level.

Other FAA orders and notices applicable to identifying ISS requirements are located in the [ISS section](https://employees.faa.gov/tools_resources/orders_notices/) of the FAA Orders link.

## System Safety

For NAS investments only, identify requirements for a safety program to ensure the acquired solution manages risk and safety during acquisition and its in-service lifecycle. The pPRD should include as minimum a listing of applicable standards and orders:

* [JO 1000.37 - Air Traffic Organization Safety Management System](http://www.faa.gov/documentLibrary/media/Order/ND/1000.37.pdf)
* [Safety Risk Management Guidance for System Acquisitions (SRMGSA)](https://www.faa.gov/air_traffic/publications/media/SRMGSA.pdf)
* [Safety Management System Manual](https://www.faa.gov/air_traffic/publications/media/ATO-SMS-Manual.pdf)

Include the specific safety requirements in the iPRD and fPRD as soon as possible once identified in the applicable safety assessments. All controls or requirements in this template that are outside of those listed in 5.4, 5.4.1, and 5.4.2 but that have a safety impact or effect must be identified. Identify them by marking the requirements with an asterisk so they may also be tracked by Enterprise Safety and Information Security Division (ANG-B3).

Identify safety requirements to ensure the selected solution manages for safety risk during the lifecycle management process. System Safety Management must be in accordance with [FAA Order 8000.369B, Safety Management System Guidance](http://www.faa.gov/documentLibrary/media/Order/FAA_Order_8000.369B.pdf) and [FAA Order 8040.4A, Safety Risk Management](http://www.faa.gov/documentLibrary/media/Order/8040.4A%20.pdf).

Conduct program safety assessments in accordance with the Safety Management System Manual and SRMGSA.

This section of the pPRD constitutes the safety plan required by the SRMGSA for the IARD. You must develop a Program Safety Plan (PSP) for the IARD and updated versions for IID and FID in accordance with the SRMGSA. This requirement for a PSP is based on the Safety Strategy Meeting (SSM) conducted with ATO’s Safety and Technical Training (AJI) Office and will include a list of any required safety risk management activities.

For Mission Support investments, contact ADE-210 for more guidance.

### Existing Controls

Beginning with the Operational Safety Assessment (OSA), list the existing controls/requirements identified in the current Safety Risk Management Document (SRMD) for the program under consideration. List the existing controls/requirements by Hazard Identification number as in the Existing Control column of the applicable hazard analysis, e.g., Operational Hazard Assessment, Preliminary Hazard Analysis and beyond, worksheet.

### Safety Requirements

Begin a list with the Operational Safety Assessment followed by other safety requirements recommended for having potential to mitigate the hazard in the program’s current SRMD. List the Safety Requirements by Hazard Identification number as they appear in the Safety Requirements column of the applicable hazard analysis, e.g., Operational Hazard Assessment, Preliminary Hazard Analysis and beyond, worksheet.

Include a requirement that all software will comply with the software integrity standard, RTCA DO-278A. As such, this will require a safety assessment to identify if any hazards have software causes. Once completed, the program office proposes an appropriate software development-assurance level in accordance with section 2.3 of the standard. That assurance level will determine if any/how much of the standard applies.

The NAS Configuration Management (ECM) Office reviews the fPRD and requirements identified above as part of the JRC Checklist process. Submit the approved fPRD to the ECM Office via the Enterprise Change Notice (ECN) Process.

# QUALITY AND CONFIGURATION MANAGEMENT REQUIREMENTS

## Quality Assurance

Identify requirements for a quality program for acquisition and in-service lifecycle. Quality management requirements become increasingly specific as a program progresses. In addition, configuration management plays a key role in quality assurance. Limit the pPRD requirements to following standards and orders for quality assurance as they apply:

* [JO 7210.633 – Air Traffic Quality Assurance (QA) Program](http://www.faa.gov/documentLibrary/media/Order/JO_7210_633.pdf)
* [FAA-STD-013D - Quality Control Program Requirements](http://www.tc.faa.gov/its/worldpac/standards/faa-std-013d.pdf)
* [FAA-STD-016A - Quality Control System Requirements](http://www.tc.faa.gov/its/worldpac/standards/faa-std-016a.pdf)

When developing the iPRD and fPRD, include requirements that are more specific as soon as there is more knowledge acquired.

## Configuration Management

The Configuration Management (CM) section of the pPRD requires the program to work with the ECM Office to validate and identify high level Configuration Management Requirements against the approved ConOps, during IARD. The Configuration Management requirements must comply with the following:

* [<u>FAA Order 1800.66, Configuration Management Policy</u>](http://www.faa.gov/documentLibrary/media/Order/1800.66.pdf)
* [<u>FAA STD 058, Facility Configuration Management</u>](http://www.tc.faa.gov/its/worldpac/standards/faa-std-058.pdf)
* [<u>FAA STD 021A, Configuration Management Contractor Requirements</u>](http://www.tc.faa.gov/its/worldpac/standards/faa-std-021a.pdf)

The ECM Office must review the pPRD as part of the JRC Checklist process. Submit the approved pPRD to the ECM Office via the Enterprise Change Notice (ECN) Process.

The CM Section of the iPRD requires the program office to develop and provide the FAA Configuration Management Plan and a project schedule for the development of the following:

* Product Baseline Index (PBLI)
* Facility Configuration Management Plan
* Contractor Configuration Management Plan

The ECM Office must review the iPRD as part of the JRC Checklist process. Submit the approved iPRD to the ECM Office via the Enterprise Change Notice (ECN) Process.

The CM Section of the fPRD requires the Product Sponsor to develop and provide the following:

* FAA Configuration Management Plan
* Product Baseline Index (PBLI)
* Facility Configuration Management Plan
* Contractor Configuration Management Plan

# TEST AND EVALUATION REQUIREMENTS

This section and subsections address test and evaluation requirements for NAS and Mission Support investments. Test and Evaluation must be performed to verify and validate the system or solution that satisfies functional and performance requirements, and is operationally suitable and effective. All versions of the PRD must include testing requirements for planning and design, development testing, operational testing, site testing, reporting, and test support as defined in the subsections below.

State that test and evaluation must be performed in accordance with applicable FAA test and evaluation policies, orders, standards, and test guidance documents. List applicable documents in this section. Below is a list of FAA standard test documentation:

* [AMS Policy Section 4.4 Test and Evaluation](http://fast.faa.gov/docs/acquisitionManagementPolicy/AcquisitionManagementPolicy4.4.pdf)
* [Test and Evaluation Process Guidelines](https://fast.faa.gov/docs/teguidelines.docx)
* [FAA William J Hughes Technical Center Test and Evaluation Handbook](https://fast.faa.gov/docs/tehandbook.pdf)
* [FAA AMS Lifecycle Verification and Validation Guidelines](http://fast.faa.gov/docs/vandvguidelines.doc)
* [FAA SEM](https://sep.faa.gov/policy_and_guidance/main)

## Planning and Test Design Requirements

Identify requirements for the planning and design of all Test and Evaluation (T&E) activities conducted during the investment’s lifecycle. Identify all test plans (including the Test and Evaluation Master Plan (TEMP) and individual test plans) conducted for each test. The means to test interoperability, functionality and capabilities between and with other potentially impacted SoS enterprise systems must be included in the test plans.

## Development Test Requirements

Identify the requirement for conducting Development Test (DT) to verify that all specified requirements in the PRD for a system or service are fully integrated and stable and has no adverse effect on the NAS or other FAA systems.

The DT progresses from verifying requirements at the lowest component level and moves incrementally to the fully integrated/ fielded system level. The basis of test for DT must be the System Specification that traces to the PRD via the VRTM.

## Operational Test Requirements

Define the requirement for conducting an Operational Test (OT):

* to encompass the T&E of a system’s or service’s operational requirements
* to validate that the new or modified system is operationally effective and suitable for use by the FAA
* to validate that the FAA infrastructure is ready to accept the system
* for NAS investments, ensure it has no adverse effect on the rest of the NAS
* for Mission Support investments, ensure that it has no adverse effect on other systems or services

The basis of test for OT is the PRD with explicit focus on the CPRs and Critical Operational Issues (COIs). Show traceability for all requirements via the VRTM.

* 1. **Site Test Requirements**

Define the requirements for the conduct of testing at field sites and/or multiple key sites. Testing at field sites shall be required, if necessary, to expand upon laboratory testing to provide an environment that thoroughly tests requirements that cannot be adequately tested in a laboratory/simulated environment. Additionally, key site testing shall be required prior to national deployment to uncover and correct site-specific issues.

* 1. **Reporting Requirements**

Identify the requirement for the development of test reports for all tests conducted during the lifecycle of a system or service. Test reports address test results, including tests conducted, status of applicable requirements, data collected, the Data Recording and Analysis process, and conclusions and recommendations drawn from the test data (including performance and operational readiness).

## Test Support Requirements

Define the requirements for necessary test tools and environments that thoroughly evaluate the system or service. Typical test support items include but are not limited to the following:

* System interfaces
* Telecommunication services
* Test tools
* Models
* Simulations
* Environments
* Laboratories
* Field Sites
  1. **Critical Operational Issues**

Identify and number all Critical Operational Issues (COIs) that must be addressed during Operational Test and Independent Operational Assessment (IOA), if designated, and resolved prior to the In-Service Decision. A COI is a critical element or operational objective examined during testing to determine the ability of the system, service, or capability to provide the intended benefit, address shortfalls, and support the operational mission. COIs are stated in the form of a question at a high level and usually cannot be answered directly from a single test or measurement. COIs support the evaluation of the operational effectiveness and suitability of the system, service, or capability. The list of COIs will normally consist of five to ten issues and should reflect only those that are truly “critical” in nature.

The following are some key characteristics of acceptable COIs:

1. Contains an interrogative word demanding a “yes” or “no” answer. Examples are “Does”, “Can” or “Is”.
2. Assess relevant required operational capabilities that address a shortfall or intended benefit
3. Focus on fundamental mission critical operational suitability and effectiveness capabilities of the system or services
4. Contains applicable operational conditions
5. <u>Does not</u> contain or address system or service characteristics, parameters, or thresholds

COIs typically relate to:

1. Operational effectiveness, which measures the degree to which a product accomplishes its mission when used by representative personnel in the expected operational environment.
2. Operational suitability, which measures the degree to which a product intended for field use satisfies its availability, interoperability, reliability, maintainability, safety, human factors, logistics supportability, documentation, personnel and training requirements.

Based on operational effectiveness and suitability, consider the following list of areas when generating the COIs:

1. High level operating capabilities provided by the system or service
2. Site Adaptation
3. Interfaces to other FAA systems/services
4. Reliability/Maintainability/Availability (RMA) requirements to support sustained/safe operations including resiliency requirements that support avoidance and mitigation, operational response and airspace recovery operations.
5. Transition from legacy systems to the new capability
6. Security
7. Safety
8. Stress/Load/Degraded Operations
9. Certification
10. Human factors and training
11. System of Systems (as appropriate)

# IMPLEMENTATION AND TRANSITION REQUIREMENTS

Implementation requirements typically encompass implementation planning, pre-installation checkout, site preparation, installation and checkout, site integration, system shakedown, dual operations, and the removal and disposal of replaced systems, equipment, land, facilities, and other items.

Define requirements related to transition from the current capability to the new capability to prevent service disruption.

All programs must use the [Corporate Work Plan (CWP)](https://my.faa.gov/org/staffoffices/afn/finance/training/cwp/cwp_welcome.html) system for all implementation and transition activities.

For services investments where there will be transitions from an existing services provider to a different services provider, implementation requirements may include training, setting up contacts, office automation, support systems, databases, and operational procedures.

The [In-Service Review (ISR) checklist](https://my.faa.gov/content/dam/myfaa/org/linebusiness/ato/safety/isd/documents/ISR-Checklist.doc) identifies implementation concerns. In the fPRD, define rulemaking requirements related to commissioning the new capability in the FAA.

For facility investments, define requirements related to transition from the current facility to the new facility so there is no disruption in services (if applicable).

# IN-SERVICE SUPPORT AND MANAGEMENT REQUIREMENTS

Define the activities during in-service management supporting the FAA mission of providing air traffic control and other services. This entails operating, maintaining, securing, and sustaining systems, products, services, and facilities in real time to provide the level of service required by users and customers. It also entails periodic monitoring and evaluation of fielded products and services, and feedback of performance data into service and investment analysis as the basis for revalidating the need to sustain deployed assets or taking other action to improve service delivery.

## Integrated Logistics Support

Implement a comprehensive Integrated Logistics Support Program in accordance with [FAA AMS, Section 4.3: Integrated Logistics Support (ILS)](http://fast.faa.gov/docs/acquisitionManagementPolicy/AcquisitionManagementPolicy4.3.pdf) to meet In-Service Support requirements.

Include in an investment’s requirements the appointment of a Service-team logistics manager (STLM) responsible for defining, documenting, obtaining, and managing integrated logistics support requirements in accordance with AMS 4.3.1: ILS Principles.

As investments develop requirements, consider each of the nine FAA Integrated Logistics Support Elements as defined in AMS 4.3.2 Standard Elements of Logistics Support:

* Maintenance Planning
* Supply Support
* Support Equipment
* Technical Data
* Direct Work Maintenance Staffing
* Maintenance Support Facilities
* Computer Resources Support
* Training
* Packaging Handling Storage and Transportation (PHS&T)

Capture these elements into an Integrated Logistics Support Plan (ILSP) detailing the implementation of the maintenance concept.

It is encouraged for investments to work with the Integrated Logistics Management Team (ILMT), in accordance with AMS section 4.3, throughout the lifecycle. Document integrated logistics support planning with the Implementation Strategy and Planning Document (ISPD). Address and close all ILS-related items in the ISR checklist.

## Maintenance Planning

Derive requirements by identifying all activities associated with monitoring, evaluating, and adjusting the tasks for achieving, maintaining, or restoring the operational capability of a system, equipment, or facility in accordance with [FAA Order 6000.30F National Airspace System Maintenance Policy](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1020968).

Establish a maintenance concept in accordance with FAA Order 6000.30F identifying maintenance roles and responsibilities for field maintenance, engineering support, second level maintenance, and depot level maintenance.

Ensure Remote Maintenance Monitoring requirements are coordinated and identified with the Maintenance Automation Program (AJW-131) in accordance with [JO 6000.53D, Remote Maintenance Monitoring Interface Development and Implementation](https://employees.faa.gov/documentLibrary/media/Order/JO_6000_53D.pdf). Apply the Reliability Centered Maintenance (RCM) Process to capture appropriate maintenance strategy techniques.

### Field Maintenance Support

Conduct NAS field maintenance support in accordance with [FAA Order 6000.15H – General Maintenance Handbook for National Airspace System (NAS) Facilities](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1021786).

#### Service and System Certification Criteria

Certify services and systems meet the criteria specified in [FAA Order 6000.15H – General Maintenance Handbook for National Airspace System (NAS) Facilities](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1021786).

#### Remote Maintenance Monitoring

Specify software maintenance requirements for on-site and engineering support provided by FAA or contractor personnel. Define requirements for off-site or centralized software maintenance. Identify requirements for software maintenance development, diagnostics and data reduction, and analysis tools. Project system shall ensure that remote maintenance procedures are included in the training for technical operations personnel.

The pPRD, iPRD, and fPRD must contain the same maintenance philosophy unless it changes prior to fPRD. Include warranty requirements if applicable.

### Second Level Engineering, Maintenance, and Technical Support

Identify provided engineering support for NAS hardware and software in accordance with [FAA Order 1100.157A -- National Systems Engineering Divisions Maintenance Program Procedures, Operational Support (AOS)](http://www.faa.gov/documentLibrary/media/Order/ND/1100.157.pdf) and [FAA Order 6000.30F – National Airspace System Maintenance Policy](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1020968)

Identify Second Level Engineering (SLE) that provides support to Airway Transportation System Specialist (ATSS) with any of the following:

* troubleshooting calls
* future modifications or enhancements
* computer resource management
* software maintenance and development

Ensure that investments have contract provisions to cover the transition of engineering support from the contractor.

### Depot-Level Support

Consider the most cost-effective depot-level support concepts by evaluating the following:

1. FAA Logistics Center (FAALC) Repair
2. Contractor Depot Logistics Support (CDLS)
3. Interim Contract Depot Logistics Support (ICDLS)
4. Contractor Repair Service (CRS)

Conduct a business case analysis to determine the most cost effective depot-level support alternative. Reference the appropriate [Business Case Analysis (BCA) Template](https://fast.faa.gov/archive/v1011/docs/businesscasetemplate.doc) for more details.

Ensure contract options and funds are available to support depot maintenance requirements in the event the approved maintenance concept dictates Contractor Depot Logistics Support Investments adequately fund contract depot maintenance in accordance with [FAA Order 2500.8B](https://www.faa.gov/documentLibrary/media/directives/nd/ND2500-8B.pdf).

Account for the request of Transition to Operations and Maintenance (TOM) funding for depot-level contractor repair services after the first year program office funding expires in accordance with [FAA Order 2500.8B, Funding Criteria for OPS, F&E, and RE&D accounts](https://www.faa.gov/documentLibrary/media/directives/nd/ND2500-8B.pdf). Establish contract provisions to cover the transition of depot support from the contractor.

## Supply Support

Identify all activities associated with ordering, receiving, tracking, cataloging, and managing all items and supplies needed to sustain operational systems, facilities, and equipment in accordance with [FAA Order 4250.9B, Field Materiel Management and Control](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/8151) and GEIA-STD-007 Logistics Product Data (LPD).

### Site Sparing

Identify predetermined positions for initial site spares at designated servicing System Support Centers (SSC) and/or field locations in support of the operations and maintenance activities. An analysis of the number of systems, subsystems, or equipment implemented in support of Readiness-Based Sparing (RBS) concepts determines initial site spares servicing SSC / field locations.

### Life Cycle Provisioning/Depot Spares

Identify and conduct provisioning in accordance with [FAA Order 4250.9B, Field Materiel Management and Control](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/8151) and GEIA-STD-007 Logistics Product Data (LPD).

### Screening

Identify assigned National Stock Numbers (NSNs) to material in accordance with [FAA Order 4500.3D - Federal Catalog and Standardization Programs (FCSP)](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/8297).

### Warranty

Identify reporting and management of warranty items in accordance with [FAA Order 4650.20A - Reporting and Replacement of Items Falling under Warranty](http://www.faa.gov/documentLibrary/media/Order/4650.20A.pdf).

### Asset Management

Identify management of assets in accordance with [FAA Order 4140.1, Integrated Material Management Program](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/8142), and [FAA Order 4600.27C Personal Property Management](https://www.faa.gov/documentLibrary/media/Order/FAA_Order_4600.27C.pdf).

## Packaging, Handling, Storage, and Transportation

Identify all activities associated with packaging, handling, storage, and transportation in support of operational systems, equipment, and facilities in accordance with [ASTM-D-3951-18 Standard Practice for Commercial Packaging](http://www.dla.mil/Portals/104/Documents/LandAndMaritime/V/VS/Packaging/LM_HandoutFY2014rev6_151007.pdf), MIL-STD-2073-1, DOD Material Procedures for Development and Application of Packaging Requirements and [MIL-STD-129R Military Marking for Shipment and Storage](https://vsc.gsa.gov/administration/files/MIL-STD-129R.pdf).

### Depot Spares

Depot sparing should be planned for and provisioned to support the maintenance plan and intended solution lifecycle.

### Barcoding

Ensure that all equipment has a barcode in accordance with [FAA Asset Identification Specification dated January 29, 2013](https://faaco.faa.gov/index.cfm/announcement/view/12706).

## Support Equipment Maintenance

Identify all activities associated with replenishing, repairing, maintaining, and calibrating test, measurement, and support equipment.

### Tools and Test Equipment

Identify tools and test equipment provided to each NAS facility in accordance with [FAA Order 6200.4H – National Test Equipment Program Management](http://www.faa.gov/documentLibrary/media/Order/6200.4G.pdf) and GEIA-STD-007, Logistics Product Data (LDP).

## Direct-Work Maintenance Staffing

Identify all activities associated with providing FAA staffing for first-level touch labor, supervision, and support functions necessary to maintain NAS systems and equipment. (Note: Currently there is no FAA Order defining this activity).

## Maintenance Support Facilities

Identify all activities associated with any facility or portion thereof used in the operation, maintenance and support of operational systems and equipment. This includes all activities associated with leasing facilities for developmental laboratories and support services, and replacement of government facilities that support second-level engineering. This further includes leasing systems and equipment to meet specific government operational requirements.

## Training, Training Support, and Personnel Skills

Identify all activities associated with on-the-job training, attrition training, and refresher training of personnel who directly operate, maintain, or support operational systems or equipment in accordance with [JO 3120.4 - Air Traffic Technical Training](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1028512) and [FAA Order 3000.57, ATO Technical Operations Training and Personnel Certification](https://www.faa.gov/documentLibrary/media/Order/3000.57.pdf).

Specific activities include:

* Training for airway transportations system specialists
* Training for air traffic control specialists
* Training for support personnel (such as depot repair technicians and second-level engineering staff)
* Course maintenance and specific training by contractors
* Course conduct including the instructor, facilities, travel, and per diem for students

### FAA Academy Training System

When the maintenance philosophy dictates it, ensure the FAA Academy and on-site ATC facilities provides system/systems to support Air Traffic (AT) and ATSS training.

## Technical Data

Identify all activities associated with product-specific documentation including engineering drawings, operator manuals, maintenance manuals, repair and test procedures, provisioning data, logistics management information, software manuals and other technical data used by or directly associated with operations, maintenance, and support of operational systems, facilities, and equipment.

### Manuals and Instructions

Identify provided manuals and technical instructions in accordance with [FAA Order FAA-D-2494, Technical Instruction Book Manuscript: Electronic, Electrical and Mechanical Equipment, Requirements for Preparation of Manuscript and Production Books](http://everyspec.com/FAA/FAA-Spec/FAA-D-2494B_8416/). Provide manuals and technical instructions in soft copy.

### Drawing and Specifications

Provide drawings and specifications in accordance with [Engineering Drawing Practices, ASME Y14.100-2013](http://www.browntechnical.org/content/PDF/api/asmey14.100-2013.pdf) and [MIL-T-31000, Technical Data Package Specifications](http://www.product-lifecycle-management.com/download/MIL-DTL-31000C.pdf).

### Escrow Package

Provide a baselined technical data escrow package consisting of technical manuals, drawings, specifications, source code and related software documentation.

### Computer Resources Support

Identify all activities associated with sustaining the logistics support of computer resources in operational use including:

* technical documentation to reflect operational computer resources
* the infrastructure of operational computer resources support facilities
* technical instruction books and other documentation supporting operational computer resources

Maintenance of the currency of software licenses for assemblers, compilers, code libraries, and commercial-off-the-shelf (COTS) and commercially available software.

# APPENDIX 1. CRITICAL PERFORMANCE REQUIREMENTS

CPRs are a subset of the overall PRD requirements and represent attributes or characteristics considered essential to meeting the needs that the program is seeking to satisfy. CPRs also form the basis for the operational framework and performance baseline for the investment.

Like other PRD requirements, CPRs are expressed as either quantitative or qualitative requirement values. Identify initial CPRs in the iPRD prior to IID, finalize them in the fPRD, and include them in the Acquisition Program Baseline (APB). The formulation and composition of CPRs are consistent with Primitive Requirements Statements as defined in the FAA SEM. Write CPRs as mature requirement statements and include CPRs in the iPRD and fPRD. It is required that CPRs are testable for effective verification and validation (V&V) and decision-making processes. Summarize the CPRs as shown in Table 1 below.

Table 1. Critical Performance Requirements

|  |  |  |  |
| --- | --- | --- | --- |
| **Critical Performance Requirements** | | | |
| CPR # | PRD # | PRD Requirement Text | Quantitative/Qualitative Value Type |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

Table 2 describes some high-level selection for determining whether a requirement is a CPR. Every CPR must fit one or more of these selection criteria items.

Table 2. First-Pass Critical Performance Requirements Determination Guidelines

| **Primary Critical Performance Requirements Determination Guidelines** | |
| --- | --- |
| CPR Criteria Item | Explanation |
| Requirement is directly tied to the a FAA business case | Heavily consider requirements that directly contribute to a program’s business case as candidates for CPR status. During investment analysis, the program office usually develops a Business Case Analysis Report (BCAR) as well as a Shortfall Analysis Report (SAR) as part of their investment approval process. The BCAR and SAR may define metrics or measure that can form the basis for developing CPRs. |
| Requirement is directly tied to an Investment COI | At least some of the CPRs are able to address a program’s critical operational issues, although there does not have to be a one-to-one relationship. A tie-in contributes to a given requirement’s potential to be a CPR. |
| Requirement poses a high level of technical risk | Requirements that are technically more difficult to achieve may pose a higher level of risk to the program. In addition to posing higher risk to the program, certain requirements may have greater risk associated to the NAS or FAA systems, as determined by following the FAA’s Safety Management System. As a result, the program may want to monitor these requirements with greater attention. Therefore, consider requirements with a higher risk rating as candidates for CPR status. |
| Requirements poses a high risk to enterprise strategy | Requirements allocated to investments from the enterprise can represent a risk to the plans of the enterprise. These requirements often represent capabilities that are necessary for multiple investments to deliver on their expected benefits. The disruption enterprise-level strategies is possible if an investment is not able to deliver on one of these requirements. Requirements that cannot be ‘traded off’ to other investments have a higher level of risk. |

Table 3 asks some general questions about the nature of the requirements that are candidate CPRs. These are not meant to be specific selection criteria. The list below clarifies the role of a specific requirement compared to the others within the program. This can help determine the relative importance of larger sets of requirements.

Table 3. Second-Pass Critical Performance Requirements Determination Guidelines

| **Secondary Critical Performance Requirements Determination Guidelines** | |
| --- | --- |
| CPR Criteria Item | Explanation |
| Requirement provides new functionality | Consider if a program consolidates, eliminates or duplicates any of the existing legacy capabilities. Consolidation and elimination of legacy capabilities, in particular may have cascading effect on existing FAA capabilities, and therefore the requirements associated with these investments may have a significant set of CPRs.  Duplication of functionality may or may not result in identification of CPRs. A program whose business case depends on having redundant or duplicate systems, may want to consider identifying duplicate functionality requirements as CPRs. However, merely having duplicate functionality requirements without a strong business is not a strong indicator for having CPRs.  New functions are often critical to a program’s business case. If the requirement provides a new capability, consider it for CPR designation; however, just because a requirement is new, it does not mean that it is necessarily a CPR. (E.g., a function to turn off nuisance alarms benefits controllers, but is not critical to the program). |
| Requirement consolidates existing functionality |
| Requirement removes existing functionality  Requirement duplicates existing functionality |
| Requirement improves existing function performance | Not all CPRs are new functions to the agency. The purpose of some investments is to enhance existing capabilities (e.g. via a Tech Refresh). If the benefits for the program are tied to those improvements, then those performance requirements could be CPRs. |
| Requirement affects NAS safety | Safe movement of aircraft is a primary mission of the agency. A requirement that directly affects NAS safety is a candidate for CPR status. |
| Requirement affects NAS Information Security | Information security is critically important to the FAA. A requirement that directly contributes to Information security is a candidate for CPR status. |
| Requirement has a direct effect on an external interface | Functionality is not the only characteristic of a program that can be critical. Interface requirements often enable the significant benefits of a program. If an interface requirement is necessary to provide the benefits of the program, heavily consider the requirement as a candidate for CPR status. Examples of these can include addition, modification, removal, or consolidation of cables between two systems. |

Given the criteria outlined in Tables 2 and 3, it may be necessary to use an objective means to determine which requirements are critical to the investment. Section 4.6 Decision Analysis (in the SEM) outlines several methods for doing this. Document the means and the results for determining the CPRs in this appendix or the VRTM.

**Explanation of Key Terms**

**Definition** – CPRs are primary requirements that represent attributes or characteristics considered essential to meeting the mission need the program is seeking to satisfy. CPRs are a part of total program requirements that define the operational framework and performance baseline for the investment program. Program requirements are the basis for evaluating the readiness of products for operational use, with particular emphasis and priority given to CPRs. Express CPRs in terms of quantitative or qualitative measurable values. Summarize them in a table as shown in Table 1.

**Implementation** – Identify initial CPRs in the iPRD prior to the initial investment decision, finalize CPRS in the fPRD, and include CPRs verbatim in the acquisition program baseline. The formulation and composition of CPRs are consistent with primitive requirements statements as defined in the FAA SEM. The service organization with the mission need must write all CPRs as mature requirements statements in appropriate locations of sections 3-10 using measurable qualitative and quantitative values in the statement. CPRs must be testable to enable test and evaluation efforts to support effective verification and validation and decision-making. The service organization with the mission need is responsible for identifying and documenting meaningful CPRs that are central to meeting the intended mission need and benefit targets in the business case.

Perform verification and validation of CPRs and other program requirements throughout the program lifecycle— from the time of their development until in-service use of the system or service— as described in the verification and validation guideline document.

**Management of Critical Performance Requirements** – CPR status provides the decision authority with pertinent information regarding a solution’s progress toward operational acceptability. At milestone decisions, verified and validated CPRs (or lack thereof) justify approvals (or disapprovals) for proceeding (or not) into:

1. Solution implementation (final investment decision)
2. System production (if applicable)
3. Initial operational use (initial operating capability)
4. In-service management (in-service decision)

During program reviews, the status of CPR provides the decision authority with insight into program progress towards its end state. This status information is used to identify program risks and issues; allowing opportunities for adjustments to underperforming investments. The decision authority must ensure the total number of CPRs is the minimum number required to meet the mission need. During development of the Program Requirements Document, performance requirements that do not support achievement of a CPR are part of the engineering trade space.

CPRs also provide additional attention and priority during the conduct and reporting of tests and evaluations to assess the ability of the system or service to fulfill the mission. Planning for early formal tests give precedence to CPRs over other requirements. Test and evaluation results roll up detailed test and evaluation data based on CPRs to assess overall performance and limitations of the system or service to better support decision-making and risk management.

# APPENDIX 2. ACRONYMS AND GLOSSARY TERMS

The table below lists all abbreviated terms used in this template. Each investment’s PRD will define its own acronyms and glossary terms in Appendix 2. At a minimum, the technical terms used repeatedly in the document must be in the glossary. Acronyms and Glossary terms must be consistent with the FAA Enterprise Architecture where applicable. The official FAA source for acronyms and abbreviations are on the [FAA Acronyms and Abbreviation](https://www.faa.gov/jobs/abbreviations) website.

## Acronyms

Table 4: Acronyms

| **Acronym** | **Term** |
| --- | --- |
| ACAT | Acquisition Category |
| AMS | Acquisition Management System |
| APB | Acquisition Program Baseline |
| ART | Acquisition Readiness Team |
| AT | Air Traffic |
| ATSS | Airway Transportation System Specialists |
| BCA | Business Case Analysis |
| BPM | Business Process Model |
| CDLS | Contractor Depot Logistics Support |
| CM | Configuration Management |
| ConOps | Concept of Operations |
| COIs | Critical Operational Issues |
| COTS | Commercial Off-The-Shelf |
| CPRs | Critical Performance Requirements |
| CRD | Concept and Requirements Definition |
| CRDRD | CRD Readiness Decision |
| CRS | Contractor Repair Service |
| CWP | Corporate Work Plan |
| DT | Developmental Test |
| EA | Enterprise Architecture |
| ECM | Enterprise Configuration Management |
| ECN | Enterprise Change Notice |
| EIM EC | Enterprise Information Management Enterprise Capability |
| EISA | Energy Independence and Security Act of 2007 |
| EPA | Environmental Protection Agency |
| EPACT | Energy Policy Act of 2005 |
| FA | Functional Analysis |
| FAD | Functional Analysis Document |
| FAA | Federal Aviation Administration |
| FAALC | FAA Logistics Center |
| F&E | Facilities and Equipment |
| FID | Final Investment Decision |
| fPRD | final Program Requirements Document |
| HF | Human Factors |
| HSI | Human System Integration |
| HVAC | Heating Ventilation Air Conditioning |
| IARD | Investment Analysis Readiness Decision |
| ICD | Interface Control Documents |
| ICDLS | Interim Contract Depot Logistics Support |
| IID | Initial Investment Decision |
| ILMT | Integrated Logistics Management Team |
| ILS | Integrated Logistics Support |
| ILSP | Integrated Logistics Support Plan |
| iPRD | Initial Program Requirements Document |
| IRD | Interface Requirements Document |
| ISPD | Implementation Strategy and Planning Document |
| ISR | In Service Review |
| ISS | Information Systems Security |
| ISGSA | Information Security Guidance for System Acquisitions |
| IT | Information Technology |
| JRC | Joint Resource Council |
| LOB | Line of Business |
| LPD | Logistics Product Data |
| MTTR | Mean-Time-To-Restore |
| NAS | National Airspace System |
| NAS RD | NAS Requirement Document |
| NDI | Non-developmental Item |
| NEPA | National Environmental Policy Act |
| NCP | NAS Change Proposal |
| NIST SP | National Institute of Standards and Technology Special Publication |
| NSN | National Stock Number |
| OGB | Operations Governance Board |
| ORD | Operational Readiness Date |
| OSA | Operational Safety Assessment |
| OSHA | Occupational Safety & Health Administration |
| OT | Operational Test |
| PBLI | Product Baseline Index |
| PHS&T | Packaging Handling, Storage, and Transportation |
| pPRD | preliminary Program Requirements Document |
| PIR | Post Implementation Review |
| PRD | Program Requirements Document |
| PSP | Program Safety Plan |
| QA | Quality Assurance |
| RCM | Reliability Centered Maintenance |
| RF | Radio Frequency |
| RMA | Reliability, Maintainability, Availability |
| ROI | Return on Investment |
| SA | Service Analysis |
| SAR | Shortfall Analysis Report |
| SASP | Separation and Airspace Safety Panel |
| SEM | Systems Engineering Manual |
| SLE | Second Level Engineering |
| SOW | Statement of Work |
| SRMD | Safety Risk Management Document |
| SRMGSA | Safety Risk Management Guidance for System Acquisitions |
| SSC | System Support Centers |
| SSD | System Specification Document |
| SSM | Safety Strategy Meeting |
| T&E | Test and Evaluation |
| TOM | Transition to Operations and Maintenance |
| UDL | Unified Data Layer |
| UPS | uninterruptable power supply |
| V&V | Validation and Verification |
| VRTM | Verification Requirements Traceability Matrix |
| WSDD | web service description document |

## Glossary

Table 5: Glossary

| **Term** | **Definition** |
| --- | --- |
| Acquisition Management System (AMS) | Establishes agency-wide policy and guidance for all areas of lifecycle acquisition management. (FAA FAST) |
| Acquisition Program Baseline (APB) | Establishes the performance achieved by an investment program, as well as the cost and schedule boundaries within which the program authorizes to proceed. The acquisition program baseline is a formal document approved by the investment decision authority at the final investment decision and is a contract between the FAA and the service organization. (FAA FAST) |
| Availability | The probability that a system or constituent piece will be operational during any randomly selected period, or, alternatively, the fraction of the total available operating time that the system or constituent piece is operational. (FAA SEM 5.1) |
| Business Case Analysis | Summarizes the analytical and quantitative information developed during investment analysis in the search for the best means for satisfying mission need. It is the primary information document supporting the initial investment decision. (FAA FAST) |
| Business Process Model | The BPM consists of the BPM diagrams as well as the data analysis worksheet. |
| Commercial off-the-shelf(COTS) | A product or service developed for sale, lease or license to the public. It is currently available at a fair market value. (FAA FAST) |
| Concept and Requirements Definition (CRD) | Translates priority operational needs in the enterprise architecture into preliminary requirements and a solution concept of operations for the capability needed to improve service delivery. It also quantifies the service shortfall in sufficient detail for the definition of realistic preliminary requirements and the estimation of potential cost and benefits. (FAA SEM 8.3.2.2) |
| Configuration Management | A management process for establishing and maintaining consistency of a product's performance, functional, and physical attributes with its requirements, design, and operational information throughout its life. (FAA FAST) |
| Critical Operational Issues (COIs) | A key operational effectiveness or operational suitability issue that must be examined during operational test to determine the system’s capability to perform its mission. [FAA T&E Handbook] |
| Critical Performance Requirements (CPRs) | Primary requirements of a solution representing attributes or characteristics considered essential to meeting the mission need that the investment program is seeking to satisfy. Critical performance requirements and associated qualitative and quantitative values are specified in the program requirements document. |
| Data Teams | A group that handles a backlog of data that needs to be brought into the EIM Data Platform. |
| [DOORS](http://pic.dhe.ibm.com/infocenter/doorshlp/v9r5/index.jsp?topic=%2Fcom.ibm.doors.requirements.doc%2Ftopics%2Fc_welcome.html) | A requirement management tool used for requirements management, analysis and traceability. |
| Electrical Safety | Recognizing hazards associated with the use of electrical energy and taking precautions so that hazards do not cause injury or death. (2004 NFPA 70E) |
| Enterprise Level Services/Capabilities | Includes enterprise-level requirement documents that investments needs to align with. Enterprise level service/capabilities form the basis for performance requirements. |
| FAA Acquisition Toolset (FAST) | Is the official record of AMS. As a toolset, FAST contains AMS Policy (agency-wide, mandatory requirements) and AMS Guidance (information implementing or supplementing policy) (FAA FAST) |
| FAA Systems Engineer Manual | Defines the systems engineering practices that FA employees follow and specifies how the agency agrees to implement these practices to accomplish the mission. (FAA SEM Preface) |
| Final Investment Decision (FID) | When the key investment analysis work-products are sufficiently mature and fully validated and verified, the team prepares the final investment package and briefing material for the Final Investment Decision. This is a major review and determines the approval of an investment opportunity for funding and implementation. The investment decision authority approves, disapproves, or modifies the recommendations in the final investment package. If the authority disapproves the recommendations, it returns the investment package with specific instructions for further work or terminates the effort. (FAA SEM 2.2.4.2) |
| Final Program Requirements Document (fPRD) | Updates the Initial Program Requirements to provide a complete statement of functional and performance requirements. Final Program Requirements tailor to the solution selected for implementation and form the basis for program assessment during Solution Implementation. (FAA SEM 2.2.4.2) |
| Fire Life Safety | A written review dealing with the adequacy of life safety features relative to fire |
| Functional Analysis | A Systems Engineering process that translates stakeholders' needs into a sequenced and traceable functional architecture (FAA SEM 3.2) |
| High-Level Operational Concept Diagram (OV-1) | Provides a graphical overview of the system depicted in its intended operational environment. The OV-1 is a technical vision for the system end state and the systems engineer frequently must work with a graphical artist to produce and effective OV-1. The diagram comes with some descriptive text. (FAA SEM 3.4.2.1) |
| Indoor air quality | the air quality within and around buildings and structures, especially as it relates to the health and comfort of building occupants.([Environmental Protection Agency](https://www.epa.gov/indoor-air-quality-iaq/introduction-indoor-air-quality)) |
| Initial Investment Decision (IID) | When the business case is sufficiently mature, investments present IIA results and recommendations are to the investment decision authority for approval. Complete and socialize the following item before this decision point: briefing material and supporting documentation, readiness checklist, verification that exit criteria are satisfied, stakeholder coordination identification of outstanding issues or concerns, briefing of the financial review authority, and a pre-brief of investment-decision authority members. Based on program requirements, business case, and Implementation Strategy and Planning Document, The Initial Investment Decision selects the best alternative to proceed to Final Investment analysis. The investment decision authority may also reject the alternatives and specify the most needed alternate action. The decision-makers determine which solution best contributes to FAA strategic and performance goals and provides the greatest economic benefit. (SEM 2.2.4.1) |
| Initial Program Requirements Document (iPRD) | Updates the preliminary program requirements to provide an implementation-specific statement of functional and performance requirements. Used to solicit market capability information from industry. Initial Program Requirements are not vendor-specific. (FAA SEM 2.2.4.1) |
| In-Service Review (ISR) | This formal review ensures that all activities necessary for the in-service decision are completed. This includes resolution of all support issues identified by the operating service organization and integrated logistics management team; completion of management actions arising from the in-service review checklist and independent operational assessment report (designated investments only); resolution of stakeholder issues; development of the in-service decision briefing and action plan; and concurrence of key stakeholders. (FAA SEM 4.1.4.7) |
| Integrated Logistics Management Team (ILMT) | A cross-functional team comprised of the contracting officer, project lead, lead engineer, and representatives from the operations and maintenance organizations. |
| Interface Requirement Document (IRD) | Document that provides FAA interface requirements between two elements, including type of interface (electrical, pneumatic, hydraulic, etc.) and the interface characteristics (functional or physical). (FAA SEM 4.2.3.3) |
| [Investment Analysis Readiness Decision (IARD)](http://www.ipa.faa.gov/Tasks.cfm?PageName=Investment+Analysis+Readiness+Decision) | At the Investment Analysis Readiness Decision (IARD), the Investment Decision Authority (IDA) reviews the analytical products produced during the Concepts and Requirements Definition (CRD) phase of the Acquisition Management System (AMS) lifecycle and validates that the proposed initiative proceeds to the Investment Analysis phase by entering Initial Investment Analysis (IIA) for further consideration. The following items are created during CRD and are instrumental for a successful completion of the Investment Analysis process:  Final Shortfall Analysis Report  ACAT Determination Request  preliminary Program Requirements (pPRD) Document   Enterprise Architecture products and Amendments   Signed Investment Analysis Plan (IAP)   preliminary Alternatives Description (pAD) |
| Investment program | A sponsored, fully funded effort initiated at Final Investment Decision of the lifecycle management process by the investment decision authority in response to a priority agency need. The goal of an investment program is to field a new capability that satisfies performance, cost, and schedule targets in the acquisition program baseline and benefit targets in the business case analysis report. (FAA FAST) |
| Line of Business (LOB) | An informal term used to characterize the major organizations of the FAA, headed by the Chief Operating Officer (ATO) or the Assistant or Associate Administrator (non-ATO), having major roles and responsibilities in the lifecycle Acquisition Management System (FAA staff offices led by an Assistant Administrator are considered a line of business for purposes of AMS). They are Air Traffic Organization; Aviation Safety, Airports; Commercial Space Transportation; Security and Hazardous Materials Safety; Finance and Management; NextGen and Operations Planning; Policy, International, Affairs and Environment; Human Resources; Civil Rights; Government and Industry Affairs; and Communications. (FAA FAST) |
| Lockout/tag out | Refers to specific practices and procedures to safeguard employees from the unexpected energization or startup of machinery and equipment, or the release of hazardous energy during service or maintenance activities. This requires, in part, that a designated individual turns off and disconnects the machinery or equipment from its energy source(s) before performing service or maintenance and that the authorized employee(s) either lock or tag the energy-isolating device(s) to prevent the release of hazardous energy and take steps to verify that the energy has been isolated effectively. If the potential exists for the release of hazardous stored energy or for the accumulation of stored energy to a hazardous level, the employer must ensure that the employee(s) take steps to prevent injury that may result from the release of the stored energy.  Lockout devices hold energy-isolation devices in a safe or "off" position. They provide protection by preventing machines or equipment from energizing because they are positive restraints that no one can remove without a key or other unlocking mechanism, or through extraordinary means, such as bolt cutters. Tag out devices, by contrast, are prominent warning devices that an authorized employee fastens to energy-isolating devices to warn employees not to reenergize the machine while he or she services or maintains it. Tag out devices are easier to remove and, by themselves, provide employees with less protection than do lockout devices. |
| Maintainability | The measure of the ability of a failed system or constituent piece to be restored to its fully operational status (FAA SEM 5.1) |
| Material handling | The movement, protection, storage and control of materials and products throughout manufacturing, warehousing, distribution, consumption and disposal. |
| Mean-Time-To-Restore (MTTR) | The average total elapsed time from initial failure to resumption of operation (FAA SEM 5.1.1) |
| NAS Change Proposal (NCP) | The NCP is the coordination vehicle used internally to formally manage NAS baselines. Every NCP must consider any safety or security issues that the change could generate. (FAA SEM 4.4.1) |
| National Airspace System (NAS) | The overall environment in which aircraft operate, including aircraft, pilots, tower controllers, terminal area controllers, en route controllers, oceanic controllers, maintenance personnel, and airline dispatchers, as well as the associated infrastructure (facilities, computers, communication equipment, satellites, navigation aids, and radars) (FAA SEM 1.5) |
| Non-Developmental Item (NDI) | A previously developed item for use by federal, state, local, or a foreign government and for which no further development is required. (FAA FAST) |
| [Operational effectiveness](http://www.businessdictionary.com/definition/operational-effectiveness.html) | The degree to which a product accomplishes its mission when used by representative personnel in the expected operational environment. |
| The Operational Event/Trace Description (OV-6) | Used to describe operational activity sequence and timing that traces the actions in a scenario or critical sequence of events. (FAA SEM 3.4.2.1) |
| Operational suitability | The degree to which a product satisfies its availability, compatibility, transportability, interoperability, reliability maintainability, safety, human factors, logistics supportability, documentation, personnel, and training requirements. |
| Personal Protective Equipment | Commonly referred to as "PPE", is equipment worn to minimize exposure to hazards that cause serious workplace injuries and illnesses. These injuries and illnesses may result from contact with chemical, radiological, physical, electrical, mechanical, or other workplace hazards. Personal protective equipment may include items such as gloves, safety glasses and shoes, earplugs or muffs, hard hats, respirators, or coveralls, vests and full body suits. ([Occupational Safety and Health Administration](https://www.osha.gov/SLTC/personalprotectiveequipment/)) |
| Post Implementation Review (PIR) | Reviews that the FAA conducts between 6 and 24 months after the first product of an investment program has become operational. PIR exception reports provide the agency with useful information and recommendation on how best to satisfy unfulfilled requirements, needs, and performance either with the current program or by other means. (FAA SEM 3.3.3.4) |
| Preliminary Program Requirements Document (pPRD) | High-level functional, performance, interface, safety, security, and constraint requirements that must be solution-agnostic. (FAA SEM 2.2.3) |
| Program Safety Plan (PSP) | Overall plan for conducting system safety management in the AMS. (FAA SEM 5.6.3) |
| Quality assurance | A way of preventing mistakes or defects in manufactured products and avoiding problems when delivering solutions or services to customers. QA applies to physical products in pre-production to verify what will be made meets specifications and requirements, and during manufacturing production, runs by validating lot samples meet specified quality controls. QA is also applied to software to verify that features and functionality meet business objectives, and that code is relatively bug free prior to shipping or releasing new software products and versions. |
| Readiness-Based Sparing (RBS) | The practice of using advanced analytics to set spares levels and locations to maximize system readiness. Readiness-Based Sparing determines the inventory requirements for achievement of readiness goals:   * What to stock: parts, components, sub-systems (multi-indenture) * Where to stock: strategic distribution points (SDPs), forward distribution points (FDPs), and/or at operational-level distribution points (multi-echelon) * Taken together, these make up a two-dimensional Multi-Indenture, Multi-Echelon—or “MIME” RBS * Typically, the RBS model objective is to achieve readiness (such as Operational Availability) at the least investment |
| Reliability | Ability of a system and its parts to perform its mission without failure, degradation, or demand on the support system. It is generally characterized by the Mean-Time-Between-Failure (FAA SEM 5.1) |
| Reliability Centered Maintenance (RCM) Process | A method for determining maintenance requirements based on the analysis of the likely functional failures of systems/equipment having a significant impact on safety, operations, and lifecycle cost. RCM supports the failure-management strategy for any system based on its inherent reliability and operating context |
| Resiliency | Ability for the NAS to effectively prepare for and adapt to changing conditions and withstands and recovers from deliberate attacks, accidents, and naturally occurring threats or incidents. Key principles for building resiliency into the NAS include redundancy, diversity, separation, transparency, response, and recovery. |
| Safety risk | The composite predicted severity and likelihood of the potential effect of a hazard.  1. Initial- The predicted severity and likelihood when initially assessed. 2. Current- The predicted severity and likelihood at the current time. 3. Residual- The remaining predicted severity likelihood that exists after all selected risk control techniques have been implemented. (FAA SEM 2.2.2) |
| Safety Risk Management Document (SRMD) | Document that must be developed at each of the principal AMS decision points. The goal is to ensure the safety of the NAS by identifying system risks and associated mitigations as early as possible. (FAA SEM 2.2.3) |
| Safety Risk Management Guidance for System Acquisitions (SRMGSA) | Is the required guide for applying Safety Risk Management (SRM) to acquisitions that affect the NAS. The SRMGSA serve as: - SMS guidance for acquisitions during these phases of the AMS cycle: Mission Needs Analysis (MNA), Concept and Requirements Definition (CRD), Investment Analysis (IA), Solution Implementation (SI), and In-Service Management.  - Specific guidance for system changes. - A definition of the Investment Decision Authority's (IDA's) expectations regarding SRM. The SRMGSA provides a framework and further process definition to ensure the execution of SRM throughout the entire lifecycle of a system or product. (FAA SEM 5.6.1) |
| Solution Concept of Operations (ConOps) | Description of the expectation from the system, including its various modes of operation and time-critical parameters. (FAA SEM 2.2.3) |
| Statement of Work (SOW) | The SOW is a detailed description of the specific services or tasks that a contractor is required to perform under a contract. The SOW incorporates into a vendor contract. (FAA SEM 2.2.4.2) |
| [Strategic](http://www.businessdictionary.com/definition/strategic-goals.html) goals | The planned objectives that an organization strives to achieve. Most senior managers will take the time to develop and articulate appropriate strategic goals for their business in order to demonstrate to subordinate employees what their plans and vision for the company are. Such strategic goals must be achievable and reflect a realistic assessment of the current and projected business environment. |
| System of Systems (SoS) | Is a collection of task-oriented or dedicated systems that pool their resources and capabilities together to create a new, more complex system that offers more functionality and performance than simply the sum of the constituent systems. |
| Systems Functionality (SV-4) | Documents system functional hierarchies and system functions as well as the data flows between the system functions. The Enterprise-level SV-4 represents as a "Taxonomic functional hierarchy" rather than a set of data flow diagrams. A taxonomic functional hierarchy helps to visualize the evolution of the NAS towards a service-oriented paradigm where services are reused across the enterprise as opposed to individual investments implementing all functions as a standalone capability. This is particularly useful in capability-based procurement that it is necessary to model the functions that are associated with particular capability. For Service Unit and Program-level architectures, Data Flow Diagrams represent SV-4. In addition, the Enterprise-level SV-4 is the structure by which NAS requirements align. (FAA SEM 3.4.2.1) |
| System specification | Derived from the program requirements, specifications provide low-level detail for functional and performance attributes of the selected solution. (FAA SEM 2.2.4.2) |
| The Systems/Services Communications Description (SV-2) | Describes the data mechanism used to execute systems interfaces. This product focuses on establishing boundaries and depicting communication implementation approaches between the NAS and various stakeholder systems (FAA SEM 3.4.2.1) |
| Validation | Confirmation that an end-product or end-product component will fulfill its intended purpose when placed in its intended environment. The methods employed to accomplish validation apply to selected work products as well as to the end-product and end-product components. Select work products based on which are the best predictors of how well the end-product and end-product component will satisfy the intended purpose and user needs. Validation may address all aspects of an end-product in any of its intended environments, such as operation, training, manufacturing, maintenance, or support services. (FAA FAST) |
| Verification | Confirmation that selected work products meet their specified requirements. This includes verification of the end-product (system, service, facility, or operational change) and intermediate work products against all applicable requirements. Verification is inherently an incremental process since it occurs throughout the development of the end-product and work products-beginning with initial requirements, progressing through subsequent changes, and culminating in verification of the completed end product. (FAA FAST) |
| Verification Requirements Traceability Matrix (VRTM) | Matrix correlating requirements and the associated verification method(s). The VRTM defines how each requirement (functional, performance, and design) verifies, the stage verification is to occur, and the applicable verification levels. (FAA SEM 4) |
| [Web Service Description Document (WSDD)](http://www.faa.gov/about/office_org/headquarters_offices/ato/service_units/techops/atc_comms_services/swim/documentation/media/briefings/How%20to%20read%20and%20understand%20WSDD%20for%20SWIM%20060811r2.ppt) | Is a Web service description (as it is defined and understood in Service-Oriented Architecture (SOA)) which is rendered as a human-readable document in a way consistent with FAA acquisition process standards and practices. WSDDs develop in accordance with FAA-STD-065. WSDD has become de facto “Interface Control Document (ICD) for Web Services”. National Airspace System and/or other configuration boards in accordance with established configuration management policies process WSDD. |

# APPENDIX 3. REFERENCE DOCUMENTS

Reference Documents used in the Program Requirements must be consistent with the FAA Enterprise Architectures [TV-1](https://nasea.faa.gov/file/get/2658) where applicable. If a more current version of a document exists, cite the most current version. List investment-specific references for each section in the table below. Please refer to the [FAA Orders](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1021786) and [FAA Handbooks & Manuals](http://www.faa.gov/regulations_policies/handbooks_manuals/) for more information.

Table 6: Reference Documents

| **PRD Template Section** | **Referenced Document** |
| --- | --- |
| **General Guidance** | [FAA-STD-067 Preparation of Specifications](http://www.tc.faa.gov/its/worldpac/standards/faa-std-067.pdf)  [FAA Order 1000.36](https://www.faa.gov/documentlibrary/media/order/branding_writing/order1000_36.pdf)  [Operations Governance Board (OGB)](http://fast.faa.gov/NNOFCA_Operations_Governance_Board.cfm)  [The Clinger-Cohen Act](http://dodcio.defense.gov/Portals/0/Documents/ciodesrefvolone.pdf)  [Executive Order 13011, Federal Information Technology](https://govinfo.library.unt.edu/npr/library/direct/orders/27aa.html)  [Office of Management and Budget (OMB) Circular A-130](https://obamawhitehouse.archives.gov/sites/default/files/omb/assets/OMB/circulars/a130/a130revised.pdf)  [FAA Systems Engineering Manual (SEM)](https://sep.faa.gov/policy_and_guidance/main)  [FAA Order 1370.121- FAA Information Security and Privacy Program & Policy](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1030708) |
| **Signature Page/Focal Point** | N/A |
| **1. Introduction** | N/A |
| **1.1 Description** | N/A |
| **1.2 Scope** | N/A |
| **2 Capability Description and Program Information** | N/A |
| **2.1 Operational Concept** | [EA Program Manager Guidance](https://my.faa.gov/content/dam/myfaa/org/staffoffices/afn/information/processes/ade/AIT-ASP-004-W2-Non-NAS-EA-PM-Guidance.pdf) |
| **2.2 Quantities and Location** | N/A |
| **2.3 Constraints** | N/A |
| **3 Functional and Performance Requirements** | [FAA Systems Engineering Manual (SEM)](https://sep.faa.gov/policy_and_guidance/main)  INCOSE Systems Engineering Handbook Fourth Edition, 2015  ISO/IEC/IEEE 15288-2015 |
| **3.1 Functional Requirements** | N/A |
| **3.2 Data and Information Requirements** | N/A |
| **3.3 Performance Requirements** | N/A |
| **3.4 Reliability, Maintainability, and Availability and Resiliency Requirements** | [FAA RMA Handbook (RMA-HDBK-006C](http://www.tc.faa.gov/its/worldpac/standards/faa-hdbk-006c.pdf)  FAA Order JO 6000.36 <u>National Airspace System Service Survivability</u> |
|  |  |
| **4 Integration Requirements** | N/A |
| **4.1 Physical Integration** | [FAA-G-2100 H, Electronic Equipment, General Requirements](https://ksn2.faa.gov/nextgen/SysEng/NASEAandRqmts/ISE/SiteAssets/Attachment_6_FAA-G-2100H.pdf) |
| **4.1.1 Environmental Requirements** | [FAA Order 1050.19B - Environmental Due Diligence Audits in the Conduct of FAA Real Property Transactions](http://www.faa.gov/documentLibrary/media/Order/ND/1050.19B.pdf)  [FAA Order 1050.1F, Environmental Impacts: Policies and Procedures](http://www.faa.gov/documentLibrary/media/Order/FAA_Order_1050_1F.pdf)  [29 CFR 1910, Subpart J, General Environmental Controls](https://www.osha.gov/pls/oshaweb/owasrch.search_form?p_doc_type=STANDARDS&p_toc_level=1&p_keyvalue=1910) |
| **4.1.2 Land and Facility** | N/A |
| **4.1.2.1 Grounding, Bonding, Shielding, Lightning Protection, Cables, Power and HVAC** | [FAA-STD-019E - Lightning and Surge Protection, Grounding, Bonding and Shielding Requirements for Facilities and Equipment](http://everyspec.com/FAA/FAA-STD/download.php?spec=FAA_STD_019e.2259.pdf)  [FAA-G-2100H - Electronics Equipment, General Requirements](https://ksn2.faa.gov/nextgen/SysEng/NASEAandRqmts/ISE/SiteAssets/Attachment_6_FAA-G-2100H.pdf)  [FAA Order 6030.20F - Electrical Power Policy](http://www.faa.gov/documentLibrary/media/Order/6030_20_F%20with%20CHG%201%20incorporated.pdf)  [FAA Order 6950.2D - Electrical Power Policy Implementation at National Airspace System Facilities](http://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/9882)  [American National Standards Institute/Institute of Electrical and Electronics Engineers (ANSI/IEEE) Standard 1100-2005, Recommended Practice for Powering and Grounding Electrical Equipment](https://standards.ieee.org/findstds/standard/1100-2005.html)  [FAA Order 1370.121- FAA Information Security and Privacy Program & Policy, Appendix 2, Paragraph 17.3., and Appendix 12](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1030708) |
| **4.1.2.2 Energy and Water Conservation** | [National Energy Conservation Policy Act](https://www1.eere.energy.gov/femp/pdfs/necpa_amended.pdf)  [The Energy Policy Act of 2005 (EPACT)](http://www.gpo.gov/fdsys/pkg/PLAW-109publ58/pdf/PLAW-109publ58.pdf)  [The Energy Independence and Security Act of 2007 (EISA)](http://www.gpo.gov/fdsys/pkg/BILLS-110hr6enr/pdf/BILLS-110hr6enr.pdf)  [Executive Order 13693](https://www.gpo.gov/fdsys/pkg/FR-2015-03-25/pdf/2015-07016.pdf)  [FAA Order 1053.1B, Energy and Water Management Program for FAA Buildings and Facilities](http://www.faa.gov/documentLibrary/media/Order/1053.1B.pdf) |
| **4.1.2.3 Hazardous Materials** | [OSHA Standard 1910.120 subpart H - Hazardous Waste Operations and Emergency Response](https://www.osha.gov/pls/oshaweb/owadisp.show_document?p_table=STANDARDS&p_id=9765)  [EPA Regulation 40 CFR Part 260 - Hazardous Waste Management System: General](http://www.ecfr.gov/cgi-bin/text-idx?SID=ce1c367b165ba9c97020a904000ccefd&mc=true&node=pt40.28.260&rgn=div5)  [FAA Order 1050.10D, Prevention, Control, and Abatement of FAA Environmental Pollution](https://employees.faa.gov/tools_resources/orders_notices/index.cfm/go/document.information/documentID/1028586)  [FAA Order 1050.14B- Polychlorinated Biphenyls (PCBs) in the National Airspace System](http://www.faa.gov/documentLibrary/media/Order/order%201050.14B.pdf)  [FAA Order 1050.18 - Chlorofluorocarbons and Halon Use at FAA Facilities](http://www.faa.gov/documentLibrary/media/order/energy_orders/1050.18.pdf)  [FAA Order 1050.20A - Airway Facilities Asbestos Control Program](http://www.faa.gov/documentLibrary/media/Order/1050.20A.pdf)  [FAA Order 4600.27B - Personal Property Management](http://www.faa.gov/documentLibrary/media/Order/4600.27B.pdf) |
| **4.1.3 Telecommunications** | [FAA Order 1830.10 - Managing New Telecommunications Requirements](http://www.faa.gov/documentLibrary/media/Order/1830.10.pdf)  [FAA-STD-049 - Fiber Optic Telecommunication System and Equipment](http://www.tc.faa.gov/its/worldpac/standards/faa-std-049.pdf)  [FAA Order 1370.121- FAA Information Security and Privacy Program & Policy](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1030708) |
| **4.1.4 Special Considerations** | N/A |
| **4.2 Functional Integration** | N/A |
| **4.2.1 Interfaces to Other FAA Enterprise Architecture Elements** | [FAA-STD-025F - Preparation of Interface Documentation](http://www.tc.faa.gov/its/worldpac/standards/faa-std-025f.pdf)  [JO 6000.53D - Remote Maintenance Monitoring Interface Development and Implementation](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1029689) |
| **4.2.2 External Interfaces** | [FAA STD-025F](http://www.tc.faa.gov/its/worldpac/standards/faa-std-025f.pdf) |
| **4.2.3 Spectrum Requirements** | [FAA Order 6050.32B - Spectrum Management Regulations and Procedures Manual](http://www.faa.gov/documentLibrary/media/Order/6050_32B_WITH_CHG_1_AND_2_INCORPORATED.pdf)  [FAA Order 6050.19F - Radio Spectrum Planning](https://www.faa.gov/documentLibrary/media/Order/6050_19F.pdf) |
| **4.3 Human-System Integration** | [Aviation Safety and Air Traffic](http://www.hf.faa.gov)  [HF Design Standard](http://hf.tc.faa.gov/hfds)  [HF Job Aid](http://www.hf.faa.gov/workbenchtools/Tools/HFAcqJobAid2012.pdf)  [HF Order](http://www.faa.gov/documentLibrary/media/Order/9550.8.pdf) |
| **4.4 Employee Safety and Health** | [FAA Order 3900.19B - FAA Occupational Safety and Health Program](http://www.faa.gov/documentLibrary/media/Order/3900.19B.pdf)  [FAA-G-2100 H, Electronic Equipment, General Requirements](https://ksn2.faa.gov/nextgen/SysEng/NASEAandRqmts/ISE/SiteAssets/Attachment_6_FAA-G-2100H.pdf)  [29 CFR 1910.303, Electrical](https://www.osha.gov/pls/oshaweb/owadisp.show_document?p_table=standards&p_id=9880)  [NFPA 13, Standard for the Installation of Sprinkler Systems](http://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards?mode=code&code=13)  [NFPA 70, National Electrical Code](http://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards?mode=code&code=70)  [NFPA 101, Life Safety Code](http://www.nfpa.org/codes-and-standards/all-codes-and-standards/list-of-codes-and-standards?mode=code&code=101)  [29 CFR 1910.95, Occupational Noise Exposure](https://www.law.cornell.edu/cfr/text/29/1910.95)  [29 CFR 1910.145, Specifications for Accident Prevention Signs](https://www.law.cornell.edu/cfr/text/29/1910.145)  [29 CFR 1910.1001, Asbestos](https://www.law.cornell.edu/cfr/text/29/1910.1001)  [29 CFR 1910, Subpart E, Means of Egress](https://www.osha.gov/pls/oshaweb/owadisp.show_document?p_id=10113&p_table=standards)  [29 CFR 1910, Subpart I, Personal Protective Equipment](https://www.law.cornell.edu/cfr/text/29/part-1910/subpart-I)  [29 CFR 1910, Subpart L, Fire Protection](https://www.law.cornell.edu/cfr/text/29/part-1910/subpart-L)  [ANSI Z535.4, Product Safety Signs and Labels](http://www.safetysign.com/help/h39/safety-labels)  [29 CFR Part 1960, Basic Program Elements for Federal Employees Occupational Safety and Health Programs and Related Matters](https://www.law.cornell.edu/cfr/text/29/part-1960) |
| **5. Security and Safety Requirements** | N/A |
| **5.1 Facility Security** | [FAA Order 1600.6E - Facility Security Policy](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/13920),  [FAA Order 1600.69C, FAA Facility Security Management Program](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1029860) |
| **5.2 Personnel Security** | [FAA Order 1600.1E - Personnel Security Program](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/14801)  [FAA Order 1600.72A, Contractor & Industrial Security Program.](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/15573) |
| **5.3 Information Systems Security** | [ISGSA](https://fast.faa.gov/EMP_Information_Security.cfm)  [AMS Section 4.11](http://fast.faa.gov/docs/acquisitionManagementPolicy/AcquisitionManagementPolicy4.11.pdf)  [FAA Order 1370.121](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1030708)-FAA Information Security and Privacy Program & Policy  [National Institute of Standards and Technology Special Publication (NIST SP) 800-53](http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf)  [FAA Information Security](http://fast.faa.gov/EMP_Information_Security.cfm)  [ISS section](https://employees.faa.gov/tools_resources/orders_notices/) |
| **5.4 System Safety** | [JO 1000.37 - Air Traffic Organization Safety Management System](http://www.faa.gov/documentLibrary/media/Order/ND/1000.37.pdf)  [Safety Risk Management Guidance for System Acquisitions (SRMGSA)](https://www.faa.gov/air_traffic/publications/media/SRMGSA.pdf)  [Safety Management System Manual](https://www.faa.gov/air_traffic/publications/media/ATO-SMS-Manual.pdf)  [FAA Order 8000.369B, Safety Management System Guidance](http://www.faa.gov/documentLibrary/media/Order/FAA_Order_8000.369B.pdf)  [FAA Order 8040.4A, Safety Risk Management](http://www.faa.gov/documentLibrary/media/Order/8040.4A%20.pdf) |
| **5.4.1 Existing Controls** | N/A |
| **5.4.2 Safety Requirements** | RTCA DO-278A |
| **6. Quality and Configuration Management Requirements** | N/A |
| **6.1 Quality Assurance** | [JO 7210.633 – Air Traffic Quality Assurance (QA) Program](http://www.faa.gov/documentLibrary/media/Order/JO_7210_633.pdf)  [FAA-STD-013D - Quality Control Program Requirements](http://www.tc.faa.gov/its/worldpac/standards/faa-std-013d.pdf)  [FAA-STD-016A - Quality Control System Requirements](http://www.tc.faa.gov/its/worldpac/standards/faa-std-016a.pdf) |
| **6.2 Configuration Management** | [FAA Order 1800.66, Configuration Management Policy](http://www.faa.gov/documentLibrary/media/Order/1800.66.pdf)  [FAA STD 058, Facility Configuration Management](http://www.tc.faa.gov/its/worldpac/standards/faa-std-058.pdf)  [FAA STD 021A, Configuration Management Contractor Requirements](http://www.tc.faa.gov/its/worldpac/standards/faa-std-021a.pdf) |
| **7 Test and Evaluation Requirements** | N/A |
| **7.1 NAS Testing Requirements** | [AMS Policy Section 4.4 Test and Evaluation](http://fast.faa.gov/docs/acquisitionManagementPolicy/AcquisitionManagementPolicy4.4.pdf)  [AMS Policy Section 4.4 Test and Evaluation](http://fast.faa.gov/docs/acquisitionManagementPolicy/AcquisitionManagementPolicy4.4.pdf)  [NG 1810.8A FAA William J. Hughes Technical Center’s Test and Evaluation Policy](http://www.faa.gov/documentLibrary/media/Order/NG_1810.8A.pdf)  [FAA William J Hughes Technical Center Test and Evaluation Handbook](http://www.tc.faa.gov/its/worldpac/standards/vvspt-a2-pdd-013%20tne%20handbook.pdf)  [FAA AMS Lifecycle Verification and Validation Guidelines](http://fast.faa.gov/docs/vandvguidelines.doc)  [FAA SEM](https://sep.faa.gov/policy_and_guidance/main) |
| **7.2 Planning and Design Requirements** | N/A |
| **7.3 Developmental Test Requirements** | N/A |
| **7.4 Operational Test Requirements** | N/A |
| **7.5 Site Test Requirements** | N/A |
| **7.6 Reporting Requirements** | N/A |
| **7.7 Test Support Requirements** | N/A |
| **7.8 Critical Operational Issues** | N/A |
| **8 Implementation and Transition Requirements** | [Corporate Work Plan (CWP)](https://my.faa.gov/org/staffoffices/afn/finance/training/cwp/cwp_welcome.html)  [In-Service Review (ISR) checklist](https://my.faa.gov/content/dam/myfaa/org/linebusiness/ato/safety/isd/documents/ISR-Checklist.doc) |
| **9 In-Service Support and Management Requirements** | N/A |
| **9.1 Integrated Logistics Support** | [FAA AMS, Section 4.3: Integrated Logistics Support (ILS)](http://fast.faa.gov/docs/acquisitionManagementPolicy/AcquisitionManagementPolicy4.3.pdf) |
| **9.2 Maintenance Planning** | [FAA Order 6000.30F National Airspace System Maintenance Policy](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1020968)  [JO 6000.53D, Remote Maintenance Monitoring Interface Development and Implementation](https://employees.faa.gov/documentLibrary/media/Order/JO_6000_53D.pdf) |
| **9.2.1 Field Maintenance Support** | [FAA Order 6000.15G – General Maintenance Handbook for National Airspace System (NAS) Facilities](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1021786) |
| **9.2.1.1 Service and System Certification Criteria** | [FAA Order 6000.15H – General Maintenance Handbook for National Airspace System (NAS) Facilities](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1021786) |
| **9.2.1.2 Remote Maintenance Monitoring** | N/A |
| **9.2.2 Second Level Engineering, Maintenance, and Technical Support** | [FAA Order 1100.157A -- National Systems Engineering Divisions Maintenance Program Procedures, Operational Support (AOS)](http://www.faa.gov/documentLibrary/media/Order/ND/1100.157.pdf)  [FAA Order 6000.30F – National Airspace System Maintenance Policy](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1020968) |
| **9.2.3 Depot-Level Support** | [Business Case Analysis (BCA) Template](https://fast.faa.gov/archive/v1011/docs/businesscasetemplate.doc)  [FAA Order 2500.8B, Funding Criteria for OPS, F&E, and RE&D accounts](https://www.faa.gov/documentLibrary/media/directives/nd/ND2500-8B.pdf) |
| **9.3 Supply Support** | [FAA Order 4250.9B, Field Materiel Management and Control](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/8151)  GEIA-STD-007 Logistics Product Data (LPD) |
| **9.3.1 Site Sparing** | N/A |
| **9.3.2 Life Cycle Provisioning/Depot Spares** | [FAA Order 4250.9B, Field Materiel Management and Control](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/8151)  GEIA-STD-007 Logistics Product Data (LPD) |
| **9.3.3 Screening** | [FAA Order 4500.3D - Federal Catalog and Standardization Programs (FCSP)](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/8297) |
| **9.3.4 Warranty** | [FAA Order 4650.20A - Reporting and Replacement of Items Falling under Warranty](http://www.faa.gov/documentLibrary/media/Order/4650.20A.pdf) |
| **9.3.5 Asset Management** | [FAA Order 4140.1, Integrated Material Management Program](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/8142)  [FAA Order 4600.27C Personal Property Management](https://www.faa.gov/documentLibrary/media/Order/FAA_Order_4600.27C.pdf) |
| **9.4 Packing, Handling, Storage, and Transportation** | [ASTM-D-395118 Standard Practice for Commercial Packaging](http://www.dla.mil/Portals/104/Documents/LandAndMaritime/V/VS/Packaging/LM_HandoutFY2014rev6_151007.pdf)  MIL-STD-2073-1 DOD Material Procedures for Development and Application of Packaging Requirements  [MIL-STD-129R Military Marking for Shipment and Storage](https://vsc.gsa.gov/administration/files/MIL-STD-129R.pdf) |
| **9.4.1 Depot Spares** | N/A |
| **9.4.2 Barcoding** | [FAA Asset Identification Specification dated January 29, 2013](https://faaco.faa.gov/index.cfm/announcement/view/12706) |
| **9.5 Support Equipment Maintenance** | N/A |
| **9.5.1 Tools and Test Equipment** | [FAA Order 6200.4G – National Test Equipment Program Management](http://www.faa.gov/documentLibrary/media/Order/6200.4G.pdf)  GEHA-STD-007 Logistics Product Data (LPD) |
| **9.6 Direct-Work Maintenance Staffing** | N/A |
| **9.7 Maintenance Support Facilities** | N/A |
| **9.8 Training, Training Support, and Personnel Skills** | [JO 3120.4 - Air Traffic Technical Training](https://www.faa.gov/regulations_policies/orders_notices/index.cfm/go/document.information/documentID/1028512)  [FAA Order 3000.57, ATO Technical Operations Training and Personnel Certification](https://www.faa.gov/documentLibrary/media/Order/3000.57.pdf) |
| **9.8.1 FAA Academy Training System** | N/A |
| **9.9 Technical Data** | N/A |
| **9.9.1 Manuals and Instructions** | [FAA Order FAA-D-2494, Technical Instruction Book Manuscript: Electronic, Electrical and Mechanical Equipment, Requirements for Preparation of Manuscript and Production Books](http://everyspec.com/FAA/FAA-Spec/FAA-D-2494B_8416/) |
| **9.9.2 Drawing and Specifications** | [Engineering Drawing Practices, ASME Y14.100-2013](http://www.browntechnical.org/content/PDF/api/asmey14.100-2013.pdf)  [MIL-T-31000, Technical Data Package Specifications](http://www.product-lifecycle-management.com/download/MIL-DTL-31000C.pdf) |
| **9.9.3 Escrow Package** | N/A |
| **9.9.4 Computer Resources Support** | N/A |

# APPENDIX 4. PROGRAM REQUIREMENTS TRACEABILITY AND VERIFICATION

**Traceability**

Validate each program requirement against a source to establish requirement traceability. Establish traceability both vertically and horizontally. Vertical traceability establishes a relationship between program requirements and the higher-level enterprise requirements. Horizontal traceability establishes a relationship between peer products at the same level. Validation sources include the following four types of artifacts:

1. Target NAS Requirements Document (TNRD): Trace each program requirement to one or more enterprise level requirement listed in the TNRD. Trace to the most recent version of the TNRD on the SE Portal. Programmatic or design constraint information may not be applicable to the TNRD, but may be sourced to other documentation. Guidance for conducting the trace is available in the Guide for Tracing Program Requirement Documents (PRDs) to the Target NAS Requirements Document (TNRD).
2. Functional Analysis Functions: Functional Analysis is the primary driver of program functional requirement derivation. Trace each functional requirement to a function identified in the FAD delivered by the program.
3. Program Requirements Document (PRD): Trace the iPRD and fPRD requirements to the associated requirement in the pPRD and iPRD, respectively. This provides a means for tracing the requirement to previous versions of the PRD.
4. Other Sources: The PRD requirement may be sourced from other materials such as FAA orders, AMS policies, standards, regulations, laws, best practices and guidance materials. Requirements can be sourced from subject matter experts, management and systems engineering decisions, enterprise initiatives (e.g., cloud computing), ConOps, etc.

**Verification**

The typical verification phases for a program include Developmental Test (DT), Operational Test (OT), and Site Acceptance Test (SAT). The TEMP will identify the verification method associated with each verification phase. The PRD must include at least a general method of verification for each requirement, but the PRD may instead outline the Method of Verification (MOV) for each verification phase.

Verification methods include test, demonstration, inspection, and analysis. Initial verification methods may be revised as the program and test-planning processes develops*.* Use the Verification Requirements Traceability Matrix (VRTM) shown in Table 8 to demonstrate traceability. Refer to the [Test and Evaluation Handbook issued by the FAA William J. Hughes Technical Center](http://www.tc.faa.gov/its/worldpac/standards/vvspt-a2-pdd-013%20tne%20handbook.pdf), and [V&V Guidelines](http://fast.faa.gov/docs/vandvguidelines.doc) in the AMS Toolset for additional guidance on verification methods.

**Allocation**

Allocation identifies the architectural element or organization that is responsible for implementing the requirement. Allocation is appropriate for elements within the defined boundaries of the program’s system architecture or for responsibilities, the program has delegated to other organizations.

It is important to distinguish allocation from external dependencies. A program may be dependent on another system in order to provide the solution. The system may interface or integrate with this external system, but a program is not responsible for the external system other than ensuring the interface with that system is functioning. For example, a program may rely on receiving timing from FTI’s NTP Server, but it will not verify the function of the NTP Server. It will only verify that the interface works. Some FTI functions such as inter-facility communication or NESG boundary protection will be internal to the program’s architecture. The FAD for the program defines internal functions and identifies the interfaces with external components.

Table 7: VRTM Column Descriptions

| **Column** | **Description** |
| --- | --- |
| PARA\_ID | Paragraph Identifier (Optional): The section number or the paragraph number of the requirement, e.g., 3.1.2.4. This column is helpful for locating the requirement in the PRD main body especially if it is not in an electronically searchable format. |
| REQ\_ID | Requirement Identifier (Mandatory): A unique requirement identifier typically consisting of a program prefix followed by a number, e.g., ERAM\_1254. Assign unique reference numbers not tied to a paragraph number, because additions/modifications of the outline structure may limit the uniqueness of the paragraph identifier. The requirements in the main body need to include the associated REQ\_ID. This can be accomplished by a bracketed or parenthetical identification right after the ‘must’ word or at the end of the requirement statement. |
| REQ\_TEXT | Requirement Text (Recommended): The requirement statement repeated from the main body of the PRD. While not required, it is useful to see the MOV next to the requirement statement to ensure the MOV is correct. |
| PHASE | Phase (Conditional): For multi-segment investments, annotate each requirement with the applicable segment/phase (see Special Consideration for Multi-Segment Investments in the general guidance section). Either list all segment/phases for which the requirement applies or enter the segment/phase where the requirement is first introduced. Disclose which method used so the applicable phase(s) for the requirement is clear. Ensure a general description of each phase is included in Section 2. |
| PRD\_ID | PRD Identifier (Mandatory for iPRD/fPRD): To facilitate horizontal traceability, include the Requirement Identifier for the previous edition of the PRD. Changes in this PRD must reference the applicable REQ\_ID for the prior PRD. New requirements must use the term NEW in this column. This column is not required for the pPRD. Tracing is required only for the previously signed PRD. Ensure the previous edition of the PRD (version/date) is included in Appendix 3, References. |
| TNRD\_ID | Target NAS Requirement Document Identifier (Mandatory): Include the specific requirement paragraph number(s) for the traceable TNRD requirement(s). Use the most recent Target NAS RD available on the portal and include the TNRD version information in the Appendix 3, References. Identify the leaf (or leaves) requirements rather than a higher level TNRD requirement unless the higher-level TNRD requirement needs to cover the scope of the PRD requirement. Mark requirements that are not within the TNRD scope as N/A. Reference the Guide for Tracing Program Requirement Documents (PRDs) to the Target NAS Requirements Document (TNRD). |
| FAD\_ID | Functional Analysis Document Identifier (Mandatory): Include the function identifier used to develop the associated requirement statement. The requirements in PRD Section 3.1 (Functional Requirements) and PRD Section 4.2 (Functional Integration) must have FAD references. Mark requirements that are not within the FAD scope as N/A. Ensure the FAD (version/date) is included in Appendix 3, References. |
| SOURCE | SOURCE (Mandatory): If a requirement is not sourced to either the TNRD or the FAD, provide the source that validates the need for the requirement. Sources may include the ConOps, Orders, Standards, SMEs and Use Cases. Please be specific as possible. For example, if a specific standard paragraph is the reason for the requirement, cite the specific standard paragraph. If the requirement can be sourced to either the TNRD or the FAD and another Source is not applicable, mark this column as N/A. Ensure any sources listed are included in Appendix 3, References. |
| MOV | Method of Verification (Mandatory): The method used to verify the requirement, e.g., Test (T), Inspection (I), Demonstration (D) and/or Analysis (A). Multiple enumerations for a requirement are permitted. If a requirement is not applicable for verification, e.g., verified in an earlier test phase, mark it as not applicable (X). Use of abbreviations in the VRTM will make it more readable given the space limitations. Include in the VRTM a reference to where the MOV definitions are located, or restate the definitions within first part of the Appendix. If the definitions are different from the T&E Handbook, include a statement to this effect in the Appendix. |
| CPR | Critical Performance Requirement (Mandatory for iPRD/fPRD): Indicate whether the requirement is a CPR or not by marking the requirement as Y (yes a CPR) or N (not a CPR). |
| ALLOCATION | Allocation (Mandatory): Include the allocated system, service, program or organizational element responsible (in this order) for implementing the requirement. Multiple enumerations are permitted. When a program has not identified internal subsystem elements, cite the program or the program’s system as an entity. Notwithstanding, it is important to identify requirements that are allocated to other NAS systems, e.g., SWIM, FTI, etc., that are within the investment’s architecture (defined boundaries). Please be as specific as possible while capturing the intended scope. For example, cite NCR for the SWIM architecture element rather than citing SWIM. For dependencies on systems outside the boundaries of the architecture, capture the interaction dependencies in the associated IRD/ICD and included in Section 4.2, Functional Integration. |
| NOTES | Notes (Optional): Include any additional information that will clarify the content in the other VRTM columns. |

Table 8:VRTM

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **PARA\_ID** | **REQ\_ID** | **REQ\_TEXT** | **PHASE** | **PRD\_ID** | **TNRD\_ID** | **FAD\_ID** | **SOURCE** | **MOV** | **CPR** | **ALLOCATION** | **NOTES** |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |  |
