---
title: "scotemplate"
source_url: https://fast.faa.gov/docs/scotemplate.docx
source_type: docx
converted: 2026-10-27
---
# scotemplate

|  |  |  |  |
| --- | --- | --- | --- |
| |  |  | | --- | --- | | ![m](data:image/png;base64...) | ***Acquisition Management System Guidance*** | |  |   **Solution Concept of Operations Document Template** |

For NextGen and Mission Support AMS Acquisitions

Version 1.0, March 10, 2022

**Responsible Organizations:**

ANG-C5 Technology Development & Prototyping Division

ANG-B1 NAS Enterprise Architecture & Requirements Services Division

Or

ADE-001 Office of Information & Technology, Solution Delivery Service

**Solution Concept of Operations – Overview**

The Solution Concept of Operations document (Solution ConOps) is intended to address the shortfalls in services, or improvements in capabilities, initially identified in the Shortfall Analysis Report (SAR). Once the shortfall is identified, the responsible Line of Business (LOB) and designated program management office, along with other program stakeholders, develop the Solution ConOps. From the perspective of a user, a ConOps describes how a set of capabilities will result in operational improvements or achieve desired objectives for a proposed system. Although not a true “solution” at this phase, the title is used to distinguish it from other National Airspace System (NAS) ConOps documents.

Preliminary development of the ConOps may be initiated as early as the Service Analysis and Strategic Planning (SASP) phase of the Acquisition Management System (AMS) lifecycle. However, it is formalized during the Concept Requirements Definition (CRD) phase in preparation for the Investment Analysis Readiness Decision (IARD).

The ConOps document outlines the characteristics of the concept in a straightforward manner to facilitate a shared understanding among stakeholders. It should clearly state the proposed functionality and processes in the intended operational environment. Because it provides a common frame of reference, the ConOps facilitates stakeholder agreement and the evolution from vague capabilities to specific technical requirements. The ConOps should not include detailed technical issues that will be addressed during system analysis and development activities. Rather, these aspects will be integrated later, when the activities are completed and the concept is matured.

