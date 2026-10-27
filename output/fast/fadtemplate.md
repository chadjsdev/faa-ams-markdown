---
title: "fadtemplate"
source_url: https://fast.faa.gov/docs/fadtemplate.docx
source_type: docx
converted: 2026-10-27
---
# fadtemplate

|  |  |
| --- | --- |
| ![Description: m](data:image/png;base64...) | ***Acquisition Management System Guidance*** |
|  |

**Functional Analysis Document Template**

For NAS and Mission Support AMS Acquisitions

Version 3.0, March 10, 2022

**Responsible Organizations:**

ANG-B1 NAS Enterprise Architecture & Requirements Services Division

*Or*

ADE-001 Office of Information & Technology, Solution Delivery Service

**Functional Analysis Document Template**

**General Information**

The Functional Analysis Document (FAD) template offers a structured format and guidance to assist programs going through the FAA’s Acquisition Management System (AMS) lifecycle in developing their FAD. This section serves to describe the functional analysis process and is for information purposes only. It is not expected for a program to include this section in their FAD. This FAD template replaces previous versions of the template referred to in the AMS guidelines as the Functional Analysis Template (FAT). The FAD can be used to satisfy the program level architecture artifact requirement referred to as the Systems Functionality Description (SV-4) based upon prior coordination with the NAS Enterprise Architecture & Requirements Services Division (ANG-B1). According to the AMS, a FAD is initially required for programs during their Concept & Requirement Definition (CRD) phase if there is new functionality being proposed. The FAD is then matured and updated during the Initial Investment Analysis (IIA) and Final Investment Analysis (FIA) phases. A FAD is not required for programs where no new functionalities are being introduced, such as a Tech Refresh program. However, programs are required to verify that the functions in their existing FAD are still valid during CRD along with other architecture artifacts. Any tailoring or modification of FAD development must be coordinated with ANG-B1 prior to the start of a particular investment phase.

The FAD documents the system functional architecture, which is derived from an operational analysis of the enterprise. In order to be effective, the FAD documents the operational analysis and the subsequent system functional analysis. The operational analysis consists of two parts:

* **Business Process analysis:** the set of tasks and techniques used to understand, study, and assess how an organization operates to achieve its goals and deliver value to its stakeholders.It begins by understanding how the organization works from an operational perspective – identifying the business processes that fulfill the operational activities of the organization and analyzing those processes to understand the people and activities or tasks needed to perform them well. Business Process Models (BPM) document the operational analysis and are developed by programs in collaboration with ANG-B1 in the Service Analysis and Strategic Planning (SASP) and CRD phases and subsequently are incorporated into the Shortfall Analysis Report (SAR) and the Solution Concept of Operations (ConOps) so that the operational analysis can form the basis for identifying shortfalls and proposed concept changes. The SAR focuses on incorporating the “As-Is” business processes in order to provide a platform for identifying shortfalls. Operational analysis should be completed before initiating the system functional analysis, and the operational analysis should be incorporated into the FAD as the basis for doing the program level system functional analysis.
* **Data analysis:** the set of tasks and techniques used to understand data requirements and the data elements necessary to satisfy those requirements. This analysis, as modeled in conjunction with the BPMs, defines where data originates, and where it is stored or replicated since its origination, including all interim processing (transforms and enrichments). Data analysis is conducted in tandem with the operational analysis and the results of both analyses can be refined and expanded as a program matures through its AMS lifecycle. Data analysis should be completed before initiating the system functional analysis, and the data analysis should be incorporated into the FAD as the basis for doing the program level system functional analysis.

Together, the results of the operational and data analyses are linked to the Operational Activities Hierarchy (OV-5H) and the Logical Data Model (OV-7) and assists in helping to understand the alignment of the program’s proposed solution to the NAS Enterprise Architecture.

**System Functional analysis:** the set of tasks and techniques used to identify the system functions required to support the efficient implementation of the business processes identified in the operational analysis. The system functional analysis is the major focus of the FAD and is covered explicitly in sections 3.0 and 4.0 of the FAD. System functional analysis leverages the results from the previously initiated business and data analysis.

