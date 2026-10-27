---
title: "teoperationaltestplan"
source_url: https://fast.faa.gov/docs/teoperationaltestplan.docx
source_type: docx
converted: 2026-10-27
---
# teoperationaltestplan

![m](data:image/png;base64...)

**Acquisition Management System Guidance**

Operational Test Plan Template for Investment Programs

**Version 6, April 2024**

DOCUMENT VERSION CONTROL

| Version | Description of Change | Date |
| --- | --- | --- |
| 1.0 | Initial Release of document | 11/12/2009 |
| 2.0 | Release Version 2.0 | 04/25/2011 |
| 3.0 | Release Version 3.0 | 10/20/2011 |
| 4.0 | Release Version 4.0, 508 Compliant | 07/08/2015 |
| 5.0 | Release Version 5.0, redesign, reorganization, branding, synchronized with T&E Handbook enhancements | 11/23/2020 |
| 5.0 | **Note:** Version date synchronized with AMS quarterly update of January 2021. Version remains the same (5.0) | January 2021 |
| 6 | Corrections to subsection subordination in Sections 7 and 8 | 2024/4/12 |

**GENERAL GUIDANCE**

The Operational Test (OT) Plan forms the basis for the OT program. It describes the various planning and preparation activities required prior to OT, the testing to be accomplished, organizational responsibilities for the testing, how test procedures will be executed, discrepancy management, and reporting test results. The OT Test Plan describes the OT program to stakeholders. It also provides sufficient detail to guide the development of OT Test procedures. This template can be used for plans associated with operational evaluations and operational testing of systems, services, or capabilities.

**Formatting:**

Modify the following pages of this template with cover and footer information that is accurate for your organization and the document’s control number, version, and date.

Conventions:

The following conventions are used in this template to assist you. Delete these signs and any text instructions as you write.

|  |  |
| --- | --- |
| ![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\938DE85E.tmp](data:image/jpeg;base64...) | Informational text explains what content must appear in the section. |
| ![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...) | The compass icon denotes instructions applicable to the subsection you are authoring. |
| Magenta | Magenta text provides you with sample content to update according to your test effort. |

![m](data:image/png;base64...)

**FAA
William J. Hughes Technical Center**

![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\938DE85E.tmp](data:image/jpeg;base64...)<u>Cover Page</u>: Contains all the elements required for the cover page: FAA logo, official system, service, or capability nomenclature, document identification (e.g., Operational Test Plan for xxxx), document control number, version number, publication date, and organization name.

**Operational Test Plan for Program Name**

| **Document #** | **XXXX-XXX-XXX-XX** |
| --- | --- |
| **Version #** | **X.X** |
| **Version Date** | **Month Date, Year** |
| **Division** | **XXXXXX** |
| **Branch** | **XXXXXX, ANG-Exxx** |

**FAA William J. Hughes Technical Center**

**Atlantic City International Airport, New Jersey 08405**

**DOCUMENT VERSION CONTROL**

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Identify the document version number, version date, and change summary for each document version throughout the Operational Test (OT) Plan history.

| Version | Description of Change | Date |
| --- | --- | --- |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

**Approval Signatures**

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Obtain signatures and dates for each approving authority, title, and organizations. Add lines if necessary.

![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\938DE85E.tmp](data:image/jpeg;base64...) Required approval authorities are the Program Manager, the Division Manager, the Test and Evaluation (T&E) First-Line Supervisor, and the OT Test Director.

| **DOCUMENT TITLE:** | **OPERATIONAL TEST PLAN FOR PROGRAM NAME** |
| --- | --- |

| Program Manager Org code | Date |
| --- | --- |

| Division Manager Org code | Date |
| --- | --- |

| Test and Evaluation First-Line Supervisor Org code | Date |
| --- | --- |

| Operational Test Director Org code | Date |
| --- | --- |