A ConOps is required in order for a program to exit the AMS CRD phase ([AMS Section 2.4.1](https://fast.faa.gov/docs/acquisitionManagementPolicy/AcquisitionManagementPolicy2.4.pdf)). If the program intends to implement solutions across multiple segments (i.e. Solution Segment 1, Solution Segment 2, etc.), separate ConOps must be developed for each. The document must clearly identify which segment it represents. With regard to the content of a ConOps, AMS Section 2.4.1 specifies the following:

The solution concept of operations describes *how users will employ the new capability* within the operational environment and *how it will satisfy service need*. The solution ConOps defines the roles and responsibilities of key participants (e.g., controllers, maintenance technicians, pilots); explains operational issues that system engineers must understand when developing requirements; identifies procedural issues that may lead to operational change; and establishes a basis for identifying alternative solutions and estimating their likely costs and benefits. More than one solution concept of operations may be required if proposed alternative solutions differ significantly from each other.

In the National Airspace System (NAS), the ConOps is approved by the NextGen Technology Development and Prototyping Division (ANG-C5) and the NAS Enterprise Architecture and Requirements Division (ANG-B1). For Mission Support gaps, consultation with AIT, Solution Delivery will be necessary.

**Solution Concept of Operations Workflow**

The figure on the following page depicts the process of developing/creating the components of a ConOps document for input into the Investment Analysis Readiness Decision. Please refer to the ConOps Template on the following pages of this guide for more specific instructions.

![](data:image/x-emf;base64...)

**Template Scope**

This template serves the needs of both NAS and Non-NAS (i.e., Mission Support) programs. Differences between NAS and Mission Support ConOps are highlighted when appropriate to accommodate process and semantic variances between the two types of programs.

**NextGen Solution ConOps**: The NextGen program office prepares the AMS artifacts with the support of the NAS Requirements Services Division (ANG-B1). During the CRD phase of the AMS lifecycle, ANG-B1 will coordinate review of the Solution ConOps with the Technology Development & Prototyping Division (ANG-C5) and other stakeholders. Programs that are strictly sustainment of an existing system (formerly identified as a “technical refresh”) and do not expand functionality may be exempted from preparing a Solution ConOps if a tailoring request is approved by the Joint Resources Council (JRC).

**Mission Support Solution ConOps**: The sponsoring Mission Support program office initiates development of the mission support Solution ConOps in coordination with Enterprise Architecture & Portfolio Insight (ADE-200) during the CRD phase of the AMS lifecycle.

The NAS Enterprise Architecture and Requirements Division (ANG-B1), the Technology Development & Prototyping Division (ANG-C5), and the Enterprise Architecture & Portfolio Insight (ADE-200) maintain the Solution ConOps template.

**Version History**

|  |  |  |
| --- | --- | --- |
| **Version** | **Date** | **Notes** |
| Coordination Draft (v0.5) | 8/7/18 | Integrated ANG-B edits into template. |
| Coordination Draft (v0.6) | 10/10/18 | Integrated ANG-B PBM edits into template. |
| Coordination Version 1.0 | 03/10/22 | Final draft for review and approval. |

![](data:image/x-wmf;base64...)**Solution Concept of Operations**

for

**[Name of AMS investment program]**

Version *(#)*

|  |
| --- |
| **Approved:** |
| \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date:\_\_\_\_\_\_\_\_\_\_\_\_\_  Director, Service Organization with Need  *(For NAS and MS initiatives)*  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date:\_\_\_\_\_\_\_\_\_\_\_\_\_  Manager, Technology Development & Prototyping Division (ANG-C5)  *(For NAS initiatives only)*  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date:\_\_\_\_\_\_\_\_\_\_\_\_\_  Manager, NAS Enterprise Architecture and Requirements (ANG-B1)  *(For NAS initiatives only)*  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date:\_\_\_\_\_\_\_\_\_\_\_\_\_  Director, Office of Information & Technology, Solution Delivery Service (ADE-001)  *(For Mission Support initiatives only)* |

Federal Aviation Administration
800 Independence Avenue
Washington, D.C. 20591

Table of Contents

[1. Introduction 1](#_Toc529891321)

[1.1 Context 1](#_Toc529891322)

[1.2 Problem Statement 1](#_Toc529891323)

[1.3 Concept Overview 1](#_Toc529891324)

[1.4 Alignment 2](#_Toc529891325)

[2. “As is” Operations 2](#_Toc529891326)

[2.1 [System] or [Subsystem 1] or [User 1]. 3](#_Toc529891327)

[3 Justification and Description of Changes 4](#_Toc529891328)

[4 “To Be” Operations 4](#_Toc529891329)

[4.1 Assumptions 4](#_Toc529891330)

[4.2 Constraints 5](#_Toc529891331)

[4.3 Operational Environment 5](#_Toc529891332)

[4.4 Concept Operations 6](#_Toc529891333)

[4.5 Supporting Infrastructure 6](#_Toc529891334)

[4.6 Benefits 7](#_Toc529891335)

[5 Operational Scenarios 7](#_Toc529891336)

[6 Summary of Impacts 7](#_Toc529891337)

[7 References 7](#_Toc529891338)

[Appendix A Acronyms 8](#_Toc529891339)

List of Figures

[Figure 1. Current Operational Environment 3](#_Toc98943418)

[Figure 2. [Name of AMS investment program] Operational Environment 6](#_Toc98943419)

[Figure 3. [Named Concept] Operations 6](#_Toc98943420)

List of Tables

[Table 1. Operational Concept Hierarchy 2](#_Toc527367564)

#

# Introduction

The purpose of this concept of operations document is to describe the *operational* and *functional* characteristics of the [Name of AMS investment program] concept in its intended operational environment. “Concept” in this document refers to the proposed concept.

## 1.1 Context

Briefly summarize the objective [i.e., how the concept fits into the overall mission]:

* Overall objective in relation to Federal Aviation Administration (FAA), National Airspace System (NAS) objectives (e,g., NextGen objectives, Service/Roadmap, FAA Orders and Policy, or Mission Support objectives.)
* High-level NAS or Mission Support areas supported/improved by the concept
* Key stakeholders (e.g., who will benefit / be impacted)
* Identify overall technical/operational approach (e.g., cloud storage, improved data processing) [i.e., focus on *what* the concept will resolve]
* Identify any key program phases or segments [briefly describe the overall phases, but restrict this Solution ConOps to the current phase only]
* Tailor this section as necessary for a system enhancement

## 1.2 Problem Statement

Briefly describe:

* Specific problem(s) or shortfall(s) in current operations addressed by the concept (e.g., shortfalls in technology, enterprise data, functionality, procedures, and policy). Summary problem and shortfall descriptions should align directly to those detailed within the concept’s corresponding Shortfall Analysis Report (SAR), when available

## 1.3 Concept Overview

Provide a high-level technical summary of the concept. This section serves as the basis for further detailed descriptions within Sections 2 – 6 of this document. The Concept Overview should include:

* How the concept addresses the identified shortfall(s)/shortfall mitigations
* Expected change(s) (e.g., enabling technologies, operational improvements, enhancements, and new capabilities)
* Expected benefits (e.g., safety, delay savings, flight efficiency, cost avoidance, environmental)
* Key impacts to stakeholders, NAS systems, functions, or enterprise data

The results of this section will be used to support the PRD template (section 1.2 – Scope).

## 1.4 Alignment

[Complete *one* of the following: NAS or Mission Support]

***NAS***

Identify how this concept traces to relevant NextGen Operational Improvements (OIs) or Current Operations (COs) or Business and Technology (B&T) initiatives.

Identify:

* Relationship of the concept within the Operational Concept Hierarchy (Table 1). Sub-service may not apply to your concept
* Specific timeframe that the concept applies to (e.g., Segment [i.e., Bravo, Charlie], target year)
* Key NextGen Portfolios, Current Operations, Operational Improvements, and increments supported by the concept. Describe how your concept addresses the increment(s) identified. Identify any OI(s), Business Technology Initiative (BTI), increment(s), and increment description for the service along with their associated identifier numbers. List them in tabular form

Note: Operational Improvements (OIs) and Increments should be identified in the Shortfall Analysis Report as programs need to describe how the needed services enable the operational improvements. A portion of an operational improvement that delivers incremental benefits is found in an increment and can be expressed as a shortfall. OIs and Increments should also be identified in the Concept of Operations (ConOps) as programs describe the set of capabilities which will result in operational improvements or achieve desired objectives for a proposed solution.  The functions from the proposed system are later documented in the Functional Analysis Document (FAD).

Table 1. Operational Concept Hierarchy

|  |  |  |
| --- | --- | --- |
|  | **CONCEPT LEVEL** | **HIERARCHY** |
| Level 1 | *Enterprise* | NextGen Mid-Term ConOps for the NAS |
| Level 2 | *Service* | Applicable domain ConOps (e.g., NextGen Weather) |
| Level 3 | *Sub-Service* |  |
| Level 4 | *Solution* |  |

***Mission Support***

For mission support concepts, identify how the concept traces to mission needs identified by FAA Orders, Policy, or relevant NAS programmatic metrics.

# “As - Is” Operations

Provide a detailed description of relevant current (“As-Is”) operations and systems (i.e., how things work today):

* Select an appropriate structure for the subsections (use as many sections/subsections as necessary). Sample structures include:
  + By type or class of facility
  + By user/stakeholder type or class
  + By NAS system, function, or capability
  + Combination of these and/or other classifications
* Reference the “As Is” Business Process Models (BPM) done during shortfall analysis
* Include a graphical overview of the existing service or system in the form of a context diagram, a top-level object diagram, BPM diagrams, or other graphic(s) depicting the existing operational environment (Figure 1). If this is an enhancement, use the “To-Be” base-lined system BPMs as the ‘As-Is” for the enhancement. The BPM models can be included in PRD form as an appendix

|  |
| --- |
| Graphical overview of the current (“As Is”)  operational environment |

Figure 1. Current Operational Environment

## 2.1 [System] or [Subsystem 1] or [User 1]

* In the description:
  + Describe the supporting infrastructure and the components in the NAS or Mission Support that interact with the current operation. If this is an enhancement, refer to the original baselined system information
    - Where appropriate, include sub-systems, adjacent systems, roles and responsibilities, procedures, airspace, and facilities. Tailor this statement for an enhancement
  + Where appropriate, include states (e.g., active, idle, degraded, or emergency) and modes of operation (e.g. primary, backup, maintenance and test, and training). For an enhancement, only include changes made to the system states by the enhancement
  + Emphasize shortfalls in the current operation or system and their impact on users (see the concept’s or enhancement’s SAR)

# Justification and Description of Changes

[Briefly summarize each of the key *changes* being proposed. Identify the shortfall, urgency, and how the concept will mitigate the issue. Select an appropriate structure for the descriptions (e.g., facility, user, system).]

Identify and clearly explain the changes that will be implemented by the concept, including the justification. Describe:

* Shortfalls in the current environment - this may be summarized from relevant sections of the SAR
* Shortfalls in the current business process - Reference “As-Is” BPMs with information flows developed during shortfalls analysis work
* The problem, urgency, and impact on users/stakeholders - this may be summarized from relevant sections of the SAR
* How the concept addresses the shortfalls
* New or modified aspects of current operations (e.g., proposed changes in systems, technology, information flows, processes, technology, procedures, etc.). If this is an enhancement, provide only the changes in the baseline system
* Include BPM diagrams to explain the operational changes and include the “To-Be” BPM diagrams in the appendices. If this is an enhancement, include the baseline system “To-Be” BPMs as the “As-Is” for the enhancement

# “To - Be” Operations

Provide an overview of the proposed concept, or alternative concepts. [The detailed description goes in Section 4.4]:

## 4.1 Assumptions

Identify any known *assumptions* specific to the proposed concept.

* Assumptions are events you expect to occur, but there is no guarantee
* Assumptions *are external to the concept*<u>,</u> and enable, guide, dictate, or control how the service or system is expected to operate (e.g., All commercial carriers will be equipped with *ADS-B* *Out* prior to concept initial operating capability [IOC])
* Focus on the proposed (“To-Be”) environment, not the current (“As-Is”) environment
* Provide assumptions in a list or table format

## 4.2 Constraints

Identify any known *constraints* specific to the proposed concept:

* Constraints are *known limitations* or factors which will impact the effectiveness or completeness of the solution (e.g., waterfall for upgrades essential for implementing the concept; cost, scope, time limits). For an enhancement, some constraints will be from the baselined system
* Include existing policies, procedures, technical issues, or other limitations that may require relief or change in order to adopt the concept (e.g., staffing, training, separation standards, first come/first served)
* Include existing information limitations with the enterprise data, enterprise data platform or data services limitations that may require change in order to adopt the concept and support Enterprise Information Management concepts
* Focus on the proposed (“To-Be”) environment, not the current (“As-Is”) environment
* Provide constraints in a list or table format

The constraints identified in this section will be used to support the PRD template (section 2.3 - Constraints).

## 4.3 Operational Environment

Describe relevant aspects of the environment in which the concept will be operating:

* Organize the sections by facility, phase of flight, or other logical structure
* Identify the concept characteristics (e.g., airports, airspace, facilities, technologies, services, or procedures). If this is an enhancement, identify characteristics that are only applicable to the enhancement; refer to baseline system ConOps sections if necessary
* Identify changes in the operational environment that are required to support the concept (e.g., facilities, systems, roles and responsibilities, training)
* Identify enterprise information in which the concept will collect, consume, create and/or change
* If appropriate, include a table to summarize key changes (e.g., columns identifying shortfalls, impacts, & mitigations)
* Include a figure depicting the concept in its operating environment (Figure 2). An Operational View (OV-1) may be used here

|  |
| --- |
| Graphical overview of the proposed (“To Be”) operational environment |

Figure 2. [Name of AMS investment program] Operational Environment

## 4.4 Concept of Operations

Describe the concept and its enhancements in detail:

* Include improvements in technological capabilities (e.g., automation, communication, navigation, surveillance, etc.) and systems
* Include changes to procedures, operations (e.g., sequencing and spacing, weather avoidance, service(s) delivery, and processes)
* Emphasize where specific improvements and changes address the shortfalls and demonstrate associated opportunities detailed in Section 3
* *Include a figure of key aspects of the concept (e.g., functions, components, systems, services, or interfaces) (Figure 3)*

|  |
| --- |
| Graphical overview of the concept |

Figure 3. [Named Concept] Operations

Provide a synopsis of this section in the PRD template (section 2.1 - Operational Concept).

## 4.5 Supporting Infrastructure

Describe the required infrastructure by including systems, services, information, and other infrastructure that are required to support the concept. Again, refer to baseline ConOps sections if this ConOps is for an enhancement.

## 4.6 Benefits

Describe the expected improvements:

* Include benefits to operations and to user’s/service providers
* Include benefits to management of enterprise information
* Describe benefit mechanisms in terms of improvement in capacity, efficiency, safety, environmental considerations, or other relevant areas (e.g., increased system capacity, improved schedule integrity, reduced delays, and reduced fuel consumption)
* If the concept is in the Service Analysis & Strategic Planning Phase, identify benefits from a qualitative perspective
* If the concept is in the Concept and Requirements Definition Phase, where possible, quantify the benefits in rough order of magnitude (ROM) terms; e.g., dollars, time, fuel savings, environmental impact. Capabilities not quantified are assessed qualitatively

# Operational Scenarios

Develop scenarios that:

* Include relevant assumptions and conditions to define the operational context
* Show how users interact with the system and how the system operates. Include detailed steps/bullets with any necessary descriptions, figures, or timelines
* Demonstrate key features or user benefits of the concept
* Illustrate a range of benefits (e.g., individual scenarios may be needed to demonstrate standard and contingency operations, operating modes, or different stakeholders/operations)
* Are solution agnostic

# Summary of Impacts

Summarize the impacts of the concept:

* Include operational and organizational impacts (in separate sections, if warranted)
* Include any key changes in user community, equity of airspace access, organization and staffing, training, airspace capacity, cost effectiveness, efficiency, environmental impact, global interoperability, enterprise information, reliability, maintainability, safety, and/or security

# References

Document all references (published and unpublished) used in the document.

Appendix A Acronyms

|  |  |
| --- | --- |
| **Acronym** | **Term** |
| AMS | Acquisition Management System |
| B&T | Business and Technology |
| BTI | Business Technology Initiative |
| ConOps | Concept of Operations |
| CRD | Concept Requirements Definition |
| COs | Current Operations |
| FAA | Federal Aviation Administration |
| IARD | Investment Analysis Readiness Decision |
| NAS | National Airspace System |
| NextGen | Next Generation Air Transportation System |
| OIs | Operational Improvements |
| SASP | Service Analysis and Strategic Planning |
| SAR | Shortfall Analysis Report |