The FAD addresses the needs and shortfalls of the organization by documenting the system functions that support existing, and new operational concepts and business processes. For programs going through the AMS, it draws input from the SAR, the ConOps, and the Business Process Models (BPM). Additional input sources include functions and requirements allocated to the program by the NAS Enterprise Architecture and the Target NAS Requirements Document (TNRD). The FAD serves as the foundation for the development of the Program Requirements Document (PRD). The PRD defines the functional, performance, and data requirements, which the investment program must implement. The FAD, which contains the Business Process and the System Functional analyses, also serves as a primary input to the development of other parts of the program architecture, enterprise-level artifacts, and the Operational Safety Assessment (OSA), as well as indirect input into the Comparative Safety Assessment (CSA), and the Preliminary Hazard Analysis (PHA). It is therefore crucial that the FAD accurately represent the full set of business functions and processes, system functions, and data that are envisioned in the operational concept.

Operational analysis begins in Service Analysis & Strategy Planning phase with the “As-Is” business and data analysis. The “As-Is” business and data analysis will be used to facilitate the development of the preliminary shortfalls and is documented in the SAR. A “To-Be” business and data analysis must be developed either prior to starting the CRD phase or early in the CRD phase, before starting the system functional analysis. Both the “As-Is” and the “To-Be” business and data analyses are documented in the ConOps. Since the “To-Be” business and data analysis are the starting point for determining the business process functions that involve the system, they are recommended to be included in the FAD. ANG-B highly recommends that a reasonably complete final draft of the ConOps be completed, before proceeding with the system functional analysis. Additionally, it is expected that the SAR is complete before starting the FAD. It is also crucial that programs engage with ANG-B prior to starting their analyses as it will shorten the development time and facilitate the approval process for the FAD.

System functional analysis begins by analyzing the “To-Be” activities (business process steps) and identifying which process steps will be performed by a system in support of any activity. Each system function will then be transformed into a functional requirement, which is then inserted into section 3.1 of the Preliminary Program Requirements Document (pPRD).

During Initial Investment Analysis (IIA), the FAD is refined and updated with additional detail some of which is derived from the alternative analysis. The associated Functional Flow Block Diagrams (FFBD) and N-squared (N2) diagrams will be developed for these additional levels of function. Each new function will be used to derive functional requirements for section 3.1 of the Initial Program Requirements Document (iPRD). Prior to the development of the Final Program Requirements Document (fPRD), each program re-examines the FAD and updates it, if necessary.

Each system function in the FAD must be traceable to one or more activities in the BPMs, as well as being aligned with the enterprise level functions. The individual activities may in turn be associated with one or more BPM processes. As each system function in the FAD is transformed into a functional requirement, it must be appropriately stated as a “shall/must” statement in section 3.1 of the PRD during the requirements development phase of a program. Multiple functional requirements may be needed to fully describe the implementation of a system function.

When developing the FAD, special consideration will be given to multi-segmented programs that structure their investments into discrete and sequenced series of work packages (WP), each of which follow the AMS lifecycle phases. Often programs structure their procurement investments in multiple work packages for business case, logistics or cost reasons, rather than out of pure technical necessity. However, the capabilities being proposed across multiple work packages may functionally be part of a single integrated solution. The program team should also consider developing a single functional architecture for their solution, using the previous FAD and PRDs as baseline sources. This single functional architecture can be documented in a FAD that can be expanded and updated both for each phase within a segment and for subsequent segments of the program. Only the relevant areas of the functional architecture pertaining to a particular work package need to be fully completed at any one time. There are some significant advantages to this method. First, having a single baseline FAD helps to consolidate a program’s functional architecture into a single artifact, including the full set of capabilities envisioned across the multiple phases. Second, having a single consolidated FAD ensures that other dependent systems engineering artifacts, such as the requirement documents and architecture products can also continue to evolve as single integrated artifacts reflecting the full set of capabilities. Third, having a single baseline FAD avoids the need for the program manager, systems engineers, and vendors accessing multiple documents to get a full understanding of a program’s capabilities across multiple phases.

