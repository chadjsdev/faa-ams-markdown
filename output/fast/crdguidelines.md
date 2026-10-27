---
title: "crdguidelines"
source_url: https://fast.faa.gov/docs/crdguidelines.docx
source_type: docx
converted: 2026-10-27
---
# crdguidelines

![FAA Logo](data:image/png;base64...)***Acquisition Management System Guidance***

**Guidelines for Service Analysis & Strategic Planning (SASP) and Concept & Requirements Definition (CRD)**

*For NextGen and Mission Support AMS Acquisitions*

*Version 9.0, March 10, 2022*

| **Document History**  **Date** | **Version** | **Change Description** | **Rationale** | **Author** |
| --- | --- | --- | --- | --- |
| August 2006 | 4.0 | Original | Acquisition Management System (AMS) early phase guidance needed |  |
| July 2012 | 5.0 | Rewritten to address agency changes and meet plain language requirements | Agency reorganization, policy and process changes | HT Parker, Jr. |
| June 2014 | 6.0 | Rewritten to address AMS changes & reflect reorganization into Shared Services IT. | “i2i” integrated into AMS, AIO reorganized in November 2013. |  |
| July 2017 | 7.0 | ANG Organizational changes  Inclusion of: Enterprise Information Management (EIM), Human Factors, JRC Checklist items, Information System Security (ISS), Testing and Evaluation Master Plan (TEMP), IP&A and Mission Support processes  Modifications to ConOps, Service Analysis & Strategic Planning processes sub-section (2.1), Functional Analysis, and Enterprise Architecture sub-sections  Updated support & approval organization signatures  Updates to AMS artifact template links  Changed Non-NAS to Mission Support | Agency reorganization, policy and process changes | M. Porter |
| April 2020 | 8.0 | Modified flowcharts and re-ordered several sections of the document to match changes. Added references to new ACAT categories of Technology Refresh Portfolios and Software Enhancements, updated Mission Support and National Airspace System Enterprise Architecture definitions to current approved versions, and added annual roadmap update process as an alternative to an Architecture Change Notice for adding a program to the Enterprise Architecture. Added references to business process modeling in Shortfall Analysis Report and Concept of Operations. Several types of administrative changes including updated links and organizational codes, verbiage and formatting fixes, and consistent use of acronyms. | Agency reorganization, policy and process changes | G. Key |
| March 10 | 9.0 | Updated Process Flowcharts (Figures 2 & 3): Reordered activity boxes to accurately reflect the order in which activities are conducted.  Included EIS Language:  Link updates, ACAT Designation Updates, and Refined Enterprise Architecture language. A |  | J. Asmat |

**Note:** Provisions of this document addressing new NAS initiatives may be waived. These guidelines will be updated to reflect any changes to AMS policy.

Table of Contents

