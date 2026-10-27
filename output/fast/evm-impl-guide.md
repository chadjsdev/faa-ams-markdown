---
title: "EVM Impl Guide"
source_url: https://fast.faa.gov/docs/EVM%20Impl%20Guide.docx
source_type: docx
converted: 2026-10-27
---
# EVM Impl Guide

tratu

![](data:image/png;base64...)

***Acquisition Management System Guidance***

**Federal Aviation Administration (FAA) Earned Value Management (EVM) Implementation Guide**

**April 2025**

**VERSION CONTROL TABLE**

|  |  |  |  |
| --- | --- | --- | --- |
| **REVISION** | **DATE** | **FIGURE, TABLE, PARAGRAPH, OR DOCUMENT NUMBERS** | **TITLE OR BRIEF DESCRIPTION** |
| 4.0 | March 2024 | Not Applicable. | Fourth version delivered to EVMFP for distribution. Includes minor edits, formatting, and removal of Appendices. |
| 3.0 | November 2024 | Not Applicable. | Third version delivered to EVMFP for distribution. |
| 2.0 | August 2024 | Not Applicable. | Second version delivered to EVMFP for distribution. |
| 1.0 | July 2024 | Not Applicable. | Original version delivered to EVM Focal Point (EVMFP) for distribution. |

**TABLE OF CONTENTS**