The FAD serves the needs of both NAS and Mission Support programs. To accommodate process and semantic differences between the two types of programs, NAS/Mission Support differences are highlighted where appropriate. The sponsoring NAS program office initiates FA with the support of the National Airspace System (NAS) Enterprise Architecture and Requirements Services Division (ANG-B1) during the Service Analysis phase of the Acquisition Management System (AMS) lifecycle. The sponsoring Mission Support program office initiates FAD development with the Office of Information & Technology, Solution Delivery Service, Enterprise Architecture and Portfolio Insight (ADE-200) during the Concept and Requirements Development (CRD) phase of the Acquisition Management System (AMS) lifecycle. The development of the business process analysis section of the FAD must comply with *FAA Business Process Model (BPM) Guidance Document, version 13*. The development of the data analysis section of the FAD must comply with *FAA Data Analysis Guidance Document, version 3.0.* Please contact ANG-B1 for referenced documents.

The system functional analysis sections of the FAD must comply with the preferred diagramming techniques as documented in Section 3.2 of the FAA Systems Engineering Manual (SEM), version 2.0. The FAA SEM is located on the [Systems Engineering Portal](https://sep.faa.gov/) and can be directly accessed there. To facilitate development of the FAD, ANG-B1 and ADE-001 highly recommend using a software tool to help with FA, although usage of a tool is not mandatory. This template provides the general structure on producing the FAD; the program office representatives may consult with either ANG-B1 or ADE-001 for tailoring the FAD to suit their particular investment program, and to obtain access to available software tools.

![](data:image/x-wmf;base64...)

**Functional Analysis Document**

[Enter name of AMS investment program]

[Enter name of AMS decision type]

Version *(#)*

**Approved:**

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date:\_\_\_\_\_\_\_\_\_\_\_\_\_

Director, Service Organization with Need

*(For NAS and Mission Support initiatives)*

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date:\_\_\_\_\_\_\_\_\_\_\_\_\_

Manager, NAS Enterprise Architecture & Requirements Services Division, ANG-B1

*(For NAS initiatives)*

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date:\_\_\_\_\_\_\_\_\_\_\_\_\_

Director, Office of Information & Technology, Solution Delivery Service, ADE-001

*(For Mission Support initiatives)*

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date:\_\_\_\_\_\_\_\_\_\_\_\_\_

Manager, Service Organization with Need

*(For NAS and Mission Support initiatives)*

**Federal Aviation Administration**

**800 Independence Avenue SW**

**Washington, DC 20591**

**Table of Contents**

Contents

[1.0 Introduction 8](#_Toc97651188)

[1.1 Summary of the Solution Concept of Operations 8](#_Toc97651189)

[1.2 Boundary Systems and Stakeholders 8](#_Toc97651190)

[1.3 Operational Environment 9](#_Toc97651191)

[1.4 Time Frame 9](#_Toc97651192)

[2.0 Business Process Analysis Results 9](#_Toc97651193)

[2.1 “To-Be” Business Process Analysis 9](#_Toc97651194)

[2.2 “To-Be” Data Analysis 9](#_Toc97651195)

[3.0 System Functional Analysis 11](#_Toc97651196)

[3.1 High Level Context Diagram 11](#_Toc97651197)

[3.2 System Functional Hierarchy 11](#_Toc97651198)

[3.3 Functional Behavior Model – FFBD 12](#_Toc97651199)

[3.4 Functional Behavior Model – N2 Diagram 12](#_Toc97651200)

[4.0 Systems Engineering Traceability 13](#_Toc97651201)

[5.0 References 14](#_Toc97651202)

[6.0 Acronyms 14](#_Toc97651203)

[7.0 Lexicon 14](#_Toc97651204)

[8.0 Acronyms 15](#_Toc97651205)

# 1.0 Introduction

## 1.1 Summary of the Solution Concept of Operations

*[This section summarizes all the proposed operations described in the program’s Level 4 Solution Concept of Operations (ConOps) Document (section 4.4), and how those operations fit within the NAS or the Mission Support operations. This section focuses on the key functional capabilities identified in the ConOps. A full copy of section 4.4 from the Solution ConOps may be used to describe the specific functionality of the program. For guidance on the different types of ConOps, refer to the FAA Solution Concept of Operations Document Template, version 1.0.*

*For NAS initiatives this section should identify any Operational Improvements (OIs), Business Technology Initiative (BTI), increment(s), and increment description for the service along with their associated identifier numbers. List them in tabular form.]*

*Note: OIs and increments are identified in the Concept of Operations (ConOps) as programs describe the set of capabilities which will result in operational improvements or achieve desired objectives for a proposed solution. OIs and increments are aligned to the BPMs, which are further decomposed into functions. The functions from the proposed system are later documented in the Functional Analysis Document (FAD).*

## 1.2 Boundary Systems and Stakeholders

*[This section identifies the external systems and stakeholders covered within the domain of this functional analysis. During the CRD phase, this section may only contain preliminary information on external systems and stakeholders in this version of the FAD. As a program progresses through IIA, identify proposed system and stakeholder alternatives. As the system progresses through FIA, identify the final selected systems and stakeholders.*

*If possible, depict the boundary systems and stakeholders using a graphical format. Additionally, provide a textual description of the external systems, stakeholders, and the expected high-level data elements impacted by the new functionality. Identify the boundary systems for the same time period the target program is expected to be in service. These could include FAA stakeholders as well as other external stakeholders (i.e. pilots, maintenance staff, and airlines). The identified external boundary systems, stakeholders, and high-level data elements must be consistent with the Solution ConOps.]*

## 1.3 Operational Environment

*[This section describes the environment in which the program will be operating. This includes operating conditions, environmental factors, human interactions, and restrictions. Include operational changes that accommodate the program capabilities to be achievable. The identified operational environment must be consistent with the Solution Concept of Operations, specifically, section 4.3.]*

## 1.4 Time Frame

*[This section describes the developmental time frame for which the operations and functions described in the FAD apply, including mapping to the appropriate Infrastructure Roadmap. If there are new functionalities or services that are to be introduced during the life cycle that impact the planned functions, identify and record the planned implementation dates. Highlight any dependencies on planned implementation of new or updated systems and functions. The identified time frame must be consistent with time frame identified in the Solution ConOps.]*

# 2.0 Business Process Analysis Results

## 2.1 “To-Be” Business Process Analysis

*[Starting with operational analysis ensures that existing business processes are supported by the new acquisition and changes to those processes are fully understood and supported by the new functional architecture. This section contains the full set of “To-Be” BPM process models that are directly applicable to a program. Additionally, identify specific automated BPM processes and activities that will need to be allocated to the functional architecture for system implementation within the scope of this FAD. BPM activities establish traceability to the enterprise OV-5H Operational Activities Hierarchy which helps build the enterprise data architecture. Refer to the FAA Business Process Model (BPM) Guidance Document.]*

## 2.2 “To-Be” Data Analysis

*[This section documents the results of the “To-Be” data analysis associated with the process models. The inputs and outputs (data elements) from the BPM processes that are directly allocated to system implementation within the scope of this FAD are identified in this section. Programs may use the NAS Enterprise Architecture OV-3/SV-6 template to document the data analysis. Refer to the FAA* Data Analysis *Guidance Document for instructions on how to implement this allocation. Coordinate and review the “To-Be” data analysis with the apropriate SCoPs for Enterprise Information Management (EIM) alignment.]*

# 3.0 System Functional Analysis

*[Section 3.0 and its sub-sections document the primary results of the system functional analysis portion of the functional architecture. System functional analysis consists of five major parts:*

1. *Context diagram*
2. *Hierarchy of system functions*
3. *FFBD*
4. *N2 interfaces diagram*
5. *Lexicon*

*The context diagram, hierarchy of system functions, FFBD, and N2 diagrams are documented in sections 3.1 – 3.4 of the FAD. The Lexicon is documented in section 7.0 of the FAD. Section 3.0 does not require any text, but programs may include optional introductory information.]*

## 3.1 High Level Context Diagram

*[This section shows a diagram of the highest-level system function that defines the program. This diagram consists of a single high-level system function representing the new functional capabilities identified in the ConOps. This high-level system function is an abstraction to represent all the lower level set of system functions and data elements needed to enable the high-level system function. In addition to this high-level system function relevant to the program, the context diagram must identify external systems functions that are part of the functional architecture being developed, as described in section 1.2 – Boundary Systems and Stakeholders. Show the high-level data elements across the interfaces. Provide a textual description of the high-level functions and the high-level data elements shown. The high-level context diagram must be consistent with the one in the Solution ConOps.]*

## 3.2 System Functional Hierarchy

*[The system functional hierarchy is a parent-child representation of the system functions that implement a solution. The top level of the system functional hierarchy must start with the high-level system function from Section 3.1, and the resulting hierarchy must contain those system functions which map to and enable the implementation of the automated processes from the “To-Be” BPM functional hierarchy. There is a many-to-many relationship between the system functions and the automated processes. Identify each system function in the hierarchy with a unique identifier. The system functions identified during CRD phase must directly trace to the operations described in the program’s Solution ConOps and BPM diagrams.*

*During initial investment analysis, add or decompose sub-functions. Functional decomposition helps to define complex functions by identifying constituent sub-functions that are more readily understood and managed. This process is repeated until the functions are decomposed to adequately describe the architecture for a particular investment phase.*

*For Mission Support programs, the functions in the system functional hierarchy of this section must trace to the Business Reference Model (BRM). Document the traceability to the BRM in section 4.0.*

*ANG-B1 recommends that for CRD, the system functional hierarchy decompose to 4 or more levels, with increasing decomposition as the program progresses further along the AMS lifecycle. However, if your program is an enhancement or has been waived from IIA, then decompose the functional hierarchy as low as possible. This level of decomposition ensures enough detail to perform systems engineering analyses including safety analysis, cost estimation, and requirements development. ANG-B1 will provide feedback as to whether the level of decomposition is adequate and work with the program to come to a common agreement.]*

## 3.3 Functional Behavior Model – FFBD

*[This section describes how the system functions from the hierarchy in Section 3.2 perform the sequence of functions. Represent the sequence of functions using the Functional Flow Block Diagram (FFBD) method, which is described in detail in section 3.2 of the FAA Systems Engineering Manual. The FFBD displays functions at the lowest level of the system functional hierarchy. Segment the FFBD to reduce complexity and enhance readability.]*

## 3.4 Functional Behavior Model – N2 Diagram

*[This section describes the data elements that are transferred across the functional interfaces between each of the system functions in the FFBD at a specific hierarchy level. An N2 diagram must accompany each FFBD. Completely define the functional interfaces along with the interfaces to the environment and external systems. Represent the resulting functional interfaces description as a series of N2 diagrams. Associate an N2 diagram with each FFBD to fully capture the data elements as inputs and outputs for each function in an FFBD. Refer to section 3.2 of the FAA Systems Engineering Manual for more detail on developing the N2 diagram.]*

# 4.0 Systems Engineering Traceability

*[This section captures the traceability between the system functions and data elements and their associated source business activities and data objects. Capture the traceability of the system functions in Section 3.2 and data elements in Section 3.4 with the BPM activities and data object messages associated with the BPM processes documented in Section 2.0. Table 1 and 2 below may be used to document this traceability. Due to the use of various tools in developing the FAD, ANG-B1 is flexible in how this section is developed. To demonstrate traceability, programs may modify Table 1 and 2, or provide a tool-generated traceability matrix as an appendix. If a program chooses an alternate method of demonstrating traceability or needs to tailor traceability, it must be clearly explained in this section and coordinated with ANG-B1.]*

|  |  |  |  |
| --- | --- | --- | --- |
| ***System Function Identifier*** | ***System Function*** | ***BPM Activity ID*** | ***BPM Activity*** |
|  |  |  |  |
|  |  |  |  |

***Table 1: Traceability of system functions Matrix***

|  |  |  |  |
| --- | --- | --- | --- |
| ***Data Element Identifier*** | ***Data Element Name*** | ***BPM Activity Data Objects Message ID*** | ***BPM Activity Data Object Message*** |
|  |  |  |  |
|  |  |  |  |

***Table 2: Traceability of system data elements Matrix***

|  |  |  |  |
| --- | --- | --- | --- |
| ***Data Element Identifier*** | ***Data Element Name*** | ***BRM Reference Model ID*** | ***BRM Reference Model*** |
|  |  |  |  |
|  |  |  |  |

***Table 3: Traceability of system data elements Matrix (Mission Support)***

# 5.0 References

*[This section provides a listing of documentation used in the definition of the functions and information flows. It also identifies key organizations or Subject Matter Experts (SME) used to help formulate the functionality, flows, and data needs for the analysis. References include the ConOps, relevant architecture products, requirements products, specifications and standards that are driving the functional analysis.]*

# 6.0 Acronyms

*[This section provides a list of acronyms used in the FAD along with the terms they represent.]*

# 7.0 Lexicon

*[This section defines the various elements of the functional architecture contained within this FAD. The following items at a minimum must be defined****:***

1. *All functions contained in section 3.2*
2. *Input/output data elements between functions from the N2 diagram in Section 3.4*
3. *External system functions identified in the context diagram, section 3.1*
4. *Stakeholders identified in the context diagram, section 3.1*
5. *Data elements identified in the context diagram, section 3.1*

*Each definition must reference a source, which may include FAA standards or documents, program documentation, external standards, and subject matter expertise.*

*Due to the use of various tools in developing the FAD, ANG-B1 is flexible in how this section is developed. To facilitate the creation of a lexicon, the program may use different strategies to identify definitions. For instance, a separate appendix may be used to list all the required items that may have been gathered from a tool such as CORE. Alternatively, functions, systems, stakeholders, and data elements may be defined separately in their respective sections 3.1 – 3.4. If a program chooses an alternate method of documenting their lexicon, it must be clearly explained here.]*

# 8.0 Acronyms

|  |  |
| --- | --- |
| **Acronym** | **Term** |
| AMS | Acquisition Management System |
| BPM | Business Process Model |
| BRM | Business Reference Model |
| BTI | Business Technology Initiative |
| ConOps | Concept of Operations |
| CRD | Concept & Requirements Definition |
| CSA | Comparative Safety Assessment |
| EIM | Enterprise Information Management |
| FA | Functional Analysis |
| FAA | Federal Aviation Administration |
| FAD | Functional Analysis Document |
| FAT | Functional Analysis Template |
| FFBD | Functional Flow Block Diagrams |
| FIA | Final Investment Analysis |
| fPRD | Final Program Requirements Document |
| IIA | Initial Investment Analysis |
| iPRD | Initial Program Requirements Document |
| N2 | N-squared Diagrams |
| NAS | National Airspace System |
| OSA | Operational Safety Assessment |
| OV-5H | Operational View - Operational Activities Hierarchy |
| OV-7 | Operational View - Logical Data Model |
| PHA | Preliminary Hazard Analysis |
| pPRD | Preliminary Program Requirements Document |
| PRD | Program Requirements Document |
| SAR | Shortfall Analysis Report |
| SASP | Service Analysis and Strategic Planning |
| SEM | FAA Systems Engineering Manual |
| SME | Subject Matter Experts |
| SV-4 | System View - Systems Functionality Description |
| TNRD | Target NAS Requirements Document |
| WP | Work Packages |

#