[1.0 Introduction 6](#_Toc97580607)

[2.0 Service Analysis & Strategic Planning Process 8](#_Toc97580608)

[2.1 Gather Information on Service Environment; Analyze Service Shortfalls and Concepts, and Assess FAA Strategic & Performance Goals 10](#_Toc97580609)

[2.2 Prepare Preliminary Shortfall Analysis Report 10](#_Toc97580610)

[2.2.1 Introduction 11](#_Toc97580611)

[2.2.2 Assumptions 11](#_Toc97580612)

[2.2.3 Interdependencies 11](#_Toc97580613)

[2.2.4 Current Operational Capability (Legacy Case) 11](#_Toc97580614)

[2.2.5 Participating Organizations 11](#_Toc97580615)

[2.3 Safety Assessment 12](#_Toc97580616)

[2.4 Cloud Suitability Assessment 13](#_Toc97580617)

[2.5 Information System Security Risk Factors Assessment 14](#_Toc97580618)

[2.6 Does Shortfall Impact NAS? 15](#_Toc97580619)

[2.7 Complete NAS ConOps Change Development and Decomposition (NAS Only) 15](#_Toc97580620)

[2.7.1 Develop & Validate NAS ConOps Changes through Concept Maturity and Technology Development 16](#_Toc97580621)

[2.7.2 Document NAS ConOps Changes as OIs and OSs 17](#_Toc97580622)

[2.7.3 Develop Operational Capability Business Case 18](#_Toc97580623)

[2.7.4 Decompose NAS OIs and OSs (New Concepts Only) 18](#_Toc97580624)

[2.8 Prepare EA Change 19](#_Toc97580625)

[2.8.1 Assess Priority & Time Phasing 19](#_Toc97580626)

[2.9 Enterprise Architecture Endorsement 20](#_Toc97580627)

[2.10 Prepare the CRD Plan 21](#_Toc97580628)

[2.1 CRD Readiness Decision 22](#_Toc97580629)

[3.0 Concept and Requirements Definition Process 22](#_Toc97580630)

[3.1 Obtain ACAT Designation 24](#_Toc97580631)

[3.2 Finalize Shortfall Analysis 24](#_Toc97580632)

[3.3 Develop Solution ConOps 26](#_Toc97580633)

[3.4 Analyze Functions 28](#_Toc97580634)

[3.5 Perform Cloud Suitability Assessment 30](#_Toc97580635)

[3.6 Perform Preliminary Information System Security Assessment 30](#_Toc97580636)

[3.7 Assess Operational Safety (NAS Only) 31](#_Toc97580637)

[3.8 Develop Preliminary Requirements 32](#_Toc97580638)

[3.8.1 Program Requirements Management Tool (NAS Only) 33](#_Toc97580639)

[3.7.2 Consult with Specialty Engineering 34](#_Toc97580640)

[3.8.2.1 Human Factors (HF) 34](#_Toc97580641)

[3.8.2.2 Spectrum Impact 35](#_Toc97580642)

[3.9 Develop EA Products 35](#_Toc97580643)

[3.10 Identify and Develop Alternatives 36](#_Toc97580644)

[3.10.1 Define Alternatives 36](#_Toc97580645)

[3.10.2 Estimate Alternative Costs 37](#_Toc97580646)

[3.11 Verify and Validate Work Products 38](#_Toc97580647)

[3.12 Plan for Investment Analysis 39](#_Toc97580649)

[4 Investment Analysis Readiness Decision 40](#_Toc97580650)

[Appendix A – Acronyms 42](#_Toc97580651)

[Appendix B – Reference Documents and Associated Links 45](#_Toc97580652)

[Appendix C – JRC Readiness Criteria and Checklists 47](#_Toc97580653)

**List of Tables and Figures**

[Figure 1: AMS Lifecycle Management Process 6](#_Toc97579562)

[Figure 2: Service Analysis & Strategic Planning Process Flowchart 9](#_Toc97579563)

[Figure 3: Concept and Requirements Definition Process Flowchart 23](#_Toc97579564)

**Tables**

Table 1: Shortfall Analysis Report (Preliminary) Participating Organizations

Table 2: Information System Security (ISS) Risk Factors Assessment Participating Organizations

Table 3: NAS ConOps Change Participating Organizations

Table 4: Operational Capability Business Case Participating Organizations

Table 5: NAS OIs, BTIs and Increments Decomposition Participating Organizations

Table 6: EA Change Participating Organizations

Table 7: EA Endorsement Participating Organizations

Table 8: Concept and Requirements Definition Plan Participating Organizations

Table 9: ACAT Determination Participating Organizations

Table 10: Shortfall Analysis Report (Final) Participating Organizations

Table 11: Solution ConOps Participating Organizations

Table 12: Functional Analysis Document Participating Organizations

Table 13: Information System Security Participating Organizations

Table 14: Safety Assessment Participating Organizations

Table 15: Preliminary Program Requirements Participating Organizations

Table 16: NAS Program Requirements DOORS Module Participating Organizations

Table 17: Spectrum Impact Determination Participating Organizations

Table 18: Enterprise Architecture Products Participating Organizations

Table 19: Preliminary Alternative Descriptions Participating Organizations

Table 20: Estimate Costs Participating Organizations

Table 21: Verification and Validation Participating Organizations

Table 22: Investment Analysis Plan Participating Organizations

# 1.0 Introduction

This document provides guidance for completing the Service Analysis & Strategic Planning (SASP) and Concept & Requirements Definition (CRD) phases of the FAA Acquisition Management System (AMS), leading to two decisions: the CRD Readiness Decision (CRDRD) and Investment Analysis Readiness Decision (IARD).

AMS is a mature policy with clearly defined processes that address the unique needs of the agency and provide for timely and cost-effective acquisition of equipment, materials, and services. Further information on acquisition management policy is available on-line via the FAA Acquisition System Toolset [(FAST)](http://fast.faa.gov/).

The first steps of AMS are to develop products for the SASP and CRD phases. After each section, a product/process table identifies the product, supporting organizations and approval authorities necessary for completing the SASP and CRD activities. Appendix B provides links to reference documents and products described in the sections below. The sequential AMS phases and decision points are shown in Figure 1.

![FAA Lifecycle Management Process ](data:image/png;base64...)

Figure 1: AMS Lifecycle Management Process

The mission environment of the FAA is continuously monitored for (1) changes and trends influencing demand for services, (2) the agency’s capacity to provide services, and (3) technological opportunities offering the potential for improving safety, lowering costs, or improving efficiency and effectiveness. This forward-looking activity is referred to as Service Analysis and Strategic Planning.

SASP is the evaluation of how well FAA legacy assets satisfy existing needs and emerging demands for new services. Program offices within FAA Lines of Business (LOBs) and Staff Offices use this phase to identify and prioritize service-level shortfalls and opportunities, which are then linked to strategic goals along with the appropriate enterprise architecture roadmap. Additionally, SASP enables the Next Generation Air Transportation System (NextGen) organization, with input from all FAA LOBs and Staff Offices, to manage a single point of entry for inclusion of new ideas, concepts, or operational capabilities (OCs) into the National Airspace System (NAS) Concept of Operations (ConOps).

Operational Improvements (OIs) that represent new and better ways to manage air traffic and other FAA services; or OCs that group OIs and BTIs to achieve a desired operational outcome and benefit. This foundation enables OIs and BTIs to be collectively evaluated within an enterprise context, with heavy involvement from all participants in the process.

The SASP phase concludes upon FAA Enterprise Architecture Board (FEAB) approval of the CRDRD. The output of the SASP phase provides the foundation, structure, and content for the products created in the CRD phase of AMS. The CRD phase is a multi-step process that helps service organizations (e.g., service teams and program offices, etc.) perform and document the required analyses needed for an IARD. CRD products ensure a shortfall or service gap is adequately defined, functional and performance requirements are defined, technology is mature, and safe, secure, and viable alternative solutions are described.

Operational Improvements (OIs) are divided into operational increments, which are incremental operational changes to the NAS. FAA updates all OIs and operational increments annually. These updates reflect the latest research results and developments. Furthermore, the impact of readiness and feasibility assessments, further analyses, and acquisition decisions may also result in changes to the OIs or increments. OI’s and increments may be deleted, combined, or split.

OIs and Increments should be identified in the Shortfall Analysis Report as programs need to describe how the needed services enable the operational improvements. A portion of an operational improvement that delivers incremental benefits is found in an increment and can be expressed as a shortfall.

OIs and Increments should also be identified in the Concept of Operations (ConOps) as programs describe the set of capabilities which will result in operational improvements or achieve desired objectives for a proposed solution. OIs and increments are aligned to the BPMs, which are further decomposed into functions. The functions from the proposed system are later documented in the Functional Analysis Document (FAD). OIs, increments, and shortfalls drive the need to address requirements in the PRD. The PRD should identify those OIs, increments, and shortfalls for the investment program. The investment program should identify one or more CPRs in relation to the identified OIs, increments, and shortfalls.

The CRD phase concludes upon Joint Resources Council (JRC) approval of the IARD.

The primary sources of support and coordination for initiatives going through SASP and CRD phases of AMS are, but are not limited to, the following:

1. NAS Systems Engineering & Integration Office (ANG-B13) provides guidance, oversight, and coordination for NAS initiatives.
2. FAA Office of Information & Technology, Solution Delivery Service, Enterprise Architecture and Portfolio Insight (ADE-200) provides guidance, oversight, and coordination for Mission Support (MS) initiatives.
3. AMS Stakeholders ([Point of Contact list)](https://ksn2.faa.gov/afn/jrcportal/Shared%20Documents/Stakeholder%20Contact%20Info.pdf) meet on a bi-weekly basis to discuss progress on candidate programs seeking investment decisions or direction (i.e. Strategy Discussions) from the JRC. The JRC Executive Secretariat (AAP-200) manages the meeting.
4. Communities of Interest (COI) and Stewardship Communities of Practice (SCOP) function as the focal point for identifying and providing enterprise asset management for the integrated data of a distinct set of business activities that produce a unique set of information products and services.

# 2.0 Service Analysis & Strategic Planning Process

Figure 2 shows the primary elements of the SASP phase that new initiatives must complete. This is the recurring analysis from which service organizations determine and prioritize service shortfalls and opportunities over time. The results of this analysis are used to propose modifications to agency strategic planning documents. In the following sections, key components of SASP are described in more detail.

![](data:image/jpeg;base64...)

Figure 2: Service Analysis & Strategic Planning Process Flowchart

# 2.1 Gather Information on Service Environment; Analyze Service Shortfalls and Concepts, and Assess FAA Strategic & Performance Goals

The service organizations consider all initiatives that are necessary and sufficient to deliver targeted business outcomes (i.e., Agency strategic goals). Using a service-level approach, issues within the operational, business, data and information, technology, organizational, process, and people (including human factors) areas that might affect delivery of targeted business outcomes are identified.

The needs identified in the FAA operational environment usually represent service shortfalls associated with Enterprise information management and agency goals and objectives. There are various sources of data to support shortfall findings based on identified operational issues and trends in maintainability, supportability, reliability, availability, and capacity (e.g., software, etc.).

As LOBs evaluate environmental and operational data, the service capability that can be provided by existing and programmed assets is compared against projected demand to determine service shortfalls.

There are many types of shortfalls that should be considered, such as missing functionality, deficient business process, data coming from a source that is not a trusted source (authoritative or approved replicated sources), data availability or data accuracy, and security shortfalls.

A method for identifying shortfalls is the use of business process modeling. The results of the business process and data analyses support the development of the solution ConOps and system analysis performed in the CRD phase.

In addition, it will be necessary to obtain information on new technologies and methodologies that might change the way services are provided in the future. These new NAS technologies, ideas, or concepts are vetted through the NAS ConOps Change Development and Decomposition process presented in section 2.7.

# 2.2 Prepare Preliminary Shortfall Analysis Report

Shortfall analysis includes a description of the problem or technological opportunity, its nature, urgency, and impact. The preliminary and final shortfall analysis are documented in the Shortfall Analysis Report (SAR). In this step, the focus is in the preparation of the preliminary shortfall analysis. Refer to the [Shortfall Analysis Report](http://fast.faa.gov/docs/ShortfallAnalysisReportGuide.doc) for more information.

Brief descriptions of the key sections of the SAR are described below:

## 2.2.1 Introduction

Briefly describe the shortfall in easy to understand language using FAA Plain Language guidance. When writing the shortfall statement, describe the capability gap using a single sentence or a short paragraph that:

1. Characterizes the current operational asset’s behavior.
2. Describes its impact on service delivery and how it is changing over time.
3. Specifies the timeframe when service delivery will become untenable.

## 2.2.2 Assumptions

A critical step in shortfall analysis is explicitly articulating all assumptions. The assumptions section lists and fully defines all specific statements that are used as a basis to create the shortfall analysis. Assumptions represent a set of judgments about past, present and/or future conditions postulated as true in the absence of absolute proof. Categories of assumptions that are used in most shortfall analysis reports include: concept of operations/use, functions, capabilities, schedule, cost limitations, high-level time phasing, analysis period, economic service life. Each assumption includes detailed explanations and/or justifications for its basis, including data, sources, and methodology. Cite references and/or source materials used to create the assumptions.

## 2.2.3 Interdependencies

Identify other programs affected by this initiative and whether it is affected by, or dependent on, other programs. State whether the shortfall under consideration is being addressed, in whole or in part, by other FAA initiatives. Identify planned future initiatives that may replace the legacy capability completely or in part.

## 2.2.4 Current Operational Capability (Legacy Case)

Describe the shortfall from the perspective of the current operational asset's capability. The Legacy Case provides a common, consistent basis against which comparisons can be made to measure performance improvements resulting from the investment. It includes assets, systems, data, facilities, people, and processes relevant to the initiative; it may also include funded assets awaiting future delivery. The Legacy Case does not include capabilities beyond what is already in an acquisition program baseline. Include in this section the As-Is business process models used to identify the shortfalls.

## 2.2.5 Participating Organizations

List the individuals and their organizations that are a part of the shortfall analysis team and describe their roles.

**Table 1: Shortfall Analysis Report (Preliminary) Participating Organizations**

| **PRODUCT** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| Shortfall Analysis Report (Preliminary) | **NAS:** ANG-B1, ANG-B2, ANG-B3, ANG-B7, ANG-E5A, ANG-C1, ANG-C5, ANG-B13, AJW-13, AJI-2210, AJI-2300, AJV-S, AJW-1X, AFI, AJM-2 | **NAS:** Director, Service Organization; Director, Operational Concepts, Validation, and Requirements for ATO-related programs (AJV-S); and Director NAS Systems Engineering & Integration Office (ANG-B) |
| **MISSION SUPPORT:** ADE-200, AFI, AVS | **MISSION SUPPORT:** Director, Service Organization with Need; Director, Office of Information & Technology, Solution Delivery Service (ADE-001) |

# 2.3 Safety Assessment

The safety assessment may provide a new concept or program with as much information as possible on the potential hazards that may be faced as well as identify any potential hazards or operational concerns that would prevent its deployment and lead to wasted resources.

A safety collaboration group will conduct this assessment. This group will be composed of safety stakeholders representing organizations such as NextGen, ATO Safety and Technical Training (AJI), Aviation Safety (AVS), Program Management Organization (AJM), FAA Airports (ARP), Commercial Space Transportation (AST), Technical Operations (AJW), and various service units.

It is recommended to start exploring potential safety hazards related to the proposed concept at the early phase of the program. The Integrated System Safety Assessment (ISSA) will be triggered by a new concept entering AMS, a request from a program to perform an ISSA, or an update of any number of activities including but not limited to:

1. NAS ConOps changes.
2. NAS Enterprise Requirements Document changes.
3. NAS-Requirements Document changes.
4. NAS Enterprise Architecture (EA) changes (NAS SV-1, Functional Analysis Document (FAD), and OV-6).
5. NAS Segment Implementation Plan (NSIP) changes.
6. Operational Capability Integration Plan changes.

The key question in this assessment is “How does this idea/change affect the safety of the NAS?” The ISSA team will assess the concept across vertical, horizontal, and temporal planes. The vertical plane is hierarchical, providing connections from specific projects up to the NAS-level system of systems. The horizontal plane spans organizations, programs, and systems. Finally, the temporal plane attempts to eliminate safety gaps across program and system implementation timelines.

In addition to identifying safety issues, the ISSA team will also identify potential interaction hazards, human performance hazards, and provide a picture of safety issues that can then be used to influence change through the program-level safety assessments. The assessment may also provide feedback to higher-level planning documents (i.e., the NSIP).

During this stage, the ISSA may require updates as the OC is developed. The ISSA serves as an important reference for identifying potential safety hazards associated with proposed concept at this stage. The ISSA, conducted on the related OCs, should be evaluated, and used as basis for the future Safety Risk Management (SRM) efforts as the program progresses through the AMS.

An ISSA team should be convened to assess higher level abstractions of the idea under development such as its OI, OS, or OC. Depending on available information, this ISSA will use various data sources as inputs, such as the NAS ConOps, EA, NSIP, roadmaps, human performance hazard assessments, case studies, capability and concept level safety assessments, system-wide and capability-specific risk modeling efforts, prototypes, and flight trial data.

# 2.4 Cloud Suitability Assessment

At each AMS decision point there is a requirement to assess FAA Cloud Services (FCS) implementation suitability and document the results. The output from the FCS Suitability Assessment Process is an input for the Engineering Infrastructure Services (EIS) Assessment that is presented to the Architecture Review Board (ARB) or Technical Review Board (TRB). Enterprise Services Infrastructure Framework (ESIF) analysis may be performed to inform the cloud suitability assessment. Re-assessments are an inherent part of the Acquisition and Lifecycle Management Framework as an investment moves from one AMS decision point to a subsequent one.

# 2.5 Information System Security Risk Factors Assessment

During the SASP, the service organization must perform an Information Security Risk Factors assessment of the prospective capability to determine: (1) the provisional security category, i.e. a provisional ranking of the damage that would result if the confidentiality, integrity or availability of the information capability is lost, and (2) characterization of the capability security threat profile, i.e. the unauthorized persons or entities with the motivation, means, and opportunity to access and misuse the capability.

The results of the assessment will be used as input to the Cloud Suitability Assessment of the prospective capability and also will give the FAA Enterprise Architecture Board (FEAB) an early indication of the capability security needs. Service organizations assess the investment initiative to determine the provisional investment initiative security category (i.e., a provisional ranking of the damage that would result if the confidentiality, integrity, or availability of the information capability is lost).

The proposed security concepts should be evaluated against the following criteria:

1. Will the new capability create a condition where data will be shared between NAS and Mission Support entities, or between NAS and outside entities?
2. Will the new capability in any way handle or store privacy data? (i.e., names, addresses, social security numbers or any other form of Personally Identifiable Information (PII))

If either of these conditions are met, a cross-organizational security team will be organized to ensure that the concept is fully analyzed for compliance with relevant agency orders at all stages of development.

**Table 2: Information System Security (ISS) Risk Factors Assessment Participating Organizations**

| **PRODUCT** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| Information System Security (ISS) Risk Factors Assessment | **NAS:** AIS 200, AJW-B420, ANG-B31, Program Management Organization PMO / Communications, Information & Network Programs (CINP) | **NAS: NAS Authorizing Official Designated Representative (AODR)** |
| **MISSION SUPPORT:** AIS-100, AIS-200, ANG-B31, PMO CINP | **MISSION SUPPORT:** Organization Representative |

# 2.6 Does Shortfall Impact NAS?

Service needs and shortfalls must be assessed to determine whether they merit inclusion in the FAA EA when evaluated against other service needs of the agency and whether they should be aligned to the Mission Support Architecture or NAS Architecture component. The FEAB conducts this initial assessment. JRC approved definitions of FAA EA components are as follows:

**FAA Enterprise Architecture**: The FAA EA is an integrated view of the programs, assets, services and governance of the enterprise in its current and future state, and the transition strategy from the present to the future. Its scope includes FAA capital and operational assets, services, and other elements as defined by Office of Management and Budget (OMB) publication.

**Mission Support Architecture**: The operational and technical framework for the subset of enterprise assets exclusive of the FAA NAS. Includes mission support systems with a primary function other than NAS. The Mission Support Architecture represents current and future systems, as well as the transition strategy for moving from the current to the future state. Complementary and responsive to requirements of the NAS Architecture, with a planning emphasis on efficiency and reuse. The Mission Support Architecture emphasizes FAA use of commodity services, off-the-shelf engineering solutions, and industry best practices.

**NAS Architecture**: The operational and technical framework for the subset of enterprise assets directly associated with FAA NAS, as well as other systems and services on which NAS dependencies will be documented for planning and management purposes. The NAS Architecture represents services and functions that directly support safe Air Traffic Operations and Air Traffic Management. It represents current and future systems, as well as the transition strategy for moving from the current to the future state. The NAS Architecture maximizes FAA responsiveness to mission requirements with efficiency.

# 2.7 Complete NAS ConOps Change Development and Decomposition (NAS Only)

All new NAS initiatives must also complete a sequence of activities referred to as the NAS ConOps Change Development and Decomposition process. The NAS ConOps describes the vision for NAS modernization and serves as a principal input to identify and develop operational and performance requirements for supporting systems and services.

Concept ideas are generated from multiple sources internal and external to the FAA, such as FAA research partners and the aviation industry. This standard process for organizing and vetting concepts avoids duplication and ensures only the best new approaches are pursued. The process also encourages communication, enterprise-wide participation, and coordination across all FAA LOBs.

The Concept Steering Group (CSG) performs the role of coordination as described in the CSG Standard Operating Procedures (including membership). The CSG, by way of the Concept Steering Work Group (CSWG), facilitates communication and collaboration across the LOBs to assess the operational validity and technical feasibility of prospective concepts and their relationship to agency objectives. The CSG recommends whether a proposed concept to address a NAS service shortfall should be included within the NAS ConOps.

The NAS Enterprise Planning & Analysis Division, NAS Planning Branch (ANG-B22) is responsible for establishing new OCs (if needed), decomposing OCs into OIs or BTIs, and decomposing OIs into NAS enterprise requirements and investment increments. New shortfalls or concepts that are already within the scope of the NAS ConOps move to decomposition into NAS enterprise requirements after determining whether they should be incorporated into a new or existing OCs (Section 2.7.4 – Decompose NAS OIs, BTI, and Increments The service organization with the shortfall must coordinate with the Technology Development and Prototyping Division (ANG-C5) to confirm whether the concept is covered in the NAS ConOps and with the Enterprise Safety and Information Security Division (ANG-B3) to confirm that there are no adverse safety or security implications. Information regarding the process for establishing safety issues is discussed in section 2.3.

Most initiatives within the NAS ConOps are included on an FAA EA Roadmap — inclusion must be validated by the TRB. If the shortfall or service need is not in an EA Roadmap, the service organization must develop an Architecture Change Notice (ACN) and seek approval from the FEAB before proceeding to the CRD phase (section 2.9). New concepts or ideas not reflected in the scope of the NAS ConOps proceed to section 2.7.1 and undergo development and validation activities as necessary.

## 2.7.1 Develop & Validate NAS ConOps Changes through Concept Maturity and Technology Development

As noted above, proposed concepts are assessed by the CSWG within the context of the NAS ConOps and associated initiatives. The service organization or concept sponsor completes and submits a Concept Assessment Request containing an overview of the proposed concept and the activities required for maturation to the CSWG chair. Additionally, the service organization or concept sponsor submits any anticipated changes to the NAS along with documentation that supports the development of the concept (e.g., NAS enterprise requirements, test reports, benefits, and safety analyses, etc.).

The CSWG chair compiles the information for assessment by the work group and works with the service organization or concept sponsor to obtain any additional information needed to determine operational validity and technical feasibility of the proposed concept.

The operational validity of the proposed concept is determined by whether the concept fits within the vision of the NAS ConOps. The [Concept Maturity and Technology Development (CMTD)](https://employees.faa.gov/org/staffoffices/ang/development/csg/) process is used to assess the technical, operational, strategic, and economic feasibility of the concept. Detailed [CMTD Guidelines](https://employees.faa.gov/org/staffoffices/ang/development/csg/media/pdf/CSG%20SOP%20%2803-28-2013%29.pdf) are available on the [FAST website](http://fast.faa.gov/AMS_Policy.cfm). Assessment and validation activity will also include a safety and security assessment to determine potential safety and security issues that may result from the proposed concept.

When requirements or technology are not sufficiently mature to proceed further in the AMS lifecycle management process, the service organization or program office must undertake requisite concept maturity and technology development or research activity to correct the maturity shortfall. The organizations to consult with are the Technology Development and Prototyping Division for CMTD projects or the Research Engineering & Development (RE&D) Executive Board.

If the CSWG recommends that the concept be included in the NAS ConOps, a NAS ConOps change notice must also be prepared and presented to CSG. If the CSG endorses the concept, it is presented to the NextGen Management Board (NMB) for ratification before inclusion into the NAS ConOps. Endorsement by the CSG is confirmation that a concept is deemed operationally valid and technically feasible to be considered for inclusion into the NAS ConOps; only the NMB may approve concepts for inclusion into the NAS ConOps.

**Table 3: NAS ConOps Change Participating Organizations**

| **PRODUCT** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| Concept Assessment Request; Concept Assessment Report; NAS ConOps Change Notice; Safety Assessment | **NAS:** ANG-B1, ANG-B2, ANG-B3, ANG-C5, ANG-C1, AJW-13, AJI-2210, AJI-2300, AJV-S | **NAS:** CSG endorses; NMB approves |
| **MISSION SUPPORT:** N/A | **MISSION SUPPORT:** N/A |

## 2.7.2 Document NAS ConOps Changes as OIs and OSs

NAS ConOps proposed changes identified during this activity are mapped against existing OIs, OSs, or OCs. New OIs, OSs, or OCs will be created if existing ones do not align with the approved NAS ConOps.

During this step, a determination of the need for a new OC must be made. The NAS Systems Engineering & Integration Office (ANG-B), the Technology Development and Prototyping Division (ANG-C), along with the ATO Operational Concepts, Validation & Requirements Organization (AJV-S) (ATO-related), and other relevant stakeholder offices as necessary, will determine if a new OC may be warranted based on the complexity of the concept (cross organizational and/or involvement of multiple investment increments or systems). An OC business case is developed and presented to the NMB along with the recommendation to create a new OC.

## 2.7.3 Develop Operational Capability Business Case

The **ATO Program Management Office** works with the service organization, NextGen Technology Development and Prototyping Division, and Investment Planning & Analysis (IP&A) organizations to develop a preliminary assessment of risk, priority, affordability, and political sensitivity in order to complete the OC business case. The NMB will consider the merits of establishing an OC based on the OC business case, contribution to agency strategic goals, and affordability. Depending upon the complexity of the proposed new capability, the NMB may require the creation of a capture team to manage the OC if approved.

**Table 4: Operational Capability Business Case Participating Organizations**

| **PRODUCT** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| New OC; OC Business Case; Integration Safety Assessment | **NAS:** ANG-B3, ANG-B7, ANG-C5, ANG-B13, AJI-31, AJW-13, AJI-2210, AJI-2300, AJV-S | **NAS:** Director, Investment Planning and Analysis (AFI); ANG-5 |
| **MISSION SUPPORT:** N/A | **MISSION SUPPORT:** N/A |

## 2.7.4 Decompose NAS OIs, BTI, and Increments (New Concepts Only)

The Service Organization works with the NAS Enterprise Planning & Analysis Division (ANG-B2) to decompose new OIs, BTIs, and Increments resulting from NAS ConOps changes into NAS Enterprise requirements. ANG-B2 collaborates with ANG-B1 providing them with new OIs/BTIs/Increments and ANG-B1 ensures that the improvements and child increments are further decomposed into NAS Enterprise requirements that are incorporated in the Target NAS Enterprise Requirements Document (Target NAS RD). These requirements are specified with sufficient detail for allocation to investment increments that will be undertaken to achieve the OIs, BTIs, and Increments in the NAS ConOps.

**Table 5: NAS OIs, BTIs and Increments Decomposition Participating Organizations**

| **PRODUCT** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| Functional and Performance Requirements and investment Increments | **NAS:** ANG-B1, ANG-B2, ANG-B3, ANG-B7, ANG-C5, ANG-B1, Operating Org, Service organization, AFI, AJW-13, AJI-2210, AJI-2300, AJV-S | **NAS:** Director of NAS System Engineering and Integration Office (ANG-B) |
| **MISSION SUPPORT:** N/A | **MISSION SUPPORT:** N/A |

# 2.8 Prepare EA Change

When an initiative requires modification to decision points in future calendar years, the modification(s) should be submitted to the appropriate Infrastructure Roadmap Domain Lead as part of the annual Infrastructure Roadmap update cycle. The amendment will be submitted to the TRB (NAS) or ARB (MS) and then to the FEAB for endorsement. Approval occurs when the JRC approves the entire FAA EA annually.

If the initiative requires modification to decision points within the current calendar year’s approved FAA EA, the sponsor must prepare an Architecture Change Notice ([ACN](https://nam11.safelinks.protection.outlook.com/?url=https%3A%2F%2Fksn2.faa.gov%2Fafn%2FIT%2FADE%2FEA%2FFEAB%2FACN%2FShared%2520Documents%2FArchitecture%2520Change%2520Notice%2520(ACN)%2520Template.docx&data=04%7C01%7Cjames.conomea%40lstechllc.com%7C802af3f6687b465cc1d608da02b80763%7C93bb738069e94c7ca5fbfd30a5f59cc9%7C0%7C0%7C637825286694125896%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=i7A4%2F1ubgXtt8SG50fpqriYjqk5178HKpRHvb4Mkdac%3D&reserved=0)) documenting the proposed amendment and coordinate with the NAS Chief Architect (ANG-B2) for NAS initiatives, or the FAA Chief Architect (ADE-200) for Mission Support initiatives, to determine next steps for approval and entry into the EA.

# 2.8.1 Assess Priority & Time Phasing

A new service shortfall or need must be shown to have sufficient merit to warrant inclusion in the enterprise architecture when evaluated against other service needs of the agency. The line of business works with the TRB (NAS) or the ARB (MS) and other lines of business to determine how a new service need, technology refresh, or sustainment activity should be planned, time-phased, and integrated within the architecture relative to all other agency service needs. This activity may require rework of existing shortfalls and improvements already in the architecture.

**Table 6: EA Change Participating Organizations**

| **PRODUCT** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| Architecture Change Notice (ACN) | **NAS:** ANG-B1, ANG-B2, ANG-B3, ANG-C5, ANG-B13 | **NAS:** FEAB |
| **MISSION SUPPORT:** ADE-200 | **MISSION SUPPORT:** FEAB |
| Annual Roadmap Update | **NAS:** ANG-B1, ANG-B2, ANG-B3, ANG-C5, ANG-B13 | **NAS:** JRC |
| **MISSION SUPPORT:** ADE-200 | **MISSION SUPPORT:** JRC |

# 2.9 Enterprise Architecture Endorsement

1. The TRB oversees the technical content of the NAS Architecture with special emphasis on cross-domain issues and strategic business case development.
2. The ARB places special emphasis on identifying and resolving cross-domain issues and Mission Support architecture governance, strategy, and development that is consistent with the FEAB strategies and plans.

The TRB or ARB recommendation is necessary before the FEAB completes its analysis. For both NAS and Mission Support initiatives, Service Analysis & Strategic Planning results are presented to the FEAB for endorsement. During the CRDRD briefing, the FEAB will:

1. Decide if a shortfall or need has been adequately defined and whether it is an agency priority.
2. Determine the time-phasing of the shortfall or need within the appropriate EA roadmap and resolve architecture issues and inconsistencies across the enterprise.
3. Evaluate the readiness of the initiative to enter CRD.

The FEAB may recommend to the JRC that the proposed initiative advance to the CRD phase or remain in the SASP phase for additional work, or may disapprove the initiative in part or in full.

**Table 7: EA Endorsement Participating Organizations**

| **PRODUCT** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| EA Integration Analysis | **NAS:** TRB | **NAS:** FEAB |
| **MISSION SUPPORT:** ARB | **MISSION SUPPORT:** FEAB |

# 2.10 Prepare the CRD Plan

The CRD Plan identifies team members, defines expected products, establishes a milestone schedule, and documents the agreements between all organizations providing resources for the initiative during CRD.

The sections of the CRD Plan include:

1. Short description of the proposed initiative, including the EA roadmap that contains the initiative.
2. Short description of the service need(s) or shortfall(s) being addressed and the enhancement in service capability the effort is expected to produce, with reference to the Shortfall Analysis Report.
3. Interdependencies and time-phasing with other initiatives.
4. The organizations that will provide resources for the conduct of CRD phase activities and their responsibilities.
5. A short description of specialty engineering analyses that need to be conducted during the CRD phase.
6. Schedule for the conduct of CRD phase activities.
7. List of expected CRD phase outputs and products.
8. Entrance criteria for the IARD.
9. Resources needed for the work.
10. Resources needed to perform information management and data gathering.

The Integrated System Engineering (ISE) Team Lead is responsible for supporting the NAS service organization in developing the CRD plan. The ISE Team Lead will recommend requisite team members needed to help develop each CRD deliverable, monitor and participate in document development, and ensure schedules are specified in the approved CRD plan. For more information on deliverables, please refer to the [CRD Plan Template.](https://ksn2.faa.gov/nextgen/SysEng/NASEAandRqmts/ISE/ANGB13%20Library/CRD%20Plan%20Template%20v4_updated%20_2017_07_11.doc)

**Table 8: Concept and Requirements Definition Plan Participating Organizations**

| **PRODUCT** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| Concept and Requirements Definition Plan | **NAS:** ANG-B1, ANG-C1, ANG-B13, AJW-13, AJI-2210, AJI-2300, AJV-S, AJM-2, Labor Management Relations | **NAS:** FEAB Co-Chairs |
| **MISSION SUPPORT:** ADE-200, AVS | **MISSION SUPPORT:** FEAB Co--Chairs |

# 2.1 CRD Readiness Decision

The CRD Readiness Decision (CRDRD) is the first decision point in the AMS lifecycle management process and serves as the gateway between the SASP and CRD phases. An investment initiative is ready for a CRDRD when:

1. An enterprise architecture roadmap specifies action must be taken now to resolve a priority agency service shortfall or opportunity.
2. All SASP phase products are completed, reviewed, and signed.
3. All items in the JRC Readiness Criteria and Check List have been checked off by the JRC Secretariat through the JRC Readiness process (see JRC Readiness Criterial and Checklist).

The purpose of the CRDRD is to determine whether the identified service need is an appropriate investment opportunity for the FAA. The Co-Chairs of the FEAB approve the readiness of the initiative to proceed to the CRD Phase of the AMS process. An approved CRDRD represents a commitment of people and <u>not</u> a commitment of funds. JRC approval and commitment of funds to an investment initiative occurs at the Final Investment Decision (FID).

An approved CRDRD means the service organization may begin work in the CRD phase, leading to the IARD.

# 3.0 Concept and Requirements Definition Process

CRD is the second phase in the FAA lifecycle management process and is the means for gaining JRC approval of the IARD. The CRD phase ends with an approved set of products in support of an Investment Analysis Readiness Decision. The CRD process is shown in Figure 3 and is described in more detail in subsequent paragraphs.

![](data:image/jpeg;base64...)

Figure 3: Concept and Requirements Definition Process Flowchart

# 3.1 Obtain ACAT Designation

Acquisition Categories (ACATs) are determined by a two-step process. First, a proposed FAA investment initiative will be classified into an Investment Type (e.g., New Investment [NI], Sustainment [S], Technology Refreshment Portfolio [TRP], Variable Quantity [VQ], Facility Initiative [FI], Support Services Contract [SSC], Software Enhancements [SE], Research & Concept Maturity). Second, the investment initiative will be classified into an ACAT level within Investment Type based on the designation criteria. Initiatives will be assigned to the highest level ACAT (e.g., starting with ACAT 1) when they meet one or more of the designation criteria. Designation criteria includes factors such as total Facilities & Equipment (F&E) costs, single year F&E costs, Operations & Maintenance (O&M) costs, and factors such as complexity, risk, political sensitivity, safety, and security. Definitions for investment type and criteria for acquisition categories are located in the [AMS Table of Acquisition Categories](http://fast.faa.gov/docs/acqcattable.doc).

The investment initiative initiates this process by completing an [ACAT Determination Request Form](https://fast.faa.gov/docs/acqcatform.pdf), which is presented to the Acquisition Executive Board (AEB) early in the CRD phase for TR/TRP, TP, VQ, FI, S and SSC initiatives. NI investment initiatives may apply for an ACAT designation later in the CRD phase when costs are roughly known. The AEB may concur, assign a different ACAT, or reject the request.

The acquisition type and ACAT level of the initiative impacts the nature of the products generated during the CRD and Investment Analysis phases. This guidance document is written from the perspective of a ‘New Investment’, which requires the development of all CRD phase outputs and products<u>.</u> Refer to the [JRC Readiness Criteria and Check List](https://ksn2.faa.gov/afn/jrcportal/Shared%20Documents/JRC%20Readiness%20Criteria%20Checklist.pdf) for the full list of items to complete based on the ACAT investment type.

**Table 9: ACAT Determination Participating Organizations**

| **PRODUCT** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| ACAT Determination Request | **NAS:** AFI, ANG-B, AJW-13, AJI-2210, AJI-2300, AJV-S, AAP-100, AAP-200 | **NAS**: FAE |
| **MISSION SUPPORT:** AFI, ADE-200, AVS, AAP-100, AAP-200 | **MISSION SUPPORT:** FAE |

# 3.2 Finalize Shortfall Analysis

During the SASP phase, a Preliminary Shortfall Analysis Report was created to describe the difference, or shortfall, between the current service or OC and the desired service or capability. For investment initiatives which have been authorized to skip the SASP phase, legacy Shortfall Analysis Reports should be located and revalidated. During the CRD phase, the preliminary shortfall analysis is refined, and a Final Shortfall Analysis Report is developed. In order to develop the Final Shortfall Analysis Report, investment initiatives will develop a Legacy Case Cost Estimate and perform Shortfall Category Analyses. The goal of performing a final shortfall analysis is to quantify/monetize the problem, its nature, urgency, and impact in operational terms (e.g., airborne or ground delays, accident rate, etc.).

A shortfall can be quite complex. For example, operational assets may erode over time due to obsolescence, physical deterioration, or lack of logistics support. In other cases, a new OC may need to be established, requiring the completion and integration of multiple investment increments. The SAR should be comprehensive and build on the OC work from the SASP phase. For example, the As-Is Business Process Models which helped identify the shortfalls in the preliminary SAR should be fleshed out as needed to refine the shortfalls. For more information, please refer to the [Shortfall Analysis Report Guide](http://fast.faa.gov/docs/ShortfallAnalysisReportGuide.doc).

The Shortfall Analysis Report is a part of the IARD package, which presents the justification for continuing to study the proposed investment through the Investment Analysis phases. The justification addresses an existing or emerging shortfall, a technological opportunity, or a change in FAA or public policy. All final shortfall analyses require AFI-1 participation and approval.

**Table 10: Shortfall Analysis Report (Final) Participating Organizations**

| **PRODUCT** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| Shortfall Analysis Report (Final) | **NAS:** ANG-B1, ANG-B2, ANG-B3, ANG-B7, ANG-E5A, ANG-C1, ANG-C5, ANG-B13, AFI, AJW-13, AJI-2210, AJI-2300, AJV-S, AJW-1X, AFI | **NAS:** Director, Service Organization; Director, Operational Concepts, Validation, and Requirements for ATO-related programs (AJV-S); and Director NAS Systems Engineering & Integration Office (ANG-B); Director, Office of Investment Planning and Analysis (AFI-001) |
| **MISSION SUPPORT:** ADE-200, AFI, AVS, AJM-2 | **MISSION SUPPORT:** Director, Service Organization with Need; Director, Office of Information & Technology, Solution Delivery Service (ADE-001); Director, Office of Investment Planning & Analysis (AFI-001) |

# 3.3 Develop Solution ConOps

The Solution Concept of Operations document (Solution ConOps) is intended to address the shortfalls in services, or improvements in capabilities, initially identified in the SAR. The Solution ConOps describes how users will employ the new capability which will result in operational improvements within the operational environment and how it will achieve desired objectives for the proposed service need. The Solution ConOps defines the roles and responsibilities of key participants (e.g., controllers, maintenance technicians, pilots); explains operational issues that system engineers must understand when developing requirements; identifies procedural issues that may lead to operational change; incorporates and reflects key enterprise data and information needs; and establishes a basis for identifying alternative solutions and estimating their likely costs and benefits. Business processes modeling done to support the Preliminary Shortfall Analysis can be used to describe “As-Is” operations, while a new business process model should be created to describe the “To-Be” operations envisioned by the solution. More than one Solution ConOps may be required if proposed alternative solutions differ significantly from each other. For more information, please refer to the [ConOps template](https://ksn2.faa.gov/nextgen/SysEng/NASEAandRqmts/ISE/ANGB13%20Library/ConOps%20Template_Coordination_v%201.0.docx).

**Table 11: Solution ConOps Participating Organizations**

| **PRODUCT** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| Solution ConOps | **NAS:** ANG-B1, ANG-B2, ANG-B3, ANG-B7, ANG-E5A, ANG-C1, ANG-C5, ANG-B13, AJW-13, AJI-2210, AJI-2300, AJV-S, Labor Management Relations | **NAS:** Manager, Service Organization; Director, Operational Concepts, Validation, and Requirements for ATO-related (AJV-S); Manager, Technology Development and Prototyping Division (ANG-C5), and Manager, Division Manager, NAS Enterprise Architecture and Requirements Services  (ANG-B1) |
| **MISSION SUPPORT:** ADE-200, AVS | **MISSION SUPPORT:** Director, Office of Information & Technology, Solution Delivery Service (ADE-001); Director, Sponsoring Organization |

# 3.4 Analyze Functions

The purpose of the Functional Analysis process is to transform stakeholder-needed capabilities into a functional view of a required solution (regardless of complexity) that can deliver those capabilities. These activities begin with the business and data analysis in the SASP phase, where the NAS Enterprise Architecture & Requirements Services Division(ANG-B1) engages in business process analysis with primary stakeholders and subject matter experts to gain an in-depth understanding of business objectives (the end state the initiative is seeking to achieve), the problem to be solved, the opportunity for improvement if solved, and the desired outcome (the benefit resulting from meeting the business need).

Functional analysis provides a functional description of the needs of the business and the associated functionality allocated to a solution. It becomes a framework for requirements definition and synthesis that significantly improves innovation and product integration, as well as decreasing requirements creep. Functional analysis translates stakeholder needs/shortfalls into functions that meet these needs or mitigates/eliminates the shortfalls. Functional analysis consists of three (3) types of analysis:

1. **Business Process analysis -** the set of tasks and techniques used to understand, study, and assess how a business operates to achieve its goals and deliver value to its stakeholders.
2. **Data analysis -** the set of tasks and techniques used to understand data requirements and data elements necessary to satisfy those requirements are identified, defined, specified, and organized.
3. **Systems Functional analysis -** the set of tasks and techniques used to identify the parts of the business processes that will be performed by the initiative to achieve them in an efficient way.

A function is an activity that must be performed to achieve a desired outcome. A functional analysis examines **what** the proposed solution must do to address the needs or mitigate the shortfalls. Please note that it is **what** the solution must do, **not** **how** the solution will achieve the improvement. The result is a high-level description of the functions a solution must perform. The FAD contains the artifacts of functional analysis, which include:

1. Business process analysis - “As Is” and “To Be” business process models.
2. Data analysis - System Data Exchange Matrix.
3. System functional analysis - N-squared (N2) diagrams.
4. System functional analysis - Functional Flow Block Diagrams (FFBD).
5. Glossary defining all functions and data.

In the CRD phase, the results of the business process analysis and data analysis performed in the SASP phase are used along with the preliminary shortfalls to develop the Solution ConOps. Once the ConOps is at least 80% complete, the next step of functional analysis begins. ANG-B1 continues to work with primary stakeholders and subject matter experts to allocate the functions to the solution and further refine them.

A key part of functional analysis is looking at the activities, inputs, and outputs in the Business Process Models. The objective here is to determine which system functions are needed to achieve an activity in the model. The ConOps are verified for traceability and additional system functions are extracted as needed. System functions are then logically organized into a system functional hierarchy. As the high-level functions are decomposed into sequentially lower-level sub-functions, the corresponding N2 and FFBD diagrams are developed. Through this process of analyzing system functions and sub-functions, a description of the solution emerges and becomes the framework for developing requirements and physical architectures. Normally in the CRD phase, the system functional hierarchy is decomposed at least 3 levels below the top-level function allocated to the solution (e.g., ‘provide solution functions’). Once the system functional analysis is completed, the results are documented in the FAD. For more information, please reach out to ANG-B1 to obtain the latest FAD Template.

**Table 12: Functional Analysis Document Participating Organizations**

| **PRODUCT** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| Functional Analysis Document (FAD) | **NAS:** ANG-B1, ANG-B13, ANG-B2, ANG-B7, ANG-B3, ANG-C1, ANG-C5, AJW-13, AJI-2210, AJI-2300, AJV-S, Labor Management Relations | **NAS:** Manager, Service Organization and Division Manager, NAS Enterprise Architecture and Requirements Services (ANG-B1) |
| **MISSION SUPPORT:** ADE-200, AVS | **MISSION SUPPORT:** Manager, Service Organization, Director, Office of Information & Technology, Solution Delivery Service (ADE-001) |

# 3.5 Perform Cloud Suitability Assessment

At each AMS decision point there is a requirement to assess FAA Cloud Services (FCS) implementation suitability and document the results. The output from the FCS Suitability Assessment Process is an input for the Engineering Infrastructure Services (EIS) Assessment that is presented to the Architecture Review Board (ARB) or Technical Review Board (TRB). Enterprise Services Infrastructure Framework (ESIF) analysis may be performed to inform the cloud suitability assessment. Re-assessments are an inherent part of the Acquisition and Lifecycle Management Framework as an investment moves from one AMS decision point to a subsequent one.

# 3.6 Perform Preliminary Information System Security Assessment

The main objective of the Preliminary Information System Security (ISS) Assessment is to assess the potential security impact of the information types underlying the service need. If the investment initiative performed the previous assessment (i.e., the ISS Risk Factors Assessment), then this assessment is nothing more than an update based on firmer data discovered during the CRD phase.

Service organizations assess the investment initiative to determine: (1) ISS risk factors for input to the Acquisition Category (ACAT) determination, (2) ISS requirements for the pPRD, (3) factors for a rough ISS cost estimate for each alternative solution, and (4) factors for a rough estimate of annual operational benefits gained from Ie5mplementing security requirements.

If one of the solution alternatives identified is a cloud solution, the investment initiative should provide a preliminary indication of which security requirements would be implemented by the cloud provider

**Table 13: Information System Security Participating Organizations**

| **PRODUCT** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| **Preliminary** Information System Security (ISS) Assessment | **NAS:** AJW-0, ANG-B1, ANG-B31, AJW-13, AJI-2210, AJI-2300, AJV-S | **NAS**: Originating Organization’s Authorizing Official Designated Representative (AODR) |
| **MISSION SUPPORT:** AIS-200, AIS-300 | **MISSION SUPPORT:** Originating Organization’s AODR |

# 3.7 Assess Operational Safety (NAS Only)

The next step is to complete the appropriate safety risk management activity. ATO Safety and Technical Training (AJI-3) help determine what safety analysis and documentation is required and will assist in the analysis if requested. AJI-3 is also the approving authority for determining whether proposed changes affect the safety of the NAS. NAS acquisitions going through the CRD phase must submit their safety analysis for review and approval as documented in the Safety Risk Management Guidance for System Acquisitions (SRMGSA).

If the initiative affects the NAS, the program office is required to conduct an Operational Safety Assessment (OSA). (Note: there are some exceptions to this requirement. Contact AJI-3 for more information). The OSA identifies, analyzes, and documents operational hazards and associated requirements and consists of:

1. The Operational Services & Environment Description (OSED), which describes the physical and functional characteristics of the initiative including ground and air elements.
2. An Operational Hazard Assessment (OHA), which describes operational hazards classified by potential severity.
3. An Allocation of Safety Objectives and Requirements (ASOR), which is the process of using hazard severity to determine the objectives and requirements of the solution.

The key question is: Does the initiative introduce a safety risk? If so, the complete OSA must be conducted. If not, the analysis can be terminated at the OHA. In either case, the AJI-3 Safety Case Lead conducts a peer review of the completed analysis and concurs with the OSA before it can receive final approval from the ATO Chief Safety Engineer. If there is a potential for the investment initiative to affect the safety of the NAS, then an OSA is required regardless of if a hazard is identified. Results from the OSA may create safety requirements for the pPRD.

**Table 14: Safety Assessment Participating Organizations**

| **PRODUCT** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| Safety Assessment | **NAS:** ANG-B3 | **NAS**: Manager, Safety Management Group (**AJI-3),** Director of the program office |
| **MISSION SUPPORT:** N/A | **MISSION SUPPORT:** N/A |

# 3.8 Develop Preliminary Requirements

The preliminary Program Requirements Document (pPRD) identifies:

1. Essential functional and performance characteristics of a solution.
2. Implementation requirements of the solution.

Principal contributors to the pPRD include the Solution ConOps, SAR, FAD (derived from the ConOps) and the EA Artifacts. Functions contained in the functional analysis are transformed into functional requirements and inserted into the pPRD.

The pPRD does not dictate a solution; it is considered the starting point for identifying the essential characteristics of a solution and estimating basic costs that will provide the desired OCs and service outcomes. The sponsoring service organization typically forms a team of experienced technical, user, and program personnel (e.g., operations, human factors, safety and security disciplines, system engineering, test and evaluation, etc.) to develop and analyze preliminary program requirements. Research or prototyping may be necessary to define an acceptable range of requirements. The pPRD establishes the basis for determining alternative solutions and estimating costs. It is important to identify high-level requirements that drive cost and a statement of work definition. The preliminary requirements must be testable and should address and be consistent with the elements documented in SAR, FAD and ConOps. The ISS and Safety Assessments are predecessors to the pPRD.

**Table 15: Preliminary Program Requirements Participating Organizations**

| **PRODUCT** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| Preliminary Program Requirements | **NAS:** ANG-B1, ANG-B13, ANG-B3, ANG-B7, ANG-C1, ANG-E5A, AJW-13, AJI-2210, AJI-2300, AJV-S, AJV-P | **NAS**: Director or Vice President, Service Organization; Director, Operational Concepts, Validation and Requirements for ATO-related and Concurrence of Director (AJV-S), Director of NAS System Engineering and Integration Office (ANG-B) |
| **MISSION SUPPORT:** ADE-200, AVS | **MISSION SUPPORT:** Director, Office of Information & Technology, Solution Delivery Service (ADE-001); Director, Sponsoring Organization |

# 3.8.1 Program Requirements Management Tool (NAS Only)

The sponsoring service organization enters requirements into the [requirements](http://www.telelogic.com) management tool Dynamic Object-Oriented Requirements System (DOORS) (the preferred tool) as identified in the [Program Requirements Document (PRD) Template](http://fast.faa.gov/docs/programreq.docx). DOORS is a requirements management tool. It can be used to trace PRDs to enterprise-level documents such as the Target NAS RD.. DOORS is also used as a requirements repository for investment initiatives and each approved pPRD has a DOORS module that is managed by the Requirements and Analysis Branch, ANG-B11. DOORS modules are updated throughout the AMS process for developing requirements until the final Program Requirements Document (fPRD) is approved. ANG-B11 has primary custodial responsibility of the DOORS tool.

**Table 16: NAS Program Requirements DOORS Module Participating Organizations**

| **PROCESS** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| NAS Program Requirements DOORS Module | **NAS:** ATO Program Management Office, ANG-B11, ANG-B13, ANG-B5 | **NAS**: Manager,Requirements Analysis Branch (ANG-B11) |
| **MISSION SUPPORT:** N/A | **MISSION SUPPORT:** N/A |

##

## 3.8.2 Consult with Specialty Engineering

The specialty processes are systems engineering analyses customized to unique projects. The CRD package will include “sign-offs” demonstrating that the initiative has considered the results of these processes, including:

1. Human Factors (HF).
2. Spectrum (impact on radio signals).

The descriptions below describe how to move forward. Setting up the first meeting with the appropriate offices early in the CRD phase will help with time management of the overall process.

### 3.8.2.1 Human Factors (HF)

AMS policy Section 4.7 states that service organizations must assure that planning, analysis, development, implementation, and in‐service activities for equipment, software, facilities, and services include Human Factors engineering to ensure performance requirements and objectives are consistent with human capabilities and limitations.

1. The service organization or program office, facilitated by the Human Factors Division (ANG-C1), should address HF as early as practical to minimize technical, programmatic, and operational risk. In order to assess the appropriate level of HF involvement, ANG-C1 can assist coordination with agency HF resources such as the HF Acquisition Working Group to identify HF specialists that might provide direct support or other resources to a program. Ideally, HF specialists are involved prior to the CRD phase and throughout the AMS lifecycle to help gather data about the service environment and participate in the preliminary shortfall analysis.
2. HF involvement during the definition of solution alternatives (this section of CRD guidance) can illuminate many implications of each alternative related to human performance. As examples, HF implications can include the appropriateness of automation or procedures from a HF perspective, in the context of other systems and tasks. Such analysis can be performed well before establishing details such as Computer Human Interface (CHI) requirements later in the AMS lifecycle.
3. HF involvement during the CRD phase has important downstream implications. For example, during the Investment Analysis phase, AMS artifacts such as the Program Requirements Document, Business Case, Implementation Strategy and Planning Document (ISPD), and Integrated Human Factors Plan can benefit from HF activities during the CRD phase. Therefore, it is recommended that an HF specialist participates during the CRD phase to bring a HF perspective into overall analyses and AMS artifacts, tailored to the program.

### 3.8.2.2 Spectrum Impact

The service organization or program office, with the Spectrum Engineering Services Group’s (AJW-1C) assistance, must address spectrum requirements for solutions that utilize radio frequencies. Mission Support initiatives still must contact the Spectrum team to get a statement that the Spectrum checkmark is complete or obtain a waiver.

**Table 17: Spectrum Impact Determination Participating Organizations**

| **PRODUCT** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| Spectrum Impact Determination | **NAS:** ANG-B13, AFI, ANG-B1, ANG-B2, ANG-C1, AJW-13, AJI-2210, AJI-2300, AJV-S, AJV-P | **NAS**: Director, Spectrum Engineering Group (AJW-1C) |
| **MISSION SUPPORT:** N/A | **MISSION SUPPORT:** Director, Spectrum Engineering Group (AJW-1C) |

# 3.9 Develop EA Products

Every initiative going through the CRD phase must include a set of project-level EA products that are associated to the corresponding enterprise products which show the potential solution from different perspectives. The products are developed with assistance from the Enterprise Architecture Modeling Branch (ANG-B12) for NAS related initiatives, or the Enterprise Architecture and Portfolio Insight (ADE-200) for Mission Support related initiatives. ANG-B1 and ADE-200 provides the guidance and templates that identifies the products to be developed and how they are to be completed and submitted. This process ensures that initiatives are aligned with the appropriate architecture and its planned evolution.

Using the functional analysis results done earlier, each capability must examine the proposed data (inputs and outputs) and assess if existing data exchange formats and models can be used. Exchanges and models should be consistent with those identified in the appropriate EA.

**Program offices are encouraged to contact the EA leads as soon as possible as specific EA products may vary for each initiative.**

**Table 18: Enterprise Architecture Products Participating Organizations**

| **PRODUCT** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| **Enterprise Architecture Products** | **NAS:** ANG-B1, ANG-B2, ANG-B12, ANG-B13, ANG-E5A, AJW-13<u>,</u> AJI-2210, AJI-2300, AJV-S | **NAS**: Manager, NAS Enterprise Planning & Analysis Division (ANG-B2) |
| **MISSION SUPPORT:** ADE-200 | **MISSION SUPPORT:** Manager, Enterprise Architecture & Portfolio Insight (ADE-200) |

# 3.10 Identify and Develop Alternatives

## 3.10.1 Define Alternatives

Generating a range of distinct and viable alternatives increases the probability that the best possible solution is selected. At least three technically distinct and feasible alternatives that will eliminate or significantly decrease the shortfall or service need are identified. Enterprise Services Infrastructure Framework (ESIF) analysis is encouraged in identifying potential alternatives. Trade studies may be needed to generate data and information to support the transition from existing functionality to new capabilities.

The alternatives developed during the CRD phase will be high-level concepts, and thus referred to as preliminary alternative descriptions. If information technology functions are involved (e.g., voice or data processing, etc.), OMB now requires cloud computing to be evaluated as a potential alternative. Performing an ESIF analysis helps identify potential uses of cloud computing and related technologies. The alternative description document is further developed during the Investment Analysis phases as technical details associated with each alternative are added and cost and benefit data is generated. If the initiative is part of a NextGen portfolio or OI, the description document includes links to the portfolio or improvement.

Alternatives have the following characteristics:

1. Technically diverse, creative, flexible, and innovative.
2. Consider both material (technical) and nonmaterial (policy, procedures, or personnel) solutions.
3. Commercial or non-developmental solutions are preferred.
4. Solutions that meet a portion of the requirements may be considered.
5. Must comply with FAA standards.

The NAS Enterprise Architecture and Requirements Services Division (ANG-B1) or Enterprise Architecture and Portfolio Insight (ADE-200), can provide assistance in identifying alternatives.

**Table 19: Preliminary Alternative Descriptions Participating Organizations**

| **PRODUCT** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| Preliminary Alternative Descriptions (also referred to as Range of Alternatives) | **NAS:** ANG-B13, AFI, ANG-B1, ANG-B2, ANG-C1, AJW-13, AJI-2210, AJI-2300, AJV-S | **NAS**: Director, Service Organization; Director, Operational Concepts, Validation, and Requirements for ATO-related and Director, NAS Systems Engineering and Integration Office (ANG-B) |
| **MISSION SUPPORT:** ADE-200, AFI, AVS | **MISSION SUPPORT:** Director, Sponsoring Organization; Director, Office of Information & Technology, Solution Delivery Service (ADE-001) |

## 3.10.2 Estimate Alternative Costs

The requirements for the OC vary by ACAT and may be tailored based on the specific needs of the investment analysis.

The rough estimate of costs (also called “monetizing the shortfall”) for a proposed alternative should address at least part of the shortfall finalized earlier in step 3.1, and provide a reference for evaluating the potential benefits a given initiative may provide. AFI-1 provides guidance on techniques, estimating, and documentation needs. A detailed benefit estimate is created during the Investment Analysis phase.

A summary table containing the legacy cost alternative is presented in the IARD briefing package.

**Table 20: Estimate Costs Participating Organizations**

| **PRODUCT** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| ROM Cost Estimate for One Alternative | **NAS:** AFI, ANG-B13, ANG-B7, AJW-13, AJI-2210, AJI-2300, AJV-S | **NAS**: Director, Service Organization; Director, Operational Concepts, Validation, and Requirements for ATO-related and Director, Investment Planning and Analysis (AFI) |
| **MISSION SUPPORT:** AFI, ADE-200, AVS | **MISSION SUPPORT:** Director, Service Organization (AVS); Director, Investment Planning and Analysis (AFI-1) |

# 3.11 Verify and Validate Work Products

Verification ensures a quality product is built according to requirements and specifications. This includes evaluation of the end product (system, service or operational change) and intermediate work products against all applicable requirements. Validation ensures the right product is built to fulfill its intended purpose and user needs when placed in its intended environment. The methods employed to accomplish validation are applied to selected work products as well as to the end product and end product components.

Verification and Validation (V&V) is a disciplined approach to assessing select products, along with associated product components and work products, throughout the lifecycle of a system, service, facility, or operational change. These work products are verified against requirements and validated against needs, as identified in previous work products, products, and product components. V&V is performed by independent stakeholders or reviewers that are not directly involved with the development of the work product, product component or product being verified and validated. While performing V&V, all independent stakeholders and reviewers must be cognizant of the validity of V&V activities that were performed (or missed) on prerequisite work products, product components, and products. The order and significance of verification versus validation may change throughout the lifecycle based on the state of the mission definition, operational concept, requirements, product development, and product.

The primary focus of V&V during CRD is to validate the preliminary Program Requirements Document (pPRD), Solution Concept of Operations (ConOps), EA products, and Shortfall Analysis Report (SAR) to ensure that the existing or planned product properly addresses mission needs and trace to FAA strategic plans, OIs, and the Enterprise Architecture. This can be accomplished with early evaluations performed in support of concept feasibility determinations and analysis of alternative solutions during SASP and CRD phases. Further, early evaluations may be used throughout the program planning process to minimize program risks.

**Table 21: Verification and Validation Participating Organizations**

| **PROCESS** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| **SASP and CRD Work Products** | **NAS:** ANG-B1, ANG-E5A | **NAS**: N/A |
| **MISSION SUPPORT:** N/A | **MISSION SUPPORT:** N/A |

# 3.12 Plan for Investment Analysis

The Investment Analysis Plan (IAP) defines the products, identifies team members and resources, establishes a milestone schedule, and documents agreement among all organizations providing resources for completing the Investment Analysis phase.

For both NAS and Mission Support initiatives, the team develops the IAP with assistance from the AFI-100. Information required for the IAP includes:

1. Scope and assumptions.
2. A short description of alternatives.
3. Planned activities and specifies how tasks will be accomplished.
4. Outputs and exit criteria.
5. A schedule for completion.
6. Roles and responsibilities of participating organizations.
7. Estimated resources needed to complete the work.

Detailed templates and instructions for the IAP are located on both the FAST website and Appendix B of this guidelines document.

**Table 22: Investment Analysis Plan Participating Organizations**

| **PRODUCT** | **SUPPORTING ORGANIZATIONS** | **APPROVAL AUTHORITY** |
| --- | --- | --- |
| Investment Analysis Plan (IAP) | **NAS:** AFI, ANG-B13, ANG-B7, AJW-13, AJI-2210, AJI-2300, AJV-S | **NAS**: Director, Service Organization; Director, Operational Concepts, Validation and Requirements for ATO-related and Director, Investment Planning and Analysis (AFI) |
| **MISSION SUPPORT:** AFI, AVS | **MISSION SUPPORT:** Investment Planning and Analysis (AFI-1); Director, Sponsoring Organization |

# 4 Investment Analysis Readiness Decision

IARD is the second decision point in the AMS lifecycle management process and serves as the gateway between the CRD phase and the Investment Analysis phases. The purpose of this decision is to verify the shortfall is adequately quantified, preliminary requirements are defined, and the range of alternatives is technically diverse and feasible. Both NAS and Mission Support programs require an IARD.

The JRC is the Investment Decision Authority (IDA) for IARDs. The JRC Executive Secretariat uses the JRC Readiness Criteria and Check List to evaluate whether CRD products are sufficiently developed to present to the JRC for decision. At the IARD, the JRC determines whether the initiative warrants entry into investment analysis and approves the alternatives to be studied during initial investment analysis. The initiative must contribute to FAA strategic goals and include diverse and feasible alternatives. After the JRC receives the briefing they will make their decision. Once approval has been obtained, the service organization may begin work in Investment Analysis.

The [JRC Readiness Criteria and Checklist](https://ksn2.faa.gov/afn/jrcportal/Shared%20Documents/JRC%20Readiness%20Criteria%20Checklist.pdf#Home) lists the required deliverables as well as the offices that support their development and approval.

# Appendix A – Acronyms

| **Acronym** | **Full Name** |
| --- | --- |
| ACAT | Acquisition Category |
| ACN | Architecture Change Notice |
| AEB | Acquisition Executive Board |
| AIS | Information Security & Privacy Services Division |
| AJI | ATO Safety and Technical Training |
| AJM | Program Management Organization |
| AJW | Technical Operations |
| AMS | Acquisition Management System |
| **AODR** | **Authorizing Official Designated Representative** |
| ARB | Architecture Review Board |
| ARP | FAA Airports |
| ASOR | Allocation of Safety Objectives and Requirements |
| AST | Commercial Space Transportation |
| ATO | Air Traffic Organization |
| AVS | Aviation Safety |
| CHI | Computer Human Interface |
| CINP | Communications, Information & Network Programs |
| CMTD | Concept Maturity and Technology Development |
| COI | Communities of Interest |
| ConOps | Concept of Operations |
| CRD | Concept and Requirements Definition |
| CRDRD | Concept and Requirements Definition Readiness Decision |
| CSG | Concept Steering Group |
| CSWG | Concept Steering Work Group |
| CTO | Chief Technology Officer |
| DOORS | Dynamic Object-Oriented Requirements System |
| EA | Enterprise Architecture |
| EIS | Engineering Infrastructure Services |
| F&E | Facilities & Equipment |
| FAA | Federal Aviation Administration |
| FAD | Functional Analysis Document |
| FAST | FAA Acquisition System Toolset |
| FCS | FAA Cloud Services |
| FEAB | FAA Enterprise Architecture Board |
| FFBD | Functional Flow Block Diagram |
| FI | Facility Initiative |
| FID | Final Investment Decision |
| fRD | final Requirements Document |
| HF | Human Factors |
| IA | Investment Analysis |
| IAP | Investment Analysis Plan |
| IARD | Investment Analysis Readiness Decision |
| IDA | Investment Decision Authority |
| IP&A | Investment Planning and Analysis |
| ISE | Integrated System Engineering |
| ISPD | Implementation Strategy and Planning Document (ISPD) |
| ISSA | Integrated System Safety Assessment |
| ISS | Information Systems Security |
| ISSM | Information Systems Security Manager |
| IT | Information Technology |
| JPDO | Joint Planning and Development Office |
| JRC | Joint Resources Council |
| LOB | Line of Business |
| MS | Mission Support |
| NAS | National Airspace System |
| NextGen | Next Generation Air Transportation System |
| NI | New Investment |
| NMB | NextGen Management Board |
| NSIP | NAS Segment Implementation Plan |
| O&M | Operations & Maintenance |
| OC | Operational Capability |
| OCIP | Operational Capability Integration Plan |
| OHA | Operational Hazard Assessment |
| OI | Operational Improvement |
| OS | Operational Sustainment |
| OMB | Office of Management and Budget |
| OSA | Operational Safety Assessment |
| OSED | Operational Services and Environment Description |
| PAD | Preliminary Alternative Descriptions |
| PII | Personal Identifiable Information |
| PMO | Program Management Organization |
| pPR | preliminary Program Requirements |
| RD | Requirements Document |
| RE&D | Research Engineering and Development |
| ROM | Rough Order of Magnitude |
| SAR | Shortfall Analysis Report |
| SASP | Service Analysis & Strategic Planning |
| SCOP | Stewardship Communities of Practice |
| SE | Software Enhancements |
| SEM | Systems Engineering Manual |
| SME | Subject Matter Expert |
| SMS | Safety Management System |
| SMTS | **Safety Management Tracking System** |
| SRM | Safety Risk Management |
| SRMGSA | Safety Risk Management Guidance for System Acquisitions |
| SSC | Support Services Contract |
| TR | Technology Refreshment |
| TRB | Technical Review Board |
| TRP | Technology Refreshment Portfolio |
| V&V | Verification and Validation |
| VQ | Variable Quantity |

# Appendix B – Reference Documents and Associated Links

| **Work Product/Process** | **Supporting Tools and Guidance** |
| --- | --- |
| **ACAT Determination Request** | * [ACAT Determination Process](http://fast.faa.gov/NFFCA_Acquisition_Categories.cfm) * [ACAT Determination Request Form](http://fast.faa.gov/docs/acqcatform.doc) * [ACAT Determination Process & Request Form Criteria](http://fast.faa.gov/docs/ACATProcessCriteria.doc) * [ACAT Table of Acquisition Categories and Tailoring](http://fast.faa.gov/docs/AMSTailoringRequestFlowchart.ppt) |
| **Architecture Change Notice** | * [Architecture Change Notice Template](https://nam11.safelinks.protection.outlook.com/?url=https%3A%2F%2Fksn2.faa.gov%2Fafn%2FIT%2FADE%2FEA%2FFEAB%2FACN%2FShared%2520Documents%2FArchitecture%2520Change%2520Notice%2520(ACN)%2520Template.docx&data=04%7C01%7Cjames.conomea%40lstechllc.com%7C802af3f6687b465cc1d608da02b80763%7C93bb738069e94c7ca5fbfd30a5f59cc9%7C0%7C0%7C637825286694125896%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=i7A4%2F1ubgXtt8SG50fpqriYjqk5178HKpRHvb4Mkdac%3D&reserved=0) |
| **Concept and Requirements Definition (CRD) Plan** | * [CRD Plan Template](https://ksn2.faa.gov/nextgen/SysEng/NASEAandRqmts/ISE/ANGB13%20Library/CRD%20Plan%20Template%20v4_updated%20_2017_07_11.doc) |
| **EA Integration Analysis** | * [TRB/ARB Briefing Template](https://ksn2.faa.gov/afn/IT/ADE/EA/ARB/Other%20ARB%20Documents/ARB%20Investment%20Decision%20Briefing%20Template.ppt) |
| **Estimate Costs and Monetize Shortfall** | * [Government Accountability Office Cost Estimating and Assessment Guide](https://www.gao.gov/products/GAO-20-195G) * [Guide to Conducting Business Case Cost Evaluations](https://my.faa.gov/org/staffoffices/afn/finance/organization/investment/ipa_cat.html) |
| **Functional Analysis (Including N2 Diagram & Block Diagram)** | * [Systems Engineering Manual](https://sep.faa.gov/file/get/2974) |
| **Information System Security Risk Assessment** | * [Information Security Guidance for System Acquisitions (ISGSA)](http://fast.faa.gov/EMP_Information_Security.cfm) * [ISS Risk Factors Assessment template](http://fast.faa.gov/EMP_Information_Security.cfm) |
| **Integrated Safety Assessment** | * [Safety Risk Management Guidance for System Acquisitions (SRMGSA)](https://my.faa.gov/org/linebusiness/ato/safety/sms/documents/SRMGSA.html) * [ANG-B3 Safety Website](https://ksn2.faa.gov/nextgen/SysEng/SafetyandISS/default.aspx) * [NAS Enterprise Safety Handbook](https://ksn2.faa.gov/nextgen/SysEng/SafetyandISS/team/Shared%20Documents/Enterprise%20Safety/SMS%20Policy%20and%20Guidance/NAS%20Enterprise%20Safety%20Handbook/NESH_20190930_NAS%20Enterprise%20Safety%20Handbook%20v1.0_FINAL_508.pdf) |
| **Investment Analysis Plan** | * [Investment Analysis Guidelines and Template](http://fast.faa.gov/docs/iainitial.docx) **(Initial)** * [Investment Analysis Guidelines and Template](http://fast.faa.gov/docs/iafinal.docx) **(Final)** |
| **NAS ConOps Change Development** | * [Concept Maturity and Technology Development (CMTD) Guidelines](https://fast.faa.gov/docs/rsaguidelines.doc) |
| **NAS Program Requirements DOORS Module** | * [Access to DOORS Software](https://sysarc.faa.gov/) |
| **Operational Capability Integration Plan** | * [Service](https://sep.faa.gov/products/sr/main) and [Infrastructure](https://sep.faa.gov/products/ir/main) Roadmaps * Capital Investment Plan |
| **Preliminary Information System Security (ISSA) Assessment** | * [Lifecycle Management Process Flowchart - Information Systems Security](http://fast.faa.gov/flowcharts/grid_platform.cfm?p=iss) (click on activity boxes in flowchart) * [ATO Information Systems Security (ISS) Procedures and Guidance](https://employees.faa.gov/org/linebusiness/ato/operations/technical_operations/neo/issp/authorization/) * [Information Systems Security Authorization Handbook](https://employees.faa.gov/org/linebusiness/ato/operations/technical_operations/neo/issp/authorization/media/FY19_FAA_Security_Authorization_Handbook.pdf) * [Information Security Guidance for System Acquisitions (ISGSA)](http://fast.faa.gov/EMP_Information_Security.cfm) * [Preliminary Information System Security (ISS) Assessment template](http://fast.faa.gov/docs/isgsa2.doc) |
| **Preliminary Program Requirements** | * [Program Requirements Document Template](http://fast.faa.gov/docs/programreq.docx) * [Handbook for Writing Requirements](https://ksn2.faa.gov/nextgen/SysEng/NASEAandRqmts/ISE/ANGB13%20Library/Handbook%20for%20Writing%20Program%20Requirements.pdf) |
| **Shortfall Analysis Report** | * [Guidelines and Template for conducting Shortfall Analysis](http://fast.faa.gov/docs/ShortfallAnalysisReportGuide.doc) |
| **Solution ConOps** | * [Solution ConOps Guidelines and Template](https://ksn2.faa.gov/nextgen/SysEng/NASEAandRqmts/ISE/ANGB13%20Library/ConOps%20Template_Coordination_v%201.0.docx) |
| **Verification and Validation** | * [Verification and Validation Guidelines](http://fast.faa.gov/docs/vandvguidelines.doc) |

# Appendix C – JRC Readiness Criteria and Checklists

Refer to the [JRC Readiness Checklist](https://ksn2.faa.gov/afn/jrcportal/Shared%20Documents/JRC%20Readiness%20Criteria%20Checklist.pdf#Home) for the complete list of investment-phase checklist items.

Final Investment Analysis Plan is required for Variable Quantity Investment Types