[**FAA EVM IMPLEMENTATION GUIDE’S PURPOSE AND OBJECTIVES** 1](#_Toc192658773)

[**Document Organization** 1](#_Toc192658774)

[**SECTION 1.0 Implementation of EVM at FAA** 2](#_Toc192658775)

[**1.1 EVM and FAA Lifecycle Management Process** 3](#_Toc192658776)

[**SECTION 2.0: EARNED VALUE MANAGEMENT ROLES AND RESPONSIBILITIES** 4](#_Toc192658777)

[**2.1 Program Manager** 4](#_Toc192658778)

[**2.2 Control Account Manager**  5](#_Toc192658779)

[**2.3 Business Manager / Program Control Manager** 7](#_Toc192658780)

[**2.4 EV Analyst** 7](#_Toc192658781)

[**2.5 Scheduler** 8](#_Toc192658782)

[**2.6 Risk Analyst/Manager** 9](#_Toc192658783)

[**SECTION 3.0: FAA PROGRAM ORGANIZATION FRAMEWORK** 10](#_Toc192658784)

[**3.1 Investment Analysis (Planning) Phase (Pre-FID) Activities** 10](#_Toc192658785)

[**3.1.1 Pre-FID EVM Activities that align with the NDIA Guidelines** 10](#_Toc192658786)

[**3.1.2 The Office of Investment Planning & Analysis (IP&A)** 13](#_Toc192658787)

[**3.1.3 Implementation Strategy and Planning Document** 13](#_Toc192658788)

[**3.1.4 Program IT Dashboard Milestone Table** 14](#_Toc192658789)

[**3.1.5 Program Management Plan** 14](#_Toc192658790)

[**3.1.6 Earned Value Management Plan** 15](#_Toc192658791)

[**3.1.7 Earned Value Management System Description** 15](#_Toc192658792)

[**3.1.8 Earned Value Management Determination (EVMD)** 15](#_Toc192658793)

[**3.1.9 FAA Standard Work Breakdown Structure (WBS)** 17](#_Toc192658794)

[**3.2 Solution Implementation Phase (Post FID) Activities** 19](#_Toc192658795)

[**3.2.1 Update EVM Planning Documents** 19](#_Toc192658796)

[**SECTION 4.0: FAA EARNED VALUE MANAGEMENT PMB BASELINE COMPONENTS** 19](#_Toc192658797)

[**4.1 Acquisition Program Baseline Components** 19](#_Toc192658798)

[**4.1.1 Estimated Lifecycle Cost** 19](#_Toc192658799)

[**4.1.2 EVM Total Allocated Budget Attributes** 20](#_Toc192658800)

[**4.1.3 Acquisition Program Baseline** 20](#_Toc192658801)

[**4.1.4 Management Reserve** 21](#_Toc192658802)

[**SECTION 5.0: ESTABLISH EARNED VALUE MANAGEMENT PMB** 22](#_Toc192658803)

[**5.1 Control Account Budget Components** 22](#_Toc192658804)

[**5.2** **Establish Program Performance Baseline** 23](#_Toc192658805)

[**5.2.1** **Development of Management Reserve** 23](#_Toc192658806)

[**5.2.2** **Program Detailed Schedule** 23](#_Toc192658807)

[**5.2.3** **Program Detailed Budgets** 24](#_Toc192658808)

[**5.2.4** **Work Authorization Document**  24](#_Toc192658809)

[**SECTION 6.0: FAA PROGRAM ANALYSIS AND MANAGEMENT REPORTING** 24](#_Toc192658810)

[**6.1 FAA Program Analysis and Management Reporting** 24](#_Toc192658811)

[**6.2 Variance Reporting APB-Level** 25](#_Toc192658812)

[**6.3 Status Program Schedule/Program Schedule Changes** 25](#_Toc192658813)

[**6.4 Earned Value Calculations** 25](#_Toc192658814)

[**6.4.1** **Estimated Costs for Earned Value Work Accomplished** 26](#_Toc192658815)

[**6.5 Summarized EVM Performance Measurement Data** 27](#_Toc192658816)

[**6.6 Generate Earned Value Reports** 27](#_Toc192658817)

[**6.7 Internal Review by Program Manager/Program Control** 28](#_Toc192658818)

[**SECTION 7.0: PMB REVISIONS AND DATA MAINTENANCE** 28](#_Toc192658819)

[**7.1 Baseline Reconciliation** 28](#_Toc192658820)

[**7.2 PMB Change Control** 29](#_Toc192658821)

[**7.3 Change Control Process** 29](#_Toc192658822)

[**7.4 Types of Baseline Change Request** 30](#_Toc192658823)

[**SECTION 8.0: EVM GOVERNANCE** 31](#_Toc192658824)

[**8.1 Program Integrated Baseline Review (IBR)** 31](#_Toc192658825)

[**8.2** **Contractor Level IBR** 32](#_Toc192658826)

[**8.3** **Program Surveillance** 33](#_Toc192658827)

# **FAA EVM IMPLEMENTATION GUIDE’S PURPOSE AND OBJECTIVES**

The Federal Aviation Administration's (FAA) Earned Value Management (EVM) Implementation Guide is designed to serve as a comprehensive resource for integrating the principles and practices of EVM into the FAA's program management processes. The goal is to coordinate the requirements of the Office of Management and Budget's (OMB) Circular No. A-11 Part 7, Appendices and Capital Programming Guide, with the specific needs and standards of the FAA while emphasizing the critical roles of risk management and performance measurement in successful program execution.

At the FAA, programs are defined as Major IT Investments in the IT Portfolio requiring special management attention because of their importance to the mission or function of the government; significant program or policy implications; high executive visibility; high development, operating, or maintenance cost, unusual funding mechanism, or defined as a major by the Agency’s Capital Planning and Investment Control (CPIC) Process. Additionally, OMB may work with the agency to declare IT Investments as Major IT Investments. A Chief Information Officer (CIO) rating is also required to be a Major IT Investment, and the investment may have additional reporting requirements via the Agency IT Portfolio Summary Detail.

The FAA EVM Implementation Guide will provide direction for the EVM implementation, which serves as a critical component of risk management and provides an early warning system for cost overruns and schedule delays. It also highlights the importance of performance management, which includes establishing a Performance Measurement Baseline (PMB) and using designated cost, schedule, and technical metrics. These elements are essential for enabling informed decision-making and providing FAA management with the tools necessary for effective integrated program management.

## **Document Organization**

This document is organized to provide a comprehensive understanding of the implementation of EVMS at the FAA by facilitating the practical application of EVM principles in FAA program management processes. Each section is designed to provide insight and practical steps to implement, control, execute, and maintain an EVMS at the FAA. The guide is structured in the following sequence:

* Section 1.0: Implementation of EVM at FAA
* Section 2.0: Earned Value Management Roles and Responsibilities
* Section 3.0: FAA Program Organization Framework
* Section 4.0: FAA Earned Value Management PMB Baseline Components
* Section 5.0: Establish Earned Value Management PMB
* Section 6.0: FAA Program Analysis and Management Reporting
* Section 7.0: PMB Revisions and Data Maintenance
* Section 8.0: EVM Governance

# **SECTION** **1.0 Implementation of EVM at FAA**

The FAA requires Major IT Investments in the IT Portfolio, such as Terminal Flight Data Manager (TFDM), En Route Automation Modernization (ERAM), System Approach for Safety Oversight (SASO), and Enterprise-Information Display System (E-IDS) to perform EVM and report EVM metrics monthly to the Joint Resources Council (JRC) AAP-200, the EVM Focal Point (EVMFP) Office AAP- 410, and the PMO Program Health and Analytics Team, AJM-122.

EVM is a methodology that integrates a program’s (or contract's) work scope, schedule, and resources with risk management, thereby providing government and contractor managers with objective visibility into the progress of their programs, enhancing their ability to manage programs effectively. EVM enables Program Managers (PMs) to determine if a program is on track, predict the future performance of the program, and make informed decisions to achieve program objectives efficiently. Ultimately, the goal is to improve program management and control by enabling data-driven decisions throughout the program’s lifecycle.

To address the OMB Circular A-11 requirement for the application of EVM on programs, the FAA uses a two-tier approach to implement EVM on its major developmental programs. Tier 1 is the implementation of EVM in the FAA Program Offices (POs), referred to as program-level EVM. Program-level EVM is required for all FAA programs identified as Major IT Investments by OMB memo M-10-27 with Acquisition Management System (AMS) Policy requirements for EVM. The program-level data is subject to integrated performance measurement analysis, which includes the development of EVM metrics by the PO, which use input from the contractor's Integrated Program Management Report (IPMR) Formats 1, 3, 5, and 6 and support contractor metrics. The FAA POs provide EVM metrics, including IPMR Formats 1, 3, 5, and 6, which they develop at the program-level, to the EVMFP Office monthly. Program-level EVM does not include government Full-Time Equivalents (FTEs), Activity 5, or Operations and Maintenance (O&M) metrics.

Tier 2 involves contractor-level EVM, which is subject to integrated performance measurement analysis performed by the contractor and reported to the government in IPMR Formats 1, 3, 5, and 6 on a monthly basis. The contractor is required to have a validated EVMS that meets the guidelines in Electronics Industry Association (EIA) -748, "Earned Value Management Systems," and possess a current EVMS Acceptance Letter or an EVMS Validation Letter from the Department of Defense (DOD)/ Defense Contract Management Agency (DCMA), National Aeronautics and Space Administration (NASA), FAA, or a qualified third party that conducts EVMS validations.

The EVM Implementation Guide will lead the reader through the FAA's approach to EVM application. Its goal is to ensure that integrated performance measurement is properly implemented and conducted, allowing for the systematic implementation of EVM throughout the organization.

## **1.1 EVM and FAA Lifecycle Management Process**

To understand how EVM fits within the FAA Lifecycle Process, it is necessary to understand its relationship to the program Phases. EVMS is included in the Investment Analysis (Planning) Phase, which occurs pre-Final Investment Decision (FID) and the Solution Implementation Phase, which occurs post-FID, within the FAA Lifecycle Management Process, along with acquisition planning timelines.

Lifecycle acquisition management is built around a logical sequence of phases and decision points (see Figure 1, which describes the EVMS decision points and how the EVMS fits into the Lifecycle process). The FAA uses these phases and decision points to determine and prioritize its needs, make sound investment decisions, implement solutions efficiently, and manage services and assets over their lifecycle. The overarching goal is continuous improvement in delivering safe, secure, and efficient services over time. Application is flexible and may be tailored by the FAA Acquisition Executive (FAE) or JRC.

The FAA Lifecycle Management Process begins with Research for Service Analysis, which includes Service Analysis and Strategic Planning. Pre-FID EVM planning occurs during this phase. Section 3.1 Investment Analysis (Planning) Phase (Pre-FID) Activities (below) discusses these EVM activities. Service Analysis and Strategic Planning are followed by the Concepts and Requirements Definition Phase and subsequently by the Investment Analysis Phase. The EVMFP Office establishes the EVM Determination (EVMD) within the Initial Investment Analysis (IIA). This is recorded in the EVMD document, with all required signatures in place by the FID, which happens at the Final Investment Analysis (FIA).

The Solution Implementation Phase is the control process. This is where EVM is implemented and reported. A program stops reporting EVM when it reaches the In-service Management Phase, and all Facilities and Equipment (F&E) funds have been expended. Information on baseline closeout can be found in Section 9.3 Process Steps Baseline Management Closeout of the FAA Acquisition Baseline Management Standard Operating Procedure – July 2024 on the FAA Acquisition System Toolset (FAST).

![A diagram of a lifecycle management process  Description automatically generated](data:image/png;base64...)

Figure 1.The FAA Lifecycle Management Process

# **SECTION 2.0: EARNED VALUE MANAGEMENT ROLES AND RESPONSIBILITIES**

EVM requires the coordination of six key roles and the ability to effectively implement and report the schedule and cost performance of the technical accomplishments related to the FAA AMS standard program milestones. The six key roles are PM, Control Account Manager (CAM), Business Manager/Program Control Manager, EVM Analyst, Scheduler, and Risk Manager.

## **2.1 Program Manager**

The PM is an individual assigned responsibility and authority for accomplishing program goals and scope approved by the JRC. The PM is typically responsible for planning, implementing, controlling, and reporting cost, schedule, and technical performance on a particular program.

The PM assumes overall responsibility for implementing and using an EVMS throughout the program for Development, Modernization, and Enhancement (DM&E) activities as defined in the AMS and documented in the JRC-approved Acquisition Program Baselines (APB). Responsibilities include program planning, approving resource work authorization, managing funding, administration of Management Reserve (MR), program performance reporting overview, and managing the schedule, cost, and risk. The following is a list of program-level specific responsibilities that are conducted by the PM:

* Guidance and direction of the development of the program Work Breakdown Structure (WBS) and the WBS Dictionary;
* Guidance of the establishment of the Control Accounts (CAs) and direction to the responsible managers;
* Approval of the Responsibility Assignment Matrix (RAM) used to document the PMB by CA and map to the program IT Dashboard cost/schedule milestone table;
* Approval of the program Integrated Master Schedule (IMS) used to plan and status schedule accomplishments;
* Approval of the level of the schedule critical path reporting that identifies program schedule risks during the Solution Implementation Phase;
* Approval of the schedule and cost reserves associated with the EVM PMB;
* Approval of the EVM PMB that will be used to report program cost, schedule, and technical performance;
* Approval of changes to the PMB;
* Establishment of PMB controls to ensure the PMB is current and reflects JRC-approved scope and funding authorized for the program as defined in the Capital Investment Plan (CIP) and by OMB;
* Review of analysis of cost/schedule table milestone significant variances;
* Approval of the PMB Estimate at Completion (EAC) reported to FAA management and external stakeholders;
* Leadership and coordination with the EVMFP Office for the program-level IBR;
* Approval of FAA program performance surveillance reports;
* Participation in prime contractor EVM surveillance;
* Provision of information to FAA management and external stakeholders signaling early warning cost and schedule EVM metrics and trends; and
* Support the program-level IBR by developing an in-brief, briefing the content during the start of the IBR, and answering interview questions.

 The following is a list of contract-level specific responsibilities that the PM conducts:

* Initiation and conduct of the prime contractor IBR with support from the EVMFP Office (if requested);
* Leadership and support of the contractor-level IBR;
* Collaboration with the Contracting Officer (CO) and prime vendor to distribute a contract letter with IBR date, requirements, and artifacts;
* Review of artifacts and provision of comments and/or questions;
* Development of interview questions for the day of the IBR;
* Participation in conducting interviews with the prime vendor CAMs and resources during the IBR;
* Participation in findings and out-brief content;
* Delivery of the out-brief to the prime vendor team; and
* Collaboration with CO and team to conclude the IBR through findings closure, action items, and contract letters.

## **2.2 Control Account Manager**

The CAM is a program team member assigned by the PM and is documented in the RAM. The CAM is responsible for the budget, schedule, and technical components associated with the scope of the CA. The CAM reports monthly on the CA cost, schedule, and technical performance. A CA can have only one CAM. The following is a list of program-level specific responsibilities that the CAM conducts:

* Concurrence with the CA scope, schedule, and budget documented in the RAM;
* Support of the development of the program IMS by developing detailed CA activities required to accomplish the scope within the schedule documented in the RAM;
* Review and concurrence with CA Earned Value (EV) and schedule status while supporting the program variance analysis for cost/schedule table milestone variance reporting;
* Preparation of quarterly Estimate to Complete (ETC) and EAC for CAs (supported by EVM Analysts and Business Manager/Program Control Manager);
* Analysis of variances and other events, including root causes and mitigation proposals (supported by the scheduler);
* Identification/forecast of the need for changes to Program Control staff;
* Review of Monthly Status Reports (MSR) and quarterly EAC/Variance at Completion (VAC) data;
* Review of current work estimates based on known, future changes (includes pending baseline change proposals);
* Direction of corrective action(s), where necessary, and the status of implemented corrective actions;
* Submission of Change Requests (CRs) when a CA constraint (cost, schedule, or scope) must be modified;
* Provision of monthly updates to milestones and other events to maintain status;
* Attendance at Change Control Board (CCB) meetings to present change proposals for CCB approval as required;
* Responsibility for the cost/schedule and technical scope of the specified Statement of Work (SOW) to be accomplished;
* Preparation and review of their Control Account Plans (CAPs), including the task list from the program schedule, which identifies planned work by task and resource for the CA;
* Submission of CAPs to the Business Manager/Program Control Manager for review and authorization;
* Verification that the CAP accurately represents their assigned work and the allocated resources (hours and budget);
* Verification that if the CAP does not accurately identify the work, CAMs must submit a revised CAP via CR to the Business Manager/Program Control Manager before commencing work on the affected work packages (WPs);
* Verification that the appropriate EV methodology is applied when planning efforts will be measured for performance;
* Provision of cost and schedule updates to be entered into the EVMS monthly;
* Verification that any significant cost/schedule and technical variances that arise during the monthly reporting period will be addressed, and that the PM will be informed of any issues to include recommended corrective actions to be carried out; and
* Support of the program-level IBR by responding to interviews about their CA.

 The following is a list of contract-level specific responsibilities that the CAM conducts:

* Support of the contractor-level IBR;
* Review of artifacts and provide comments and/or questions;
* Creation of interview questions for the day of the IBR;
* Participation in conducting interviews with the prime vendor CAMs and resources during the IBR;
* Participation in findings and out-brief content;
* Work with CO and team to close IBR through closing findings, action items, and contracts letter; and
* Draft of an IBR closeout letter with the consultation of the EVM Analyst to be provided to PM and CO to finalize for IBR contract closure.

## **2.3 Business Manager / Program Control Manager**

The Business Manager/Program Control Manager supports the PM and the CAM in planning and implementing EVM processes and tools. The following is a list of program-level specific responsibilities that are conducted by the Business Manager/Program Control Manager:

* Coordination of the development of the program PMB budget and the RAM;
* Maintenance of the EVM PMB control log;
* Maintenance of the EVM PMB change control process;
* Provision of quarterly EAC reports to the PM and CAMs;
* Verification that there is alignment with the program spend plan, budget resources, IMS, and critical path;
* Update of the schedule and cost status in the Major Investment Business Case (MIBC) and Simplified Program Information, Reporting, and Evaluation System (SPIRE) ; and
* Support of the program-level IBR.

The following is a list of contract-level specific responsibilities that the Business Manager/Program Control Manager conducts:

* Support of the contractor-level IBR;
* Review of artifacts and provision of comments and/or questions;
* Development of interview questions for the day of the IBR;
* Participation in conducting interviews with the prime vendor CAMs and resources during the IBR;
* Participation in findings and out-brief content; and
* Collaboration with CO and team to conclude the IBR through findings closure, action items, and contract letters.

## **2.4 EV Analyst**

The EV Analyst supports the program by creating, implementing, and maintaining a compliant EVMS. The following is a list of program-level specific responsibilities that the EV Analyst conducts:

* Coordination with the PM and the CAMs to develop the WBS, the WBS Dictionary, and the RAM;
* Creation of Work Authorization Documents (WADs);
* Revision of CA and WPs to accommodate changes in requirements, work, resources, and other variables;
* Conduct of program-level variance analysis and provision of support to CAMs in conducting variance analysis at the CA level for cost and schedule data;
* Collaboration with CAMs to create CAPs and incorporate them into the EV engine;
* Assistance in quarterly EAC reporting;
* Preparation and delivery of EVMS output and reports to CAMs for review and status;
* Assurance that EVM documentation is traceable and kept updated (IMS, CPR (Contractor Performance Reports), WBS, CAP, and RAM);
* Verification that the EVM policy and guidelines are being met;
* Integration of contractor and program-level data;
* Creation of all artifacts, Standard Operating Procedures (SOPs), and EVMS documentation (EVM Plan and EVM System Description);
* Review and provision of feedback on the monthly prime contractor EVM Contract Data Requirements List (CDRL); and
* Support of the program-level IBRs.

 The following is a list of contract-level specific responsibilities that the EVM Analyst conducts:

* Support of the contractor-level IBR;
* Review of artifacts and provision of comments and/or questions;
* Comparison of the EVM System Description documents to management processes;
* Development of interview questions for the day of the IBR;
* Leadership and participation in conducting interviews with the prime vendor CAMs and resources during the IBR;
* Participation in findings and drafting the out-brief content;
* Collaboration with CO and team to conclude the IBR through findings closure, action items, and contract letters; and
* Collaboration with the CAM to draft an IBR closeout letter and provide it to the PM and CO to finalize the IBR contract closure.

## **2.5 Scheduler**

The scheduler supports the program by creating and maintaining an IMS that breaks down the SOW into manageable tasks. The following is a list of program-level specific responsibilities that the scheduler conducts:

* Development of the program IMS used to plan and provide schedule status for CAs, WPs, and cost/schedule table AMS standard program milestones;
* Conduct of a schedule critical path analysis to identify schedule risk candidates;
* Conduct of a program-level variance analysis and provision of support to CAMs in conducting variance analysis at the CA level;
* Review and validation of the appropriate EV methodology or type selected by the CAM to assess performance review and validation of completed planned work, resource requirements, milestones and task dates, CAM identification, and WBS;
* Verification that the APB milestones are included within the IMS;
* Verification that all risks are incorporated into the IMS;
* Verification that the contractor schedule is integrated within the program schedule;
* Verification that the schedule has been planned out to the completion of the program;
* Verification that the process that is executed to update the schedule and ensure it is maintained and is updated frequently;
* Verification that tasks have been broken down into discrete work and that the Level of Effort (LOE) assignment is less than 15%;
* Provision of processes in the EVM Plan, other related SOPs, and artifacts;
* Responsibility for Schedule Risk Assessment (SRA) tools to evaluate the program schedule for quality. The analyzer includes schedule validation reports, government standard checks, comparison reports, schedule performance reports; and
* Support of the program-level IBR.

The following is a list of contract-level specific responsibilities that the scheduler conducts:

* Support of the contractor-level IBR;
* Review of artifacts and provision of comments and/or questions;
* Responsibility for SRA on the IMS and documentation of all findings;
* Comparison of SOP documents to management processes;
* Development of interview questions for the day of the IBR;
* Leadership and participation in conducting interviews with the prime vendor CAMs and resources during the IBR;
* Participation in findings and drafting the out-brief content; and
* Collaboration with CO and team to conclude the IBR through findings closure, action items, and contract letters.

## **2.6 Risk Analyst/Manager**

The Risk Analyst/Manager

* Verification of the accuracy of the risk plan that is being incorporated within the program;
* Verification that the risk ratings given meet the level of risk categorized;
* Verification that the risk and the mitigation plan for each is achievable;
* Leader of the Risk Management process, proposing the approach and participating in working groups to shape risk initiatives;
* Maintenance of the risk register;
* Maintenance of risks, issues, and opportunities (RIO) in the risk register;
* Possession of strong quantitative skills, particularly around statistics; and
* Influence of facilitation and partnering with the ability to build a strong internal network across functions and expand within risk.

The following is a list of contract-level specific responsibilities that the Risk Analyst/Manager conducts:

* Support of the contractor-level IBR;
* Support of traceability analysis throughout documentation;
* Review of artifacts to include SRAs, schedule reserve, IPMR (Format 5), and EACs projections to provide comments and/or questions;
* Comparison of risk management plan to management processes;
* Development of interview questions for the day of the IBR;
* Participation in conducting interviews with the prime vendor CAMs and resources during the IBR;
* Participation in findings and drafting the out-brief content; and
* Collaboration with CO and team to conclude the IBR through findings closure, action items, and contract letters.

# **SECTION 3.0: FAA PROGRAM ORGANIZATION FRAMEWORK**

The FAA organizational framework defines the documents that will assist as the frame of reference and building blocks for the foundation, organization, monitoring, and execution of the program and how EVM fits within this framework.

## **3.1 Investment Analysis (Planning) Phase (Pre-FID) Activities**

As mentioned in Figure 1 The FAA Lifecycle Management Process (above), Pre-FID EVM planning begins during the Research for Service Analysis Phase. These activities align with the first two National Defense Industrial Association (NDIA) EIA-748 EVMS Guideline categories: 1) Organizing and 2) Planning, Scheduling, and Budgeting. More information on the NDIA EIA-748 EVMS Guideline categories can be found on FAST on the EVM page under Toolkit, which provides linkage to several external guides, including the current NDIA Intent Guide.

### **3.1.1 Pre-FID EVM Activities that align with the NDIA Guidelines**

**Organizing**

When organizing the work that must be accomplished to complete the product, the FAA programs, prime vendors, and non-prime support must use the current FAA WBS document found on FAST to break down the scope into small, manageable pieces based on the scope agreed to in the SOW. The WBS is the framework used to define each element of work that makes up a program. This tracks and monitors the entire program’s cost, schedule, and technical progress. The WBS should be product or deliverable-oriented and reflect all the work scope of the program, including far-term effort. (see more detail provided in section 3.1.9 below).

The scope must be traceable to a WBS element. A notes or customized field should be created to enter this information into the IMS and listed within the assigned WBS. The WBS Dictionary is subsequently developed to define each WBS element at the reporting level and provide the structure for establishing each CA. Once the scope has been assigned to the appropriate WBS element, the Organization Breakdown Structure (OBS) is developed to identify the organization that will accomplish the work. This structure is used as the framework for assigning work responsibilities to an individual manager identified in the WBS. Subsequently, the work established through the WBS and the OBS is integrated between planning, scheduling, budgeting, work authorization, cost accumulation, and the PMB. The program must crosswalk the scope, WBS, WBS Dictionary, and IMS.

Integrating the WBS and the OBS creates the RAM. This document provides a framework for organizing, planning, budgeting, measurement, monitoring, and reporting of program performance. Integrating the WBS and OBS through the RAM facilitates the assignment of the CA and the responsible CAM. The CA is a management control point where scope, budget, actual cost, and schedule are integrated with program-level, contractor-level, and support staff data. The CAM is responsible for the assigned CA's cost, schedule, and technical performance.

The programs typically will not have to control overhead (indirect costs). However, the prime contractor must document the process for managing and controlling indirect costs in the program. This can be included in the program EVM System Description or another SOP document.

**Planning, Scheduling, and Budgeting**

An IMS must be established that documents the sequential order of completing the work assigned to each WBS from the SOW. This schedule is integrated with the technical, schedule, and costs at the program, contractor, and support staff levels. All program contract deliverables, milestones, and interdependency are included in the schedule. Additionally, the risks from the risk register must be included in the schedule within the assigned WBS. All support that provides schedules should utilize the GAO Schedule Assessment Guide: Best Practices for Project Schedules, found on the U.S. Government Accountability Office (GAO) website (gao.gov), to drive the building, executing, and maintaining of a reliable and compliant schedule. A SRA tool should also be used to identify any inconsistencies or errors within the schedule.

Once the schedule is established, the WBS is assigned the applicable EVM technique for that element. After determining what elements are assigned LOE (which should be no more than 15%), the program determines if the remaining techniques are apportioned effort, discrete milestones, percent complete, 50/50, or 0/100. Figure 2 below provides details on what EVM techniques should be utilized based on the duration of the work being completed.

![](data:image/x-emf;base64...)

**Figure 2 EVM Techniques**

The next step in developing the EVMS is to develop a time-phased budget at the CA level. This plan will detail all the work planned and authorize the management of the program's performance. Future planning periods may be allocated to a Planning Package (PP) or Summary-Level Planning Package (SLPP). A PP work is scheduled to start beyond the near-term period within a CA. It contains effort that eventually will be planned in detail and converted to WPs. A SLPP is a future budget associated with the approved scope but not yet detailed and planned at the CA level. This establishes the PMB.

Once the PMB is established, the program must develop WADs to authorize the work. The WAD must contain the SOW, budget in dollars (time-phased and summarized), schedule start and finish dates, unique identifying number (normally a CA number), and identify the person responsible for managing the work. Once this document is signed by the responsible CAM, Program Control Manager, and PM, it will authorize the work to begin and become a contract amongst those signatures. Any SOW, budget, or schedule changes are identified on a revised WAD. Work should not begin until all responsible parties document and sign this formal authorization.

The program must plan work in six-to-twelve-month increments. Work planned over longer periods must be broken into smaller manageable pieces. Work that cannot readily be planned in a detailed WP is planned in a PP. The PP should be decomposed into detailed WPs as soon as the CAM has sufficient visibility, but not later than (NLT) 60 days before the PP is scheduled to start. Each PP developed should not exceed one fiscal year. The CA comprises WP and PP, each representing a manageable and measurable unit of work. The sum of the WP and PP should equal the amount of the CA.

Once the CA has been established, the program develops a CAP. A CAP is a detailed plan that includes each CA. It represents the tasks, WPs, schedule information, EV technique, PP, and monthly spread of hours or dollars for which cost, and schedule will be monitored.

LOE is utilized when the Planned Value (PV) or Budgeted Cost of Work Schedule (BCWS) and the EV, or Budgeted Cost of Work Performed (BCWP) each month, are equal (PV=EV or BCWS = BCWP). This indicates the work being performed is not measurable. The program should have no more than 15% LOE for the program to have enough measurable work so that EVM can be used as a method for determining early warning signs on the program.

A range of 5% to 15% of the program's approved JRC cost should be removed for the purpose of MR; the percentage is generally based on risk. The amount remaining is UB. This UB amount is allocated to CAs and PPs, which will become Distributed Budget (DB). Any remaining cost is considered UB and can be designated as a temporary holding account for approved work that has not been planned into a CA or PP. This amount should be distributed into CAs or PPs within 30 – 90 days. The distribution timeline should also be included within the program’s EVM Plan document and EVMS Description Guide.

The program-level approved FID cost must be integrated with the contractor-level data and reconciled to the Total Allocated Budget (TAB), which consists of the PMB and MR. This amount must be reconciled to the program logs to include:

* Contract Budget Base (CBB) – Displays the end-of-month totals combining and reconciling all cost allocations and deductions into one log to include the PMB, MR, UB, Authorized Unpriced Work (AUP), and Overruns and Underruns;
* Management Reserve (MR) – Displays the end-of-month totals, including the distribution of a range of 5% to 15% MR taken at the start of the program, and then any additional set-asides to address potential cost, schedule, and technical risk, including any “unknowns” within the guidelines of MR distribution;
* Undistributed Budget (UB) – Displays the end-of-month totals of the distribution from UB to DB into CAs and PPs and any remaining unassigned budget;
* Performance Measurement Baseline (PMB) – Displays the end-of-month totals for the entire SOW and resources required to complete the program, including any contractual funding changes; and
* Total Allocated Budget (TAB) – This log is reconciled to the CBB log and includes any over-target baseline.

### **3.1.2 The Office of Investment Planning & Analysis (IP&A)**

The Office of IP&A supports strategic investment decision-making at the FAA by ensuring major capital investments are reinforced by robust business cases and primarily works within the Concepts and Requirements Definition (CRD) and Investment Analysis (IA) phases of the AMS lifecycle. IP&A works with the POs to validate the shortfall the investment plan addresses, properly characterize the urgency of the investment, and review the early cost and schedule estimates used to support budget formulation.

Additionally, IP&A performs detailed reviews of the schedule, cost, and benefits estimates for each of the program alternatives, as well as review of the overall business case for the investment, including strategic alignment, acquisition and support strategy, risk, and economic return to the public and the Agency.

The Office of IP&A and the Chief Financial Office (CFO) also oversee the Agency’s major contract procurement decisions, ensuring that each contract action is supported by a business case and that pre-award contract planning is adequate.

These analyses assist the agency in prioritizing competing investments and support several stakeholders, including the JRC for investment decisions, the Capital Budget for establishing the investment's APB, the Capital Investment Team (CIT) for the capital budget formulation process, and the acquisition team through procurement oversight and the Independent Government Cost Estimate (IGCE).

### **3.1.3 Implementation Strategy and Planning Document**

The Implementation Strategy and Planning Document (ISPD) identifies how a given system intends to implement a capability, integrates it into the National Airspace System (NAS), and is supported for its lifecycle. It is expected that this document, along with the functional requirements document, will form the basis for subsequent cost/benefit analyses and the acquisition baseline formulation for the program. These documents are all presented to the JRC as the basis for any FID. This process ensures that new services are achievable and service certification provisions with costs are fully understood as part of their proposed baseline.

There are two sections of the ISPD related to EVM (Section 2: Acquisition Planning and Section 3: Program Management) that the FAA EVMFP Office reviews and approves before FID. The EVM requirements for these sections are:

* **Section 2 Acquisition Planning:** The program should state that the EVMS for program and contractor implementation will follow the FAA AMS EVM policy 4.16 and guidelines. Deviations or waiver requests should be included in this section.
* **Section 3 Program Management** This section must include a plan for contracting for EVM. The program must state the contract deliverables, and a CDRL is required to support EVM. This section must describe the SOW requirements for reporting program EVM performance data for program management reviews and other management reports. Programs are encouraged to define contractor EVM reports that can be used by program management during regular contract performance reviews. Programs must require contractors to provide schedule status reports, particularly when they tie to the APB and IT Dashboard milestones. The programs must include a contract WBS that maps to the program WBS.

### **3.1.4 Program IT Dashboard Milestone Table**

The General Services Administration’s (GSA) Federal IT Dashboard enables agencies, the OMB, Congress, the GAO, and the public to understand the health of IT investments, the impact of federal IT portfolios and to track key website indicators in an agency’s ability to deploy technology that is secure by design, retire legacy systems, and ultimately, deliver a better digital experience for the public. The IT Portfolio is a management tool that contains budgetary data for Federal IT investments and displays Key Performance Indicators (KPIs), metrics, and key data points to monitor the health of different investments. This information can be found at itdashbord.gov. The IT Dashboard contains a snapshot of the agency's provided IT budget and management data for the current fiscal year (October 1st to September 30th each year). The IT spending data is the total amount of non-classified DM&E and O&M agency funding spent in the current year.

The OMB IT Dashboard CIO Risk ratings for IT investments are classified as low, medium, and high risk based on pre-established criteria for the current fiscal year. Agencies provide updates on program activities and operational performance. Schedule Variance (SV) and Cost Variance (CV) are used to measure agencies' progress quantifiably. Projects on-schedule are defined as project activities that have an absolute value of SV < 10%. Projects on-budget are defined as project activities that have an absolute value of CV < 10%.

* Green (low risk): Percentage scoring a CIO evaluation number of 4 or 5
* Yellow (medium risk): Percentage scoring a CIO evaluation number of 3
* Red (high risk): Percentage scoring a CIO evaluation number of 1 or 2

### **3.1.5 Program Management Plan**

A Program Management Plan (PMP) is a formal, approved document that defines how the program is executed, monitored, and controlled. It is detailed and may comprise one or more subsidiary management plans and other planning documents. The objective of a PMP is to define the approach to be used by the program team to deliver the intended scope. The PM develops the plan following input from the program team and key stakeholders. The program team and its key stakeholders should agree and approve the plan. The plan should be a living document updated periodically to remain current with the program.

### **3.1.6 Earned Value Management Plan**

Per AMS policy section 4.16, an EVM-designated program must use EVM to manage its government and contractor development efforts and ensure the availability of timely, accurate, and integrated cost, schedule, and technical data for performance management purposes. Each of these programs is required to develop a unique EVM Plan for each JRC-approved phase and segment. The objective is to develop a single-source document to facilitate the operation and maintenance of the EVMS specific to the program processes and implementation. (EVM Plan template available upon request to the EVMFP Office)

### **3.1.7 Earned Value Management System Description**

This document will also provide a means to document compliance with the EIA -748 standard for EVMS and FAA policy on EVM. The program will document the unique process used to plan, implement, control, execute, and monitor the established EVMS based on the EIA -748 guidelines.

This document describes the FAA program's approach to EVM and provides details for implementing an FAA EVMS. The system description document will reference the tools, techniques, and processes required to implement, control, execute, and maintain a compliant EVMS within the guidelines. To meet the agency's EVM requirements, each program is required to follow the guidance established in this document. The EVMFP Office must approve any deviations from the outlined procedure. (EVM Plan template available upon request to the EVMFP Office)

### **3.1.8 Earned Value Management Determination (EVMD)**

The EVMD is the EVM artifact provided to the JRC Secretariat during the Investment Analysis Phase to close the EVM Stakeholder/checklist item for the JRC decision that is being requested. The purpose of the EVMD is to formally document the EVM requirements for a FAA program and associated contracts. The EVMD also documents the program IBR requirements and the contract IBR requirements.

The EVMFP Office will make a determination to require EVM on efforts outside the contractor EVM requirement (refer to AMS EVM policy 4.16 for EVM thresholds) whenever it is determined that the nature of the government's effort includes a scope that is developmental and which is significant enough from a criticality, risk, or cost perspective that the benefits of EVM reporting for that portion of the scope justify cost and administration of a program-level EVM requirement. The JRC can also determine if any program and/or its prime contractor will provide EVM reporting requirements based on assessing the program effort's cost, schedule, and technical risk.

The EVMFP Office considers the PO's plan when developing the EVMD, which addresses whether EVM is required for the program. The EVMD is based upon the review and consideration of the ISPD, PMP, and numerous other factors, including designation by the OMB as an IT Major Investment, program risk, criticality to the NAS, the extent of government development effort, and Acquisition Category (ACAT). If the program does not use EVM or a modified version of EVM, it must provide an example of its management approach for risk, cost, and schedule control.

![](data:image/png;base64...)

**Figure 3 The EVMD Process**

The EVMD Process Steps are as follows:

* **JRC Planning Calendar Development**
  + The JRC Executive Secretariat develops a JRC Planning Calendar of all investment-seeking programs at the beginning of the calendar year.
  + The calendar helps the FAE, JRC Executive Secretariat, and EVMFP monitor the progress of all investment-seeking programs.
* **EVMD Development**:
  + The EVMFP or the PO of the Investment-seeking program develops the draft JRC EVM checklist item called the EVMD NLT 60 days before the JRC planned meeting date.
* **EVM Requirement Determination**:
  + The EVMFP’s Office determines if program/contractor level EVM is required in accordance with the FAA AMS EVM Policy 4.16.
* **Develop Draft EVMD**:
  + The EVMFP drafts the EVMD based on the EVM requirement determination and input from various sources, including ISPD, PMP, APB, current program briefings, JRC Familiarization briefing, and other factors such as risk, cost, developmental status, and visibility.
  + Other EVM stakeholders, such as AJM, ABP, and IP&A, may also provide input.
* **Complete and Submit Draft EVMD**:
  + The PO completes a draft of the EVMD and submits it to the EVMFP Office.
  + The EVMFP reviews the draft and provides a final draft to the PO for signature.
* **Status EVMD at Weekly JRC Readiness Meeting**:
  + The EVMD is statused at the weekly JRC Readiness Meeting until the PM and Directors accept and sign the EVMD.
* **Finalize and Close the EVMD JRC Checklist item:**
  + After the EVMFP approves and signs the EVMD, the EVMD is provided to the JRC Executive Secretariat for closure of the checklist item.
  + The process is complete when the EVMFP provides the investment program with a copy of the approved EVMD.

FAA Investments or programs that appear on the JRC Planning calendar are reviewed to determine if they have a FID or BCD. If they have a FID or BCD listed on the JRC Planning Calendar, the EVM Stakeholders led by the EVMFP Office will determine if the program is a developmental effort. If yes, then the following minimum factors are evaluated for the program: ACAT, Risk, Major IT Business Case status, sensitivity, and cost. Stakeholders within the program management organization and finance and budget offices also provide input. Following the EVM requirement determination, a draft EVMD is developed by the EVMFP and provided to the PO for review and concurrence before the signature review process. The EVMD is routed through the signature process for acceptance and approval by the PM, Directors, and EVMFP. The approved EVMD is provided to the JRC Secretariat by the EVMFP for closure of the EVM Checklist item.

### **3.1.9 FAA Standard Work Breakdown Structure (WBS)**

The FAA standard WBS establishes a common framework and uniform work activity definitions for use by the acquisition management workforce when planning work activities throughout the lifecycle management process and estimating associated costs and schedules. The lifecycle management work activity includes all work necessary to plan, develop, obtain, and support air traffic control and other FAA services mandated by law over their service life. POs are to use the current version of the FAA WBS, which can be found on the FAA Acquisition System Toolset (fast.faa.gov) under the FAA Standard Work Breakdown Structure.

**FAA Standard Work Breakdown Structure Organization**

![](data:image/x-emf;base64...)

**Figure 4 (Structure of the FAA Standard Work Breakdown Structure Version 5.3 Figure 2)**

1. **Service analysis** work activities precede the establishment of specific investment programs. They define the agency's strategic and performance goals and identify promising opportunities and technologies for achieving those goals.
2. **Investment analysis** work activities analyze alternative solutions to priority service needs and develop detailed planning and baseline values for the best overall approach.
3. **Solution implementation** work activities develop and deploy specific investment programs and their lifecycle support packages. During this phase, many organizations, including the prime mission product contractor, the FAA program management office, and other supporting FAA offices and contractors, conduct work as planned and managed by the service team or PO.
4. **In-service management** work activities support and sustain operational assets over their service life, whether they are systems, equipment, facilities, infrastructure, or services. They also support and sustain the overall NAS and other elements of the FAA Enterprise Architecture, such as administrative information technology systems.

The FAA standard WBS designates the work breakdown detail for all NAS investment initiatives, including research programs and service acquisitions, as well as for all non-NAS administrative and mission support initiatives, regardless of appropriation. It also defines WBS level four for the prime mission product.

The standard WBS applies to all phases of the acquisition management lifecycle. It displays and defines the product to be developed and produced using hardware, software, facilities, and services, and it relates work elements to each other and to end products. It also provides a systematic and standardized method for gathering cost data across all aspects of FAA investment initiatives.

**Program Work Breakdown Structure (WBS)**

FAA policy and guidance organize standard WBS work activities during Solution Implementation as a program WBS. The program WBS is a logical framework for planning and managing all program activities, assessing technical results, supporting event-based technical reviews, and measuring cost and schedule performance. It encompasses the entire investment program, including prime mission contractor activities and all related activities by support contractors and other government organizations (e.g., PO support, Government-Furnished Equipment (GFE), government testing, and controller and maintenance training). The common thread links program management and control activity, the contract SOW, and contractor management and control systems.

The program WBS is developed early in FIA as the foundation for planning implementation activities and estimating the associated costs and schedules necessary to develop, produce, deploy, and obtain lifecycle support for needed investment products and services. It is used during Solution Implementation to control the investment program by gathering actual program costs for work activities and tracking them against PVs.

Although EVM is applied during the Solution Implementation Phase, planning for EVM begins during the Research for Service Analysis Phase (see Figure 1 The FAA Lifecycle Management Process). Detailed WBS requirements can be found on the FAA Acquisition System Toolset (fast.faa.gov) under the FAA Standard Work Breakdown Structure.

**Post FID Activities**

## **3.2 Solution Implementation Phase (Post FID) Activities**

The FID completes the Planning Phase and marks the beginning of the Solution Implementation Phase. During this phase, the programs are responsible for implementing EVM consistent with the EVM plans and artifacts previously approved and with the FAA EVM System Description. The NDIA EIA-748 EVMS Guideline categories Performing and Accounting Considerations, Analysis and Reporting, and Baseline Management apply to post-FID activities.

### **3.2.1 Update EVM Planning Documents**

Below is a summary of steps to follow to update planning documents regarding EVM. EVM helps identify and manage deviations or changes that may affect the program's scope. These changes should be continuously updated throughout the program's lifecycle.

1. Identify Updates: Determine the specific changes that need to be made.

2. Revise Document Processes:

1. Update the associated form with the information requiring the change for auditing purposes.
2. Provide outcomes for the requested change.
3. Receive the necessary approvals to implement the change.

3. Update Plans and Schedules:

1. Modify the associated log for tracking.
2. Implement the changes.

4. Monitor document changes:

1. Keep track of changes made to the planning document.

# **SECTION 4.0: FAA EARNED VALUE MANAGEMENT PMB BASELINE COMPONENTS**

Establishing the EVM Program Baseline should begin post-FID. The EVM PMB cost, schedule, and technical baselines are derived from the FID-approved business case documentation for the Business Case Analysis Report (BCAR) and the APB.

### **4.1 Acquisition Program Baseline Components**

### **4.1.1 Estimated Lifecycle Cost**

The JRC usually approves the Solution Implementation Phase in segments or phases. The BCAR identifies the cost for the baseline segments by F&E less Activity 5 (government FTEs), OPs, etc. As segments are approved by the JRC, cost, schedule, and technical attributes can be incorporated into an existing APB or measured as a standalone APB. If there is a separate APB for each segment, there will also be a separate PMB for each segment.

A full risk-adjusted lifecycle cost estimate is required for all New Initiative investments at both the IID and FIDs. For the IID, lifecycle costs are captured for all alternatives. The lifecycle cost estimate for the FID is updated and finalized for the alternative selected for implementation at the IID. Parametric and analogous cost-estimating techniques may be applied during IIA. The final cost estimate developed during the FIA should be based on actual cost data from vendors responding to the screening information request (SIR) for the solution.

The EVM PMB is the approved acquisition segment(s) portion of the estimated lifecycle cost as an F&E portion of the total cost. The program must use the Risk-Adjusted Then-Year (RATY) F&E dollar portion to create the PMB. Total F&E costs include development, procurement, deployment, support, and infrastructure cost. Total OPS costs, which include all operational and support costs over the intended service life, are not included in the EVM PMB, nor are Activity 5 (government FTEs) costs.

When referencing the RATY, it is equivalent to the APB approved at FID. This funded amount starts as UB within the EVM implementation process. The agreed-upon MR amount or percentage is then removed from UB to allocate funds to unplanned risk. The program will then begin to create the PMB that will move UB to DB through CAs and planning packages.

### **4.1.2 EVM Total Allocated Budget Attributes**

The EVM TAB is the total planned cost, consistent with the program segments, which is approved by the JRC. This includes the Solution Implementation scope for the approved segments as documented in the BCAR and the APB. There may be instances where acquisition costs are included in the Planning or O&M phases (i.e., sunk costs, authority to proceed (ATP)). The EVM TAB is segregated into the PMB and the program’s MR. The PMB is further segregated into WBS elements for the CAs, SLPP, WP, and PPs.

### **4.1.3 Acquisition Program Baseline**

The APB establishes the performance to be achieved by an investment program and the cost and schedule boundaries within which the program is authorized to proceed. The acquisition program baseline is a formal document approved by the JRC at FID. It is a contract between the JRC and the PM of the service organization to which the acquisition has been assigned. The APB consists of three interdependent acquisition baselines: schedule, cost, and performance.

The PMB represents the time-phased budget (planned cost) established by the PM and reports the program EVM schedule and cost performance to FAA management and external stakeholders. The PMB is segregated by CA and SLPP, as documented in the RAM. The PMB is subdivided into milestones reported in the IT Dashboard Cost/Schedule Table.

##### **4.1.3.1 Schedule Baseline**

The APB of AMS Solution Implementation Level One, Two, and Three milestones are selected from the AMS Standard Milestone List. The schedule duration is measured in overall months and is the period from the FID to the commissioning of the last system or equivalent milestone. In cases where the AMS standard milestones do not apply, the PO should work with the Capital Program Formulation Branch to develop a set of tailored measurable milestones to be used in the acquisition schedule baseline.

##### **4.1.3.2 Cost Baseline**

The Acquisition Cost Baseline includes costs for the prime contract, testing, deployment, site preparation, installation, and headquarters and field support contracts. The cost baseline does not include government FTEs (Activity 5).

##### **4.1.3.3 Performance Baseline**

The APB contains the requirements in the Program Requirements document designated for control by the JRC. These consist of technical performance parameters and associated values essential for achieving the desired operational effectiveness. The performance baseline also includes the number of systems being acquired.

### **4.1.4 Management Reserve**

A portion of the program budget is set aside for unforeseen risks and events that fall within program scope requirements. The PM will establish a MR after considering all identified risks. Where possible, quantitative analyses of high-impact and/or high-probability risks will be performed to better understand the potential time and financial impacts to the program if the risks do occur.

#### **4.1.5 Establishing the PMB**

The PMB represents the time-phased budget (planned cost) established by the PM. It is used to report the program EVM schedule and cost performance to FAA management and external stakeholders. The PMB is segregated by CA and SLPP, as documented in the RAM. The PMB is subdivided into milestones reported in the IT Dashboard Cost/Schedule Table.

#### **4.1.5.1 Cost Definition of the PMB**

The PMB costs are allocated to a specific scope for a program consistent with the APB scope. The PMB consists of the time-phased costs at the WP, PP, and SLPP levels. The time-phasing of the budget is consistent with the program schedule and the Federal IT Dashboard Cost and Schedule Table milestones.

#### **4.1.5.2 Schedule Definition of the PMB**

The program schedule related to the PMB is consistent with the Federal IT Dashboard Cost and Schedule Table milestone dates. The PMB includes the efforts and procurements to achieve milestones. The APB Schedule Milestones define the EVM PMB schedule baseline.

#### **4.1.5.3 Technical Scope Definition of the PMB**

The PMB technical scope includes the products, program milestones, and support included in the program WBS used for the FID.

#### **4.1.5.4 Program WBS**

The Program WBS is a subset of the FAA Standard WBS that represents the scope for the JRC-approved program segments. It is extended to CAs and SLPPs.

#### **4.1.5.5 IT Dashboard Cost/Schedule Table**

The Program IT Dashboard Cost/Schedule Table identifies the program milestones that measure technical progress. These milestones are usually consistent with the Level One and Level Two AMS standard program milestones. This table is used to report the program's technical, schedule, and cost status to FAA management and external stakeholders.

# **SECTION 5.0: ESTABLISH EARNED VALUE MANAGEMENT PMB**

Once the JRC approves the program's FID, the next step is to update the EVM planning documents, expand the CAP and SLPPs, and establish reserves. From here, the program uses the point estimate and establishes the baseline. The cost estimate from FID is used to determine the baseline costs.

DB takes place when the UB is distributed to CAs, SLPPs, or MR as soon as possible after definitization. All updates will be included in the log the program utilizes to document changes.

## **5.1 Control Account Budget Components**

CAs contain two key components of the program budget: the WP, the PP, and the SLPP. Elements of Cost (EOC) are the building blocks for developing the budget. The following sections describe the components that make up the budgets developed during this process.

**Work Package**

A WP is a subdivision of a CA. It is a detailed plan of deliverables, milestones, and activities used in planning, controlling, and measuring program performance. It describes the work to be performed and serves as a vehicle for monitoring and reporting progress and accomplishing work. All WP, PP, and SLPP budgets must be added to the CA budget. WP characteristics include:

* Clear distinction from all other WPs;
* Scheduled start and completion dates;
* Development at the level at which work is performed and earned value is claimed;
* Assignment of budget or value (F&E); and
* Earned value techniques.

**Planning Package**

A PP is an aggregate of future tasks and budgets within a CA that will eventually be detail-planned and segregated into WPs. It represents far-term efforts that cannot be defined in detail at the start of the CA. PPs are similar to WPs in that they include scope, schedule, and budget.

PPs are distributed within the last month of each fiscal year unless a rolling wave is being implemented. If a rolling wave (which occurs every three or six months) is being implemented, it should be distributed prior to the month the rolling wave will occur. The work in a PP must be converted into WPs before that work begins. The CAM manages the conversion of a PP to WPs. All EVM artifacts should be reviewed and updated, including the RAM, CAP, WADs, change management documents, logs, and WBS/Dictionary (if new WPs are added) with each PP or rolling wave.

**Summary-Level Planning Package**

There are times when authorized work cannot be planned to the CA level. It is common for programs to include un-appropriated future funding in SLPPs. SLPPs must have a clearly defined scope, schedule, and budget. Although it is not required, limiting the use of SLPPs to future funding not appropriated is recommended.

**Elements of Cost**

Programs should segregate elements of cost (labor, travel, material, and other direct costs) as required to manage the program costs.

## **5.2** **Establish Program Performance Baseline**

The PMB is documented in the program control log after the PM approves all the CAs and SLPP budgets and schedules. When the PMB has been established, any changes become subject to the program baseline change control procedure.

### **5.2.1** **Development of Management Reserve**

Every program may establish and manage reserves against the EVM PMB to handle unplanned costs or schedule issues due to risks or "unknowns." MR is the amount of the program budget set aside for risk mitigation and unknown requirements. The PM will establish MR after consideration of all identified risks. As a part of the FID, MR is the difference between the Program's Risk-Adjusted Cost Estimate and the Program's Point Cost Estimate. Therefore, MR is part of the Total Program Budget but separate from the PMB, which is set at the point estimate. MR will equal the Risk Adjusted Estimate (Total Program Budget) less the Point Estimate (PMB). The total amount of the reserve is maintained at the program level and maintained in the baseline control log. The distribution of MR to a CA needs to be documented in a program baseline control log that should be used to track distributions of MR.

### **5.2.2** **Program Detailed Schedule**

The CAP includes detailed schedules for the work assigned to the CAP. It is recommended that appropriate funding be planned in detail at the CA level. All efforts required to complete the SOW need to be identified and scheduled. The activities should be planned at the WP level for near-term funded work. Future work that is not well-defined may be planned as a PP. Using the mix of detailed WP activities and PPs is called rolling wave planning. Rolling wave planning is a method where near-term activities are detail-planned down to discreet activities, and work that is not yet fully defined is scheduled as a PP. This allows the PO to focus on the detailing of the near-term work and not waste valuable resources and time trying to detail activities that are not well-defined.

### **5.2.3** **Program Detailed Budgets**

CAs are subdivided into PPs and WPs. Budget requirements and time phasing are prepared for each WP and PP in accordance with the timing of the work planned in the program schedule. The CA budget is based on when the work will be accomplished or performed. The time phasing of the budget may be generated from the resource-loaded detailed schedule.

### **5.2.4** **Work Authorization Document**

WADs are required to authorize work. Programs are encouraged to use existing FAA processes and documents to authorize work. Examples include a contract, funding authorization documents, and a CA approved by the PM.

# **SECTION 6.0:** **FAA PROGRAM ANALYSIS AND MANAGEMENT REPORTING**

The following section describes the FAA's and external stakeholders' program performance reporting as it takes into consideration performing and accounting considerations, analysis and reporting, and baseline change management. This reporting should be understood and applied during the Solution Implementation Phase to ensure the program control processes and procedures support the reporting requirements.

## **6.1 FAA Program Analysis and Management Reporting**

After the EVM PMB has been established and the program is executing and performing work, the program will monitor schedule accomplishments, technical progress, earned value, and cost incurred to determine program performance metrics that will be provided to the PM, reported to FAA management, and reported to external management. These parties have different needs; although the metrics may not be identical, they should be reconcilable. The program is responsible for maintaining and reporting program performance metrics to different stakeholders. It must justify and reconcile the differences between audit and review parties (i.e., DOT, GAO, IG, and Congress).

The program performance metrics should be integrated with the risk management plan to identify technical, schedule, and cost risks. The program IT Dashboard cost/schedule table includes technical milestones, and each milestone should have CAPs detailing the EVM plan to achieve the milestones. The EVM metrics should be used to identify schedule/cost risk candidates for these milestones.

The risk plan criteria for impact or consequence criteria are recommended to include schedule metrics and cost metrics to identify risk candidates. The Schedule Performance Index (SPI), Cost Performance Index (CPI), SV, and CV are useful indicators to identify program risks.

## **6.2 Variance Reporting APB-Level**

AMS policy establishes internal baseline variance thresholds for reporting requirements. A baseline variance for cost, schedule, or performance of greater than negative 5% triggers the generation of a Baseline Management Notice (BMN) and a briefing to the JRC to present the PO plan for mitigating variance growth. A baseline variance of greater than negative 10% and negative 50% for cost, schedule, or performance will trigger the generation of a BMN and a briefing to the JRC to consider the following:

1. Termination of the program,
2. Continuation of the program with existing variance, or
3. Rebaseline and continuation of the program.

To reiterate, an APB variance of greater than negative 10% and negative 50% for cost, schedule, or performance will also trigger a notification sent to the Administrator to consider termination of the program as required by US Code §40121. For variances greater than negative 50%, the Administrator shall terminate the program. If the Administrator makes a determination to continue, the Administrator shall transmit a copy of the determination, together with a statement of the basis for the determination, to the Committees on Appropriations of the Senate and House of Representatives, the Committee on Commerce, Science, and Transportation of the Senate, and the Committee on Transportation and Infrastructure of the House of Representatives. More information about US Code §40121 can be found within the FAA Acquisition Baseline Management Standard Operating Procedure July 2023 on FAST.

## **6.3 Status Program Schedule/Program Schedule Changes**

After a CAM or PM initiates a CR, the scheduler assesses the request, initiating a "What if" scenario to ascertain the potential impact of the proposed changes. Subsequently, the designated Point of Contact (POC) reviews the anticipated outcomes and decides whether to approve or cancel the request. The approved outcome is documented in the Baseline Change Management request form, and final approval is granted by the PM, CAM, Program Control/Finance, or Business Manager. Once approved, the scheduled changes are implemented.

Every month, the scheduler extracts the schedule data into Excel and distributes copies to each CAM responsible for their designated areas. The CAM then utilizes specific criteria or status deliverables to calculate the percentage of completion. Once the CAM completes this assessment, they return the information to the scheduler. The scheduler, in turn, inputs these updated estimated dates, completion dates, and EVM percent complete into the scheduling system, initiating a processing update. After all information is consolidated and updated, a copy of the schedule is forwarded to the EVM analyst to update performance metrics and the EVM tool.

## **6.4 Earned Value Calculations**

EVM is a project management technique that integrates scope, schedule, and cost data to assess project performance and progress. The key earned value calculations include the following:

 1. Planned Value (PV) or Budgeted Cost of Work Scheduled (BCWS):

1. The planned cost of the work scheduled or the budgeted cost for the work planned to be done by a specific point in time.
2. PV = Budget at Completion (BAC) X % of Work Scheduled.

 2. Earned Value (EV) or Budgeted Cost of Work Performed (BCWP):

1. The value of the work performed or the budgeted cost for the work accomplished.
2. EV = BAC X % of work Completed.

 3. Actual Cost (AC) or Actual Cost of Work Performed (ACWP):

1. The actual costs incurred in completing the work.

 4. Cost Performance Index (CPI):

1. A measure of cost efficiency indicates how much value you get for each dollar spent.
2. CPI = EV/AC.

5. Schedule Performance Index (SPI):

1. A measure of schedule efficiency indicates how much work is accomplished against what was planned.
2. SPI = EV/PV.

6. To Complete Performance Index (TCPI):

1. The future cost performance is needed to achieve a specified management goal.
2. TCPI = (BAC – EV) / (BAC – AC).

 7. Estimate at Completion (EAC):

1. An estimate of the total project cost at completion, based on project performance to date.

EAC = ETC + Actuals (manual)

1. Costs to Date + [(Remaining Work)/ (Efficiency Factor)] (calculated)

 8. Estimate to Complete (ETC):

1. An estimate of the remaining cost to complete the project.
2. ETC = EAC – AC.

9. Variance at Completion (VAC):

1. The difference between the budget at completion and the EAC.
2. VAC = BAC – EAC.

10. Budget at Completion (BAC):

1. The total budgeted cost for the entire project.

These calculations provide valuable insights into project performance, assisting PMs in determining whether the project is on track in terms of schedule and budget. The FAA has not selected an official tool to use to implement EVM, and programs utilize multiple tools within the agency.

### **6.4.1** **Estimated Costs for Earned Value Work Accomplished**

The following formula can be used to calculate the EV using the AC of work performed: EV = Percentage of project completion x BAC. [The entire cost of the project](https://www.bing.com/ck/a?!&&p=0fa258e0ba39ecefJmltdHM9MTcwNDI0MDAwMCZpZ3VpZD0yYzBhMWM3OS00ZmFiLTYwNjItMmMzZi0wZGUzNGViOTYxMTkmaW5zaWQ9NTg0NA&ptn=3&ver=2&hsh=3&fclid=2c0a1c79-4fab-6062-2c3f-0de34eb96119&psq=estimated+cost+for+earned+value+work+accomplished&u=a1aHR0cHM6Ly91ay5pbmRlZWQuY29tL2NhcmVlci1hZHZpY2UvY2FyZWVyLWRldmVsb3BtZW50L2Vhcm5lZC12YWx1ZQ&ntb=1) should also be calculated. [Multiply the percentage and the project budget to get the EV](https://www.bing.com/ck/a?!&&p=7af8c1e07d029464JmltdHM9MTcwNDI0MDAwMCZpZ3VpZD0yYzBhMWM3OS00ZmFiLTYwNjItMmMzZi0wZGUzNGViOTYxMTkmaW5zaWQ9NTg0Ng&ptn=3&ver=2&hsh=3&fclid=2c0a1c79-4fab-6062-2c3f-0de34eb96119&psq=estimated+cost+for+earned+value+work+accomplished&u=a1aHR0cHM6Ly91ay5pbmRlZWQuY29tL2NhcmVlci1hZHZpY2UvY2FyZWVyLWRldmVsb3BtZW50L2Vhcm5lZC12YWx1ZQ&ntb=1). This formula helps in estimating the financial status of the project.

## **6.5 Summarized EVM Performance Measurement Data**

The EVM Performance Measurement Data is a tool used to report monthly data to the EVMFP Office. This allows the EVMFP team to follow the progress of each program during the reporting program lifecycle phase. This is done by having each PO provide:

* **Monthly Data Call Reports:** Monthly Data Call Reports are delivered the first week of each calendar month to report the progress of each program to the EVMFP Office. The reports consist of EVM program-level cost, schedule, and technical data integrated with the prime contractor and other support areas.
* **IPMR Formats 1, 3, 5, & 6:** The program-level and contract-level IPMR reports are established to oversee the monthly cost and schedule progress or areas of potential problems in the program.
* **Six-Month Forecast:** Each month, the six-month forecast for the PV is requested to identify changes to the PMB by the program or the prime contractor. Any changes should be accompanied by a Baseline Change Request (BCR) form and updated in the BCR log.
* **Control Account EAC:** The PM shall develop a bottom-up CA's EAC yearly to keep the program updated within the total cost at the completion of the project. The EAC is then updated monthly or, at a minimum, quarterly or when a significant change occurs in the program by the CAM. The EACs are developed with varying degrees of detail and supporting documents. The EAC calculations include:
  + Best Case/Worst Case/Most Likely.
  + Best Case: EAC = Costs to Date + [(Remaining Work)/ (Efficiency Factor)].
  + Most Likely: EACCPI = ACCUM + [(BAC – EVCUM)/CPICUM]

= BAC/CPICUM.

* + Most Likely, it should always include risk because it is the PM's skilled assessment.
  + Worst case: EACComposite = ACCUM + [(BAC – EVCUM)/ (CPICUM \* SPICUM)]. Add risk. This is the worst-case scenario.

## **6.6 Generate Earned Value Reports**

There are five steps to creating an EV report:

1. **Gather performance:** The first step is to gather information regarding the task. The information begins with the task name, start date, end date, and budget. After gathering information from the field regarding how much work has been completed, several calculations are performed to find key variables that are part of the analysis.
2. **Determine schedule status:** The next step is to analyze the schedule for each task. Two calculations are performed to determine whether the task is on schedule.
3. **Determine cost status:**Next, variables regarding the cost status are analyzed. Similar to the schedule analysis, two variables are calculated.
4. **Forecasting:**Once the schedule and cost calculations for all tasks on the schedule are completed, forecasting can begin. Four additional calculations help project teams predict each task's future performance.
5. **Reporting:** Formal reporting is generated monthly/quarterly per the EVMD. Formal reporting occurs at the end of each month when the Data Call, OMB, Program/Contractor reports, Critical Acquisition Programs Performance (CAPP), Smart sheets, and the EVM quarterly briefing for the JRC are submitted.

## **6.7 Internal Review by Program Manager/Program Control**

The PM and Program Control/Finance/Business Manager will perform an internal review of the IPMR Formats 1, 3, 5, and 6 prior to submitting the monthly data report and matrix to the EVMFP Office. CAMs review and input the monthly reports and variance analysis into the CAM notebooks.

# **SECTION 7.0:** **PMB REVISIONS AND DATA MAINTENANCE**

Once the PMB is established, cost, schedule, and technical changes are processed through change control procedures. This activity supports the execution stage and is the vehicle for approving and tracking changes to the PMB. This requirement, however, is in no way meant to discourage changes to the PMB. Instead, changes that reflect the most current program conditions are encouraged. Meaningful performance measurement data requires a PMB that is documented and reflects the most current conditions of the program.

## **7.1 Baseline Reconciliation**

To support program management, actual costs must be charged to a program consistent with the corresponding budgets to achieve effective performance management and an EAC. Accumulating actual costs consistent with how the related work was planned and budgeted facilitates the comparison of the ACWP to the BCWP for performance and variance analysis. Properly collecting, recording, and transferring direct costs to the EVMS establishes a valid comparison with the associated BCWP. This ensures accurate CVs. Delphi provides all actual costs (i.e., labor, subcontractor, material, and other direct costs) to accomplish the authorized work scope. To ensure ACWP is directly compared with the associated BCWP for performance measurement, the direct cost-charging structure established in the contractor's Delphi tool should, at the very least, be mapped or traced to the CAs. Actual costs are collected at the CA level at a minimum to enable the calculation of CV information for use in evaluating cost performance and providing cost projections at the level where the work is being performed. The ACWP reported in the performance reports must reconcile with actual costs recorded in the Delphi tool.

If direct costs for subcontracted effort or material have not yet been formally recorded in Delphi, the estimated actual cost will be used by the Program Control Manager for EVM performance assessment and reporting in the EVMS. This addresses the timing differences between the Delphi tool and performance reports. Once direct costs have been recorded, they will replace the estimated costs (estimated actuals) recorded in the EVMS. Negative adjustments in the current period are estimated actuals to be used to reflect a reduction in direct costs in the EVMS, such as cost transfers, where the accounting transaction lags the identification of the pending transfer. All estimated actual costs used for performance reporting will be reconciled between Delphi and the EVMS. This data is reconciled monthly to ensure the program's current costs are up to date.

## **7.2 PMB Change Control**

Once the PMB has been established and agreed to by the PM, it needs to be properly maintained while following FAA policy 4.16 and EIA-748 guidelines. Change control processes will be implemented so that any changes to the plan will be documented. These PMB baseline maintenance disciplines ensure that:

* Budgets are assigned to specific segments of work defined as CAs, WPs, and SLPPs;
* Scope is distributed to the relevant organizational CA groups;
* Records are maintained in a change log to indicate when and where MR was applied;
* Retroactive changes to the budget PV, EV, AC, or CA/WP schedules are limited to correct errors or for normal accounting adjustments within the current period. Changing history is not permitted;
* Future PPs and WPs scheduled to start beyond the next reporting period may be rescheduled within the CA budget and schedule constraints; and
* Changes to the budget or schedule require a BCR approved by the PM.

## **7.3 Change Control Process**

Once the PMB is established, cost and schedule changes are processed through formal change control procedures. The change control process establishes, analyzes, communicates, and records approved changes to the program baseline. The change control process must ensure that only approved changes are incorporated into the EVM PMB baseline and appropriately documented. The chart below explains the steps in the change control process.

|  |  |  |
| --- | --- | --- |
| **Step** | **Description** | **Responsible** |
| Develop CR | A submitter completes a CR Form and sends the completed form to the appropriate POCs for program data input. | CAM |
| Generate CR | An estimated effort for the process is provided and a proposed solution is developed for the suggested change that is presented. It details how the scope, schedule, cost, and risk are affected, | EVM Analyst Scheduler  Risk Analyst |
| Evaluate CR | The CR is reviewed. | Program Manager Affected CAM(s)  Program Control/Manager |
| Authorize | An approval to move forward with incorporating the suggested change into the program is authorized. | Program Manager Affected CAM(s)  Program Control/ Manager |
| Implement | If approved, necessary system adjustments to implement the requested change and communicate the CR status to the submitter and Management Team are made. | EVM Analyst Scheduler  Risk Analyst |
| Log CR Status | The CR is entered into the Log. The CR's status is updated through the CR process as needed. | EVM Analyst |

## **7.4 Types of Baseline Change Request**

BCRs are submitted to the POs to evaluate the impact of the requested change. Impacts to other organizations' schedules are resolved before approval of the revision. Baseline changes are submitted to the PM, affected CAMs, and Program Control/Business/Finance Manager for approval prior to implementation. Approved changes are incorporated into the RAM.

The Baseline Change Log provides traceability from the original baseline to the current baseline for all approved changes that have been incorporated. All changes are entered in the log and are appropriately discussed in the applicable reports. The program value reflected in the TAB is reconciled against the sum of all CA budgets and MR. The following depicts what is considered a BCR and what is not considered a BCR. (BCD template is available upon request to the EVMFP Office)

Specifics:

* Formal contract changes.
* According to the Contract Modification
* AUW directed
* Formal Re-Program.
* Change to overall Contract Budget, Schedule, or Technical
* Deliverables.
* Requires formal client approval
* May require an IBR
* Used to re-organize the schedule or support Rolling Wave
* Internal re-planning.
* No change to the overall Contract Budget, Schedule, or Technical
* Rolling Wave Planning Packages.
* Usually approved internally by the Program Manager

A BCR is used for:

* New scope or scope change
  (e.g., open WPs for which the SOW has changed so dramatically that continuation with the existing WP is no longer reasonable).
* Re-planning future work.
* Corrections of data entry errors within the current period.
* Adjustments for labor rates.

A BCR is Not for:

* Closing of an active WP.
* Creation of a WP for completed work.
* Elimination of a variance.
* Change/redistribution of hour/budget allocations.
* CAM name change (must be approved by the Program Director). This can be documented in a regular revised WAD for auditing purposes.

# **SECTION 8.0:** **EVM GOVERNANCE**

Once a program establishes its required artifacts, receives its FID, and has been approved by the JRC, the PMB established for the program needs to be validated through an IBR and ongoing Surveillance. While the goal is to have the review at the most logical time regarding program definitization, the program-level IBR should occur within 60 days after the contractor's IBR.

If there is no IBR requirement at the contract level, a program-level IBR conducted by the EVMFP Office and PO should occur within 180 days after:

* The JRC FID;
* Contract award;
* Execution of a major contract modification;
* Exercise of a contract option;
* Major Rolling Wave planning;
* Significant program or PMB changes; and/or
* JRC-approved Baseline Change Decision.

Any deviation from this timeline should be coordinated with the EVMFP Office. IBRs are not a one-time event during a contract or program and should be conducted continuously to ensure the program performance baselines and processes provide useful and accurate performance measures.

## **8.1 Program Integrated Baseline Review (IBR)**

The IBR intends to guide FAA programs on the viability of the proposed baseline and to gain a mutual understanding of the assumptions and risks made in program planning. The IBR is a process that:

* Verifies that the total program technical, schedule, resource, and cost baselines are achievable, and risks have acceptable risk handling plans; and
* Verifies program management control processes and systems are in place to achieve program objectives and agency commitments.

The IBR is performed to improve FAA program and contractor performance measurement by ensuring adequate planning and risk considerations have been performed in conjunction with establishing a PMB after the JRC program or rebaseline approval. The IBR verifies that the program management processes are integrated and that an adequate and appropriate metrics management plan is in place to manage, monitor, and report program performance.

The program and contractor IBR is to be conducted at the program-level for all programs designated by the JRC for program-level EVM reporting and at the contractor-level for all required contracts by AMS policy to conduct and maintain EVM reporting. The JRC may also designate any program and/or its prime contractor for IBR conduct, regardless of EVM reporting requirements, based on assessing the program effort's cost, schedule, and technical risk.

The FAA EVMFP and the FAA PM are responsible for ensuring the IBRs are conducted on FAA programs to assess baseline implementations and program performance systems. The FAA EVMFP Office works with the FAA PM to assemble the IBR Team and schedule CAM interviews. The IBR Team coordinates the preparation and conduct of the IBRs by providing an IBR plan to the FAA EVMFP office. The FAA EVMFP will conduct the program-level IBR with FAA program management teams and independent Subject Matter Experts (SMEs) who validate the program baselines, executability, and performance management processes and are not connected with the program.

## **8.2** **Contractor Level IBR**

The contractor IBR is designed to allow the government technical and program management team to evaluate the contractor's implementation of the contract PMB. It is intended to promote early and adequate planning and to ensure that the government and contractor have a mutual understanding of the program scope, schedule, resources, management approach, and the processes and procedures under which the program will be executed. The IBR also identifies risk items that become part of the contractor and program risk management plan. An IBR conducted after the award uses EV plans and data reported by the contractor to ensure the data is analyzed and coordinated among program personnel and, if applicable, ensure follow-up surveillance of the contractor's EVMS.

Contractor IBRs are planned to correspond with the definitization of the work by the contractor and should occur within 120 days after contract award. The exact timeframe is dictated by the size and length of the contract, when the work is definitized, and in coordination with the contractor. While there will be an initial contractor IBR at the beginning of the program, additional IBRs may be conducted on the contractor’s baseline. In addition to contract awards, IBRs are required to be conducted when there is a major contract modification, a BCD is approved, changes to the contract are made, including additional awards to the contractor, or based on large portions of the work being definitized.

The contract-level IBR process is similar to the program-level IBR. However, the PM replaces the FAA EVMFP Office as the lead for the contractor IBR. The FAA EVMFP Office can support the program during its execution of the IBR at the level of support needed. It is recommended that the PO acquire team training before the IBR.

The FAA IBR Guide and the NDIA IBR Guide provide directions on the contractor IBR process.

## **8.3** **Program Surveillance**

Program or contractor surveillance is conducted during the Solution Implementation Phase of the FAA lifecycle. The surveillance process is primarily metrics-based and structured to use the existing program IPMR, reviewed documentation, and additional data sources, which can be qualitative. The process is structured into two phases: Primary Surveillance and Secondary Surveillance. The Primary Surveillance Phase considers the performance of major FAA programs (investments) or contracts to determine if further surveillance is required. The Secondary Surveillance Phase includes more extensive surveillance for those programs or contracts selected as a result of the Primary Surveillance Phase. PMs are responsible for action items and program or contract recommendations.

FAA EVM surveillance ensures policy compliance and data reliability across major programs, non-major programs, portfolios, and contracts. Data reliability includes verifying performance data consistency across data sources and reasonable data relationships between reporting periods. The process provides high-level oversight as the focus of primary surveillance for FAA programs or contracts. Program-specific issues discovered during primary surveillance may result in more detailed secondary surveillance for selected programs or contracts.

Surveillance may be performed continuously during the Solution Implementation Phase on major programs, contracts with an EVMS requirement, tailored EVM approach, or within one year after a program or contract-level IBR as defined in the EVMD. They may also be conducted on high-dollar or high-interest non-major programs. Surveillance typically will not be conducted for the operational steady-state phase of a program or contract unless the nature of the work lends itself to performance management using EVM.
