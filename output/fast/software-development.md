---
title: "Software Development"
source_url: https://fast.faa.gov/docs/sowgen_docs/templates/Software%20Development.docx
source_type: docx
converted: 2026-10-27
---
# Software Development

STATEMENT OF WORK

Software Development

**Warning:**

The Statement of Work (SOW) paragraphs, Contract Data Requirements List (CDRL) items, and Data Item Descriptions (DIDs) identified for your type of acquisition are recommendations only. You are expected to modify or add SOW paragraphs, CDRLs, or DIDs to address the specific requirements of your program.

**Table of Contents**

[1 Scope 1](#_Toc393455420)

[1.1 Locations 1](#_Toc393455421)

[2 Applicable Documents 1](#_Toc393455422)

[3 Technical Requirements 1](#_Toc393455423)

[3.1 Software Development 2](#_Toc393455424)

[3.1.1 Project Planning 2](#_Toc393455425)

[3.1.1.1 Software Development Plan (SDP) 2](#_Toc393455426)

[3.1.1.2 Size, Cost, Schedule, and Critical Computer Resource Estimations 2](#_Toc393455427)

[3.1.1.3 Work Breakdown Structure (WBS) 3](#_Toc393455428)

[3.1.1.4 Risk Management 3](#_Toc393455429)

[3.1.2 Project Tracking 3](#_Toc393455430)

[3.1.2.1 Metrics 3](#_Toc393455431)

[3.1.2.2 Software Development Folders/Files (SDF) 3](#_Toc393455432)

[3.1.2.3 Contract Data Requirements List (CDRL) Tracking 4](#_Toc393455433)

[3.1.3 Requirements Analysis 4](#_Toc393455434)

[3.1.4 Software Design 5](#_Toc393455435)

[3.1.5 Implementation 6](#_Toc393455436)

[3.1.5.1 Coding 6](#_Toc393455437)

[3.1.5.2 Testing 6](#_Toc393455438)

[3.1.5.3 Other 6](#_Toc393455439)

[3.1.6 Documentation 6](#_Toc393455440)

[3.1.7 Enhancements and Corrections 7](#_Toc393455441)

[3.1.8 Reviews 7](#_Toc393455442)

[3.1.9 Modeling and Simulation 8](#_Toc393455443)

[3.1.10 Transition Support 8](#_Toc393455444)

[3.2 Software Quality Assurance 8](#_Toc393455445)

[3.3 Configuration and Data Management 9](#_Toc393455446)

[3.3.1 Configuration Management (CM) and Control 9](#_Toc393455447)

[3.3.2 Data Management 10](#_Toc393455448)

[3.4 Independent Verification and Validation 10](#_Toc393455449)

[3.5 Status and Project Support 10](#_Toc393455450)

[3.6 Post Project Review 11](#_Toc393455451)

# 1 Scope

This Statement of Work (SOW) specifies the software development services required by the [*name of organization*], necessary to accomplish its mission.

[*Name of organization*], provides aviation [name of system(s), i.e. communication, navigation, or surveillance] that are integral components of the National Airspace System (NAS). The NAS provides the flying public with air traffic control services designed to ensure air transportation safety. The [*name of organization*] is responsible for providing technical and engineering direction and program management for many long-term NAS [name of system(s), i.e. communication, navigation, or surveillance] projects through various stages of implementation. Specific FAA programs include [name of program(s)] programs. The individual [name of system(s), i.e. communication, navigation, or surveillance] projects within these areas must satisfy the requirements of the NAS as implemented by the FAA.

There are currently [# *of teams*] and [*type of team*] Teams within the [*name of organization*] organization:

[List team(s) here]

This information is provided to establish an initial project baseline for this SOW and is subject to change.

The following programs are supported within the [*name of organization*] organization:

[List program(s) here]

Other programs and projects may be added at the discretion and direction of the Contracting Officer (CO) and the Contracting Officer's Representative (COR)/Delivery Order Contracting Officer's Representative (DOCOR).

## 1.1 Locations

The Contractor must perform the work activities described in this SOW on-site at FAA [site] and/or offsite as required. However, some tasks may require the Contractor to travel to one or more locations in support of the work effort, at the direction of the COR/DOCOR:

# 2 Applicable Documents

The following documents are a part of this contract, to the extent herein, or as specified in the individual Task/Delivery Orders issued under this contract. Succeeding revisions must be substituted or incorporated via administrative modification.

[*List your documents*]

# 3 Technical Requirements

The contractor must perform software engineering tasks for the development, evaluation, support, and maintenance of all software and associated documentation that include analysis, design, development, change implementation, and system test and evaluation. The following general task area descriptions are indicative of the work required in order to provide systems engineering support to SSC SD. The ordering of the task descriptions should not be viewed as a prioritization of the contractor support requirements.

## 3.1 Software Development

The contractor must plan, analyze, investigate, design, code, test, integrate, implement, evaluate, support, and deliver software or changes to software for [*identify project/program*].

The Government reserves the right to witness all contractor efforts to accomplish the SOW requirements and maintains the right to approve or reject resulting processes and products before subsequent related processes and products are implemented.

The contractor must maintain an interface with Government project personnel, users, sponsors, software quality and configuration management personnel, and the independent verification and validation agent throughout the execution of this SOW.

### 3.1.1 Project Planning

#### 3.1.1.1 Software Development Plan (SDP)

The contractor must develop and deliver a comprehensive SDP to define the products, the processes, and tailoring by which the products will be developed, to identify and address risks, to identify resource requirements (skill levels, facilities, computer resources) and schedules, to describe the metrics program, to define the contractor's software management organization and its interfaces, and to define use of automated tools. If separate Configuration Management and Risk Management Plans are not developed, they must be included in the Software Development Plan. The contractor must update the SDP at least after each major review.

CDRL A001 Software Development Plan

CDRL A002 Contractor's Configuration Management Plan

#### 3.1.1.2 Size, Cost, Schedule, and Critical Computer Resource Estimations

The contractor must use formal procedures to provide software size, cost, schedule, and critical computer resource estimations. A software size estimation methodology to determine the number of the delivered source lines of code (SLOC) or function points must be used to determine all module sizes comprising any software system to be developed. SLOC is defined as all executable source code statements including deliverable Job Control Language statements, Data Declarations, Data Typing statements, Equivalence statements, and input/output format statements. SLOC does not include any statement that upon its removal the program will still compile, e.g. comments, blank lines and non-delivered programmer debug statements. Ada source lines are counted as non-comment, non-embedded semi-colons, counting generics only once. Software size estimation must include estimation of software document sizes.

The contractor must use software scheduling and cost models to determine the most feasible schedules and costs for all phases of the software life cycle to include a detailed rationale for each estimate. This data must be recorded in the Software Estimation File (SEF).

The contractor must periodically provide updated size, cost, schedule, and critical computer resource estimates to accurately assess current project status. Size, cost, schedule, and critical computer resource variance must be tracked by the contractor. These models may be automated or manually implemented. This data must be recorded in the SEF.

CDRL A003 Contractor's Progress, Status and Management Report

CDRL A004 Technical Report-Study/Services

#### 3.1.1.3 Work Breakdown Structure (WBS)

The contractor must develop a detailed WBS as a section in the SDP to define precise and measurable tasks, milestones, reviews, deliverables, and mapping to the Computer Software Unit level.

CDRL A004 Technical Report-Study/Services

#### 3.1.1.4 Risk Management

The contractor must describe the procedures to be used for managing areas of risk to successful project completion in a Risk Management Plan. The Risk Management Plan must identify and prioritize as High, Medium, or Low, the areas of risk, identify the risk factors that contribute to the potential occurrence of each risk, document procedures and metrics for monitoring the risk factors and for reducing the potential occurrence of each risk, and identify contingency procedures for each area of risk. The contractor must monitor and report on the areas of potential risk.

CDRL A004 Technical Report-Study/Services

### 3.1.2 Project Tracking

#### 3.1.2.1 Metrics

The contractor must define procedures for software metrics collection and analysis. Software metrics, including product, productivity, quality, and management metrics, must be used to assure the quality of all software and documentation produced. Metrics must include Cost, Schedule, Progress, Size (software and documentation), System Maturity/Stability (requirements testability, requirements traceability, design complexity, and changes/requirements stability), Build/Release Content, Computer Resource Utilization and Throughput, Defects, and Action Items.

The contractor must perform analysis of software performance and system sizing, generating technical reports of the results and software architectural enhancements to improve the sizing and performance of the software.

CDRL A003 Contractor's Progress, Status and Management Report

CDRL A004 Technical Report-Study/Services

#### 3.1.2.2 Software Development Folders/Files (SDF)

The contractor must document and implement procedures for establishing and maintaining SDFs. Software Development Folders/Files include, directly or by reference, design considerations and constraints, design documentation and data, schedule and status information, results from reviews and inspections, test requirements and responsibilities, test cases, procedures, and results, open and resolved defect reports and action items, and rationales for significant decisions.

CDRL A004 Technical Report-Study/Services

#### 3.1.2.3 Contract Data Requirements List (CDRL) Tracking

The contractor must develop, implement, maintain, and report on a Contract Data List Requirements tracking system to provide current status of all deliverables, including due dates, delivered dates, accept/reject status, review cycles and results, status, and interface with other deliverables.

CDRL A004 Technical Report-Study/Services

### 3.1.3 Requirements Analysis

The contractor must perform software requirement analysis on existing and/or new systems and evaluate these systems' capabilities to meet both functional and non-functional requirements. Functional requirements include the technical/operational functions the software must be capable of performing. Non-functional requirements include characteristics of software to be achieved, such as, performance, reliability, maintainability, security, safety, and error handling. The analysis must also include generation of interface requirements and performance specifications needed to assure all components including software, hardware, and user, will work together to meet overall requirements. Agreement must be reached regarding the requirements among the system developers, sponsors, SSC SD project personnel, the independent verification and validation agent, and users of the end product. The contractor must define the agreed to system requirements in System/Subsystem Specification (SSS), Interface Requirements Specification (IRS), and Software Requirements Specification (SRS) documentation. The contractor must document the traceability of all software requirements from the SSS, IRS, and SRS documentation.

The contractor must provide requirement analysis. The analysis must include:

* Identification of requirements by eliciting these requirements from end users associated with the task, deriving from system requirements, and/or determining by task analysis. A traceability matrix must be produced to trace each identified requirement from origin through lowest level component
* Identification of development constraints including cost, resources, time/schedule, budget, hardware to be supported, existing software to be utilized, portability and maintainability requirements, and anticipated changes
* Analysis of requirements to assess potential problems, prioritization and evaluation of feasibility of implementation and alternative solutions (risk management)
* Representation of requirements with proper notation such as prototyping, modeling, or use of requirements analysis tools
* Communication of requirements in a clear manner to ensure consistent understanding among all players and to reduce ambiguity
* Demonstration of the verification and validation of software requirements through traceability matrices, and test plans

Requirement analysis methodologies must be used to ensure the completeness and clarity of all requirements. Rapid prototyping must be used as a means of requirement analysis. Requirements metrics must be collected, analyzed, and reported.

CDRL A003 Contractor Progress, Status and Management Report

CDRL A004 Technical Report-Study/Services

CDRL A005 System/Subsystem Specification (SSS)

CDRL A006 Interface Requirements Specification (IRS)

CDRL A007 Software Requirements Specification (SRS)

### 3.1.4 Software Design

The contractor must determine preliminary and detailed software design practices to ensure the quality and maintainability of all systems. Agreement must be reached regarding the design among the system developers, sponsors, SSC SD project personnel, the independent verification and validation agent, and users of the end product. The contractor must define the agreed to design in the Software Design Description (SDD), the System/Subsystem Design Description (SSDD), the Database Design Descriptions (DBDDs), and the Interface Design Description (IDD).

Preliminary design must include postulating and modeling a solution for each requirement, evaluating it against the original requirements, and then transforming it into data and software architecture. Detailed design must include determining detailed specifications (template) for implementation (production of code) and, refining the architectural representation that leads to detailed data structures and algorithmic representations of software. These processes may be automated or manually implemented.

The contractor must perform the required planning, design, and analysis in order to integrate components or modules within a system, including installation and check-out of the integrated components.

A traceability matrix must be produced to trace each identified software requirement from origin through lowest level component.

CDRL A004 Technical Report-Study/Services

CDRL A008 Software Design Description (SDD)

CDRL A009 Database Design Description (DBDD)

CDRL A010 Interface Design Description (IDD)

CDRL A011 System/Subsystem Design Description (SSDD)

### 3.1.5 Implementation

#### 3.1.5.1 Coding

The contractor must comply with coding standards as specified in the project specific Software Development Plan to develop software modules that implement the detailed design. Reusable software must be one of the means to satisfy the requirements of this SOW.

#### 3.1.5.2 Testing

The contractor must use well-defined written procedures and standards for software testing and produce applicable documentation. Each software requirement must be testable and documented in a Software Test Plan to include testing objectives, priorities, methodologies, specifications and evaluation criteria for each test. Software Test Descriptions must include detailed test cases and procedures necessary to execute the Software Test Plan. A Software Test Report must record the test results and analysis of applying the Software Test Plan to the implementation of the Software Test Description.

The contractor must perform checkout functions, debugging, and equipment and system software integration. The contractor must provide test integration of individual modules, subroutines, subsystems, and systems. Levels of testing must include Software Unit (SU) testing, and Computer Software Configuration Item (CSCI) Formal Qualification Testing (FQT), System testing, Integration testing, and Regression testing.

CDRL A012 Software Test Plan (STP)

CDRL A013 Software Test Description (STD)

CDRL A014 Software Test Report (STR)

#### 3.1.5.3 Other

The contractor must produce updated source code, operations and support documents version description documents and software product specifications.

CDRL A015 Software Version Description (SVD)

CDRL A016 Software Product Specification (SPS)

### 3.1.6 Documentation

The contractor must prepare, revise, and/or review software documentation during the appropriate phase of the life cycle, including technical reports to document algorithm analysis, feasibility studies, trade-off, and impact analyses. All documentation must be updated to remain current with each software development activity/phase.

The contractor must perform engineering analysis (reverse engineering) of implemented software products and develop new, or modify existing documentation, to correctly reflect the implemented code. The documentation must provide the necessary information to support life cycle maintenance of the software product by the Government.

CDRL A017 Revisions to Existing Government Documents

### 3.1.7 Enhancements and Corrections

The contractor must investigate, plan, estimate, design, code, test, and integrate enhancements and/or corrections to the software or documentation covered under this SOW. The contractor must provide change engineering and implementation support as follows: Change engineering tasks include the technical preparation, impact evaluation/analysis, and planning necessary to implement or disapprove software change proposals Software Change Proposals (SCPs), Software Trouble Reports (STRs), Engineering Change Proposals (ECPs), Program Change Proposals (PCPs), Specification Change Notices (SCNs), System/Software Change Requests (SCRs), Document Change Requests (DCRs), Development Problem Reports (DPRs), Software Anomaly Reports (SARs) (all herein after referred to as Change Proposals). These change proposals may pertain to system errors, problems, or changes, as well as to program updates in the form of new releases, or versions. They may be written against the software, documentation, or interfaces for which the contractor has responsibility.

The contractor must apply development activities to change proposals (i.e. requirements analysis, design, reviews, and walkthroughs), and then implement only Government approved change proposals by developing and testing computer program packages based on these changes, and updating documentation affected by the changes. The contractor must install the revised software and train the operations and maintenance personnel concerning the changed portions if required. The contractor must identify and report any Integrated Logistic Support (ILS) requirements which result from system software changes.

The contractor must prepare and evaluate proposed Requests for Deviation/Waivers (RFD/RFW) to address proposed/requested/approved changes to the software, documentation, or baselines when requested by the Contracting Officer's Technical Representative (COR).

The contractor must develop and maintain a change proposal tracking system.

CDRL A004 Technical Report-Study/Services

CDRL A015 Software Version Description (SVD)

CDRL A016 Software Product Specification (SPS)

CDRL A018 Request for Deviation (RFD)

CDRL A022 Document Changes

CDRL A028 Software Installation Plan (SIP)

### 3.1.8 Reviews

The contractor must perform detailed reviews, walkthroughs, requirement traceability analyses, and defined verification and validation processes which occur during the course of software development to ensure that requirements are traceable, consistent, complete, and testable. The contractor must ensure the software correctly reflects the documented requirements. The contractor must prepare for, participate in, and report on, both formal and informal reviews and inspections for the purpose of determining whether advancement to the next phase is warranted. For each review, the contractor must coordinate with the Software Quality Evaluation and Independent Verification and Validation Agents for inclusion of their findings. The contractor must use the SSC SD Peer Review Process or equivalent for review of the work products.

CDRL A020 Conference Minutes

CDRL A021 Conference Agenda

### 3.1.9 Modeling and Simulation

The contractor must develop new, modify existing, and maintain current models and simulations to support the verification and validation of requirements, design, and code.

### 3.1.10 Transition Support

The contractor must deliver software and documentation that can be regenerated and maintained using commercially available, Government owned, or contractually deliverable software and hardware that has been identified by the Government. The contractor must provide support for transition of the delivered system to the Government or its specified agent. Contractor must prepare a project specific Software Transition Plan (STRP). The STRP must address products to be turned over (software, hardware, and tools), formats and media, schedules, and support during transition. The contractor must perform installation and checkout of the deliverable software in the support environment and provide training and installation support to the activity acquiring the system. The contractor must develop and deliver the following software support and operational documentation: Computer Operation Manual (COM), Software User's Manual (SUM), Computer Programming Manual (CPM) and Firmware Support Manual (FSM).

CDRL A022 Document Changes

CDRL A023 Computer Operation Manual (COM)

CDRL A024 Computer Programming Manual (CPM)

CDRL A025 Software User Manual (SUM)

CDRL A026 Firmware Support Manual (FSM)

CDRL A027 Software Transition Plan (STRP)

CDRL A028 Software Installation Plan (SIP)

## 3.2 Software Quality Assurance

The contractor must perform independent activities to assure the quality of all software and documentation produced under this SOW and to ensure compliance with all requirements of this contract.

The contractor must develop, implement, and maintain a Software Quality Plan (SQP) to include resources required, schedules, tasks to be performed, procedures and tools to be used, records to be provided, the methodology of identifying and implementing process improvements in the software development processes and related management areas, and the contractor's software quality organization and interfaces. The Software Quality Plan will describe how the contractor's overall software quality program will be applied.

The contractor must perform detailed reviews, walkthroughs, requirement traceability analyses, and defined verification and validation processes which occur during the course of software development to ensure that requirements are traceable, consistent, complete, and testable. The contractor must ensure the software correctly reflects the documented requirements. The contractor must prepare for, conduct, report on, and/or participate in formal reviews, informal reviews, inspections, peer reviews, tests, and evaluations for the purpose of determining whether advancement to the next phase is warranted.

The contractor must ensure that quality assurance requirements are enforced for all aspects of software development and/or revision.

The contractor must collect and analyze software quality metrics which include traceability, completeness, consistency, accuracy, simplicity, and modularity. The metrics are directly related to the non-functional requirements specified for the software.

CDRL A020 Conference Minutes

CDRL A021 Conference Agenda

CDRL A004 Technical Report-Study/Services

## 3.3 Configuration and Data Management

### 3.3.1 Configuration Management (CM) and Control

The contractor must plan, implement, and maintain a comprehensive configuration management program. The CM process must include developing, implementing and maintaining a Software Configuration Management Plan (SCMP) to define and describe methods and procedures to be used to manage configuration items and their interfaces and promote usability.

This effort must also include establishing and maintaining a Software Development Library to provide storage of and controlled access to software, documentation, and associated tools and procedures. The library must also contain management data pertinent to the software development project.

The contractor must decompose the system into software configuration items, and all functional and physical characteristics of these items must be identified, documented, and tracked.

The contractor must conduct audits to assure conformance to requirements of established baselines. The contractor must plan and participate in the conduct of functional and physical configuration audits. The contractor must conform to change control procedures to ensure incorporation of approved changes only, ensure effectiveness of test objectives, and ensure that the developed software product is the same as the specified software product.

The contractor must maintain a change control system to manage all proposed and implemented changes to software configuration items to include the following areas: establishing a developmental configuration for each Computer Software Configuration Item (CSCI), maintaining current copies of all deliverable items, providing access to these items, and controlling the preparation and dissemination of changes to these items.

The contractor must provide technical representation to the SSC SD Project Software Change Control Board for the evaluation and disposition of all proposed changes to the software and documentation produced under this SOW.

The contractor must perform status accounting to provide traceability of changes to controlled products, serve as the basis for communicating the status of all configuration items, serve as the vehicle for ensuring the delivered documents describe and represent the associated software.

CDRL A002 Contractor's Configuration Management Plan

CDRL A029 Configuration Status Accounting Information

CDRL A031 Configuration Audit Summary Report

CDRL A032 Engineering Release Record (ERR)

CDRL A033 Engineering Change Proposal (ECP)

CDRL A034 Notice of Revision (NOR)

CDRL A035 Specification Change Notice (SCN)

CDRL A039 Interface Control Document (ICD)

CDRL A036 Installation Completion Notification (ICN)

### 3.3.2 Data Management

The contractor must perform data management for the documentation and material associated with the project under the cognizance of this SOW. The contractor must collect, log, and store data base elements in the areas of project process control, project status, presentation data, and project master files with a means for rapid data retrieval.

CDRL A004 Technical Report-Study/Services

## 3.4 Independent Verification and Validation

It is the intent of the Government to utilize an Independent Verification and Validation agent during the entire life of this contract to monitor the development effort and assess the utility of the operational products. The development contractor must jointly establish, with the IV&V contractor and the Government, an Independent Verification and Validation Plan to address, at a minimum, communication protocol, methods of access, joint operating procedures, specific tasks, schedules, organization, reporting, and responsibilities, and close out procedures.

The IV&V agent must participate in all major development reviews, audits, inspections, walkthroughs, and tests, and must review and provide comments on all documentation. The IV&V agent must also conduct independent evaluations, reviews, and tests of the developer's processes and products.

The IV&V agent must submit status reports and attend weekly meetings with the developer to keep the developer apprised of concerns and to discuss potential solutions and resulting action items.

The development contractor must provide easy access to all software, documentation, and information and knowledge necessary to assess the quality of the processes and products and must notify the Government of the schedule of all above mentioned activities in time to allow all participants to be notified and prepared.

## 3.5 Status and Project Support

The contractor must submit a progress and status report.

The contractor must develop and maintain an Action Item Tracking system to keep current status on all action items to include, as a minimum, a synopsis of the action required, responsible individual/point of contact, assigned date, due date, and status. This report must be discussed at a weekly team meeting comprising both Government and contractor personnel. The contractor must attend these meetings and provide current Action Item Tracking data.

The contractor must manage project related correspondence and track project management milestones.

The contractor must participate in and monitor project level and technical interchange meetings and deliver reports of proceedings including copies of minutes.

The contractor must participate in technical meetings, briefings, presentations, and reviews, and prepare reports of these events.

CDRL A003 Contractor's Progress, Status & Management Report

## 3.6 Post Project Review

The contractor must participate in the Government led Post Project Review at, or near, the end of the project supported by this SOW. The purpose of the review is to determine the level of success of this project and to document lessons learned to improve the quality of the next project. The focus of the Post Project Review will be on topics such as:

* Were all requirements met?
* Did tasks track to the Work Breakdown Structure?
* Were all deliverables acceptably received?
* Was the project completed on time?
* How much did it cost compared to the estimates?
* What problems were encountered?
* How much time was spent on unplanned tasks?
* Were the metrics collected during the project useful?
* Was the project organization effective (e.g. CM, SQA)?
* How communications among all participants could be improved?
* What specifically could be done better next time?

The contractor must prepare the Lessons Learned and Recommendations Report to include all information resulting from this review. This report will be used by both the Government and the contractor as input to their organizations' Software Process Improvement Plans.

CDRL A004 Technical Report-Study/Service