**Table of Contents**

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Generate the “Table of Contents” with page numbers. Include Appendices. Generate “List of Figures” and “List of Tables” separately. Apply TOC-Head1, TOC-Head2, and TOC-Head3 styles for formatting. Omit level 4 sections and lower. Add letter to Appendix page number.

[1 Introduction 7](#_Toc169080711)

[1.1 Background 7](#_Toc169080712)

[1.2 Purpose 7](#_Toc169080713)

[1.3 Scope 7](#_Toc169080714)

[2 Reference Documents 7](#_Toc169080715)

[2.1 FAA Documents 7](#_Toc169080716)

[2.2 Other Government Documents 8](#_Toc169080717)

[2.3 Non-Government Documents 8](#_Toc169080718)

[3 System, Service or Capability Description 8](#_Toc169080719)

[3.1 System, Service or Capability Overview 8](#_Toc169080720)

[Figure 3.1-1. *System Name* Operational View 8](#_Toc169080721)

[3.2 Interfaces Overview 8](#_Toc169080722)

[Figure 3.2-1. *System Name* Interfaces 8](#_Toc169080723)

[3.3 Operational Use and Maintenance Concept 9](#_Toc169080724)

[4 Test Management 9](#_Toc169080725)

[4.1 Test Management Organization 9](#_Toc169080726)

[4.1.1 Integrated Test Team 9](#_Toc169080727)

[4.1.2 Test Conduct Team(s) 9](#_Toc169080728)

[4.1.3 Other Participating Organizations 10](#_Toc169080729)

[4.1.4 Operational Personnel Resource Requirements 10](#_Toc169080730)

[4.2 OT Execution 10](#_Toc169080731)

[4.3 Operational Test Schedule 11](#_Toc169080732)

[5 Basis of Test 11](#_Toc169080733)

[5.1 Program Requirements 11](#_Toc169080734)

[5.1.1 Critical Operational Issues (COIs) 11](#_Toc169080735)

[6 Test Program Description 12](#_Toc169080736)

[6.1 Test and Evaluation Approach 12](#_Toc169080737)

[6.2 OT Test Plan Activities 12](#_Toc169080738)

[6.3 OT Structure 12](#_Toc169080739)

[Figure 6-1. Test Hierarchy 13](#_Toc169080740)

[6.4 Test Activity 13](#_Toc169080741)

[6.4.1 Test Group/Cases 13](#_Toc169080742)

[7 Criteria Management and Reviews 14](#_Toc169080743)

[7.1 OT Entrance Criteria 14](#_Toc169080744)

[7.2 Test Readiness Review (TRR) 14](#_Toc169080745)

[7.3 OT Pre-test Briefings 14](#_Toc169080746)

[7.4 OT Post-Test Reviews 14](#_Toc169080747)

[7.5 OT Exit Criteria 15](#_Toc169080748)

[7.6 OT Caucus 15](#_Toc169080749)

[8 OT Reporting 15](#_Toc169080750)

[8.1 Discrepancy Reports (DRs) and Program Trouble Reports (PTRs) 15](#_Toc169080751)

[8.2 Interim Assessment Report 15](#_Toc169080752)

[8.3 Quicklook Report 15](#_Toc169080753)

[8.4 OT Final Test Report 16](#_Toc169080754)

[9 Risks and Limitations 16](#_Toc169080755)

[10 Test Resources and Supporting Activities 17](#_Toc169080756)

[10.1 Test Environment 17](#_Toc169080757)

[10.2 Test Capabilities and Accreditation 17](#_Toc169080758)

[10.3 Configuration Management 17](#_Toc169080759)

[10.3.1 System, Service or Capability Configuration Management 17](#_Toc169080760)

[10.3.2 Test Environment 17](#_Toc169080761)

[10.4 Training 18](#_Toc169080762)

[10.4.1 Test Developer Training 18](#_Toc169080763)

[10.4.2 Test Participant Training 18](#_Toc169080764)

[10.4.3 Special Training Requirements 18](#_Toc169080765)

[Appendix A: Abbreviations A-1](#_Toc169080766)

[Appendix B: COI Decomposition B-1](#_Toc169080767)

[Appendix C: OT VRTM C-1](#_Toc169080768)

**LIST of Figures**

[Figure 3.1-1. *System Name* Operational View 9](#_Toc57016853)

[Figure 3.2-1. *System Name* Interfaces 9](#_Toc57016854)

[Figure 6-1. Test Hierarchy 13](#_Toc57016855)

**List of Tables**

[Table 4‑1. Test Program ITT Roles and Responsibilities 10](#_Toc54798696)

[Table 4‑2. Operational Resource Requirements 11](#_Toc54798697)

[Table 9-1. Risks and Limitations 17](#_Toc54798698)

**This page intentionally left blank**

# Introduction

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Use the following sections to provide the reader with an introduction to the OT Test Plan.

## Background

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Present an overview of the program, including the type of acquisition (e.g., system, service or capability, Commercial Off-the-Shelf (COTS)/Non-Developmental Item (NDI), software only, etc.) that the OT program will address, and any prior test activities leading to OT (e.g., Operational Capability Demonstration (OCD), Operational Capability Test (OCT), Development Test (DT), etc.). Briefly describe the investment program goals and objectives.

## Purpose

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Define the specific purpose of the OT Test Plan. Identify the decision points and milestones supported by the OT Test Program.

This OT Test Plan contains the strategy to support the determination of operational readiness through the evaluation of suitability and effectiveness.

## Scope

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** State whether the Operational Test (OT) Plan is consistent with the T&E strategy defined in the Program Requirements Document (PRD), the Implementation Strategy and Planning Document (ISPD), the Test and Evaluation Master Plan (TEMP), and the T&E Handbook. Describe any deviations or discrepancies from these documents. Also, state the source for requirements (e.g., PRD) that the OT program addresses.

1. Reference Documents

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Use the following subsections to list the documents that are specific to this investment program relative to this plan. Include the current dates and version numbers as published.

## FAA Documents

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)**Use the following subsections to list the documents that are specific to this investment program relative to this plan. Include the current dates and version numbers as published. Identify references to the applicable FAA documents, including, at a minimum, the PRD, the ISPD, the TEMP, and the T&E Handbook.

1. *FAA WJHTC Test and Evaluation (T&E) Handbook*, VVSP-A2-PDD-013, version xxxxx, dated xxxxxx
2. *Program Name Concept of Operations (ConOps)*, version xxxxxxxxxxx, dated xxxxxx
3. *Program Name Final Program Requirements Document (fPRD)*, version xxxxxxxx, dated xx xxx xxxx
4. *Program Name Implementation Strategy and Planning Document (ISPD)*, version xxxxxxxxxx, dated xx xxxx
5. *Program Name Test and Evaluation Master Plan (TEMP)*, version xxxxxx, dated xx xx xxxx
6. *Program Name Test Team Configuration Management (CM) Plan*, version xxxxxx, dated xx xx xxxx

## Other Government Documents

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Use the following subsections to list the documents specific to this investment program relative to this plan. Include the current dates and version numbers as published.

## Non-Government Documents

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Reference any applicable non-government documents (e.g., Institute of Electrical and Electronics Engineers (IEEE), RTCA Inc., vendor documentation, contractor test documents).

# **System, Service or Capability Description**

## System, Service or Capability Overview

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)**Provide a general system, service, or capability description and an operational view diagram. Summarize the operational environment in which the system, service, or capability under test will be used.

Figure placeholder

Figure 3.1-1. *System Name* Operational View

## Interfaces Overview

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Provide a functional description of the system, service, or capability interfaces. Include a diagram depicting internal and external interfaces including data exchanges and a description of the system, service, or capability interfaces.

Figure placeholder

Figure 3.2-1. *System Name* Interfaces

## Operational Use and Maintenance Concept

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Summarize the primary operational use and general maintenance concepts for the system, service, or capability under test. This summary must be consistent with the PRD and the Concept of Operations (ConOps).

1. Test Management

## Test Management Organization

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Identify the Program Office, Government and developer test organizations. Describe the structure and composition of the test organizations and teams responsible for carrying out the testing.

### Integrated Test Team

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Describe the composition of the Integrated Test Team (ITT) that is documented in the approved TEMP for the test program. Identify the roles and responsibilities of Government and non-Government organizations that will support planning, conduct, and reporting of the test program as part of the ITT.

Table 4‑1. Test Program ITT Roles and Responsibilities

| Role | Responsibility | Organization |
| --- | --- | --- |
| OT Test Director | Responsible for the overall planning and completion of the OT phase | Organization Code |
| Test Lead | Primary technical lead for test activities |  |
| Test Team | Performs OT T&E activities |  |
| System Engineers | Requirements, architecture, and design support |  |
| Human Factors |  |  |
| Prime Contractor |  | Company Name |
| Program Office SME |  |  |

*\* Add/delete roles and responsibilities as needed.*

### Test Conduct Team(s)

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Describe the duties of the test team members. Identify the organizations represented on the test team. One or more block diagram(s) of the test team(s) may be used.

### Other Participating Organizations

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Describe specific roles and responsibilities of organizations that provide support to OT Test Plan activities and test-related events [e.g., Subject Matter Experts (SMEs), field support personnel, and providers of Government Furnished Equipment (GFE)/Government Furnished Information (GFI)].

### Operational Personnel Resource Requirements

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Describe operational personnel (e.g., Air Traffic, Technical Operations, etc.) needed for each OT test activity. Operational personnel are test participants, observers, and SMEs needed to plan, conduct, evaluate, and report on OT. The description includes operational positions required and the skills associated with each position, the role of individual test personnel, the organizations supplying the personnel, and the time period when the personnel are needed. Personnel resource requirements for operational test capability development and accreditation must be included in this section.

![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\938DE85E.tmp](data:image/jpeg;base64...) This table is necessary to coordinate required resources to ensure availability for supporting planned test activities.

Table 4‑2. Operational Resource Requirements

| Operational Position | Skills & Training Associated | Role | Organization providing the resource | Time Period |
| --- | --- | --- | --- | --- |
| ATC Specialist | Certified Air Traffic Controller | Witness testing and provide technical expertise | National Air Traffic Controllers Association (NATCA) | 3 weeks |
| Tech Ops Specialist | Certified System Specialist | Witness testing and provide technical expertise | Professional Airways Systems Specialists (PASS) | 3 weeks |
| ATC Supervisor | Certified Air Traffic Controller | Witness testing and provide technical expertise | Site A | 4 weeks |
| TFM |  |  |  |  |
| Tech Ops |  |  |  |  |
| SLE |  |  |  |  |
| TGF Pilots |  |  |  |  |
| Sim Pilots |  |  |  |  |

*\* Add/delete for other participant types as needed.*

## OT Execution

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Describe the common process and flow that will be followed for the conduct of all test sessions. Address pre-test briefings, preparatory checklists, standard procedures for managing test execution (e.g., lab coordination, use of test logs, etc.), and post-test reviews. Additionally, the common criteria used to determine if a retest will be necessary (e.g., excessive missed or failed test steps, a large number of deviations or false starts, etc.) should be included in this section. Identify test records generated during conduct, such as DR&A, test logs, as-run procedures, questionnaires, etc.

## Operational Test Schedule

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Provide a dated OT schedule that includes the known details at the time of test plan development.

![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\938DE85E.tmp](data:image/jpeg;base64...) Present the OT schedule as a Gantt chart, and include other development/acquisition activities (e.g., test procedure development and dry runs, test capability development and accreditation, etc.) and milestones, as appropriate, to indicate interdependencies.

# Basis of Test

The following subsections describe the Program Requirements including the Critical Program Requirements (CPRs), the Critical Operational Issues (COIs), the MOEs/MOSs/MOPs, and the T&E approach for the OT Program.

## Program Requirements

![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\938DE85E.tmp](data:image/jpeg;base64...) OT must validate all applicable program requirements in the PRD. A subset of those requirements are the CPRs. CPRs are program requirements that are deemed essential in meeting the mission need that the investment program is seeking to satisfy. Special emphasis is placed on these requirements ensuring their visibility so management can make prudent and timely decisions.

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Provide the approved list of the CPRs from the fPRD and/or the TEMP. Identify the sources of requirements that form the basis for the OT. Programs may also place special emphasis on evaluation of SSD requirements, if applicable.

### Critical Operational Issues (COIs)

This section lists the approved COIs from the fPRD and/or the TEMP. The COI number is represented as the first numeral in the MOE/MOS/MOP identification. See Appendix B for the decomposition of COIs.

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** List the approved COIs from the fPRD and/or the TEMP.

![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\938DE85E.tmp](data:image/jpeg;base64...) COIs are key operational effectiveness or suitability issues that must be examined during OT to determine a product’s capability to perform its mission. A breakdown of the COIs into Measures of Effectiveness (MOEs), Measures of Suitability (MOSs), and ultimately, Measures of Performance (MOPs) is included in the OT Test Plan as Appendix B. Additionally, Appendix C includes a Verification Requirements Traceability Matrix (VRTM), which traces the COIs/CPRs/MOEs/MOSs/MOPs and applicable program requirements to the respective OT Test Plan activities and test cases where the MOPs and requirements are verified and/or validated.

1. Test Program Description

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Use the following subsections to describe the plans for the OT program.

## Test and Evaluation Approach

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Describe the overall test approach and reporting strategy applied to all OT addressed in this plan.

![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\938DE85E.tmp](data:image/jpeg;base64...) A systematic approach is used to evaluate the system, service, or capability under a range of operational conditions that are representative of those found at field facilities. OT activities use operationally representative systems, services, or capabilities along with realistic loads, realistic simulated interfaces and/or real interfaces, new and/or revised operational documentation, operational personnel, and actual operational procedures. OT evaluations and reports address the level of performance based on the CPRs, COIs, and applicable program requirements in support of decision-making, leading to operational use of the system, service, or capability.

## OT Test Plan Activities

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Identify the major OT Test Plan activities executed to evaluate the system, service, or capability (e.g., NAS Integration Testing, Stress and NAS Load Testing, Safety Testing, Security Testing, etc.).

## OT Structure

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Describe the test hierarchy from the OT activity level down to the individual test cases. An illustration or text may be used. Test cases may be combined as a test case group. Sample Figure 6-1, Test Hierarchy, depicts test cases as grouped (optional) or ungrouped.

Figure 6-1. Test Hierarchy

## Test Activity

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Specify the title and a sequential number designation for each test activity and each subsequent test case. Number subsequent sections and associated subsections accordingly (e.g., 6.4.1, 6.4.2, … 6.4.X).

### Test Group/Cases

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Provide an introduction to the subsections.

The following sections describe each test case to be conducted and contain sufficient information for planning and developing the test procedures and scheduling the test cases.

![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\938DE85E.tmp](data:image/jpeg;base64...) Test case groups may be used to logically organize similar test cases.

#### Test Case Title

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Refer to numbering guidance in Section 6.4, above. Replace this title with the title of the test case.

##### Test Case Objectives And Criteria

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** State the objective(s) of the test case and the criteria for meeting these objectives. The criteria describe the conditions necessary for meeting the test objectives.

The objective of this test case is to evaluate systems, service or capability performance under maximum track capacity. The criterion for meeting this objective is that the xxx system, service, or capability meets the requirements specified in Section 6.4.1.1.x, under a simulated maximum track loading.

##### Test Case Requirements

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** List in tabular format the MOEs/MOSs/MOPs and the requirements that the test case verifies/validates. Additionally, identify whether the MOEs/MOSs/MOPs and requirements are fully verified/validated or only partially verified/validated by this test case. When the MOE/MOS/MOP or requirement is only partially verified/validated, include the name and number of the test case(s) required to complete the verification/validation.

##### Test Case Approach

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** State the methods used to meet the test objectives and verify/validate the MOPs and the requirements allocated to the test case. This description includes a list of the types of tasks or activities that will occur, the specific test conditions and test scenarios, and special operational situations that may occur in the test. The test approach specifies the type and number of personnel, any special test equipment, and data collection methods needed.

##### Data Collection and Analysis Methods

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Explain how the test data is obtained and describe the method of analysis.

# Criteria Management and Reviews

## OT Entrance Criteria

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** List the items and conditions, such as system, service, or capability readiness and planned project milestones that must be met before testing can begin. Identify the TRR requirements to assess if the entrance criteria has been met. (Note: Test procedures will include more specific test readiness criteria.) Describe how discrepancies in meeting the criteria will be addressed, if applicable.

## Test Readiness Review (TRR)

![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\938DE85E.tmp](data:image/jpeg;base64...) The TRR serves as the formal review to confirm that the entrance criteria have been satisfied and OT can begin. The OT TRR is conducted by the OT test team prior to the start of the formal OT activity. This review verifies and approves the readiness to start formal OT and ensures participants understand the outstanding issues. The TRR also communicates risks and limitations for formal OT.

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Follow the guidance in the T&E Handbook to complete this subsection.

## OT Pre-test Briefings

![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\938DE85E.tmp](data:image/jpeg;base64...) The OT Test Lead conducts the OT Pre-Test Briefing before the start of each Test Case. The Pre-Test Briefings must include the approach of each test case.

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Follow the guidance in the T&E Handbook to complete this subsection.

## OT Post-Test Reviews

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** In accordance with the T&E Handbook, detail how each OT post-test review will be conducted after each test activity.

The OT Test Director will review test case results at the end of each day, including those at the end of a test-case group. In addition, the Post-Test Review will assess the results at the end of each test activity. A Final Post-Test Review will be conducted that rolls up the results of all test activities.

## OT Exit Criteria

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Describe the measures, standards, or conditions that must be met to ensure the OT objectives have been satisfied and that the system, service, or capability has been adequately verified and validated for operational effectiveness and suitability.

## OT Caucus

![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\938DE85E.tmp](data:image/jpeg;base64...) The OT Test Director conducts a caucus where all findings and test results related to operational effectiveness and suitability of the system are presented and reviewed.

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Describe the conduct of the OT Caucus at the completion of formal OT. Describe the process for conducting and reporting the results of the OT Caucus in an OT Caucus Summary Report.

![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\938DE85E.tmp](data:image/jpeg;base64...) At a minimum, the participants include representatives from the OT team and the field team(s). In preparation for the caucus, all OT Discrepancy Reports (DRs) and Program Trouble Reports (PTRs) are entered into an OT Problem Traceability Matrix, which is reviewed to assess the impact of DRs and PTRs on COIs, MOEs, MOSs, MOPs, and CPRs, and to determine their operational criticality. All DRs that require corrective action by the developer are raised to PTR status and assigned initial priorities to assist with resolution plans. Each COI must be answered based on the criticality of the problem(s) impacting it. The test team must status the safety hazards linked to requirements and report any new safety hazards.

# OT Reporting

## Discrepancy Reports (DRs) and Program Trouble Reports (PTRs)

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Describe the process of recording, prioritizing, tracking, and correcting deficiencies experienced during OT. Address the handling of supporting records.

## Interim Assessment Report

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Describe the plan for writing an Interim Assessment Report (IAR).

![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\938DE85E.tmp](data:image/jpeg;base64...) The OT IAR is an optional reporting mechanism that provides management with an assessment of the current state and maturity of the system by identifying system capabilities and limitations as tested for that reporting period. OT IARs are developed following specific milestones, whether issues exist or not, as defined in the TEMP.

## Quicklook Report

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Describe the plan for writing a Quicklook Report.

![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\938DE85E.tmp](data:image/jpeg;base64...) The OT Quicklook Test Report is developed following the completion of formal OT to provide a preliminary assessment of operational readiness. This report is provided in advance of the more detailed Final Test Report that requires more analysis and time to complete. The Quicklook Test Report contains preliminary results and, therefore, is not typically used to support programmatic or operational milestone decisions.

## OT Final Test Report

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Describe the plan for writing the OT Final Report.

![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\938DE85E.tmp](data:image/jpeg;base64...) The OT Final Test Report must include conclusions regarding operational effectiveness and suitability based on the combined results of all operational tests. Operational readiness is assessed on the basis of operational effectiveness and suitability performance in accordance with COIs and CPRs. The OT Final Test Report is used to support an In-Service Decision (ISD) or other deployment decision, and must include a very clear statement regarding whether the system is Operationally Ready (effective and suitable). In addition, the report addresses the risks and system limitations associated with shortfalls in meeting mission needs, operational requirements, and safety requirements.

# Risks and Limitations

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Use the following table to list the risks and limitations that affect full verification and validation of the system, service, or capability under test. In the first column, indicate R for a risk or L for a limitation and then number each item (e.g., R001 and L001 are the first items for each). In the second column, describe the potential impacts of any risks and proposed mitigations. Additionally, describe any known limitations affecting the evaluation of program requirements (e.g., lack of true realism due to simulation rather than live operations, unavailability of critical interfaces, etc.), as well as any planned workarounds, if any.

Table 9-1, Risks and Limitations, presents risks and limitations affecting full verification and validation of the system under test.

Table 9-1. Risks and Limitations

| Item | Description with Mitigation or Workaround |
| --- | --- |
| R001 | **<u>Risk:</u>** Some test procedures are manually intensive and will require additional schedule time to collect sufficient sample sizes for completion. Limiting the duration of these tests may limit sample size and therefore may affect results.  **<u>Mitigation:</u>** To minimize this risk, the development and execution of automated scripts required for large sample measurement will be prioritized and completed first. In addition, the planned OT schedule will include test procedure preparation, Dry Run and Formal Dry Run time. |
| L001 | **<u>Limitation</u>**: It is not possible to simulate more than one site at a time. |
| L002 | **<u>Limitation</u>**: As currently planned, OT lab configurations will require an automated test suite of accredited tools and equipment executing software scripts and scenarios.  **<u>Workaround</u>**: If the test suite cannot be automated and accredited prior to the start of DT and OT respectively, some testing will need to be performed manually. |

***Legend:*** *L = Limitation, R = Risk*

# Test Resources and Supporting Activities

## Test Environment

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Describe the test facilities required for testing and the number of systems, services or capabilities that are needed for those test facilities. Identify and describe whether multiple test environment configurations will be used.

![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\938DE85E.tmp](data:image/jpeg;base64...) The descriptions include the test locations and environmental conditions (e.g., weather, terrain) as appropriate. For example, some systems, services or capabilities may require testing at several test locations that represent the range of environmental and operational conditions in which the system, service or capability is used. This section also describes how closely the test environment represents the actual, intended operational environment. For example, some testing may be performed using testbeds, simulators and other drivers, and may not include actual interfaces and external equipment.

## Test Capabilities and Accreditation

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** List and describe the test, data reduction, and analysis tools used to support testing. These tools may include hardware (e.g., instrumentation, prototypes/mockups) and/or software (e.g., simulators, software programs). Include plans for test tool accreditation or reference a separate OT Accreditation Plan.

## Configuration Management

### System, Service or Capability Configuration Management

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Describe how the configuration of the system, service, or capability under test will remain consistent (e.g., configuration audits). Identify how changes to the baseline system, service, or capability will be controlled. If available, identify the Test Program Configuration Management (CM) Plan. Describe the process to maintain CM and test artifacts.

### Test Environment

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Identify or list the test environment elements and related test tools under CM. Describe how CM will be maintained in the test environment during OT.

## Training

### Test Developer Training

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Describe the type of knowledge of the system, service, or capability the test developers need. Identify where and when the required developer training will be provided and by whom. You may expand Table 4‑2, Resource Requirements, to include this information.

### Test Participant Training

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Describe the level of training and familiarization that participants need to operate the systems, service or capability during test. Identify where and when the required participant training will be provided and by whom. For example, system operators participating in OT receive training that represents the training that actual operators receive to perform their jobs with the new system, service, or capability. You may expand Table 4‑2, Resource Requirements, to include this information.

### Special Training Requirements

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Describe any special training needed by the test team(s), for example, familiarization with the test program and the test facility, use of special test tools, etc. You may expand Table 4‑2, Resource Requirements, to include this information.

Appendix A: Abbreviations

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)** Identify all abbreviations used in this OT Plan.

|  |  |
| --- | --- |
| Term | Definition |
|  |  |
|  |  |
|  |  |

Appendix B: COI Decomposition

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)**Using the COIs listed in Section 5.1.1, decompose them into MOEs, MOSs, and ultimately MOPs. Include associated OT Test activities and test cases for each MOP.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Critical Operational Issue (COI) | Measures of Effectiveness (MOEs) | Measures of Suitability (MOSs) | Measures of Performance (MOPs) | Test Activity |
| **COI 1.0**: text |  |  |  |  |
|  | **MOE 1.1**: text |  | **MOP 1.1.1**: text | **1.1.1**: text |
|  |  |  | **MOP 1.1.2**: text | **1.1.2**: text |
|  | **MOE 1.2**: text |  | **MOP 1.2.1**: text | **1.2.1**: text |
|  |  |  | **MOP 1.2.2**: text | **1.2.2**: text |
| **COI 2.0**: text |  | **MOS 2.1**: text | **MOP 2.1.1**: text | **2.1.1**: text |
|  |  |  | **MOP 2.1.2**: text | **2.1.2:** text |
|  |  | **MOS 2.2**: text | **MOP 2.2.1**: text | **2.2.1**: text |
|  |  |  | **MOP 2.2.2**: text | **2.2.2:** text |

Appendix C: OT VRTM

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)**Trace the COIs/MOEs/MOSs/MOPs and applicable program requirements to the respective OT Test activities and test cases in which the MOPs and requirements will be verified and/or validated.

| **COI/MOE/ MOS/MOP ID** | **COI/MOE/MOS/MOP TEXT** | **RELATED PRD REQS** | **PRD**  **TEXT** | **RELATED**  **SSD REQS** | **CPR (N/A OR #)** | **ACTIVITY ID** | **TEST CASE ID** | **VERIF METHOD** | **RUN DATE** | **TEST RESULT** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| COI-01 | Does the SYSTEM provide the ability to capture and process NAS data? | \* | \* | \* | \* | \* | \* | \* |  |  |
| MOS-01.1 | SYSTEM provides the ability to receive, process, and maintain flight data. | PRD-221 | The System must have the ability to capture… | \* | 3, 5 | \* | \* | \* |  |  |
| MOP-01.1.1 | Receive flight data messages… | PRD-221 | The System must have the ability to receive… | SSD4, SSD452 | 3 | Stability Test | 3.5.4.1 | D |  |  |
| MOP-01.1.2 | Perform format, logic, and range checks… | PRD-2212 | The System must have the ability to perform… | SSD6, SSD10, SSD37, SSD452 | 5 | Failure Mode | 3.5.4.2 | T |  |  |

**![C:\Users\Angela CTR Moore\AppData\Local\Microsoft\Windows\INetCache\Content.MSO\B700F4F2.tmp](data:image/png;base64...)**Add appendices to this test plan, as appropriate, to provide detailed information.

Additional Appendices Placeholder
