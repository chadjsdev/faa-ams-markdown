---
title: "TEHandbook"
source_url: https://www.faa.gov/sites/faa.gov/files/about/office_org/headquarters_offices/ang/TEHandbook.pdf
source_type: pdf
converted: 2026-10-27
---
# TEHandbook



**FAA William J. Hughes Technical Center** 

# **Test and Evaluation Handbook** 

|**DOCUMENT# **|**VVSPT-A2-PDD-013**|
|---|---|
|**VERSION# **|**5.0**|
|**VERSIONDATE**|**December 18, 2020**|
|**DIVISION**|**Air Traffic Systems**<br>**T&E Services, ANG-E5**|
|**BRANCH**|**V&V Strategies and Practices, ANG-E5A**|



#### **FAA William J. Hughes Technical Center Atlantic City International Airport, New Jersey 08405** 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

## **Intentionally Blank** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

ii 

**<u>T</u> EST &** **<u>E</u> VALUATION H ANDBOOK** 

# **APPROVAL SIGNATURES** 

**DOCUMENT TITLE: TEST AND EVALUATION HANDBOOK** 

Shelley J. Yak Date Director, William J. Hughes Technical Center Michael Greco Date Manager, Enterprise Services T&E Division Paula Nouragas Date Manager, Air Traffic Systems T&E Services Division John Frederick Date Manager, V&V Strategies and Practices Branch 

VVSPT-A2-PDD-013 v5.0 

12/ 18 /2020 

iii 

# **DOCUMENT VERSION CONTROL** 

|**VERSION**|**DESCRIPTION OFCHANGE**|**DATE**|
|---|---|---|
|1.0|Initial delivery for T&E process implementation|08/21/2008|
|2.0|Incorporated comments against Draft V1.2 as<br>detailed in the V&V Repository Comments<br>Database|08/31/2010|
|3.0|Release Version 3.0|09/24/2013|
|4.0|Final for Division Signature|5/16/2017|
|5.0|Release Version 5.0|12/18/2020|



## **TABLE OF CONTENTS** 

|**1**<br>**INT**|**RODUCTION ....**|**............................................................................................................................ 1-1**|
|---|---|---|
|1.1|VERIFICATION A|NDVALIDATIONPRINCIPLES.................................................................................. 1-1|
|1.2|OBJECTIVES OF|THETEST ANDEVALUATIONHANDBOOK................................................................ 1-3|
|1.3|SCOPE OF THE|TEST ANDEVALUATIONHANDBOOK........................................................................ 1-3|
|1.4|ROLES ANDRE|SPONSIBILITIES...................................................................................................... 1-4|
|1.5|FUNDAMENTAL|PRACTICES FORQUALITYTEST ANDEVALUATION................................................... 1-4|
|1.6|TAILORING AND|OPTIMIZING OFTEST ANDEVALUATIONPROCESSES.............................................. 1-5|
||1.6.1<br>Tailoring|Criteria and Processes ...................................................................................... 1-6|
||1.6.2<br>Tailoring|Guidelines ......................................................................................................... 1-7|
||1.6.2.1|Types of Tailoring ............................................................................................. 1-7|
||1.6.2.2|Commonly Tailored Processes ......................................................................... 1-7|
||1.6.3<br>Agile Ac|quisition Principles in T&E .................................................................................. 1-7|
|1.7|TEST ANDEVAL|UATIONSTANDARDSCONFORMANCEPROCESS...................................................... 1-8|
|1.8|TEST ANDEVAL|UATIONQUALITYMANAGEMENTSYSTEMPROCESSES............................................ 1-9|
|1.9|PEERREVIEWS|.......................................................................................................................... 1-10|
|**2**<br>**RE**|**LATED DOCUM**|**ENTS AND REFERENCES................................................................................ 2-1**|
|**3**<br>**TE**<br>**LIF**|**ST AND EVALU**<br>**ECYCLE ...........**|**ATION SUPPORT ACROSS THE ACQUISITION MANAGEMENT SYSTEM**<br>**............................................................................................................................ 3-1**|
|**4**<br>**TE**<br>**AN**|**ST AND EVALU**<br>**D CONCEPT AN**|**ATION SUPPORT TO SERVICE ANALYSIS AND STRATEGIC PLANNING**<br>**D REQUIREMENTS DEFINITION .................................................................... 4-1**|
|**5**<br>**TE**|**ST AND EVALU**|**ATION SUPPORT TO INVESTMENT ANALYSIS ............................................. 5-1**|
|5.1|PROGRAMREQ|UIREMENTSDOCUMENTSUPPORT.......................................................................... 5-1|
|5.2|TEST ANDEVAL|UATIONMASTERPLANDEVELOPMENT................................................................... 5-2|
||5.2.1<br>Test and|Evaluation Master Plan Objectives ................................................................... 5-4|
||5.2.2<br>Test Ma|nagement Using the Test and Evaluation Master Plan ...................................... 5-5|
||5.2.3<br>Test De|sign Process ........................................................................................................ 5-7|
||5.2.3.1|Identification and Assessment of Requirements .............................................. 5-7|
||5.2.3.2|Decomposition of Critical Operational Issues ................................................... 5-8|
||5.2.3.3|Critical Performance Requirements Evaluation Approach ............................. 5-10|
||5.2.3.4|Defining Test Activities ................................................................................... 5-11|
||5.2.3.5|Formulating the Test and Evaluation Master Plan Verification Requirements|
|||<br>Traceability Matrix .......................................................................................... 5-12|
||5.2.3.6|<br>Identifying Test Capability Requirements ....................................................... 5-13|
||5.2.3.7|Defining a Test Schedule ............................................................................... 5-14|
||5.2.3.8|Assessing Updates and Acquisition Program Baseline Changes .................. 5-14|
||5.2.3.9|<br>Documenting the Test Design in the Test And Evaluation Master Plan......... 5-14|
||5.2.3.10|<br> Interim Assessment Report Planning ............................................................. 5-15|
|5.3|IMPLEMENTATIO|NSTRATEGY ANDPLANNINGDOCUMENTSUPPORT.............................................. 5-15|
|5.4|FAA SYSTEMS|PECIFICATIONSUPPORT...................................................................................... 5-16|
|5.5|SCREENINGINF|ORMATIONREQUESTSUPPORT........................................................................... 5-17|
||5.5.1<br>Section|L of the SIR:  Instructions, Conditions, and Notices to Offerors ....................... 5-17|
||5.5.2<br>Section|C of the Screening Information Request:  Description Of Work Requirements 5-17|



||5.5.2.1|Statement of Work /Performance Work Statement ........................................ 5-18<br>|
|---|---|---|
||5.5.2.2|Statement of Objectives ................................................................................. 5-18|
|5.6<br>PRO|POSALEVA|<br>LUATIONSUPPORT.............................................................................................. 5-19|
|**6**<br>**TEST AN**<br>**TESTING**|**D EVALU**<br>**................**|**ATION SUPPORT TO SOLUTION IMPLEMENTATION – DEVELOPMENTAL**<br>**............................................................................................................................ 6-1**|
|6.1<br>DEVE|LOPMENT|TESTOVERVIEW................................................................................................... 6-1|
|6.1.1|Develop|ment Test Activities ............................................................................................. 6-1|
||6.1.1.1|Agile Acquisition in acquisition Management System ...................................... 6-3|
|6.1.2|Develop|ment Test Requirements .................................................................................... 6-4|
|6.1.3|Develop|ment Test Support to Contract Administration .................................................... 6-7|
||6.1.3.1|Development Test Screening Information Request Support ............................ 6-7|
||6.1.3.2|Contractor Documentation Support .................................................................. 6-7|
||6.1.3.3|Contractor Test Document Review Standards ................................................. 6-8|
||6.1.3.4|Formal Audit and Government Acceptance Activities Support ........................ 6-9|
|6.1.4|Develop|ment Test Engineering Support .......................................................................... 6-9|
|6.2<br>DEVE|LOPMENT|TESTPLANNING.................................................................................................... 6-9|
|6.2.1|Develop|ment Test Approach and Strategies ................................................................. 6-10|
||6.2.1.1|Commercial Off the Self/Non-Development Item Testing .............................. 6-10|
||6.2.1.2|<br>Development Test Software Testing .............................................................. 6-11|
||6.2.1.3|Development Test Hardware Testing ............................................................. 6-12|
||6.2.1.4|Factory Acceptance Testing ........................................................................... 6-12|
||6.2.1.5|Functional Qualification Testing ..................................................................... 6-13|
||6.2.1.6|Development Test Installation and Integration Testing .................................. 6-13|
||6.2.1.7|Development Test System Testing ................................................................. 6-14|
||6.2.1.8|Production Acceptance Testing ...................................................................... 6-15|
||6.2.1.9|Site Acceptance Testing ................................................................................. 6-15|
||6.2.1.10|Development Test Capability Accreditation .................................................... 6-16|
||6.2.1.11|Coordination Between Development and Operational Test Directors ............ 6-16|
||6.2.1.12|Development Test Training and Familiarization ............................................. 6-17|
|6.2.2|Contract|or Master Test Plan .......................................................................................... 6-17|
|6.2.3|Develop|ment Test Verification Requirements Traceability Matrix ................................. 6-18|
|6.2.4|Develop|ment Test Integration Test Planning ................................................................. 6-19|
|6.2.5|Develop|ment Test Plans ................................................................................................ 6-20|
|6.2.6|Develop|ment Test Procedures ...................................................................................... 6-20|
|6.2.7|Develop|ment Test Entrance Criteria .............................................................................. 6-21|
|6.2.8|Develop|ment Test Exit Criteria ...................................................................................... 6-21|
|6.3<br>DEVE|LOPMENT|TESTCONDUCT.................................................................................................. 6-22|
|6.3.1|Develop|ment Test Debug and Dry Run Testing ............................................................ 6-22|
|6.3.2|<br>Develop|<br>ment Test Readiness Review ........................................................................... 6-22|
|6.3.3|Develop|ment Test Pre-Test Briefings ............................................................................ 6-23|
|6.3.4|Formal D|evelopment Test Execution ............................................................................. 6-24|
|6.3.5|Develop|ment Test Post-Test Reviews ........................................................................... 6-24|
|6.3.6|Develop|ment Test Status Reports ................................................................................. 6-25|
|6.3.7|Develop|ment Test Problem Reporting Processes ......................................................... 6-25|
|6.3.8|Develop|ment Test Regression Testing .......................................................................... 6-26|
|6.4<br>DEVE|<br>LOPMENT|<br>TESTREPORT..................................................................................................... 6-26|



|**7**<br>**TEST AN**<br>|**D EVALUATION SUPPORT TO SOLUTION IMPLEMENTATION – OPERATIONAL**<br>|
|---|---|
|**TESTING**|**............................................................................................................................................ 7-1**|
|7.1<br>OPE|RATIONALTESTOVERVIEW.................................................................................................... 7-1|
|7.1.1|National Airspace System Integration Testing ................................................................. 7-1|
|7.1.2|Operational Effectiveness and Suitability Testing ............................................................ 7-2|
|7.2<br>PUR|POSE OFOPERATIONALTEST................................................................................................. 7-2|
|7.3<br>OPE|RATIONALTESTTEAMTASKS ANDFUNCTIONS........................................................................ 7-2|
|7.3.1|Operational Test Team Organization ............................................................................... 7-4|
|7.3.2|Operational Test Planning in Test and Evaluation Master Plan Development ................ 7-4|
|7.3.3|Operational Test Support to Contract Administration ...................................................... 7-4|
|7.3.4|Operational Test Training ................................................................................................ 7-5|
|7.3.5|Coordination with Operational Test Field Personnel ....................................................... 7-5|
|7.3.6|OT Test Capability Accreditation ..................................................................................... 7-5|
|7.4<br>OPE|RATIONALTESTPLANNING..................................................................................................... 7-5|
|7.4.1|Operational Test Plan Development ................................................................................ 7-5|
|7.4.2|Operational Test Verification Requirements Traceability Matrix ...................................... 7-6|
|7.4.3|Operational Test Procedure Development ...................................................................... 7-7|
||7.4.3.1<br>Operational Test Procedure Formulation ......................................................... 7-7|
||7.4.3.2<br>Operational Test Procedure Questionnaires .................................................... 7-7|
|7.4.4|Logistics for Formal Test Conduct ................................................................................... 7-8|
|7.4.5|Operational Test Entrance Criteria .................................................................................. 7-9|
|7.4.6|Operational Test Exit Criteria ........................................................................................... 7-9|
|7.5<br>OPE|RATIONALTESTCONDUCT................................................................................................... 7-10|
|7.5.1|Debug and Dry Runs...................................................................................................... 7-10|
|7.5.2|Operational Test Readiness Review .............................................................................. 7-11|
|7.5.3|Formal Operational Test Conduct .................................................................................. 7-12|
||7.5.3.1<br>Operational Test Pre-Test Briefings ............................................................... 7-12|
||7.5.3.2<br>Operational Test Execution ............................................................................ 7-12|
||7.5.3.3<br>Operational Test Post-Test Reviews and Test Status Reporting ................... 7-12|
|7.5.4|Operational Test Discrepancy Reporting ....................................................................... 7-13|
|7.5.5|Operational Test Caucus ............................................................................................... 7-14|
|7.5.6|Operational Test Regression Testing ............................................................................ 7-16|
|7.6<br>OPE|RATIONALTESTREPORTING................................................................................................. 7-16|
|7.6.1|Operational Test Interim Assessment Report ................................................................ 7-17|
|7.6.2|Operational Test Quicklook Test Report ........................................................................ 7-17|
|7.6.3|Operational Test Final Test Report ................................................................................ 7-18|
|7.7<br>TRA|NSITION TOIN-SERVICEMANAGEMENT.................................................................................. 7-20|
|7.8<br>FIEL|DFAMILIARIZATIONSUPPORT............................................................................................... 7-20|
|7.8.1|Field Familiarization Support Planning .......................................................................... 7-20|
|7.8.2|Field Familiarization Support Preparation ...................................................................... 7-21|
|7.8.3|Field Familiarization Support Conduct ........................................................................... 7-21|
|7.8.4|Field Familiarization Reporting ...................................................................................... 7-22|



|**8**<br>**TEST AND EVALUATION SUPPORT TO IN-SERVICE MANAGEMENT ....................................... 8-1**|
|---|
|8.1<br>MAJORPROGRAMUPGRADESUPPORT......................................................................................... 8-1|
|8.2<br>MINORPROGRAMUPGRADESUPPORT.......................................................................................... 8-1|
|8.3<br>SPECIALSUPPORTACTIVITIES...................................................................................................... 8-1|
|**9**<br>**TEST PREPARATION AND DEPLOYMENT DECISION SUPPORT ............................................... 9-1**|
|9.1<br>TESTCAPABILITYACCREDITATION................................................................................................ 9-1|
|9.1.1<br>Accreditation Definitions .................................................................................................. 9-1|
|9.1.2<br>Accreditation Testing........................................................................................................ 9-3|
|9.1.3<br>Accreditation Process ...................................................................................................... 9-4|
|9.1.4<br>Accreditation Guidance .................................................................................................... 9-4|
|9.2<br>IN-SERVICEREVIEWCHECKLIST ANDDEPLOYMENTDECISIONPLANNING........................................ 9-5|
|9.3<br>TESTNAS CHANGEPROPOSALS.................................................................................................. 9-6<br>**LIST OF FIGURES**|
|Figure 1-1.  Test and Evaluation Application to the V-Model ..................................................................... 1-2|
|Figure 3-1.  Typical Test and Evaluation Approach throughout the Acquisition Management<br>System Lifecycle .............................................................................................................. 3-3|
|Figure 3-2.  Test and Evaluation Phases and Requirements .................................................................... 3-4|
|Figure 5-1.  Test Category Hierarchy and Documentation ........................................................................ 5-3|
|Figure 5-2.  Test and Evaluation Master Plan Relational Diagram ............................................................ 5-6|
|Figure 5-3.  Generic Test and Evaluation Master Plan Test Design Process ........................................... 5-8|
|Figure 5-4.  Decomposition of Critical Operation Issues to Test Cases .................................................... 5-9|
|Figure 6-1.  Typical Development Test Activities ....................................................................................... 6-3|
|Figure 6-2.  Development Test Process Flow ............................................................................................ 6-5|
|Figure 6-3.  Site Acceptance Test Process Flow ....................................................................................... 6-6|
|Figure 7-1.  Operational Test Process Flow .............................................................................................. 7-3|
|Figure 7-2.  Operational Test: Critical Requirements Path ...................................................................... 7-15|
|Figure 9-1.  Test Capability Accreditation Process .................................................................................... 9-2|



## **APPENDICES** 

|Appendix A.  Acronyms and Glossary .......................................................................................................A-1|
|---|
|Appendix B.  Test Planning Process Conformance Checklist ...................................................................B-1|
|Appendix C.  Development Test Process Conformance Checklist ........................................................... C-1|
|Appendix D.  Operational Test Process Conformance Checklist ............................................................. D-1|
|Appendix E.  Test and Evaluation Work Products and Review Process Cycles .......................................E-1|
|Table E-1.  T&E Work Products .......................................................................................................... E-1|
|Figure E-1.  Program Requirements (Test & Evaluation Section) Review, Endorsement and/or<br>Approval Cycle ................................................................................................................ E-3|
|Figure E-2.  Implementation Strategy and Planning Document (Test & Evaluation Section)<br>Review, Endorsement and/or Approval Cycle ................................................................ E-4|
|Figure E-3.  Preliminary, Initial, and Final Test and Evaluation Master Plan Review, Endorsement<br>and/or Approval Cycle ..................................................................................................... E-5|
|Figure E-4.  Test & Evaluation Input Review Cycle for FAA System Specification, Screening<br>Information Request, Proposal Requirements, and Statements of Work Review<br>Endorsement and/or Approval Cycle .............................................................................. E-6|
|Figure E-5.  Contractor Master Test Plan Review, Endorsement and/or Approval Cycle .................. E-7|



|Figure E-6.  Development Test Plan Review, Endorsement and/or Approval Cycle (Also used<br>for Development Test Accreditation Plan) ...................................................................... E-8|
|---|
|Figure E-7.  Development Test Procedures Review, Endorsement and/or Approval Cycle .............. E-9|
|Figure E-8.  Development Test Report Review, Endorsement and/or Approval Cycle .................... E-10|
|Figure E-9.  Development Test Accreditation Record Review, Endorsement and/or Approval<br>Cycle ............................................................................................................................. E-11|
|Figure E-10.  Operational Test Plan Review, Endorsement and/or Approval Cycle (Also used<br>for Operational Test Accreditation Plan) .................................................................... E-12|
|Figure E-11.  Operational Test Procedures and Test Capability Procedures Review, Endorsement<br>and/or Approval Cycle ............................................................................................... E-13|
|Figure E-12.  Operational Test Interim Assessment Report Review, Endorsement and/or<br>Approval Cycle ........................................................................................................... E-14|
|Figure E-13.  Operational Test Quicklook Test Report Review, Endorsement and/or<br>Approval Cycle ........................................................................................................... E-15|
|Figure E-14.  Operational Test Final Test Report Review, Endorsement and/or Approval Cycle ... E-16|
|Figure E-15.  Field Familiarization Support Plan Review, Endorsement and/or Approval Cycle ..... E-17<br>Figure E-16.  Operational Test, Accreditation Test, Accreditation Record Review, Endorsement<br>and/or Approval Cycle ............................................................................................... E-18|



**<u>TEST & E</u> VALUATION H ANDBOOK** 

## **1 INTRODUCTION** 

This Handbook provides standard processes for conducting high quality and consistent Test and Evaluation (T&E) practices that support the mission of Verification and Validation (V&V). 

## **1.1 VERIFICATION AND V ALIDATION PRINCIPLES** 

As part of the Federal Aviation Administration (FAA) mission, the William J. Hughes Technical Center (WJHTC) is actively engaged in applying effective V&V principles and practices to T&E efforts.  The intent of this initiative is to improve the quality of T&E across systems, services, or capabilities; promote effective planning; reduce risks; and decrease costs.  This initiative addresses the standards for V&V process areas that are based on the Capability Maturity Model Integration (CMMI<sup>®</sup> )<sup>1</sup> standards, published by the Software Engineering Institute of Carnegie Mellon University. 

The purpose of verification is to ensure that a system, service, or capability is built right, while validation ensures that the right system, service, or capability is built.  Verification and validation represent complementary process areas that are distinguished below. 

- **Verification** - Confirmation that selected systems, services, or capabilities meet their specified requirements.  This includes evaluation of the system, service, or capability and intermediate elements against all applicable requirements. Verification is inherently an incremental process since it occurs throughout the development lifecycle of the system, service, or capability, beginning with initial requirements, progressing through subsequent changes, and culminating in verification of the completed end product. 

- **Validation** - Confirmation that an end system, service, capability, or component fulfills its intended purpose when placed in its intended environment.  The methods employed to accomplish validation are applied to selected components as well as to the end system, service, or capability.  The selection of the components should be based on which are the best predictors of how well the end system, service, or capability and their components satisfies the intended purpose and user needs. Validation can apply to all aspects of an end system, service, or capability in any of its intended environments, such as operation, training, manufacturing, maintenance or support services. 

Combined, V&V is a disciplined approach of assessing a system, service, or capability throughout its lifecycle.  V&V strives to ensure that quality is built into the system, service, or capability and that it satisfies operational requirements.  A strong focus on validation, an industry best practice, also helps to ensure customer satisfaction.  The T&E standards defined in this Handbook support a significant portion of a comprehensive V&V approach. Some CMMI V&V practices are executed outside of the T&E function, such as those that apply to the systems engineering discipline and are therefore not addressed in this 

> 1 CMMI is <mark>registered in the U.S. Patent and Trademark Office by Carnegie Mellon University.</mark> 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

1-1 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

document.  The relationship of how the T&E function applies to V&V is depicted in Figure 1-1.  The V-Model illustrates the interactions between each phase of the Acquisition Management System (AMS) lifecycle and its associated T&E phase [i.e., T&E Planning and Support, Development Test (DT), and Operational Test (OT)]. 



**Figure 1-1.  Test and Evaluation Application to the V-Model** 

The V-Model shown in Figure 1-1 illustrates that both Verification and Validation are performed throughout all phases of the AMS lifecycle, from research and concept development, through design and implementation, integration, testing and deployment. 

V&V is performed in varying degrees on a continuous basis by many entities involved in an investment program.  For instance, System Engineering has a primary role in the V&V of requirements and concepts, while the T&E organization has an equivalent role in the V&V of the integration and test of the system, service, or capability. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

1-2 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

Within the context of V&V, T&E practitioners play a critical role in the AMS lifecycle.  As depicted in Figure 1-1, the arrows on the outside of the figure depict the phases of T&E described in this Handbook.  The arrow on the left side of the “V” represents the T&E Planning and Support phase.  The primary V&V role of T&E during this phase is to support the development of concepts, requirements, and design.  The arrows on the right side of the “V” represent the DT and OT phases.  The primary V&V role during these two phases is the conduct of T&E itself. 

The arrows in the middle of the “V” are intended to show that each side of the “V” feeds the other.  For instance, the concept and requirements definition phase drives the test cases for OT, while OT development and conduct can provide feedback for future concepts and requirements definition. 

## **1.2 PURPOSE OF THE T EST AND EVALUATION H ANDBOOK** 

The purpose of this T&E Handbook is to support the following objectives: 

1. The test program is complete, well managed, and conducted in a consistent manner by the program test team throughout a system’s, service’s, or capability’s lifecycle, as well as achieving V&V objectives. 

2. T&E processes are developed in accordance with the Acquisition Management System (AMS) Policy and T&E Process Guidelines. 

3. T&E processes address the T&E elements defined in Section 3.5 of the AMS Work Breakdown Structure (WBS). 

<u>Test and Evaluation (AMS WBS, 3.5) – All test, analysis, and evaluation activities</u> to verify and validate that developed or modified products and product components meet contract specifications, satisfy program requirements, and are operationally suitable and effective. 

## **1.3 SCOPE OF THE TEST AND EVALUATION H ANDBOOK** 

This Handbook addresses the T&E preparation, planning, conduct, and reporting activities in support of FAA programs.  It is intended for use by all test personnel.  This Handbook is organized into sections that, first, provide an overview of the T&E preparation and support activities throughout the AMS lifecycle phases, and then defines the specific T&E activities required for each phase.  The T&E Handbook applies to T&E of National Airspace System (NAS) systems, Non-NAS systems, and NAS EnterpriseLevel Capabilities. 

References are made throughout the Handbook to the V&V Repository, which is an internet-based information source hosted on servers under FAA control.  The repository provides users of this Handbook with T&E templates, samples, and tools as standard guidance to accomplish specific V&V practices.  The V&V Repository is located within the WJHTC ANG-E T&E Portal on the Knowledge Services Network (KSN) site. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

1-3 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

## **1.4 ROLES AND RESPONSIBILITIES** 

In conjunction with this Handbook, the WJHTC Test Roles and Responsibilities Guide (TRRG) provides roles and responsibilities for all test personnel, as well as supporting T&E roles.  The TRRG also includes T&E management and test team structures.  The TRRG describes the roles of the DT Test Director and the OT Test Director; however, some more complex test programs designate one person to serve as an overall Test Director for the T&E program. 

The Test Standards Board (TSB) is responsible for updating and managing this Handbook in accordance with the TRRG.  The TRRG defines the organizational roles, responsibilities, TSB processes, and management processes for administering and managing the T&E standards and practices. 

For designated FAA Programs, the TSB provides independent quality T&E oversight and expert guidance with focus on the following outcomes: 

1. Consistent quality T&E products 

2. Sound technical T&E strategies and methods 

3. Defined and documented risks relating to the quality of test services and the program 

The role of the TSB is to develop and institutionalize T&E best practices and support technical integrity of testing. The TSB is a chartered team of Subject Matter Experts (SMEs) that monitors DT and OT test activities and provides recommendations on test strategies, plans, conduct, and reporting to ensure quality T&E products and conformance to T&E processes. 

NOTE:  Refer to the V&V Repository for the Test Roles and Responsibilities Guide. 

## **1.5 FUNDAMENTAL PRACTICES FOR QUALITY TEST AND EVALUATION** 

All T&E programs must implement the following set of fundamental practices to ensure a quality T&E program: 

1. T&E services are involved in all AMS lifecycle management phases to support and plan for the V&V of systems, services, or capabilities, and associated work products defined in the FAA AMS lifecycle Verification and Validation Guidelines. 

2. T&E activities are systematic and progressive in that they build in complexity by first focusing on basic components and then expanding to more complex and integrated testing. 

3. Every T&E program has one or more individuals accountable for the following: 

   - a. Planning and coordination of testing 

   - b. Conduct and coordination of activities 

   - c. Overall quality of testing 

   - d. Accepting and reporting the test results 

4. T&E activities that support acceptance of systems, services, or capabilities or approval of program milestones are well defined and tracked. 

5. T&E programs include the following typical elements: 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

1-4 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

   - a. Test teams that have a thorough understanding of the program requirements, and the knowledge, skills, and training for evaluating the system, service, or capability under test. 

   - b. Documented test plans, procedures, and reports that are comprehensive, clear, concise, objective, written in plain language, peer-reviewed, and have incorporated end user input. 

   - c. Stable, accredited and configuration-managed test capabilities that enable the test cases to meet the documented test objectives without numerous or significant deviations. 

   - d. A complete end-to-end dry run of procedures prior to the formal or final execution of procedures. 

   - e. Accurately documented as-run test procedures and test logs for dry runs and formal test runs. 

   - f. Reports that provide historical test data, results, risks, deficiencies, and recommendations with clear analysis of actual performance and limitations against planned objectives and requirements. 

- g. Integration and testing in an end-state environment. 

- 6. Prior to requirements approval, T&E personnel participate in reviews to ensure all system, service, or capability requirements are testable and validated against the operational mission. 

7. T&E personnel are involved in the procurement-package development and source-selection process to ensure that the resultant contract complies with the test strategy and scope documented in acquisition planning and test strategy documents. 

8. An integrated test plan [e.g., Test and Evaluation Master Plan (TEMP), see Section 5.2] is developed and completed early in the system, service, or capability lifecycle, and is routinely updated to reflect the evolution of the program. 

9. Operational Testing is executed in a test environment (hardware, software, interfaces, etc.) representative of the expected in-service operational conditions. Operational Testing is conducted with a representative team of end users who are expected to interface with or operate the system, service, or capability under test. 

10. Required modifications for defects are verified and validated under conditions equivalent to those that existed when the defects were identified initially. Regression testing is conducted to verify and validate that fixes and modifications correct the defects identified and do not adversely affect other interrelated operations and functionality. 

## **1.6 T AILORING AND OPTIMIZING OF TEST AND EVALUATION PROCESSES** 

T&E programs are unique and have their own set of challenges and differences.  Tailoring is a critical activity that allows controlled changes to processes to meet the specific needs 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

1-5 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

of a project or organization, as long as the ten (10) Fundamental Practices for Quality T&E are enforced. 

### **1.6.1 TAILORING CRITERIA AND PROCESSES** 

To meet the unique needs of a program, the T&E processes in this Handbook may be tailored based on the following: 

1. Test or program complexity and scope 

2. Risks associated with testing or the program 

3. Level of effort required to complete the evaluation 

4. Acquisition strategies and type (e.g., Commercial Off-the-Shelf (COTS)/ Non-Development Item (NDI), Services, Software, Hardware, procurement of systems or equipment, modification of facilities, changes in the physical infrastructure, development of functional interfaces, spiral development implementation, etc.) 

5. Program scope changes and decisions approved by the Joint Resources Council (JRC) 

6. Test strategies in the approved TEMP 

7. Programs under the authority of the Operations Governance Board (OGB) 

The OGB through delegation from the JRC, is the investment decision authority for funded capital investments allocated for Mission Support Operations.  The following phases and decision points constitute the Mission Support Operations-funded process: 

1. Need Analysis 

2. Alternatives Analysis 

3. Solution Development 

4. Development 

5. Operations and Retirement 

The actual path taken by each investment initiative depends on the governance path assigned by the OGB. These governance paths are deviations from the standard AMS lifecycle phases.  Accordingly, capital investments that are under the authority of the OGB meet the requirements for a tailored T&E process. 

T&E processes and process elements that are directly related to critical standards and process objectives and that have the word “must” in the Process Description Document (PDD) should not be tailored without a valid programmatic or technical justification. Processes defined in this Handbook that have been changed or omitted in a program require a clear rationale that relates to a specific unique program element or technical variable (e.g., Integration Testing may not be required on non-complex systems).  The Fundamental T&E Practices defined in Section 1.5 must be enforced and remain intact in any tailored or developed process. 

The tailored program processes are documented and approved in the Process Conformance Checklists as defined in Section 1.7.  The TSB reviews and assesses the tailoring approach and rationale documented in the compliance checklists and determines 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

1-6 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

if the T&E Handbook processes and fundamental practices for quality T&E are maintained.  If the checklists are adequate, they are signed by the TSB.  Any major deviations from test standards must be justified, documented, and approved in a Request for Waiver form.  This request is initiated by the Test Director or T&E First Line Supervisor. The Quality Management Lead identifies the approval authority. 

NOTE:  Refer to the V&V Repository for the Request for Waiver form. 

### **1.6.2 TAILORING GUIDELINES** 

### **1.6.2.1 TYPES OF TAILORING** 

Tailoring of T&E processes can involve the following types of adjustments to processes: 

1. Change in formality 

2. Change in frequency 

3. Change in format 

4. Modifying a process 

5. Eliminating a process 

6. Combining processes 

7. Renaming a process 

8. Changing or consolidating process roles and responsibilities 

9. Changing the order of processes 

### **1.6.2.2 COMMONLY TAILORED PROCESSES** 

Candidate T&E processes in this Handbook that are commonly tailored for a test program consist of, but are not limited to, the following major processes (as defined in Sections 6 and 7): 

1. DT activities 

2. Required DT contractor documents 

3. DT problem reporting 

4. OT Interim Assessments Reports 

5. Logistics for formal OT conduct support 

6. Field Familiarization Support 

### **1.6.3 AGILE ACQUISITION PRINCIPLES IN T&E** 

Acquisition programs may apply Agile principles to optimize programmatic implementation.  A primary principle of agile acquisition is the understanding that work products (i.e., concepts, requirements, specifications, systems) are fluid and continually maturing.  Agile is an iterative approach to implementing new operational capabilities that requires extensive collaboration with a focus and priority on a common mission.  To do this, Program Office; engineering; user, development; and T&E stakeholders work across their disciplines to achieve a common goal.  A developer’s goal should not be just to deliver software.  A tester’s goal should not be just to find problems.  They should work collaboratively to deliver operationally effective and suitable systems.  The goal of agile 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

1-7 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

acquisition principles optimizes existing processes by being both disciplined and fluid. This approach supports continually maturing concepts and requirements with a commitment to V&V all acquisition products.  The approach also looks for iterative and adaptive product development with early and continual V&V of concepts, requirements, developed elements and integrated systems. 

Agile acquisition presents a unique situation regarding tailoring of T&E.  A key feature of agile acquisition testing is that the QA role should be integrated with the engineering; development; and test teams, because quality is not an afterthought.  Embedding the QA function at the start of the program can help with connecting requirements, development testing, and operational testing processes.  Agile acquisition continually verifies and validates the requirements, developed elements, and integrated system to make sure that new features and capabilities work as intended when delivered and deployed. 

Agile principles in test program promote common acquisition goals with a collaborative approach path to meeting milestones.  The TSB can provide a QA support function, acting as SMEs across different teams and responsible for advocating best practices.  The Test Director can be the QA advocate for their respective engineering, development test, and operational test teams, ensuring that their team adheres to the Fundamental Practices for Quality T&E. 

Early and often V&V will reduce the chances of deficiencies on fielded systems.  This approach supports the start of acquisition effort sooner with an acceptable level of immature concepts and requirements.  Structured V&V and T&E will support the iterative maturity levels needed to effectively advance the acquisition to set program goals.  By adopting agile acquisition principles, programs can optimize the acquisition lifecycle and foster cost-effective, knowledge-driven outcomes through effective V&V and T&E activities. 

## **1.7 TEST AND EVALUATION STANDARDS CONFORMANCE PROCESS** 

The T&E standards conformance process is used to monitor conformance to the T&E processes specified in this Handbook and to provide supporting artifacts (conformance checklists) for quality audits.  This process supports the identification of required actions to resolve non-conformance issues.  This process also identifies the specific approach that the Test Director plans to take to address required standards. 

At the onset of T&E test team involvement in a test program, the DT and OT Test Directors must prepare and submit the initial version of the Test Planning Process Conformance Checklist (Appendix B) to the T&E First Line Supervisor and TSB for review and approval. Prior to submission, the DT and OT Test Directors must jointly review the Test Planning Process Conformance Checklist to determine which test process items, if any, need to be tailored.  In a similar fashion, the DT and OT Test Directors must review their respective DT or OT Process Conformance Checklists (Appendices C & D).  As a part of the reviews, the DT and OT Test Directors must document the tailored processes and rationale in the checklists.  The initial version of the DT and OT Process Conformance Checklists must be prepared immediately after the program Initial Investment Decision has been made. 

Each of the three Process Conformance Checklists must be maintained by the appropriate Test Director throughout the respective T&E phases of the program to 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

1-8 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

document the test team’s progress in and conformance to the T&E process.  Any additional tailoring of the approved test process items must be noted in the revised checklist and approved by the T&E First Line Supervisor and the TSB.  Additionally, with one-week prior notification to the T&E First Line Supervisor, the TSB periodically reviews each test program’s Process Conformance Checklists against work products and progress. 

Appendices B through D of this Handbook contain the Test Planning, DT, and OT Process Conformance Checklists, respectively.  These checklists delineate the test process items derived from this Handbook.  The checklists contain a column that allows for documenting tailored test process items.  The checklists also have columns for documenting status, comments, and any associated artifacts. 

NOTE:  Refer to the V&V Repository for current versions of the Test Planning, DT, and OT Process Conformance Checklist templates. 

## **1.8 TEST AND EVALUATION QUALITY M ANAGEMENT SYSTEM PROCESSES** 

The T&E Quality Management System (QMS) processes address practices that are necessary for providing quality T&E services.  These QMS processes support and enable the implementation and execution of the standards and processes defined in this Handbook.  Test personnel are required to follow these processes to be compliant with the policy defined in the FAA order titled “FAA William J. Hughes Technical Center’s Test and Evaluation Policy.”  The QMS processes are documented as PDDs and are located in the V&V Repository.  PDDs describe the processes and workflows for each process area.  Each PDD is identified below. 

1. Project Management – provides a process to manage FAA WJHTC organization T&E projects 

2. Quality Assurance (QA) – provides processes for audit activities in support of the T&E goals, and provides management with insight on the level of adherence to applicable standards 

3. Configuration Management (CM) – provides processes performed by practitioners in support of T&E-related services to ensure that Configuration Items (CIs) are managed and controlled 

4. Document Management and Control (DMC) – provides processes to manage and control T&E and QMS documents 

5. Peer Review – provides a process to improve the quality of T&E work products and to help verify that work products meet requirements 

6. Test Equipment Management – provides the processes to manage the suitability, fitness, identification, and utilization of test equipment 

7. Corrective Action – provides a process to identify and correct the cause(s) of nonconformities and/or potential nonconformities in products and processes within the T&E organization 

8. Customer Feedback – provides a process to describe how the T&E organizations receive and process feedback from customers 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

1-9 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

9. Management Review – provides a process by which the T&E organizations review the QMS to ensure that it is suitable, adequate, and effective in meeting customer requirements 

10. Nonconforming Material – provides a process for identifying, reporting, segregating, controlling and processing nonconforming test equipment, software, and custom test setups, to prevent unauthorized use during formal testing 

11. Special Support Activities (SSAs) – provides a process describing how the T&E organizations handle special projects, studies, or provide subject matter expertise based upon the customer’s needs 

## **1.9 PEER REVIEWS** 

Peer reviews are a critical component of V&V for T&E work products generated throughout a product’s AMS lifecycle.  Peer reviews are an effective verification practice for the early removal of defects from selected work products and are the first mechanism for verification prior to having partially or fully assembled system, service, or capability components. 

Peer reviews involve a methodical examination of work products by the producer's peers as a quality check to identify defects and to recommend changes or improvements.  Peer reviews provide strategic technical, operational, and procedural input for specific work products.  The peer review process must be conducted in accordance with the T&E Peer Review PDD. 

NOTE:  Refer to the V&V Repository for the T&E Peer Review PDD. 

Peer reviews must be completed prior to the final TSB review.  See Appendix E for the recommended sequence of the peer review for specific work products. 

For contract deliverables (e.g., the Contractor Master Test Plan (CMTP), DT Test Plans, DT Procedures, and DT Test Reports), the DT test team should check if the deliverables have undergone internal peer reviews by the prime contractor prior to FAA review and approval (see Section 6.1.3.2). 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

1-10 

**T ES T** **<u>&</u> E V ALU ATIO N H AND BO OK** 

## **2 RELATED DOCUMENTS AND REFERENCES** 

1. _Acquisition Management Policy_ , FAA Acquisition Management System, Washington, DC, updated quarterly 

2. _Agile Acquisition Principles and Practices_ , FAA/MITRE, April 2016, 

3. _Agile Program Management Practices for the Federal Aviation Administration,_ FAA/MITRE, October 2016 

4. _Capability Maturity Model Integration for Development, Version 1.3_ , Carnegie Mellon University CMMI Institute, Pittsburgh, PA, November 2010, 

5. _CMMI for Acquisition,_ Version 1.3, Carnegie Mellon University CMMI Institute, Pittsburgh, PA, November 2010 

6. _FAA AMS Lifecycle Verification and Validation Guidelines,_ FAA Acquisition Management System, Washington, DC, updated quarterly 

7. _FAA Order 1800.66, Configuration Management Policy with Changes 1, 2 and 3_ , March 2012, Washington, DC. 

8. _FAA Order 6032.1E, National Airspace System Modification Program_ , May 2018, Washington, DC. 

9. _FAA Systems Engineering Manual,_ Version 1.1, Air Traffic Organization Operations Planning, Washington, DC 

10. _In-Service Review Checklist_ , FAA Acquisition Management System, Washington, DC, updated quarterly 

11. _ISO 9001:2015, Quality Management Standard_ , International Organization for Standardization (ISO), Geneva, Switzerland 

12. _Order NG 1810.8B, FAA William J. Hughes Technical Center’s Test and Evaluation Policy_ , September 2019, FAA William J. Hughes Technical Center, Atlantic City International Airport, NJ 

13. _T&E Handbook Templates on WJHTC V&V Repository,_ (reference includes all documents that are referenced in “Notes” within the T&E Handbook) 

14. _Test and Evaluation Process Flowchart_ , FAA Acquisition Management System, Washington, DC, updated quarterly 

15. _Test and Evaluation Process Guidelines_ , FAA Acquisition Management System, Washington, DC, updated quarterly 

16. _Air Traffic Organization NextGen & Operations Planning Services Requirements Review Guidance_ Version 1, TSPAT-D3-GDE-004, September 2008 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

2-1 

**T ES T** **<u>&</u> E V ALU ATIO N H AND BO OK** 

## **Intentionally Blank** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

2-2 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

## **3 TEST AND EVALUATION SUPPORT ACROSS THE ACQUISITION MANAGEMENT SYSTEM LIFECYCLE** 

The FAA AMS Lifecycle Phases are summarized below: 

1. Service Analysis and Strategic Planning (SASP) - SASP planning determines what capabilities must be in place now and in the future to meet agency goals and the service needs of customers. Results are captured in the “as is” and “to be” states of the enterprise architecture, as well as the roadmaps for moving from the current to the future state. 

2. Concept and Requirements Definition (CRD) - CRD translates priority operational needs into preliminary requirements and a solution concept of operations for the capability needed to improve service delivery.  It quantifies the service shortfall in sufficient detail for the definition of realistic preliminary requirements and the estimation of potential costs and benefits.  Finally, CRD identifies the most promising alternative solutions able to satisfy the service need. 

3. Investment Analysis (IA) – IA begins after the completion of CRD with the Investment Analysis Readiness Decision (IARD).  IA is the process used to support capital investment decisions and consists of the following two components: 

   - a. Initial Investment Analysis (IIA) – IIA evaluates alternative solutions to mission needs and provides realistic options to the JRC to support the Initial Investment Decision (IID). 

   - b. Final Investment Analysis (FIA) – FIA develops detailed plans, a cost/schedule/performance baseline, and finalizes program requirements for the solution in support of the Final Investment Decision (FID). 

4. Solution Implementation (SI) – SI begins at the FID when the JRC gives approval to the service organization or Program Office to proceed with implementation of the selected investment opportunity.  The overarching goal of SI is to obtain and deploy a fully-supported operational capability that satisfies requirements, realizes benefits in the business case, is accepted by users, and is compatible with other products and services in the field. 

5. In-Service Management (ISM) – ISM begins at the In-Service Decision (ISD) when a new system, service, or capability is commissioned for operational use. The primary goal of ISM is to ensure that FAA systems, services, and facilities are operated, maintained, secured, and sustained to provide the level of service required by users and customers.  In addition, ISM provides periodic monitoring, evaluation, and improvements for fielded systems, services, and facilities. 

Figure 3-1 illustrates the typical T&E approach leading to the ISD.  The diagram depicts all major AMS lifecycle phases starting with Research for Service Analysis through SASP, CRD, IA, SI, and ending with ISM.  The diagram also indicates the key decisions, milestones, major test efforts, technical reviews, and the major T&E work products and when they would be initiated relative to the AMS lifecycle phase.  This figure depicts the 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

3-1 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

typical FAA investment program lifecycle, and the implementation of specific activities (i.e., test efforts or T&E work products) or events (i.e., key decisions, milestones, or technical reviews). 

NOTE:  Each program is unique and may deviate from the typical lifecycle approach (See tailoring discussion in Section 1.6). 

Sections 4 through 8 of this Handbook identify and define the specific T&E support required for each of the AMS program lifecycle phases.  The AMS lifecycle phases shown in Figure 3-1 are to be followed for any investment which has been identified by FAA as requiring executive decision. 

NAS Enterprise Level Capability programs need to be coordinated across multiple systems, each of which has their own requirements.  Enterprise Level Capability T&E teams need to be put in place to do the following: 

1. Identify the hierarchy of requirements 

2. Allocate the requirements to appropriate organizations 

3. Establish roles, responsibilities, and procedures for coordinating T&E activities, including problem resolution 

Figure 3-2 illustrates test phases for System/Solution-level T&E and NAS EnterpriseLevel Capability T&E.  The arrows show which set of requirements undergoes T&E in each test phase. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

3-2 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



**Figure 3-1.  Typical Test and Evaluation Approach throughout the Acquisition Management System Lifecycle** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

3-3 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



**Figure 3-2.  Test and Evaluation Phases and Requirements** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

3-4 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

## **4 TEST AND EVALUATION SUPPORT TO SERVICE ANALYSIS AND STRATEGIC PLANNING AND CONCEPT AND REQUIREMENTS DEFINITION** 

T&E support to SASP and CRD generally consists of early evaluations performed in support of concept feasibility determinations and analysis of alternative solutions.  Early evaluations may be used throughout the program planning process (i.e., during both SASP, CRD and IA) to minimize program risks.  Early evaluations include the following: 

1. Prototype tests 

2. User demonstrations 

3. Studies 

4. Modeling 

5. Simulations 

6. Operational Capability Demonstrations (OCDs) 

7. Operational Capability Tests (OCTs) 

Prototype tests, user demonstrations, studies, modeling, and simulations are used to support system engineering processes in developing requirements, evaluating operational concepts (including human factors), and selecting technologies.  OCDs and OCTs provide functional and performance information to investment decision makers to support selection from candidate solutions. 

These evaluations may be conducted on functionally equivalent prototypes or on early development systems and may be used to provide field personnel with early exposure to new products or systems under development.  The focus is to identify system, service, or capability flaws or enhancements before committing to the final investment decision to acquire production products or services (i.e., when it is least costly to implement corrective measures or improvements).  Information from early evaluations is used to develop work products for the following: 

1. Evaluating operational concepts 

2. Supporting alternative analysis decisions 

3. Developing requirements for the preliminary Program Requirements Document (pPRD) 

In keeping with best practices, early evaluations should adhere to the same fundamental T&E practices described in Section 1.5.  Early evaluations may result in changes to system, service, or capability specifications, COTS hardware or software, operational requirements, or vendor selections.  These evaluations can also provide information for the focus of future test activities.  The test processes from the DT and OT sections of this Handbook (Sections 6 and 7) should be used during these evaluations to ensure that an effective and affordable T&E effort is systematically implemented and properly documented to enable the FAA to make informed decisions. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

4-1 

**Intentionally Blank** 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

## **5 TEST AND EVALUATION SUPPORT TO INVESTMENT ANALYSIS** 

T&E support of IA consists of the initial development of T&E program planning as documented in the Program Requirements Document (PRD), the TEMP, the Implementation Strategy and Planning Document (ISPD), the System Specification, and the Screening Information Request (SIR).  Additionally, T&E support during this phase may include the continuation (or the initiation) of early evaluations begun during SASP and CRD (see Section 4). 

The set of primary acquisition planning and control documents generated during IA that are supported by T&E are as follows: 

1. Program Requirements Document – defines the operational framework and performance baseline for an investment program.  It is the basis for evaluating the readiness of resultant systems, services, or capabilities to become operational. 

2. Test and Evaluation Master Plan – is the primary test management document for the investment program throughout its lifecycle from IA through ISM.  It describes the baseline test strategy and the scope of a test program. 

3. Implementation Strategy and Planning Document – conveys critical, relevant, and meaningful planning information to the JRC or designated Investment Decision Authority as a basis for investment decision-making.  The ISPD integrates all aspects of planning for solution implementation and in-service management of a proposed investment program. 

4. System Specification – describes the physical, functional, and performance requirements of a system, service, or capability to be obtained from a contractor and contains verifiable criteria for determining whether the requirements are met. 

5. Screening Information Request – defines the specific efforts the contractor will provide.  The FAA procures systems, services, or capabilities by using agreements defined in contracts.  Before it can select a contractor to provide the system, service, or capability, the FAA issues a SIR to define the specific efforts to be provided. 

The planning and support described in this section details the T&E program planning based on the framework established in the program acquisition planning and control documents.  Specifically, the T&E support to the development of the PRD, the TEMP, the ISPD, the System Specification, the SIR and Proposal Evaluation is described in Sections 5.1 through 5.6.  Appendix E identifies the major T&E work products along with their associated review, endorsement, and/or approval cycles. 

## **5.1 PROGRAM REQUIREMENTS DOCUMENT SUPPORT** 

The Program Management Office (PMO) develops the PRD in accordance with the FAA AMS Policy.  The preliminary Program Requirements Document (pPRD) is established during the CRD phase in preparation for the IARD.  Program requirements are refined in the initial Program Requirements Document (iPRD) prior to the IID and are further refined 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

5-1 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

in the final Program Requirements Document (fPRD) prior to the FID.  The T&E section of the PRD is developed during the iPRD in support of the IID. 

T&E support for the development of the PRD includes the following: 

1. Participating in system, service, or capability engineering and implementation reviews 

2. Ensuring that all new or modified requirements for functions or services are defined and address the operational mission 

3. Ensuring that all interfaces required for the NAS operational missions are defined 

4. Reviewing and commenting on requirements for testability (Requirements must be precisely defined and leave no room for subjective interpretation. Parameters and thresholds must be measurable.  Functional performance requirements must be verifiable and expressed in unambiguous terms.) 

5. Verifying that Critical Operational Issues (COIs) are completely described, are operational in nature, represent observable events, and are testable 

6. Verifying that program requirements essential to meeting the mission are identified as Critical Performance Requirements (CPRs) 

7. Structuring the test program to address all target system or subsystem components and interfaces by: 

   - a. Defining potential test strategies and seeking feedback from engineering and implementation teams 

   - b. Providing test strategy briefings to the PMO as required 

   - c. Writing the T&E section of the PRD to require Operational and Development testing 

The T&E section of the PRD must be reviewed by the TSB, PMO, and the T&E Senior Manager, but no formal approvals or endorsements are required.  Refer to Appendix E, Figure E-1, for the complete T&E section of the PRD review, endorsement, and/or approval cycle. 

NOTE:  Refer to the V&V Repository for a sample of the T&E section of the PRD, and for Requirements Review Guidance, TSPAT-D3-GDE-004. 

## **5.2 TEST AND EVALUATION M ASTER PLAN DEVELOPMENT** 

The TEMP is the primary test management document for the investment program throughout its lifecycle from IA through ISM.  It describes the baseline test strategy and the scope of a test program.  The TEMP delineates all activities that must be performed to achieve the goals of V&V.  It also documents the T&E methodologies used to assess safety hazard controls and security risks.  All programs are required to submit a TEMP unless a waiver is approved by the Director of Test Services (or equivalent).  Figure 5-1 shows a hierarchy of test categories and the scope of the TEMP relative to other plans and procedure documents. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

5-2 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



**Figure 5-1.  Test Category Hierarchy and Documentation** 

The DT and OT Test Directors are responsible for producing and managing the TEMP through the Integrated Test Team (ITT).  The ITT is composed of PMO representatives, stakeholders, DT and OT personnel, ISM test personnel, system engineers, Subject Matter Experts (SMEs), and is jointly chaired by the DT and OT Test Directors.  (For additional information on the ITT, refer to the TRRG.)  The program follows the approved TEMP to budget for T&E resources and scheduled activities.  It is imperative that all T&E stakeholders participate early in the program and throughout the program lifecycle to ensure that a comprehensive and effective test program is developed and implemented. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

5-3 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

The preliminary TEMP (pTEMP) defines the investment program test strategy and scope. It is developed upon the concepts and functions documented in the preliminary requirements document prior to IID and is not expected to contain the complete level of detail required to fully implement the T&E program. 

The initial TEMP (iTEMP) for each T&E program must be provided prior to the FID.  While the iTEMP is not expected to contain the complete level of detail required to fully implement the T&E program, it must contain estimates of the testing scope that are sufficient to address ISPD requirements and development of T&E requirements for the SIR. 

The final TEMP (fTEMP) is completed after design reviews, such as Critical Design Review (CDR), and prior to delivery of the CMTP.  It defines the complete investment program test strategy and scope for both the government and contractor, if applicable, and is generally revised at major program milestones (see Section 5.2.2). 

The TEMP is a living document that is updated as the program progresses, and more detailed supporting information becomes available.  Unaddressed or incomplete areas within early TEMP versions which require refinement must be identified as “To Be Determined” (TBD) and must be included in the final or revised final versions as additional information becomes available. 

The pTEMP, the iTEMP, the fTEMP, and all revisions to the fTEMP impacting test strategy or scope require TSB endorsement and the approval signatures of the Program Manager and the Director of Test Service Organization (or equivalent).  Minor changes to the fTEMP that do not impact test strategy or scope (e.g., minor schedule changes, editorial corrections, etc.) are considered working drafts only and do not require these approval signatures but are still subject to controls as detailed in the DMC PDD.  The T&E strategies and methods described in the TEMP is briefed to the Program Manager to obtain input and concurrence with the general T&E approach.  The briefing occurs prior to submitting the iTEMP and fTEMP for the Program Manager’s review and approval. 

Refer to Appendix E, Figure E-3, for the complete TEMP review, endorsement, and/or approval cycle. 

NOTE:  Refer to the V&V Repository for the TEMP templates, TEMP samples, and the DMC PDD. 

### **5.2.1 TEST AND EVALUATION MASTER PLAN OBJECTIVES** 

The TEMP must accomplish the following objectives to ensure a comprehensive test program: 

1. Provide structure for managing the T&E effort 

2. Define a test plan baseline that addresses all required test activities 

3. Document the ITT’s consensus on the scope of testing that is required to evaluate the system, service, or capability in a thorough and efficient manner 

4. Define test strategies and evaluation methods for the system(s), service(s), or capability(ies) under test 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

5-4 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

5. Identify program requirements to be verified and validated, also noting any that will not be evaluated 

6. Identify the CPRs from the PRD and associated criteria 

7. Document traceability of program requirements and COIs to test activities in a Verification Requirements Traceability Matrix (VRTM) 

8. Decompose COIs into Measures of Effectiveness (MOEs), Measures of Suitability (MOSs), and Measures of Performance (MOPs) in the VRTM 

9. Define a logical schedule of T&E activities 

10. Specify equipment and resource requirements to support testing 

11. Specify T&E roles and responsibilities 

12. Define an approach for specialized evaluation areas (e.g., Human Factors (HF), Security, and Safety) 

13. Identify test tools and capabilities that require development and accreditation 

14. Fully define test limitations and their respective impacts on evaluation elements 

15. Define discrepancy/problem reporting methods 

16. Define training requirements and plans 

17. Define the T&E plan for support of major program decisions 

18. Define the plan for making a determination of operational readiness 

19. Define how test results are documented (e.g., Interim Assessment Report(s), DT reports, OT Caucus Summary Report, and other OT reports) 

### **5.2.2 TEST MANAGEMENT USING THE TEST AND EVALUATION MASTER PLAN** 

The information necessary to develop and maintain a TEMP and the process areas that are managed through the use of a TEMP are depicted in Figure 5-2.  The following sections expand upon the relationships depicted in the figure. 

The acquisition planning and control documents (see Section 5) and each program’s FAA procurement specification are the basis of the programmatic test objectives and constraints upon which the TEMP must be developed.  The test strategies defined in the TEMP must support those contained in the ISPD.  Development of the TEMP may start prior to completing the test section of the ISPD.  The TEMP must contain more refined details that support the higher-level descriptions contained in the ISPD. 

The TEMP contains strategies to be used to plan the conduct of any OCDs and OCTs. The DT section of the TEMP defines the test strategies and scope to be allocated to DT. Since the TEMP contains the integrated test approach for evaluating the system, service, or capability, it must define the details of test and support requirements to be obtained from the procurement contractor in support of both DT and OT.  These requirements are to be included in the SIR.  The TEMP is updated, as required, based on the results and findings of the OCDs, OCTs, and DT. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

5-5 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



**Figure 5-2.  Test and Evaluation Master Plan Relational Diagram** 

The TEMP must define the scope of the OT effort.  Subsequent OT plans must reflect the test strategies and scope defined in the TEMP.  The basis of the strategies is defined in the TEMP, including which DT activities support OT validation of requirements.  The simulation, modeling, and/or test tools required to execute the OT strategy must be defined so that their development and accreditation can be effectively managed. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

5-6 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

As the system development progresses, the strategies defined in the TEMP must be reassessed.  Changes to the TEMP are required when previously developed test strategies or scope are no longer valid, or if new system performance risks are identified. The TEMP must be reassessed and updated as necessary, for example: 

1. At major milestones (e.g., Contract Award, CDR, CMTP delivery/update, and OT Test Plan delivery/update) 

2. When the program baseline has been significantly modified 

3. When the ISPD has been significantly modified 

4. When the program is significantly changed or restructured 

5. When scope or test strategies are no longer valid 

### **5.2.3 TEST DESIGN PROCESS** 

The ITT develops the test design documented in the TEMP by researching information from various sources including Concept of Operations (ConOps), program requirements, associated architectures, specifications, COTS/NDI documentation, functional descriptions, and design documentation. 

The following sections describe the test design process as depicted in Figure 5-3.  Early steps of this process may not be fully applicable to a pTEMP. 

### **5.2.3.1 IDENTIFICATION AND ASSESSMENT OF REQUIREMENTS** 

The initial step in developing a test design is to identify a complete set of requirements within the scope of the test effort.  Operational requirements and system requirements are defined in the program’s PRD and FAA system specification(s).  Each requirement must be thoroughly analyzed to gain a comprehensive understanding of the system, service, or capability to be tested. 

To perform the system requirements assessment, the ITT considers the following aspects of the system, service, or capability to be tested: 

1. Mission 

2. System, service, or capability requirements 

3. Available test capabilities and limitations 

4. Application and operational concepts 

5. Major operational changes or impacts on the NAS that may be introduced by the new program or service 

6. Acquisition strategies and issues that may impact the T&E process 

7. Expected scope and size of software and hardware development efforts 

8. Safety and security risks 

9. Operational environments, configurations, and conditions in which the system is intended to be placed 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

5-7 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



**Figure 5-3.  Generic Test and Evaluation Master Plan Test Design Process** 

### **5.2.3.2 DECOMPOSITION OF CRITICAL OPERATIONAL ISSUES** 

COIs are defined in an FAA procurement program’s PRD.  A COI is a critical element or operational objective that must be examined during testing to determine the system’s overall capability to support mission accomplishment.  COIs are stated in the form of a question at a high level and usually cannot be answered directly from a single test or measurement.  Therefore, each COI must be broken down into quantifiable measures that, when combined, fully support resolution of the critical issue. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

5-8 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

COIs are decomposed in the TEMP by: 

1. Breaking down COIs into MOEs and MOSs (MOEs and MOSs are detailed subquestions of the COI which must be answered to fully determine whether a COI has been satisfied.) 

2. Further breaking down MOEs and MOSs into MOPs (MOPs are measurable, quantitative/qualitative values that characterize and support the evaluation of the COIs, MOEs and MOSs.  Decomposition must be considered preliminary for the pTEMP and the iTEMP.) 

3. Mapping MOEs and MOSs to PRD requirements in the VRTM (If a conflict is discovered between the PRD and any MOEs, MOSs, or MOPs the conflict must be resolved.) 

Figure 5-4 illustrates the decomposition of COIs down to test cases, and their relationship to operational readiness. 



**Figure 5-4.  Decomposition of Critical Operation Issues to Test Cases** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

5-9 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

MOEs evaluate the degree to which a system accomplishes its mission when used by representative personnel in the expected operational environment.  MOEs include the following areas of evaluation: 

1. Accuracy 

2. Coverage 

3. Probability of detection 

4. Tracker performance 

5. System capacity 

6. Data timeliness 

MOSs address system characteristics that determine whether it is suitable for use in the NAS.  MOSs include the following areas of evaluation: 

1. Reliability, Maintainability, and Availability (RMA) 

2. Compatibility 

3. Transportability 

4. Interoperability 

5. Safety 

6. Human factors 

7. Logistics 

8. Supportability 

9. Training requirements 

10. Site adaptability 

11. Fault tolerance 

12. Security 

NOTE:  Refer to the V&V Repository for the COI Decomposition Guide and a COI Decomposition sample. 

### **5.2.3.3 CRITICAL PERFORMANCE REQUIREMENTS EVALUATION APPROACH** 

CPRs are program requirements identified in the PRD as essential to the successful performance of the system, service, or capability in meeting the program’s mission needs. Special emphasis is placed upon the evaluation of CPRs to ensure the timely assessment of system, service, or capability capabilities and to promote program success. 

Therefore, CPRs are tracked and their status is reported throughout the test program to provide visibility to management in support of making prudent decisions.  The evaluation approach should determine the strategy for testing the CPR and the required milestones for assessing CPR performance. 

If CPRs have not been identified in the PRD or the Acquisition Program Baseline (APB), then it is recommended that the ITT select a PMO-approved set of CPRs from the PRD, in accordance with the PRD template guidance.  Additional CPRs may also be identified from other program work products.  The full set of CPRs is documented in the TEMP. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

5-10 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **5.2.3.4 DEFINING TEST ACTIVITIES** 

Requirements are allocated to a set of DT and OT activities to support a structured evaluation of the system.  In addition to the COIs and CPRs identified above, test design should consider the following factors affecting test: 

1. NAS integration requirements 

2. System interface requirements testing 

3. Degraded mode operations 

4. Stress and NAS loading 

5. Failure recovery 

6. Air Traffic (AT) and Technical Operations (Tech Ops) evaluations 

7. System, service, or capability certification requirements 

8. Transition and switchover/fallback 

9. Site adaptation 

10. HF evaluations 

11. Security evaluations 

12. Supportability evaluations 

13. Safety requirements and potential new safety hazards 

14. Monitoring and control 

15. Integrated operations 

16. Stability 

17. Hardware requirements 

18. Software requirements 

19. Functional performance 

20. RMA 

21. Risk reduction 

For DT, list of basic test activities (as defined in Section 6.1.1) are identified as Software Testing, Hardware Testing, Factory Acceptance Testing (FAT), Functional Qualification Testing (FQT), Installation and Integration Testing, System Testing, Production Acceptance Testing (PAT), Site Acceptance Testing (SAT) and Regression Testing. 

For OT, basic test activities (as defined in Section 7.1) are identified as NAS Integration Testing and Operational Effectiveness and Suitability Testing.  For the latter, this test activity may be further subdivided into the specific test activities of RMA, Supportability, Degraded Operations, Stress and NAS Loading, HF, Safety, Security, Site Adaptation, Transition, Certification, Training and OT Regression Testing. 

As part of CMTP, DT Test Plan, and OT Test Plan development, test activities are broken down into individually executable test cases in which functionally related requirements are tested.  For larger or more complex test programs, individual test cases within a test activity may be organized into test case groups for execution and/or reporting purposes. Ultimately, conditions for each test case should define the required loads, configurations, 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

5-11 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

adaptations, and environments.  Allocation of test activities and their individual test cases should support the test strategies defined in the T&E section of the ISPD. 

### **5.2.3.5 FORMULATING THE TEST AND EVALUATION MASTER PLAN VERIFICATION REQUIREMENTS TRACEABILITY MATRIX** 

The TEMP VRTM provides a structured approach that ensures planned testing is comprehensive and complete.  It maps all COIs/MOEs/MOSs/MOPs as well as the program requirements into T&E phases (DT or OT) and associated test activities (see Sections 6.1.1 and 7.1 for descriptions of the DT and OT activities).  Additionally, each MOP and program requirement contained in the TEMP VRTM is assigned one or more of the following test verification method(s): 

1. Inspection:  Verification that is accomplished by a visual examination of the item, reviewing descriptive documentation, and comparing the appropriate characteristics with predetermined standards to determine conformance to requirements without the use of laboratory equipment or procedures. Examples of verification by inspection are: 

   - a. Visual analysis of the item under test, such as displays, cables, and processors 

   - b. Reviewing descriptive documentation such as Contract Data Requirements List (CDRL) items, vendor data, and engineering drawings 

   - c. Comparing the appropriate characteristics with a predetermined or reference standard such as FAA and industry standards 

2. Analysis:  Verification that is accomplished through use of one or more of the following analysis techniques to prove that an item meets specified requirements: 

   - a. Mathematical representation such as models, algorithms, and equations 

   - b. Charts 

   - c. Graphs 

   - d. Circuit diagrams 

   - e. Data reduction/recording 

   - f. Representative data (may include data collected from previous or other equipment and system verifications) 

3. Demonstration:  Verification that is accomplished by operation, adjustment, or reconfiguration of items performing their designed functions under specific scenarios.  The items may be instrumented, and quantitative and qualitative limits of performance monitored, but only observational data rather than actual performance data is required to be recorded for verification.  Demonstration is often used to verify compliance with requirements in servicing, reliability, maintainability, transportability, and human factors engineering. 

NOTE **:** Demonstration does not require any actions beyond those identified in the Test Steps section of the associated test procedures. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

5-12 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

4. Test:  Verification that is accomplished, with or without instrumentation, through systematic exercising of the application item under appropriate conditions with the collection, analysis, and evaluation of quantitative data. 

NOTE **:** Acceptability of the item is determined by comparison of the data with preestablished quantitative criteria, requirements, and occurrences. 

Development of the VRTM is an iterative process.  During early TEMP development, the TEMP VRTM is generated with a mapping of COIs/MOEs/MOSs/MOPs and program requirements down to the test activity level for OT and to the DT phase, as appropriate. Detail below the COI level must be considered preliminary and may need to be revised and expanded as OT planning progresses.  As the program progresses, additional information such as that included in the ISPD, the CMTP, and the System Specification provide further details that must be incorporated into the VRTM. 

For DT, the contractor uses the FAA System Specification to develop their contractor specification(s) that decompose the DT requirements.  The CMTP is then developed containing a DT VRTM which maps the DT requirements to the DT activities. Subsequently, the contractor refines the DT VRTM with test case information during DT Test Plan development (see Sections 6.2.2, 6.2.3, and 6.2.5).  The TEMP VRTM is updated with the DT activity and test case information from the DT VRTM. 

For OT, the TEMP VRTM provides the basis for developing the OT VRTM.  During OT Test Plan development, the VRTM is further refined to include COI/MOE/MOS/MOP and program requirement mapping to the individual OT cases (see Sections 7.5.2 and 7.5.3). NOTE **:** Refer to the V&V Repository for the VRTM Content and Guidance Document. 

### **5.2.3.6 IDENTIFYING TEST CAPABILITY REQUIREMENTS** 

Test tools and environment requirements are to be identified in a consolidated list for traceability, including associated “need by” dates.  Particular focus is placed on items with long lead times or high costs.  Typical examples include the preparation, procurement, or development of laboratories and testbeds, models and simulations, test tools, telecommunications services, and NAS interfaces that require significant coordination. 

When assessing the need for test tools and environments, the following factors are considered: 

1. Measures of Performance:  Reviewing MOPs provides insight into the resources that may be required to collect and analyze data.  Instrumentation, databases, data extraction tools, questionnaires, and analysis tools are examples of resources that may be required. 

2. Test conditions:  Reviewing the required test conditions (e.g., loads, configurations, adaptations, and environments) provides insight into the required resources. 

3. Test methodology:  How a set of test activities is executed also contributes to the rationale or basis for resource requirements.  Reviewing the test methodologies provides insight into what might be needed to execute the test activities (e.g., field testing may add costs, modeling and simulation may incur both increased costs and potentially long lead times for development, etc.). 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

5-13 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

4. Test scenarios:  Test scenarios are simulations or scripted input developed to exercise combinations of operational factors that influence system performance.  Reviewing all factors that have been identified may provide insight into additional assets that may be required to approximate operationally realistic Air Traffic Control (ATC) situations and capture end-to-end situational flow. 

### **5.2.3.7 DEFINING A TEST SCHEDULE** 

The test program schedule is derived from and based on the test design and associated program constraints.    The test team can draw on historical data from test programs of equivalent complexity and risk to develop the test design for a program.  This data may be accessed from T&E work product archival data from other test programs.  Historical data may also be used to assess T&E tasks to establish durations estimates.  The initial test schedule milestones and completion dates are developed by linking them to key program milestones and acquisition decision points.  The test schedule is further refined by defining T&E tasks for each test milestone and completion date and can be impacted by program constraints, which should be identified using the Risk Management process defined in the FAA Systems Engineering Manual (SEM). Finally, the test schedule dependencies are established by linking all associated T&E tasks, as well as other program milestones and completion dates that relate to the T&E tasks.  This final schedule becomes part of the test program baseline. 

All planning and management of T&E program schedules should be done in accordance with the T&E Project Management PDD. 

NOTE **:** Refer to the V&V Repository for the Project Management PDD. 

### **5.2.3.8 ASSESSING UPDATES AND ACQUISITION PROGRAM BASELINE CHANGES** 

As additional information becomes available or changes to the APB are made, the test design must be reassessed to ensure that the assumptions made in the test design are still valid.  If changes in assumptions impact the ability of the test design to verify and validate the system under test, changes must be made to the test design. 

### **5.2.3.9 DOCUMENTING THE TEST DESIGN IN THE TEST AND EVALUATION MASTER PLAN** 

The TEMP documents the test design from a set of defined process steps as depicted in Figure 5-3.  As described in the previous sections, the test design is based on the following factors:  the complete set of system requirements; the decomposition of COIs that must be examined during testing; the set of CPRs that must be evaluated, tracked and assessed; a set of DT and OT activities that support a structured evaluation of the system; a structured VRTM to ensure that testing is comprehensive and complete; a set of necessary test capability requirements; the test schedule, cost and resources; and an assessment of updates and APB changes. 

When an investment program’s test design is completed and documented, its supporting factors form the basis for the TEMP and any updates. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

5-14 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **5.2.3.10 INTERIM ASSESSMENT REPORT PLANNING** 

The Interim Assessment Report (IAR) can play an important role in the early identification of program issues, risks and change opportunities.  It is a recommended method to provide management with the status of critical requirements and operational issues during a program’s design, development, and test phases.  This assessment can support programmatic decisions to help ensure that the program meets its cost, schedule or performance objectives prior to going into operation.  Test program IAR planning activities include describing how and when IARs will be provided, and to whom the IARs will be delivered.  Reporting milestones and methods for IARs are typically based on cost, schedule and complexity of the program.  The selection of milestones for when IARs are planned to be delivered should consider when critical decision points in the program can be best supported by the report and the availability of meaningful data.  Recommended reporting milestones include major reviews (e.g., preliminary, critical, software, system and program design reviews), software development, start of formal DT, completion of DT, and start of OT.  The OT Test Director documents strategic plans for IARs in the TEMP and is the responsible individual for the deliverable.  For more on the IAR content, see Section 7.7.1. 

## **5.3 IMPLEMENTATION S TRATEGY AND PLANNING DOCUMENT SUPPORT** 

The ISPD defines the overall strategy for an FAA program.  The T&E section of the ISPD defines the program’s T&E strategy.  The ISPD T&E strategy identifies high-level aspects of testing, including resources, roles and responsibilities, site selection, scheduling, training, planning, and reporting. 

T&E support for the final ISPD includes supporting the development of the T&E section. System complexity, contracting approach, project schedule, and impact on the NAS are considered when developing the test program strategies.  Both contractor and FAA test activities are addressed with an overall structure and outline of planned testing.  Any approach to streamline testing is identified with an explanation of how the test strategy mitigates program and operational risks. 

The T&E section of the final ISPD is developed by the DT and OT Test Directors in conjunction with the initial TEMP.  The T&E section of the ISPD should include the plan for delivery of the fTEMP relative to other program milestones and should be consistent with the strategies detailed in the iTEMP.  The development of the T&E section of the ISPD is supported by the ITT. 

The T&E section of the final ISPD requires endorsements from the TSB, T&E First-Line Supervisor, and the responsible T&E Senior Manager.  On programs designated for Independent Operational Assessment (IOA), the Vice President, Safety and Technical Training, approves the ISPD Section 9.2. 

Refer to Appendix E, Figure E-2, for the complete T&E section of the ISPD review, endorsement, and/or approval cycle. 

NOTE:  Refer to the V&V Repository for a sample of the T&E section of the ISPD. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

5-15 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

## **5.4 FAA S YSTEM SPECIFICATION SUPPORT** 

The DT and OT Test Directors and designated test team members participate in developing the FAA System Specification, sometimes referred to as Product Description. The specification describes the physical, functional, or performance requirements of a system, service, or capability to be obtained from a contractor and contains verifiable criteria for determining whether or not the requirements are met.  The following activities are performed in reviewing and developing requirements in the FAA System Specification: 

   1. Review proposed software, hardware, and system designs as defined by system engineering teams 

   2. Conduct prototype evaluations (as required) to support requirements definition 

   3. Attend system, service, or capability engineering and implementation reviews 

   4. Ensure that requirements are well defined, testable, and address operational requirements 

   5. Ensure consistency and traceability with operational requirements in the PRD 

   6. Ensure that all critical interfaces are defined 

   7. Review and comment on requirements for testability: 

      - a. Requirements related to COTS/NDI products should only describe functional system level requirements, since subsystem level parameters are already documented in the vendor COTS/NDI specifications. 

      - b. Requirements must be clearly defined and leave no room for subjective interpretation.  Parameters and thresholds must be measurable. Functional performance requirements must be written in unambiguous terms.  Standards for well-written requirements are provided in the Requirements Review Guidance, TSPAT-D3-GDE-004, and in the FAA SEM. 

- NOTE:  Refer to the V&V Repository for the Requirements Review Guidance. 

   8. Assess the system, service, or capability components, system design, and system implementation approach for developing potential test strategies 

   9. Define potential test strategies and seek feedback from implementation and engineering teams and provide test specification briefings to the PMO, as required, to attain buy-in 

   10. Develop test program structure to address target system components, subsystems, and critical interfaces 

   11. Write the verification section of the FAA System Specification to define essential verification areas and methods and strategies that are required to verify the documented requirements 

   12. Ensure that operational considerations have been incorporated in the selection of verification methods (inspection, analysis, demonstration, and test) 

- NOTE:  Refer to the V&V Repository for an FAA System Specification sample. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

5-16 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

The DT Test Director must ensure that all T&E-related input to the FAA System Specification has been peer reviewed prior to submission (see Section 1.9).  Refer to Appendix E, Figure E-4, for the T&E Input Review Cycle for an FAA System Specification. 

## **5.5 SCREENING INFORMATION REQUEST SUPPORT** 

The FAA procures products, systems or services from contractors using agreements defined in contracts.  Before it can select a contractor to provide the system, service, or capability, the FAA issues a SIR to define the specific efforts to be provided by the contractor.  The test strategy from the TEMP is the basis for determining what test and evaluation items belong in the SIR.  The DT and OT Test Directors must ensure that this test strategy is properly reflected in the SIR as described in the following sections. Additionally, the DT and OT Test Directors must ensure that all T&E related input to the SIR has been peer-reviewed prior to submission (see Section 1.9). 

### **5.5.1 SECTION L OF THE SIR: INSTRUCTIONS, CONDITIONS, AND NOTICES TO OFFERORS** 

Section L of the SIR contains a description of the technical requirements that the offeror must address within the proposal that they submit in response to the SIR.  Offeror proposal requirements that may be addressed in Section L of the SIR with respect to testing include: 

1. Relevant experience of the offeror in testing similar systems 

2. DT cost and schedule information 

3. Test tools to be used 

4. Test environment(s) proposed for formal tests 

5. Integration and test management approach 

6. Proposed test approaches and strategy to include expected conditions for CPR evaluation 

7. Specific operational conditions and loading that supports early evaluation of operational capabilities during DT 

8. Discrepancy reporting and corrective action processing approach 

9. Cost information for OT support 

10. Test CM methods and practices to be used 

11. OCD/OCT evaluation criteria and offeror submittal instructions (if required) 

12. Risk management approach 

### **5.5.2 SECTION C OF THE SCREENING INFORMATION REQUEST: DESCRIPTION OF WORK REQUIREMENTS** 

Section C of the SIR contains the description of the work to be performed under the contract.  This section typically includes one of the following Government developed documents:  Statement of Work (SOW), Performance Work Statement (PWS), or Statement of Objectives (SOO).  Tasks defined in these documents that require the delivery of documentation are defined in the CDRL and the corresponding Data Item Descriptions (DIDs).  The subsequent sections define each document purpose followed 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

5-17 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

by a list of T&E areas that should be considered when drafting the description of work requirements. 

### **5.5.2.1 STATEMENT OF WORK /PERFORMANCE WORK STATEMENT** 

The SOW defines the specific tasks the contractor must perform.  The SOW specifies in clear, understandable terms the work to be done in developing or producing the goods to be delivered or services to be performed by the contractor.  The SOW forms the basis for successful performance by the contractor and effective administration of the contract by the FAA.  A well-written SOW serves as the standard for determining whether the contractor meets the stated requirements. 

A PWS is a statement of work for Performance-Based Service Acquisitions (PBSAs) that describe the required results in clear, specific and objective terms with measurable outcomes.  The key to a PBSA is that all aspects of the acquisition are structured around the expected outcome.  This shifts the performance risk away from the FAA and often results in savings by allowing the contractor to provide innovative solutions for the stated need.  A PWS is typical of a contract that engages the time and effort of a contractor whose primary purpose is to perform an identifiable task rather than to furnish an end item. 

The SOW/PWS should accomplish the following T&E goals that are common across most FAA investment programs: 

1. Describe the T&E events and activities to be accomplished by the contractor that reflect the program T&E strategy described in the TEMP, the ISPD, and the Integrated Master Schedule (IMS) 

2. Specify the T&E elements critical for program success (e.g., test program management, integrated testing, test capability accreditation, discrepancy reporting, etc.) 

3. Ensure that the FAA has access to contractor data, test activities, and results 

4. FAA review and approval of contractor deliverables such as test plans, procedures and reports 

5. Contractor T&E support for FAA-run testing (e.g., on-site technical support, FAA training, meetings, Discrepancy Report (DR)/Program Trouble Report (PTR) review boards, test readiness reviews, etc.) 

Refer to Appendix E, Figure E-4, for the T&E Input Review Cycle for FAA System Specification, SIR Proposal Requirements and Statements of Work. 

NOTE:  Refer to the V&V Repository for the FAA Statement of Work (SOW) Preparation Guide and SOW sample. 

### **5.5.2.2 STATEMENT OF OBJECTIVES** 

A SOO is used when the Government intends to provide the maximum flexibility to each offeror to propose innovative approaches to meet the FAA’s needs.  The SOO is prepared by the FAA in lieu of a SOW or PWS and provides the purpose, scope and top-level objectives of the investment program.  The SOO is used by the offeror to develop a SOW or PWS as part of their proposal.  The SOO does not become part of the contract.  The 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

5-18 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

offeror’s SOW or PWS should be structured for the proposed system solution and not restricted by the structure of the FAA’s SOO.  The Government should develop a crossreference matrix tracking the FAA SOO requirements to the offeror’s proposed SOW or PWS. 

Consider the following when developing the T&E content for the SOO: 

1. The T&E approach documented in the FAA TEMP 

2. Integration of key T&E processes with program management and engineering processes (e.g., risk management, requirements management, configuration management, IMS development, status/problem reporting, etc.) 

3. Cost or schedule savings associated with use of contractor T&E best practices and processes that supports program execution 

4. Use of event-driven program milestones, T&E reviews and activities (e.g., CDRs, Test Readiness Reviews (TRRs), and entrance/exit criteria) 

5. Use of commercial products/processes/standards to reduce cost or schedule 

6. FAA participation on contractor teams to assess program progress 

7. Contractor participation in FAA T&E reviews and activities (e.g., test readiness, technical reviews, data reviews, OT, etc.) 

## **5.6 PROPOSAL EVALUATION SUPPORT** 

The Test Directors (DT and OT), and designated test team members help in the establishment of the evaluation criteria and review the offeror proposals.  The Test Directors are the SMEs for reviewing the test portion of the proposals.  However, the Test Directors also review other portions of the proposals to assess potential impacts to the test program. 

For competitive solicitations, the DT and OT Test Directors evaluate the proposals for technical content against technical evaluation criteria specified in the proposal evaluation plan.  For noncompetitive proposals [sole source procurements and Engineering Change Proposals (ECPs)], the Test Directors review the evaluation of the proposed costs as well as the technical content of the proposal. 

NOTE:  Refer to the V&V Repository for the Contractor Test Cost Proposal Review guidance 

The DT and OT Test Directors and test team members assist in developing technical evaluation criteria used to evaluate offeror proposals to the SIR.  For COTS and/or NDI equipment procurements, the FAA may institute and conduct a “try before you buy” system, service, or capability review in the technical evaluation segment.  This evaluation approach is conducted within the scope of either an OCD or an OCT.  For either approach, prospective equipment offerors develop their proposals based on evaluation criteria defined within the SIR. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

5-19 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

## **6 TEST AND EVALUATION SUPPORT TO SOLUTION IMPLEMENTATION – DEVELOPMENTAL TESTING** 

T&E support to SI begins with the Development Test phase of the T&E program.  The primary objective of DT is to demonstrate that all specified technical and performance requirements for a system, service, or capability have been met.  Another objective is to verify that the system, service, or capability is fully integrated and stable, so that it has no adverse effect on the rest of the NAS.  It may include one or more demonstrations to ensure that the system meets the requirements specified in the contract.  DT is performed by the development contractor and witnessed by the DT Test Director and DT test team. DT activities may also be monitored by IOA personnel.  These test activities can be conducted at the contractor’s facilities, the FAA WJHTC, and/or FAA field sites. 

NOTE:  DT may be conducted by the FAA (or other governmental entity).  The same disciplines this Handbook stipulates for contractor led DT apply to FAA led DT. 

This section of the Handbook describes the processes necessary for DT planning, conduct, and reporting.  Additionally, Appendix E identifies the major DT work products along with their associated review, endorsement, and/or approval cycles. 

## **6.1 DEVELOPMENT TEST OVERVIEW** 

This section of the Handbook describes the processes and best practices to be followed to help ensure a successful DT, which may include 

1. Government or private laboratory testing 

2. SAT, whether conducted by FAA personnel or a contractor and witnessed by the Government 

DT encompasses all testing necessary to verify contractual requirements and is performed at FAA-approved contractor facilities, FAA laboratories, or FAA field sites. After DT, the FAA accepts the portion of the system demonstrated through a formal Government Acceptance (GA) process, which includes a Functional Configuration Audit (FCA) and a Physical Configuration Audit (PCA) (see Section 6.1.3.4). 

There are two types of GA: the first type pertains to the acceptance of products or systems at FAA-approved contractor facilities, FAA laboratories, or FAA field sites; the second type involves the acceptance of the installed products or systems at field sites. 

### **6.1.1 DEVELOPMENT TEST ACTIVITIES** 

The DT process differs from program to program, depending on size and complexity.  It should progress from verifying requirements at the unit level (lowest component) and move incrementally to the fully integrated, fielded system level. 

The following items define the list of basic test activities (which may be modified based on program needs) for DT: 

VVSPT-A2-PDD-013 5.0 

12/18/2020 

6-1 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

1. Software Testing:  Verification of the specifications at the subsystem level. Software Testing usually addresses new and modified software broken down to the Computer Software Configuration Item (CSCI), computer software component, and functional design components. 

2. Hardware Testing:  Verification of the specifications at the subsystem level. Hardware Testing usually addresses new and modified hardware broken down to the Hardware Configuration Item and Hardware Design items. 

3. Factory Acceptance Testing:  Verification of primarily hardware, firmware, and COTS/NDI subsystem components to address subsystem level and system level specification items. 

4. Functional Qualification Testing:  Verification of requirements imposed on a vendor or subcontractor under contract to the prime contractor for delivery of a system, service, or capability or subsystem which demonstrates capabilities to integrate with the NAS through the use of drivers and simulators. 

5. Installation and Integration Testing:  Verification of proper installation and functioning of the complete system in the laboratory environment, including the verification of system interfaces with other NAS equipment and Government Furnished Equipment (GFE). 

6. System Testing:  Verification of integrated software and hardware components to address system level specification items under conditions that emulate the projected operational conditions. 

7. Production Acceptance Testing:  Verification of production line units of developed hardware prior to installations at field sites to address subsystem level and some system level specification items. 

8. Site Acceptance Testing:  Verification of fully integrated software and hardware components to address system level specification items that could not be tested sufficiently during DT System Testing.  SAT also demonstrates that the requirements that were verified under DT System Testing continue to remain in conformance as installed at the operational field site by executing a subset of the System Tests. 

9. Regression Testing:  Verification of integrated software and hardware components after changes to either have been made based on anomalies discovered during previous DT activities.  Regression Testing also ensures that the changes made did not inadvertently result in a problem elsewhere in the system. 

Figure 6-1 provides a diagram of the typical relationships of the above nine (9) DT activities. 

The typical flow shown in Figure 6-1 may be tailored for individual programs, so that some activities may be performed in parallel, or in multiple phases of program implementation. For some programs the traditional development cycle may be replaced by iterative methods known as “Agile Development” or “Agile Acquisition,” and in these cases DT test activities may need to be tailored. 

VVSPT-A2-PDD-013 5.0 

12/18/2020 

6-2 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



**Figure 6-1.  Typical Development Test Activities** 

### **6.1.1.1 AGILE ACQUISITION IN ACQUISITION MANAGEMENT SYSTEM** 

The FAA may use Agile acquisition practices to accelerate the deployment of capabilities and to ensure that capabilities exhibit greater user acceptance and operational value. The AMS includes two guidance documents: FAA Agile Acquisition Principles and Practices and Agile Program Management Practices for the FAA.  For acquisitions adhering to this framework, it is important for test practitioners to become familiar with Agile acquisition terminology and definitions. 

Scrum is the iterative and incremental agile software development framework that the FAA has adapted for use in AMS investment initiatives.  Agile development generally refers to methods of breaking large software releases into smaller units of working systems with limited capabilities, some of which may be immediately deployable.  These are developed in multiple “sprints” of durations of a few weeks, at a sustainable pace (referred to as Cadence).  Less important, or problematic, capabilities are deferred (moved to a later sprint or release) to more quickly provide prioritized operational capabilities to the field.  Testers and contractors, along with users, work together to verify and validate each sprint, and plan the development and testing of the next sprint. 

For each sprint test event, requirements are reviewed and may be replanned or deferred as they are verified and validated.  Agile development principles welcome changing requirements throughout the process.  This is a departure from traditional approaches employed for major acquisitions which typically discourage frequent requirement changes. 

Scrum terminology includes the following: 

1. Epics are large user stories often defined for a release that spans multiple sprints. 

VVSPT-A2-PDD-013 5.0 

12/18/2020 

6-3 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

2. Features are program-level requirements that represent key capabilities and are maintained in a “Program Backlog.” 

3. User stories are Sprint-level requirements. 

4. Daily Scrum is usually a 15-minute “stand-up” meeting to review what was done toward the sprint goal, what needs to be done today, and what obstacles may need help to be overcome. 

Test and evaluation best practices, as described in this Handbook, should be maintained and tailored to the extent feasible to ensure the integrity of the test program and thus support the overall objective of operational readiness.  Users of this Handbook should consult AMS for updates as FAA refines its adoption of agile acquisition methods. 

### **6.1.2 DEVELOPMENT TEST REQUIREMENTS** 

DT verification is based on contractually required activities that the prime contractor must perform to demonstrate conformance to the FAA-developed system specifications.  The prime contractor may develop and maintain separate specifications that are derived from the FAA specifications and approved by the FAA as a CDRL document.  The FAAdeveloped system specifications or the contractor system specification is the “test to” document that drives the conduct of DT.  The prime contractor and associated subcontractors may develop subsystem specifications and design documents that form the basis for subsystem level verification and system level procedure development. 

The DT Test Director and test team review the contractor’s test CDRL documentation and witness all tests during DT.  The DT Test Director reviews the team’s comments and recommends FAA approval or disapproval to the Contracting Officer (CO) and Contracting Officer’s Representative (COR) via the Program Office.  The DT test team must be proficient in their particular program domain (e.g., Communications, Navigation, Surveillance, Weather, and Air Traffic Automation) and eventually become experts on the system under test.  System expertise is necessary to ensure that the tests performed by the system contractor are valid and comprehensive. 

The DT functional flow diagram depicted in Figure 6-2 identifies the tasks and functions that support DT from the SIR through delivery of the DT Final Test Report.  The tasks and functions that support SAT, from generation of the SAT Plan through the start of Field Familiarization (FF), are identified in Figure 6-3. 

VVSPT-A2-PDD-013 5.0 

12/18/2020 

6-4 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



**Figure 6-2.  Development Test Process Flow** 

VVSPT-A2-PDD-013 v5.0 6-5 

12/18/2020 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



**Figure 6-3.  Site Acceptance Test Process Flow** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-6 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **6.1.3 DEVELOPMENT TEST SUPPORT TO CONTRACT ADMINISTRATION** 

The DT Test Director and DT test team coordinate with the CO and the COR to provide support in the following areas: 

1. Negotiating the test cost and schedule baseline prior to contract award 

2. Tracking the contractor test cost and schedule performance measured against the baseline.  This includes reviewing documents delivered by the contractor to the FAA (usually monthly) that detail the cost and schedule status of the program 

3. Participating with the PMO in occasional Integrated Baseline Reviews (IBRs) (The IBR is a formal meeting between the FAA and the contractor to ensure that the program is staying within the program baseline.) 

4. Participating in additional negotiations when changes are made to the contract cost and schedule baseline to determine a new test cost and schedule baseline 

5. Reporting status and changes in the test program 

6. Developing the contract, including modifications to criteria and contract line items that pertain to T&E 

7. Addressing test issues that could affect the cost and schedule baseline 

8. Reporting the results of tests and the disposition of test document deliverables 

9. Evaluating acceptability of test-related contract conformance/deliverable items 10. Deciding to award incentives based on test-related milestones 

11. Deciding GA after DT and SAT 

12. Reporting on minutes or issues from the Test Working Group (TWG) as required 

13. Conducting the FCA and PCA. 

14. Assisting the FAA Quality Reliability Officer (QRO) in GA activities 

### **6.1.3.1 DEVELOPMENT TEST SCREENING INFORMATION REQUEST SUPPORT** 

To ensure that the contractor’s test program meets the program goals, the DT Test Director works with the OT Test Director to develop T&E requirements for the SIR.  The SIR includes a description of work requirements (e.g., SOW, PWS or SOO) for the contractor’s proposal.  See Section 5.5 for a detailed description of DT SIR support requirements. 

### **6.1.3.2 CONTRACTOR DOCUMENTATION SUPPORT** 

The FAA specifies the necessary documentation that the contractor must deliver in accordance with the FAA AMS.  The DT Test Director ensures that the test DID requirements and the test CDRL documents are consistent with the test sections of the SOW or PWS. 

The DT Test Director recommends the schedule for delivery of test documentation by the contractor.  The schedule also includes a time period for the contractor to incorporate comments and redeliver the document to the FAA. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-7 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

Prior to submitting formal draft or final CDRL documents to the FAA, the test team and/or the QRO should check if the contractor has conducted internal peer reviews. These reviews help ensure that the documents fully reflect the contractor's technical and programmatic approach for satisfying FAA requirements.  The contractor must obtain FAA Test Director concurrence prior to the delivery of the final document.  This review is conducted to ensure that all FAA comments are clear and to verify the context in which the contractor intends to incorporate comments. 

The test documentation for any procurement consists of the following: 

1. CMTP 

2. DT VRTM (may be contained in the CMTP, DT Test Plan(s), or in a separate CDRL document) 

3. DT Test Plan(s), DT Test Procedures, and DT Test Report 

4. Accreditation Record 

5. TRR Briefing Package 

6. Integration and Test Development Plan (ITDP) and Report (as required) 

7. Other contractor documentation that may be required and impacts T&E include the following: 

   - a. CM Plan 

   - b. Software Development Plan 

   - c. COTS/NDI Documentation 

   - d. RMA Test Report(s) 

   - e. Specifications 

   - f. Design documentation 

   - g. Safety documentation 

### **6.1.3.3 CONTRACTOR TEST DOCUMENT REVIEW STANDARDS** 

The DT Test Director and test team review and comment on all contractor-delivered test documents.  The Test Director provides comments and recommendations (approval/ disapproval) on the test documents to the CO and COR.  The following guidelines should be used in document review: 

1. Ensure that the test team is familiar with the system design, NAS integration environments, and general NAS architecture prior to reviewing the test plans and procedures 

2. Ensure that the contractor has developed the DT VRTM based on the FAA System Specification in accordance with the terms of the SOW/PWS 

3. Ensure that the approved DT VRTM has been delivered prior to the FAA reviewing the test procedures 

4. Review the documents for technical content and compliance with the applicable DID 

5. Ensure that test documents are consistent with all relevant requirements and contain clearly defined test objectives and success criteria 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-8 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

6. Ensure that all interested parties receive CDRL documents with sufficient time for a comprehensive review 

7. Collect comments from test team document reviews.  Ensure that FAA comments are clear, detailed, specific, and based on compliance with FAA requirements.  Consolidate and submit comments by the due date 

8. Reject the deliverable if it does not meet contract requirements and standards. Technical directions, as approved and conveyed through the Contracting Office, are provided to the contractor to rectify the shortcomings of the deliverable 

9. Use a table, spreadsheet, or database, when practical, to manage comments for delivery to the contractor 

NOTE:  Refer to the V&V Repository for the DT Comment Form template **.** 

### **6.1.3.4 FORMAL AUDIT AND GOVERNMENT ACCEPTANCE ACTIVITIES SUPPORT** 

The DT test team supports the FCA and the PCA.  The FCA is the formal examination of functional characteristics, prior to GA, to verify that the item meets the requirements specified in its functional configuration documentation. The PCA is the formal examination of the "as-built" configuration against its technical documentation to establish or verify the system, service, or capability baseline. DT results acquired from formal test documentation are used to ensure that a system or part of a system successfully passes the PCA and FCA.  The DT Test Director provides the FAA test expertise for the PCA and FCA. 

The DT test team may also support the FAA QRO in the GA process by reviewing and assessing the accuracy of requirements verification status, system issues, and the disposition of problems reported by the contractor. 

### **6.1.4 DEVELOPMENT TEST ENGINEERING SUPPORT** 

The DT test team participates in system engineering meetings and activities held by the PMO to provide test expertise.  This participation includes meetings and events between the FAA and the system contractor (e.g., system engineering working group meetings) and internal FAA-only activities and meetings. 

The DT test team participates in hardware and software design meetings and reviews with the contractor.  This support includes reviewing contractor-developed engineering change request documentation and hardware/software documentation.  Through this activity, the DT test team provides test engineering services for the evaluation of test results from software and hardware redesigns. 

## **6.2 DEVELOPMENT TEST PLANNING** 

To ensure successful test planning and execution, the DT Test Director communicates regularly with the Contractor Test Manager.  In the early part of the contract, the DT Test Director and Contractor Test Manager work closely together to define a comprehensive test program. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-9 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

Early planning tasks involve defining the strategies for the following: 

1. Developing and maintaining the DT VRTM 

2. Overall test approach and breakdown 

3. Tools, simulations, and test environments 

4. Management of test artifacts such as plans, procedures, reports, and test logs. These artifacts are to be managed in accordance with approved configuration and/or document management plans 

5. Developing and managing test laboratories 

6. Providing resources required for testing 

7. System integration 

8. Tailoring of standard test processes 

9. Contractor test management 

10. Informal and formal test conduct 

To ensure that test issues are formally discussed and resolved with the contractor, a TWG is established.  This working group is co-chaired by the DT Test Director and the Contractor Test Manager.  The membership also includes the DT test team members, PMO representatives, system users, the OT Test Director, and the OT test team members.  The meeting schedule for the TWG is established during test planning.  The first meeting is held prior to the first formal design review.  The contractor, as required, records and maintains the minutes and actions items from the TWG meetings. 

### **6.2.1 DEVELOPMENT TEST APPROACH AND STRATEGIES** 

The approach and strategies for a successful DT must apply the test activities previously identified in Section 6.1.1 to address program needs.  Not all test activities are required for every program.  The program complexity, system impacts, and scale of development scopes the level of testing in the DT approach and strategies.  A progressive and measured approach is the best way to address T&E standards.  During DT, requirements must be verified starting at unit levels, and incrementally building through subsystem, to the integrated system(s) level. 

During DT, the test environment can differ between the contractor’s facilities, a field site, a laboratory at the FAA WJHTC, or FAA-approved laboratory.  During the test planning period, the test environment for each test is determined.  The test environment must mimic, as closely as possible, the actual operational environment of the system at the field site.  Also, formal configuration control of the test environment must be maintained throughout DT. 

### **6.2.1.1 COMMERCIAL OFF THE SELF/NON-DEVELOPMENT ITEM TESTING** 

DT must account for the use of COTS products and NDIs in the test program.  The test method for these items is determined by the DT Test Director.  Items that have undergone modification, customization, or protocol changes require specific testing and/or demonstration of the modified elements.  The integration of these items with the other NAS subsystems must be tested or demonstrated, or both.  If an item and/or its integration is specialized or used for the first time in this application, then special testing will be 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-10 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

necessary.  When planning COTS/NDI testing, it is important to identify, consider, and report all associated risk factors (see the FAA SEM for guidance on the implementation of COTS products and NDIs). 

COTS/NDI hardware, software, and firmware items that are not modified or customized can be tested through screening.  Data from COTS/NDI screening is used whenever possible as the sole means of testing requirements, or in conjunction with DT activities. Screening of these items can consist of the following FAA reviews to support verification: 

1. Assessment of vendor specification, design, and production processes 

2. Inspection of visual attributes 

3. Participation in demonstrations of performance, environmental, and suitability characteristics 

4. Evaluation of maintenance support provisions and warranties 

5. Functional integration testing (as required) to assess COTS/NDI functionality as integrated with other COTS, NDI or NAS subsystems 

### **6.2.1.2 DEVELOPMENT TEST SOFTWARE TESTING** 

DT Software Testing is primarily conducted to verify the requirements that are at a lower level (subsystem) than system level requirements.  DT software requirements are documented in contractor software requirement specifications or related design documents.  This testing is conducted by the contractor and witnessed by the FAA, when deemed appropriate.  Testing may occur at a vendor facility, a contractor facility, or the FAA WJHTC in accordance with the approved CMTP. 

DT Software Testing should include or address the following: 

1. The contractor must report the status of testing activities and requirements verification status at the DT TWG meetings or via other means. 

2. As part of the software development, the contractor must maintain CSCI documentation, sufficiently detailed to support independent evaluation of the contractor’s CSCI testing plans, status, and verification results.  CSCI documentation must minimally include, in contractor format, test plans/procedures, test logs, as-run procedures, and data recording and analysis. 

3. The contractor must make CSCI documentation available to the FAA for review. 

4. The verification of a subset of system level requirements may occur during DT Software Testing.  These system level requirements are verified in either of the following ways: 

   - a. The system level requirement is directly verified at the non-system level by the execution of DT Software Test steps. 

   - b. The system level requirement is verified through inspection and analysis of the results of the DT Software Testing for specific related non-system level requirements. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-11 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

The success criteria for the associated non-system level requirements must be included in the delivery of system level success criteria.  The FAA review of these non-system level requirements follow the same process as for the system level requirements. 

Verification of system level requirements through CSCI testing must be documented in a DT VRTM. 

### **6.2.1.3 DEVELOPMENT TEST HARDWARE TESTING** 

DT Hardware Testing is conducted at the unit and/or subsystem level for programs that require contractor-developed hardware.  This testing is conducted by the contractor and witnessed by the FAA.  The formal DT Hardware Testing requires hardware test plans, procedures, and reports at the unit and/or the subsystem level.  In addition, the manufacturing process used to develop the hardware needs to be qualified via testing. When a significant quantity of hardware items is to be produced, only a representative subset of the produced hardware is subject to test. 

DT Hardware Testing focuses on the following areas: 

1. Verifying that the hardware conforms to applicable specifications, is free from manufacturing defects, and is substantially identical to qualified hardware (only for PAT) 

2. Verifying hardware-related human factors and safety requirements 

3. Evaluating the manufacturing process for newly developed hardware 

4. Testing of COTS/NDI products 

5. Testing the hardware in the racks or assemblies to be fielded 

6. Testing the interfaces between Line Replaceable Units (This interface testing can be conducted using special test software, operational software, or both) 

7. Electrical power testing 

8. Thermal testing 

9. Acoustic testing 

10. Electromagnetic Interference (EMI)/ Electromagnetic Compatibility (EMC) testing 

11. Seismic, shock, and vibration testing 

### **6.2.1.4 FACTORY ACCEPTANCE TESTING** 

FAT is performed at the subsystem or partially integrated system level to verify some system level requirements, non-system level software requirements, and hardware subsystem requirements.  FAT may also provide for the final verification of system level requirements that do not require the final baseline environment.  FAT is conducted in accordance with the CMTP and the SOW/PWS.  FAT may be conducted at a contractor’s facility or at the FAA WJHTC. 

The following items should be considered when planning for FAT: 

1. FAT is a prerequisite to DT System Testing 

2. The contractor obtains FAA concurrence of the success criteria 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-12 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

3. FAT plans, procedures, and reports are CDRL deliverables that are approved by the FAA 

4. The FAA test team witnesses FAT activities 

5. The test executions are conducted on a configuration-managed baseline 

### **6.2.1.5 FUNCTIONAL QUALIFICATION TESTING** 

FQT is conducted on programs that have a vendor or subcontractor under contract to the prime contractor for delivery of a system, service, or capability or subsystem.  FQT demonstrates capabilities to integrate with the NAS through the use of drivers and simulators, where applicable. 

Prior to DT System Testing, the prime contractor directs associate subcontractors to perform FQTs in accordance with the CMTP, the FAA contract SOW/PWS, and the prime contractor/subcontractor SOW/PWS. FQT may be conducted at the vendor/subcontractor facility, contractor facility, or the FAA WJHTC.  The FAA monitors the prime contractor and subcontractor on all FQT activities. 

The following items should be considered when planning FQT: 

1. The prime contractor plans and approves all FQT activities 

2. All FQT Test Plans, Test Procedures, and Test Report(s) are to be provided to the FAA for review (including formal deliverables from subcontractors) 

3. FQT verifies system, service, or capability specification requirements associated with the subsystem delivered by the subcontractor 

4. The prime contractor uses the requirements from the system, service, or capability specification to address and provide traceability to the FAA system specifications 

5. All pertinent test data is collected and logged in accordance with the approved QA processes 

6. FQT may not be subjected to all of the formal FAA processes as other DT activities since it is under the auspices of the prime contractor 

### **6.2.1.6 DEVELOPMENT TEST INSTALLATION AND INTEGRATION TESTING** 

To ensure an efficient process, DT Installation and Integration (I&I) Testing is scheduled early in the development of a system and made a prerequisite to DT System Testing. Early integration testing is effective in finding low-level issues that might have been overlooked if this testing was not conducted.  For systems where the integration process is complex, specific integration milestones are required. 

The installation and integration of the hardware into laboratory environments and operational sites to be used during system tests must be verified through DT I&I Testing prior to conducting DT System Testing.  DT I&I Testing ensures that the system is properly installed and functioning, correctly interfaced with GFE, and ready to begin DT System Testing.  It includes hardware and NAS integration test activities.  The FAA witnesses all DT I&I Testing conducted by the contractor. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-13 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **6.2.1.7 DEVELOPMENT TEST SYSTEM TESTING** 

DT System Testing verifies the system’s ability to satisfy the requirements of the applicable system specifications assigned to the contractor.  The FAA witnesses all DT System Testing conducted by the contractor.  System test plans, procedures, and reports are deliverables that are approved by the FAA.  System tests can include: 

1. Integration and Interface Verification:  The verification of subsystem integration and NAS interfaces 

2. System Capacity and Response Time Performance Verification:  The verification of system processing time and stress thresholds 

3. Failure Mode and Failure Recovery Verification:  The verification of failure mode conditions and system recovery capabilities 

4. Stability Verification:  The verification of system performance under extended continuous system use 

5. Reconfiguration Verification:  The verification of system reconfiguration capabilities 

6. Functional Verification:  The verification of functional performance with a fully integrated system and realistic NAS data 

7. Site Simulation Verification:  The verification of system performance under simulated or real operational site conditions and configurations 

8. System Support Functional Verification:  The verification of system support functions with a fully integrated system required by the FAA WJHTC laboratories and the sites 

9. Monitoring and Control Verification:  The verification of required system monitoring and control functions with a fully integrated system 

10. Security Test:  The verification of the security requirements [The Security Test should comply with the program’s Information System Continuous Monitoring (ISCM) and support the Plan of Action and Milestones (POAMs), as required.] 

11. System-Level Acceptance Test:  The verification of the fully assembled and fully integrated system that addresses a sampling of all aspects of system functional performance requirements (This test may provide the foundation for regression testing and SAT.) 

12. Reliability Verification:  The verification by analysis, consisting of reliability predictions supplemented by data collected during system level verification of system reliability 

13. Maintainability Demonstration:  The demonstration of an approved subset of the maintainability requirements 

14. Electromagnetic Interference and Electromagnetic Compatibility Verification: The verification of EMI and EMC requirements 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-14 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

15. Power Quality Testing:  The verification of power quality testing requirements. 

16. Simulation:  Tests using simulated interfaces or subsystems are valid to verify requirements 

System testing often requires the use of both live and simulated interfaces and subsystems.  The use of live and simulated data should be used as complementary test methods.  Live data provides for the most relevant observation of how the system performs.  However, live data may lack repeatability of test results (which may be overcome by the recording and playback of live data).  Simulations provide for repeatability and the generation of conditions that are cost prohibitive or impractical with live data (e.g., capacity scenarios, interference, etc.).  Simulations attempt to mimic live stimuli to a system but are not an exact replication.  Minor shortfalls in simulation fidelity have been observed in practice to have a significant impact on test results (e.g., the system works in simulation but is operationally deficient in practice).  Therefore, optimal system testing is often accomplished using a combination of live and simulated interfaces and subsystems.  Simulations must be accredited (see Section 9.1) prior to the formal conduct of tests using the simulation. 

### **6.2.1.8 PRODUCTION ACCEPTANCE TESTING** 

The contractor performs Production Acceptance Testing (PAT) on newly manufactured hardware items to verify that the hardware items and installed software or firmware conform to applicable specifications.  This testing also verifies that the production unit is free from manufacturing defects and is substantially identical to qualified hardware.  FAA personnel witnesses the contractor’s PAT.  The contractor develops PAT Plan(s), PAT Procedures, and PAT Test Report(s). 

### **6.2.1.9 SITE ACCEPTANCE TESTING** 

SAT verifies the site installation, system integration, and operational configuration of the system and that the system complies with contractual requirements.  All requirements designated by the DT VRTM for verification during SAT must be verified.  SAT is conducted at each government facility where the system is installed.  Ensuring the quality of installation procedures is also part of SAT.  SAT is conducted by the contractor and is witnessed by the FAA.  The DT test team reviews the SAT Plan and Test Procedures. SAT differs from other aspects of DT in that it focuses on performance with respect to a specific location.  SAT verification addresses requirements that need operational site conditions and configurations not available during formal DT System Testing activities. 

The following items must be addressed when planning for SAT: 

1. Contractor designates the SAT Site Test Director for FAA Lead activities and formally accepts test results.  Other personnel may be designated as Alternate Site Test Directors to represent the site in the absence of the Site Test Director. 

2. The DT test team coordinates with each facility prior to SAT.  Meetings are held with the Site Test Director well in advance of any test activities.  This allows for logistical coordination and helps to familiarize site personnel with the product, test process and roles. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-15 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

3. The DT test team coordinates all site test support activities with the Site Test Director or PMO designee. 

4. The DT test team coordinates with the sites regarding the schedule and scope of the SAT for each location. 

5. SAT documentation from Contractor is delivered to the Site Test Director or PMO designee for review and comment. 

6. SAT uses a subset of DT requirements to determine fully acceptable system implementation at each site. 

7. The FAA designates where and when “Key Site” testing takes places.  One or more “Key Sites” is/are designated as the first location(s) in the system site deliveries.  More than one Key Site may be necessary to verify system performance, depending on the scope of the tests.  Some considerations in determining a Key Site include the following: 

   - a. Amount of support available from site personnel to resolve issues found during testing 

   - b. Experience of the site personnel in managing the planned testing 

   - c. Ability to coordinate and document facility procedures, and plan for use by subsequent sites 

   - d. Low risk for ATC safety impacts during system integration at the site 

   - e. Field conditions and environment representative of planned deployment locations 

   - f. Available operational interfaces 

The _AMS T&E Process Guidelines_ recommend that Key Site SAT be conducted following the completion of formal OT.  However, if a test program is designed to verify a significant number of system specification requirements at the Key Site, the Key Site SAT should be planned for completion prior to the start of formal OT. 

Systems often must be adapted depending on where the system is deployed.  The contractor, with FAA approval, identifies which parameters are site-specific and ensures those parameters are included in the software and hardware delivered to the site.  Though CM is critical throughout the test program, precautions are taken to ensure that sitespecific data is correct.  The contractor briefs the site personnel on the configuration of the system prior to SAT at the TRR and Pre-Test Briefing.  These configurations are verified by the QRO and DT test team prior to formal test conduct. 

### **6.2.1.10 DEVELOPMENT TEST CAPABILITY ACCREDITATION** 

DT test capabilities must be accredited in accordance with Section 9.1. 

### **6.2.1.11 COORDINATION BETWEEN DEVELOPMENT AND OPERATIONAL TEST DIRECTORS** 

The DT and the OT Test Directors coordinate on test strategies throughout the lifecycle of the system.  This coordination begins with the ITT when the TEMP is developed and continues through the TWGs. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-16 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

To reduce the risk of encountering major system problems during OT, the DT Test Director should incorporate operational conditions and conduct evaluations from an operational perspective.  To accomplish this, both the DT and OT Test Directors must ensure that operationally oriented test conditions and evaluation criteria are planned for by addressing them appropriately in the SIR, SOW/PWS, CMTP, and system specification. 

### **6.2.1.12 DEVELOPMENT TEST TRAINING AND FAMILIARIZATION** 

The DT Test Director is expected to be an expert in the domain for the program under test.  However, T&E specific training and qualification are required for each DT Test Director.  This training ensures that the DT Test Director understands the policies and processes related to T&E. 

The DT test team receives two types of training: 

1. Training on system operations and functionality, provided by the contractor as required by the SOW/PWS.  Also, the DT test team can become familiarized through participation in the oversight of the system development by the contractor. 

2. T&E Handbook and QMS process (see Section 1.8) training to ensure that T&E practitioners fully understand what is expected to successfully perform the DT test program. 

### **6.2.2 CONTRACTOR MASTER TEST PLAN** 

The Contractor Master Test Plan (CMTP) describes, at a high level, the contractor’s complete test approach for the system investment program.  Information in the CMTP includes the following: 

1. Test Management 

2. DT VRTM 

3. Identification and definition of major test areas 

4. Test tools and accreditation plans for test capabilities 

5. Test environment 

6. Integration testing 

7. Schedule (based on the overall program schedule) 

8. CM 

9. Tracking and verification of safety requirements (includes system safety and personnel safety during tests) 

10. Security (Coordinate these tests with the development of the ISCM to ensure that requirements are addressed) 

11. Process description 

12. Requirements tracking 

13. COTS/NDI test strategy 

14. Testing of interfaces to the NAS 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-17 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

15. PTR and corrective action process (see Section 6.3.7) 

16. Initial system certification (not applicable on all programs) 

NOTE:  Refer to the V&V Repository for the CMTP template and a CMTP sample. 

The DT test team, in accordance with the contract, conducts an early informal review of the CMTP with the contractor to discuss test strategies and issues in a collaborative environment.  This collaboration ensures that the contractor’s and FAA’s test planning is in agreement and that the CMTP is contractually adequate and compliant.  Subsequently, the DT test team and the TSB review the revised CMTP prior to the DT Test Director’s recommendation for approval by the CO.  There may be several iterations of drafts as the CMTP is worked toward acceptance by the FAA.  The TSB can consult with the DT test team to determine whether TSB review will be required for all iterations. 

Refer to Appendix E, Figure E-5, for the complete CMTP review, endorsement, and/or approval cycle. 

For planning purposes, the CMTP can be required as early as Contract Award to as late as 30 business days after the CDR.  Generally, if the system, service, or capability is COTS or an NDI, the CMTP would be required sooner (i.e., towards Contract Award) rather than later.  For development products, general guidance would be based on the maturity level of the system, service, or capability or the technology.  For example, a development program using a proven technology may require the CMTP to be delivered at the System Requirements Review or no later than the Preliminary Design Review (PDR).  Consequently, a development project with an experimental technology or other high risk may require a draft CMTP to be delivered at PDR and a final CMTP at CDR.  To summarize, using sound engineering judgment based on the product’s maturity level is the best guidance for required delivery of the CMTP. 

### **6.2.3 DEVELOPMENT TEST VERIFICATION REQUIREMENTS TRACEABILITY MATRIX** 

The DT Verification Requirements Traceability Matrix (VRTM) summarizes how each requirement is verified.  It includes the following: 

1. Specific requirement identifier 

2. Short description of the requirement 

3. Type of verification method that the contractor performs to show that the requirement is satisfied (Demonstration, Test, Analysis, or Inspection, as defined in Section 5.2.3.5) 

4. Specific DT activity 

5. Unique test identifier during which the requirement is verified 

The initial DT VRTM is developed based on system level requirements contained in the FAA System Specification in accordance with the terms of the SOW/PWS.  Lower-level DT VRTMs are established and documented during the planning for hardware and software testing. 

The baseline DT VRTM is contained in an appendix to the approved CMTP.  Subsequent changes to the DT VRTM do not require a resubmission of the entire CMTP.  Instead, the contractor can deliver formal updates via a revised CMTP appendix as a contract 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-18 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

correspondence that requires FAA approval.  Additionally, during DT Test Plan development, the contractor refines the DT VRTM with test case information and includes the updated DT VRTM as part of or an attachment to the DT Test Plan(s). 

In addition to test case mapping, the DT VRTM includes success criteria, which describe the condition needed to determine if the requirement is met.  Success criteria are used to measure a system task’s accomplishment and/or system characteristics, as well as measures of operational capabilities in terms of the system’s ability to perform its mission in an operational environment.  Success criteria are developed for each contract specification requirement (per the CMTP DID) and are generated by the contractor through a detailed analysis of requirements and provided to the FAA for concurrence prior to the start of each final test execution.  Once FAA concurrence is provided, the contract specification requirements are assessed against the established success criteria during DT.  Any changes to the established, agreed-upon success criteria normally require agreement in writing by the FAA and contractor, with updates incorporated into the DT VRTM. 

NOTE:  Refer to the V&V Repository for the VRTM Content and Guidance Document. 

### **6.2.4 DEVELOPMENT TEST INTEGRATION TEST PLANNING** 

During a complex full system development, hardware and software items are developed separately.  The integration of the hardware and software begins when both of these items reach a sufficient level of maturity. 

For large integration efforts, the prime contractor may be required to prepare and maintain an ITDP.  This plan describes the system, service, or capability integration approach and criteria, the activities for developing test procedures, and the methods and schedules for implementing and controlling the integration and test development programs.  Since this testing may not be the final or full verification of the system requirements, specific criteria and measures must be established and documented to plan for successful DT Integration activities.  If a separate ITDP is not required, the integration testing approach can be documented in the CMTP. 

The following items must be considered when planning for DT Integration Testing: 

1. Plans must measure progress and contain sufficient criteria to determine if the system, service, or capability is ready to move on to the next DT activity. 

2. Prior to an integration activity, entrance criteria must be identified and documented.  Entrance criteria provide an objective measurement of what needs to be in place, with all dependencies clearly identified. 

3. Exit criteria must be identified and documented.  Exit criteria provide objective measurements of what each activity is to accomplish, ensuring an orderly progression of activities and demonstrating that system maturity is increasing to a successful acceptance of the system. 

4. Milestones related to the type of configuration, system loads, complexity of configurations, duration of test run times, and variations of interfaces must be defined to indicate system maturity and the progress of the system integration. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-19 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

5. The test configurations required to perform integration testing must be defined in the ITDP or CMTP. 

### **6.2.5 DEVELOPMENT TEST PLANS** 

DT Test Plans provide more detail than the CMTP regarding DT for the test areas identified in the CMTP.  A DT Test Plan is developed by the contractor for each of the DT activities (e.g., SAT Test Plan, FAT Test Plan, Integration Test Plan, etc.).  DT test plans cover all aspects of DT in proper detail so that the DT Test Procedures can be written from test descriptions contained in the DT Test Plan. 

A DT Test Plan contains the following key elements: 

1. DT program management 

2. Schedule (based on the overall program schedule) 

3. Test descriptions 

4. Plans and itemized lists for required GFE, Government Furnished Information (GFI), and Government Furnished Property (GFP) 

5. PTR and corrective action process (see Section 6.3.7) 

6. CM 

7. DT VRTM 

8. Accreditation plans for test capabilities 

NOTE:  Refer to the V&V Repository for the DT Test Plan template and a DT Test Plan sample. 

Similar to the review and approval process described in Section 6.2.2 for the CMTP, the DT test team conducts an early informal review of the DT Test Plan with the contractor to discuss test strategies and issues in a collaborative environment.  This collaboration ensures that the contractor’s and FAA’s test planning is in agreement.  Subsequently, the DT test team and the TSB review the revised DT Test Plan prior to the DT Test Director’s recommendation for approval by the CO. 

Refer to Appendix E, Figure E-6, for the complete DT Test Plan review, endorsement, and/or approval cycle. 

### **6.2.6 DEVELOPMENT TEST PROCEDURES** 

The DT Test Procedures are developed by the contractor based on their respective DT Test Plan(s).  The Test Procedures include all of the details for conducting a particular test to verify requirements as specified in the respective test plan(s).  These details include the following: 

1. Tables of step-by-step instructions to run the test 

2. Observations to be made during the test 

3. Expected results, including success criteria 

4. Objectives 

5. Test limitations 

6. GFE, GFI, and GFP required for the specific test 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-20 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

7. Notations of the requirements being tested by a particular test and step 

8. Data collection, reduction, and analysis required 

9. Test tools and equipment required 

10. Configuration of the system under test and the test environment 

The DT test team reviews the DT Test Procedures and provides comments to the contractor for disposition.  Once the dispositions of comments are agreed to by both the FAA and the contractor, the DT Test Director recommends approval or disapproval of the document to the CO and COR.  The test procedures are then executed via dry run testing (see Section 6.3.1) prior to formal test conduct. 

Refer to Appendix E, Figure E-7, for the complete DT Test Procedures review and/or approval cycle. 

NOTE:  Refer to the V&V Repository for the DT Test Procedures template and a DT Test Procedures sample. 

### **6.2.7 DEVELOPMENT TEST ENTRANCE CRITERIA** 

Prior to entering any formal DT activity, the DT Test Director ensures that the following minimum DT entrance criteria are met: 

1. All entrance criteria as defined in the approved CMTP and DT Test Plan(s) are satisfied 

2. DT Test Procedures have been submitted, reviewed, and approved 

3. The test configuration is known and documented 

4. Dry run testing has been completed by the contractor 

5. The configuration under test does not have known deficiencies that affect the functions to be verified by the test 

6. If required, test capability accreditation has been conducted and approved 

### **6.2.8 DEVELOPMENT TEST EXIT CRITERIA** 

Prior to exiting any formal DT activity, the DT Test Director ensures that the following minimum DT exit criteria are met: 

1. All exit criteria as defined in the approved CMTP and DT Test Plan(s) are satisfied 

2. All tests are completed in accordance with approved test plans and test procedures 

3. All Post-Test Reviews are complete 

4. Test results are documented and accepted by the FAA 

5. All DT PTRs are fully documented, assessed, and status reported 

6. All contractor performance requirements are addressed in accordance with the contract (may include PTR priority stipulations, or requirement pass-rate percentages) 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-21 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

## **6.3 DEVELOPMENT TEST CONDUCT** 

For all DT, the DT Test Director in conjunction with the QRO ensures that the contractor performs testing in accordance with the SOW/PWS and approved Test Plan(s) and Test Procedures.  The DT Test Director also ensures that the DT test team is prepared to witness the tests.  The contractor conducts debug and dry run testing followed by a TRR prior to each formal DT activity.  The DT Test Director ensures that the minimum DT entrance criteria as defined in Section 6.2.7 have been met. 

The DT Test Director and/or the Test Lead must ensure that the contractor reports and records the status of all test activities.  Following each formal DT activity, the DT Test Director ensures that the minimum DT exit criteria as defined in Section 6.2.8 have been satisfied. 

### **6.3.1 DEVELOPMENT TEST DEBUG AND DRY RUN TESTING** 

Prior to formal DT, dry run testing and debugging of the procedures must be performed. Debug testing is where test procedures are executed against the system under test to ensure that the test steps are correct, complete, and produce repeatable expected results.  During this testing, the procedures are refined and updated to provide a logical flow to the sequence of test steps. 

Dry runs are a complete end-to-end execution of the DT Test Procedures using formal test configurations and accredited scenarios, simulations, and/or test tools to assess the following criteria: 

1. The laboratory environment is prepared 

2. The system has been properly installed and configured 

3. The system has the correct versions of both software and adaptation available, and all system parameters that need to be set have been identified 

4. Procedures are mature and redline text changes are fully incorporated (i.e., test procedures can be run start to finish, as documented, without major deviations or anomalies) 

Dry runs are executed by the contractor and witnessed by the DT test team for each test prior to entering formal DT, with dry run test results presented at the DT TRR.  For each witnessed dry run, a Test Status Report is prepared by the DT Test Lead (see Section 6.3.6).  Dry runs are often executed as if they were formal test runs in accordance with test plans and procedures, including a Pre-Test Briefing and a Post-Test Review.  If such a dry run completes without any significant problems, the contractor may request that the FAA waive a second execution.  If the FAA concurs, the dry run execution is accepted as a formal test run.  In these cases, a Pre-Test Briefing and a Post-Test Review are conducted to capture all test execution details. 

### **6.3.2 DEVELOPMENT TEST READINESS REVIEW** 

The TRR is presented by the contractor to the FAA as required by the SOW/PWS.  The objectives of the TRR are to officially establish that the contractor is prepared and ready to start formal testing of the system, and not to prematurely enter into it.  The TRR covers the following items: 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-22 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

1. Overview of testing to be performed 

2. Status of contractor development and integration milestones and checkpoints 

3. Status of all applicable test documentation 

4. Identification of required Government and contractor resources and personnel 

5. Configuration control and accreditation of test tools and test items (both hardware and software) and any other items necessary for the successful conduct of testing, including Data Reduction and Analysis (DR&A) tools and equipment 

6. Prior test results, including those from any dry runs of tests 

7. Summary of all PTRs, including status of relevant hardware, firmware, and software problems 

8. Review of test baseline, configuration, and environment 

9. System CM status 

10. GFE, GFI, and GFP status (if applicable) 

11. Traceability between requirements and their associated tests using the DT VRTM 

12. Test schedules 

13. Test entrance and exit criteria 

A draft briefing package must be provided to the DT Test Director at a contractually specified date prior to the planned TRR meeting date.  Successful completion of the TRR establishes the readiness for testing.  The DT Test Director advises the COR on whether or not DT may commence.  A copy of the TRR briefing package must be included with the associated DT Test Report. 

### **6.3.3 DEVELOPMENT TEST PRE-TEST BRIEFINGS** 

Prior to each test, the contractor conducts a Pre-Test Briefing to ensure readiness to begin the respective test.  The Pre-Test Briefing covers the following items: 

1. Test objectives and success criteria in accordance with the approved Test Plan and Test Procedures 

2. Proposed procedure changes (redlines) 

3. Test configuration definition (e.g., hardware, adaptation, software version levels, patches, configuration files), including any GFE 

4. Test personnel assignments and FAA and contractor resources 

5. Test conduct walkthrough 

6. Results of the CM audit 

7. Test limitations 

8. Review of known system anomalies that might impact testing 

9. Planned deviations 

10. DR&A methods 

11. Results of any dependent testing that demonstrate readiness for test conduct 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-23 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

The DT Test Director and contractor test manager (or their designees) review and provide signature approval of all planned deviations presented at the Pre-Test Briefing. 

### **6.3.4 FORMAL DEVELOPMENT TEST EXECUTION** 

The standard process items for formal test execution include the following: 

1. The DT Test Director may delegate signature approval to the appropriate DT test team member.  The signature approval grants that test team member with authority to initial changes to the formal Pre-Test Briefing and Post-Test Review packages and redlines during formal test conduct. 

2. The DT test team witnesses the formal runs of all tests.  Copies of procedures are provided to the FAA personnel witnessing formal test runs. 

3. Proper test configuration is verified prior to starting formal test (including hardware, software, firmware, adaptation parameters, test equipment, and test tools). 

4. A Test Status Report is prepared for each formal test run (see Section 6.3.6.). 

5. The DT test team witnesses deviations and changes to the Test Procedures. 

6. The DT test team ensures that anomalies are properly documented (at the time of occurrence) in the test log and that the test log is signed at the completion of testing. 

7. The contractor provides the “as-run procedures” (i.e., with mark-ups) and test log informally after test completion. 

8. The contractor performs a walkthrough review of the DR&A results of the test data with the DT test team to verify requirements. 

### **6.3.5 DEVELOPMENT TEST POST-TEST REVIEWS** 

The contractor conducts a Post-Test Review with the FAA for each test performed to confirm test results and completion.  The Post-Test Review consists of the following: 

1. Overall test results, including a summary of all associated requirements 

2. Status of test objectives and exit criteria as specified in the associated Test Plan and Test Procedures 

3. Test conduct details (e.g., start date and time, stop date and time, etc.) 

4. Any test configuration changes since the Pre-Test Briefing 

5. All problems encountered, including where and how they are documented 

6. Descriptions of all deviations and anomalies encountered 

7. Test procedure changes 

8. Details on any failed steps and requirements 

9. Review of DR&A results and walkthrough findings 

10. Regression test recommendations 

11. Documentation of the outstanding test issues with action plans for closure 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-24 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **6.3.6 DEVELOPMENT TEST STATUS REPORTS** 

The DT Director (or designee) prepares a Test Status Report for each dry run and formal test run and distributes it to the DT test team.  The test team develops and maintains a test status database containing the details of each Test Status Report.  The database is used to document all information pertaining to a given test execution for a particular DT activity, including the following: 

- Test name 

- FAA and prime contractor participants 

- Facility name where the test is conducted 

- Software versions 

- Lab configurations 

- Summary and specific details of the test 

- Issues/concerns 

- The next test activities 

NOTE:  Refer to the V&V Repository for the Test Status Report template. 

### **6.3.7 DEVELOPMENT TEST PROBLEM REPORTING PROCESSES** 

The contractor develops and maintains a database for submitting, tracking, reporting, and maintaining records on PTRs.  The database supports the FAA in maintaining awareness of problems from initiation to final corrective action and archiving.  The database enables status reporting of all test problems.  The contractor uses the database for tracking problems associated with any system, equipment, software, or firmware that has been placed under formal configuration control.  The FAA reviews the overall design of the database to ensure operational use and functionality.  The contractor provides government personnel with access to the database and provides reports at the request of the FAA. 

PTRs entered into the database should be prioritized by the contractor (with review and concurrence by the FAA) according to the following definitions: 

<u>Priority 1 is assigned to a problem that prevents the accomplishment of an operational,</u> mission-critical or mission-essential capability, or jeopardizes safety, security or other requirements designated as CPRs. 

<u>Priority 2 is assigned to a problem that adversely affects the accomplishment of an</u> operational, mission-critical or mission-essential capability and no work-around solution is known. 

<u>Priority 3 is assigned to a problem that adversely affects the accomplishment of an</u> operational, mission-critical or mission-essential capability, but a work-around solution is known. 

<u>Priority 4</u> is assigned to a problem that results in a user/operator inconvenience or annoyance, but does not affect a required operational, mission-critical or missionessential capability. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-25 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

<u>Priority 5 is assigned to any other problem/defect not described above (e.g., system</u> documentation errors). 

These definitions are also applicable to DRs.  DRs may be generated prior to OT for all issues discovered that impact operational requirements but are not being addressed and need to be evaluated during OT (see Section 7.6.4). 

The contractor problem-reporting system must be defined in the T&E activities section of the Test Plan.  The contractor submits the planned corrective action for each problem and identifies the proposed regression testing or future modification(s) to the testing program required to validate the successful corrective action.  If a component fails during testing, the contractor must perform failure analysis to identify the cause of the failure. Failed steps, with or without associated problems, will be explained to the satisfaction of the FAA.  The contractor and the FAA jointly analyze all anomalies to determine a recovery plan. 

The contractor is responsible for any corrective actions necessary to ensure full specification compliance.  The contractor completes repairs or procedural changes prior to submission for regression testing.  GFP-induced anomalies are identified to determine FAA responsibilities for corrective actions.  GFP anomalies do not relieve the contractor from compliance to specification requirements 

### **6.3.8 DEVELOPMENT TEST REGRESSION TESTING** 

The contractor conducts regression tests when changes have been made to the hardware or software for which the FAA has previously accepted test results.  The contractor recommends and briefs the Government on the level of regression testing as part of the corrective action.  The DT Director determines the extent of regression testing required. The contractor will not start regression testing until FAA concurrence to proceed with the regression test is received.  In addition, regression testing and analysis ensures that the fix did not cause a problem elsewhere in the system. 

The contractor determines and fully documents the cause of the noncompliance in the problem-reporting database for any failed test and provides a written notification to the FAA.  The contractor conducts the regression testing using the FAA-approved test plans and test procedures.  The FAA reserves the right to witness all regression testing. 

## **6.4 DEVELOPMENT TEST REPORT** 

The DT Test Report(s) addresses test preparation, conduct, and results, data collected, the DR&A process, and conclusions to be drawn from the test data.  The FAA uses the results contained in the Test Report to verify that a contractor has furnished a system, service, or capability that conforms to all contract requirements for acceptance.  A DT Test Report includes the following: 

1. A copy of the approved TRR briefing package 

2. All approved deviations and waivers generated as a result of testing 

3. As-run test procedures with test logs and witness signatures 

4. A test summary providing the status of each requirement tested 

5. A DT VRTM showing requirement verification status 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-26 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

6. All test results, including data analysis (graphs, pictures, etc.) 

7. Evaluation of system deficiencies and performance based on the testing results 

8. Pre-Test Briefing and Post-Test Review packages 

9. Complete identification of the test configuration, including hardware, software, firmware, adaptation parameters, test equipment, and test tools 

The DT Test Report also includes separate sections for test activities and results from security and safety requirements verification, as defined in the contract. 

The objectives of the DT Test Report are to provide essential information in support of decision-making, assess technical and investment risks, and verify the attainment of technical performance specifications and objectives documented in the DT Test Plan. 

Upon receipt from the contractor, the DT Test Director forwards the DT Test Report to the DT test team and the TSB for review and comment.  Subsequently, the DT test team and the TSB review the revised DT Test Report prior to the DT Test Director’s recommendation for approval by the CO. 

Refer to Appendix E, Figure E-8, for the complete DT Test Report review and approval cycle. 

NOTE:  Refer to the V&V Repository for the DT Test Report template and a DT Test Report sample. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-27 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

## **Intentionally Blank** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

6-28 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

## **7 TEST AND EVALUATION SUPPORT TO SOLUTION IMPLEMENTATION – OPERATIONAL TESTING** 

Following DT and GA of the system, service, or capability, T&E support to SI continues with the OT phase of the T&E program.  OT encompasses T&E of a system’s, service’s, or capability’s operational requirements.  The primary objective of OT is to examine performance and determine operational readiness (effectiveness and suitability) of a new or modified system for use in the NAS and that the NAS infrastructure is ready to accept the system.  OT data is used to assess the operational requirements (program requirements, COIs, MOEs, MOSs, and MOPs), to assess operational effectiveness and operational suitability, in support of the ISD and other relevant decisions.  OT is performed by the OT Test Director and OT test team with AT, Tech Ops, and second-level maintenance personnel.  Other participants may include representatives of other FAA organizations and/or external entities (e.g., airlines, cargo carriers, military, private industry) as required.  OT is conducted at a test facility, (e.g., FAA WJHTC or test radar sites) but may require test activities to be conducted at one or more operational Key Sites to test configurations that are not available in test facilities. 

For designated programs, the data from OT is also used to support IOA.  The results of OT are used to support the Independent Operational Assessment Readiness Declaration, which is prepared by the PMO in accordance with AMS to mark the start of IOA. 

This section of the Handbook describes the processes necessary for OT planning, conduct, and reporting.  Test artifacts such as plans, procedures, reports, and test logs must be managed in accordance with approved configuration and/or document management plans.  Additionally, Appendix E identifies the major OT work products along with their associated review, endorsement, and/or approval cycles. 

## **7.1 OPERATIONAL TEST OVERVIEW** 

The primary focus of OT is to assess the operational effectiveness and suitability of the system, service, or capability.  For major NAS acquisitions, NAS integration testing must be done as a prerequisite to effectiveness and suitability testing. 

### **7.1.1 NATIONAL AIRSPACE SYSTEM INTEGRATION TESTING** 

NAS integration testing is conducted to baseline the new/modified system’s performance, establish the NAS end-to-end performance baseline, and verify that current NAS performance has not been degraded.  Additionally, these tests verify external interface connectivity from the system under test to other FAA and/or vendor-provided systems. 

NAS integration testing may include the following: 

1. Functional verification, as required 

2. Regression testing of DT, as required 

3. Interoperability (testing how the system interacts with other systems) and Interface (testing how lower-level subsystems interact) 

4. Stability 

5. Operational load testing 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-1 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **7.1.2 OPERATIONAL EFFECTIVENESS AND SUITABILITY TESTING** 

Operational effectiveness and suitability testing includes user participation and may consist of the following: 

1. Functional validation testing 

2. Reliability 

3. Maintainability 

4. Availability 

5. Supportability 

6. Degraded operations 

7. Stress and NAS load testing of all interoperable subsystem 

8. HF evaluations 

9. Safety requirements validation and testing to identify new safety hazards 

10. Security 

11. Site adaptation 

12. Transition and switchover/fallback 

13. Certification criteria 

14. Training 

15. OT Regression Testing 

## **7.2 PURPOSE OF OPERATIONAL TEST** 

The purpose of OT is to validate operational readiness by evaluating how well the system, service, or capability satisfies the COIs, CPRs, and all other requirements specified in the PRD of the system under test.  All requirements in the PRD may not be addressable in OT.  The OT VRTM identifies those PRD requirements that are addressed in OT.  COIs focus on the system’s overall capability to support the operational mission.  CPRs are requirements deemed essential to the successful performance of the system, service, or capability in meeting the program’s mission needs. 

A COI is decomposed into MOEs and MOSs, both of which are analyzed to identify MOPs. The MOPs contain testable parameters which form the basis of the OT test case objectives.  These test case objectives form the foundation for test procedures by consolidating them into logical and comprehensive test run components. 

COIs, MOEs, MOSs, and MOPs are described in more detail in Section 5.2.3.2, Decomposition of Critical Operational Issues.  CPRs are described in more detail in Section 5.2.3.3, Critical Performance Requirements Evaluation Approach. 

## **7.3 OPERATIONAL TEST TEAM T ASKS AND FUNCTIONS** 

The OT test team conducts operational testing of a new or modified system in accordance with the tasks and functions described in the following subsections.  Figure 7-1 depicts the OT process flow. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-2 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



**Figure 7-1.  Operational Test Process Flow** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-3 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **7.3.1 OPERATIONAL TEST TEAM ORGANIZATION** 

The OT Test Director has overall program responsibility for the planning and conduct of OT and works with the ITT to define personnel and resource requirements for the OT program.  In large programs, the OT Test Director designates select test team members as Test Leads.  The various Test Lead responsibilities are selectively assigned on the basis of each member’s level of experience and area of specialization.  Test Leads are responsible for all activities related to their respective test area.  For small or non-complex programs, the OT Test Director may also serve as the Test Lead.  Additionally, for programs that have been designated for an IOA, the Independent Safety Assessment Team monitors OT activities. 

### **7.3.2 OPERATIONAL TEST PLANNING IN TEST AND EVALUATION MASTER PLAN DEVELOPMENT** 

Planning for an OT program begins with the formation of the ITT.  The OT Test Director and OT test team work in conjunction with the DT Test Director, DT test team, and other program stakeholders to develop the TEMP.  This document incorporates DT and OT approaches, which include an initial test design for determining system performance, effectiveness, and operational suitability. 

The OT section of the TEMP details the following: 

1. OT philosophy and approach 

2. All systems and configurations to be tested 

3. Any required special facilities or test capabilities, including telemetry, aircraft for flight testing, and support equipment resources 

4. Roles and responsibilities for the OT Test Director, test team, field leads, and participants 

5. Test entrance and exit criteria 

6. Methodologies for resolving COIs 

7. OT limitations and their possible impacts on validation of OT requirements (e.g., incomplete or unavailable test environment(s), operational interfaces, operational facilities, resources, training, and technical manuals) 

8. Plans and methods for early, interim, and final reporting on OT issues and results 

For programs using Agile development methods (see Section 6.1.1.1) there may be incremental deployments to the field.  For every increment put into operational use, the FAA must verify and validate that the system is operationally ready. 

### **7.3.3 OPERATIONAL TEST SUPPORT TO CONTRACT ADMINISTRATION** 

To ensure that the operational perspective is taken into account during the design, development, and testing of a new system, and to ensure that contractor support to the OT effort is made available, the OT Test Director works with the DT Test Director to develop the T&E requirements for the SIR.  The SIR includes a description of tasks (e.g., SOW, PWS, or SOO) the contractor must include in their proposal.  See Section 5.5 for a detailed description of OT SIR support requirements. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-4 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **7.3.4 OPERATIONAL TEST TRAINING** 

The OT Test Director is expected to be an expert in the domain for the program under test.  Additionally, T&E specific training and qualification are required to ensure that each OT Test Director understands the policies and processes related to T&E. 

The OT test team receives the following: 

1. Training on system operations and functionality, provided by the contractor as required by the contract, along with participation in the oversight of the system development by the contractor for system familiarization 

2. T&E  Handbook and QMS process training to ensure that T&E practitioners fully understand what is expected to successfully perform the OT test program 

3. Training through participation in prototype testbed activities and DT activities 

4. Hands-on familiarization for the system under test 

### **7.3.5 COORDINATION WITH OPERATIONAL TEST FIELD PERSONNEL** 

Coordination with OT field participants starts during the T&E Planning and Support phase to ensure that the OT field team is formed and their participation in the program is wellestablished by the time formal OT takes place.  The team is composed of field SMEs, field supervisors, PMO representatives, and representatives of other organizations as required. 

It is recommended for large programs that a member of the team be selected as a liaison to serve as a Point of Contact (POC) between the OT test team and the OT field team. This liaison assists with some or all of the following activities: 

1. Determination of field personnel requirements 

2. Coordination with field organizations, union representatives, and site personnel 

3. Travel issues such as facility security requirements for visitors 

4. OT test procedure development activities 

5. OT test procedure dry runs 

6. Formal OT conduct coordination 

7. Field test team briefings 

8. Determination of operational issues 

9. Collection and disposition of field test team issues 

### **7.3.6 OT TEST CAPABILITY ACCREDITATION** 

OT test capabilities must be accredited in accordance with Section 9.1. 

## **7.4 OPERATIONAL TEST PLANNING** 

### **7.4.1 OPERATIONAL TEST PLAN DEVELOPMENT** 

The OT Test Plan describes the planning and preparation activities required prior to the conduct of OT.  It includes a description of the testing to be accomplished, how to execute 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-5 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

test procedures, and reporting of test results.  It provides sufficient detail to guide the development of the OT Test Procedures. 

The OT Test Plan addresses the following topics: 

1. Test management 

2. Identification and descriptions of tests to be conducted (providing enough detail so that test procedures can be written based on these test descriptions) 

3. Test tools 

4. Test environments and facilities 

5. Accreditation plans for test capabilities 

6. Schedule 

7. CM in accordance with the CM Plan 

8. Safety 

9. Security 

10. Requirements tracking through an OT VRTM for each PRD requirement allocated to OT 

11. Criteria identified to develop operational readiness determination (e.g., no Priority 1 or 2 PTRs associated with a COI) 

12. Testing of interfaces to the NAS 

13. Discrepancy/PTR, categorization, and resolution 

14. Test limitations 

15. Test reporting strategy including CPR and COI status [Interim Assessment Report(s), Quicklook Test Report(s), and Final Test Report] 

The OT Test Director must ensure that the OT Test Plan has been peer-reviewed (see Section 1.9) prior to submission to management for endorsement/approval.  The OT Test Plan requires endorsement by the TSB and the T&E First-Line Supervisor, and the approval of the respective T&E Senior Manager and the Program Manager.  Minor changes to the OT Test Plan that do not impact test strategy or scope (e.g., minor schedule changes, editorial corrections, etc.) are considered working drafts only and do not require these approval signatures but are still subject to the DMC PDD. 

Refer to Appendix E, Figure E-10, for the complete OT Test Plan review, endorsement, and/or approval cycle. 

NOTE:  Refer to the V&V Repository for the OT Test Plan template and OT Test Plan samples. 

### **7.4.2 OPERATIONAL TEST VERIFICATION REQUIREMENTS TRACEABILITY MATRIX** 

The purpose of the OT VRTM is to address all COIs, CPRs, and other program requirements to be verified and validated as part of the OT test program.  The OT VRTM accomplishes this by mapping the COIs/MOEs/MOSs/MOPs and applicable program requirements from the PRD to the respective OT activities and test cases in which the MOPs and requirements will be verified and validated. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-6 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

The TEMP VRTM, which maps the COIs/MOEs/MOSs/MOPs and program requirements to the respective test phase(s) and test activities, provides the basis for developing the OT VRTM (see Section 5.2.3.5).  During OT Test Plan development, the OT VRTM is further refined to include COI/MOE/MOS/MOP and program requirement mapping to the individual OT cases. 

NOTE:  Refer to the V&V Repository for the VRTM Content and Guidance Document. 

### **7.4.3 OPERATIONAL TEST PROCEDURE DEVELOPMENT** 

The OT test procedure development process consists of translating the test descriptions and evaluation approaches contained in the OT Test Plan.  The approach to OT data collection includes both objective measurements of system parameters and subjective user-evaluation questionnaires. 

### **7.4.3.1 OPERATIONAL TEST PROCEDURE FORMULATION** 

The formulation of procedures takes into account operational conditions, measures, user stimuli, and scenarios that address the OT requirements identified in the OT VRTM.  The procedures must address COIs, MOEs, MOSs, and MOPs through their respective test cases.  They may also include system checkout activities needed to support procedure development.  Evaluating specific functionality requires that the procedures contain stepby-step detailed instructions to ensure test objectives are met and the intended data is collected.  To evaluate operational capabilities, high-level nonspecific test procedures are used to allow the participant to realistically use the system and respond to events. 

The OT Test Director oversees the OT test team’s development of the OT test procedures.  After the OT test procedures have been developed, including debugging and dry runs, the OT Test Director must ensure that the draft OT Test Procedures document has been peer reviewed (see Section 1.9).  The draft OT Test Procedures should also be made available to the TSB for optional review.  After receiving and incorporating any comments from the TSB, the OT Test Director approves the document for use in formal test conduct. 

Refer to Appendix E, Figure E-11, for the complete OT Test Procedures review, endorsement, and/or approval cycle. 

The OT test team tracks and reports the status of OT test procedure development through an OT Test Procedures Status Matrix.  This status matrix, at a minimum, indicates the progress toward completion of the documentation, debugging, and dry runs required for each planned OT test procedure. 

NOTE:  Refer to the V&V Repository for the OT Test Procedures Status Matrix. 

### **7.4.3.2 OPERATIONAL TEST PROCEDURE QUESTIONNAIRES** 

The OT test team uses questionnaires to augment information gathered from performance of OT test procedures.  Questionnaires are developed to augment objective performance measures or substantive information when objective data is unavailable or 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-7 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

difficult to collect.  Care should be taken if there is insufficient objective data and emphasis falls on the questionnaire responses.  The OT user-evaluation questionnaires must: 

1. Be effectively written to avoid the solicitation of biased replies. (It is important that the evaluation questions do not allow individual preferences of the test participant to be reflected in the reply) 

2. Be clear, concise, and directly relevant to the MOEs, MOSs, or MOPs to be assessed 

3. Support the assessment of the capabilities of the system to support operational tasks 

4. Be in the form of numerical rating scales, or “yes” or “no” answers to questions. Test participants may provide subjective elaborations, or explanations on specific questions, to support their responses 

Appropriate union approval from the National Air Traffic Controllers Association, National Association of Air Traffic Specialists or Professional Airways System Specialists is required before a questionnaire may be used.  Approval may involve significant lead time. 

NOTE:  Refer to the V&V Repository for the OT Questionnaire guidance and OT Questionnaire samples. 

### **7.4.4 LOGISTICS FOR FORMAL TEST CONDUCT** 

The following list describes the logistical activities that need to be coordinated prior to the OT TRR: 

1. When site OT testing is required: 

   - a. Approval of all required test-related NAS Change Proposals (NCPs) 

   - b. Coordination of site access and security clearances 

   - c. Site Survey 

   - d. Program/T&E Briefing 

2. Coordination of training for the test team and field participants 

3. Installation of the system under test is complete and complies with the documented baseline 

4. Completion of the configuration baseline audit to identify all software, firmware, and hardware versions in the system under test 

5. Assuring that the OT Test Director accomplishes the following: 

   - a. Defines roles and responsibilities of all team members 

   - b. Coordinates all tasks required for test conduct.  (This includes laboratory coordination and scheduling, data collection activities, Pre-Test Briefings and Post-Test Reviews, observers, simulation support, and interface support) 

   - c. Maintains all test schedules 

   - d. Establishes procedural checklists 

   - e. Conducts preliminary OT reviews of all scheduled activities with team members and the Facility Manager 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-8 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

- f. Ensures that the Facility Manager is informed on all planned test activities 

- g. Ensures that the Facility Manager coordinates planned test activities with adjacent facilities, if necessary 

- h. Ensures that the Facility Manager coordinates and schedules required live testing procedures, interfaces, and events 

### **7.4.5 OPERATIONAL TEST ENTRANCE CRITERIA** 

The OT phase begins after GA of the contractor-developed system, service or capability. In addition to ensuring that the DT exit criteria have been satisfied, the OT Test Director plays a key role in ensuring that OT entrance criteria are fully met before formal OT begins.  This is accomplished through participation in the ITT, early contractual planning, program meetings, and DT activities.  The minimum entrance criteria for formal OT include the following: 

1. DT Exit criteria, as defined in the approved _CMTP_ and the _DT Plan_ (s), have been satisfied. 

2. All Priority 1, Priority 2, and critical DT PTRs that impact OT have been fixed and incorporated into the OT baseline. 

3. The _OT Test Plan_ has been reviewed and approved. 

4. The _OT Test Procedures_ have been reviewed and dry runs have been completed. 

5. The test configuration is known and documented. 

6. All equipment and software required by the _OT Test Plan_ and _OT Test Procedures_ have been installed and are available. 

7. All planned OT test capability accreditation has been completed and approved. 

8. The T&E First-Line Supervisor approves all waivers for deviations from test standards in the T&E Handbook.  Significant deviations are described in the TRR documentation.  All deviations from the _OT Test Plan_ and approved waivers are presented to the Program Manager or representative at the TRR. 

9. The OT TRR has been conducted (see Section 7.6.2).  The Program Manager or representative approves the start of formal OT by signing the TRR package. 

The formal OT events may start once the above criteria have been satisfied. NOTE:  Refer to the V&V Repository for the Request for Waiver form. 

### **7.4.6 OPERATIONAL TEST EXIT CRITERIA** 

OT exit criteria ensure that the purpose of OT has been met and that the effectiveness and suitability of the system has been adequately verified and validated for an operational readiness determination. 

Following formal OT conduct, the OT Test Director facilitates a review of the OT results, including a discussion of the OT exit criteria, with the ITT to confirm that all exit criteria have been met.  Action plans must be created for any exit criteria that have not been met. The achievement of the OT Exit Criteria initiates the finalization of the OT Final Test Report, which is required for ISD entrance criteria. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-9 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

The minimum exit criteria for OT include the following: 

1. In accordance with the OT Test Plan and OT Test Procedures, the defined test case objectives (including criteria and test case requirements), for each test must have been addressed, met, and any support analyses completed and documented.  These include the following: 

   - a. All planned OT test procedures have been satisfactorily executed. 

   - b. All MOP data has been collected and assessed. 

   - c. All COIs and CPRs are fully assessed and their status reported. 

   - d. All OT artifacts from the Post-Test Reviews and the OT Caucus have been reviewed (e.g., DRs, As-Run Test Procedures, test logs, questionnaires). 

   - e. All required regression testing has been completed. 

2. DRs and PTRs that impact the operational readiness of the system have been fixed, verified, and regression tested.  These must be identified and approved through the OT Caucus (see Section 7.5.5). 

## **7.5 OPERATIONAL TEST CONDUCT** 

The OT test team, with the support of the field participants, conducts formal OT in accordance with the approved OT Test Plan and OT Test Procedures.  Formal OT does not begin until the OT entrance criteria (as documented in the TEMP and the OT Plan) are met.  The ITT convenes to determine compliance with the OT entrance criteria.  An OT TRR is then conducted to ensure that all elements are in place prior to commencing with formal OT conduct. 

### **7.5.1 DEBUG AND DRY RUNS** 

Prior to formal OT, debugging and dry run testing of the procedures must be performed. Debug testing is where test procedures are executed against the system under test to ensure that the test steps are correct, complete, and produce repeatable expected results.  During this testing, the procedures are refined and updated to provide a logical flow to the sequence of test steps. 

Dry runs are a complete end-to-end execution of the OT Test Procedures using formal test configurations and accredited scenarios, simulations, and/or test tools to assess the following criteria: 

1. The laboratory environment is prepared. 

2. The system has been properly installed and configured. 

3. The system has the correct versions of both software and adaptation available, and all system parameters that need to be set have been identified. 

4. Any new or modified test scenarios, simulations, or tests tools are valid. 

5. Procedures are mature and redline text changes are fully incorporated (i.e., test procedures can be run start to finish, as documented, without major deviations or anomalies). 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-10 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

NOTE: Refer to the V&V Repository for the OT Test Procedures template and an OT Test Procedures sample. 

Field site personnel should participate in the dry run process to ensure that the test environment, procedures, and system are ready for formal testing.  Additionally, a Test Status Report is generated at the conclusion of each test activity (debugs or dry runs) and provided to the ITT.  Any anomalies or discrepancies are reported and analyzed for their impact on performing formal OT. 

### **7.5.2 OPERATIONAL TEST READINESS REVIEW** 

The OT TRR is conducted by the OT test team prior to the start of the formal OT activity. This review verifies and approves the readiness to start formal OT and ensures participants understand any outstanding issues.  The TRR also communicates risks and limitations for formal OT.  The TRR includes review of the following: 

1. OT entrance criteria as documented in the OT Plan 

2. Impacts of any entry criteria not fully met 

3. OT approach, test objectives, and test structure to determine operational readiness 

4. Test schedule 

5. Hardware and software versions and configurations 

6. CM process and test data management 

7. Test team roles and responsibilities 

8. DR process 

9. Signatures on all OT Test Plan(s) and OT Test Procedures 

10. Successful conduct of all OT procedure checkouts and dry runs 

11. Known problems and workarounds (identification of test impacts and criticality of operational issues) 

12. Test limitations, risks and deviations from the approved OT Plan (understood, documented, and presented to the Program Manager or representative) 

13. Availability and training of required test personnel 

14. Completion and availability of required technical and user documentation 

15. Availability and documentation of executable system adaptations 

16. Completion of required Test Capability Accreditation Records 

17. Configuration, certification and functionality of all DR&A tools, test tools, simulators, and emulators 

18. Test NCP approval, if required 

19. OT exit criteria 

The Program Manager or representative approves/disapproves the start of formal OT based on the TRR presentation, thereby accepting all waivers and deviations.  A signature on the TRR package is required for approval (email acceptable). 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-11 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **7.5.3 FORMAL OPERATIONAL TEST CONDUCT** 

Formal OT conduct consists of Pre-Test Briefings, test executions, Post-Test Reviews, and status reporting. 

### **7.5.3.1 OPERATIONAL TEST PRE-TEST BRIEFINGS** 

The OT Pre-Test Briefing is presented by the OT Test Lead and consists of the approach for each test to be conducted.  It includes a review of the following: 

1. Test objectives and success criteria 

2. Test configurations (hardware, adaptation, software level, patches, test tool certification, and configuration files) 

3. Test personnel assignments 

4. Test conduct walkthrough 

5. Proposed procedural changes or planned deviations 

6. Test limitations 

7. The status of all known problems and anomalies that may impact the test or its results 

8. Methods of data collection 

### **7.5.3.2 OPERATIONAL TEST EXECUTION** 

OT case executions are the culmination of OT planning efforts resulting in the complete and official running of the OT Test Procedures.  These test cases are the primary data source for OT requirements validation. 

During formal OT, the Test Lead manages the test execution, maintains a log of all system state changes not documented in the procedures, and records information concerning any laboratory or system issue that results in a deviation of, or impact on, the test.  Such incidents include, but are not necessarily limited to, system reboots and hard failures. Test observer logs are used to capture issues that impact operational effectiveness or suitability.  If questionnaires are being used to capture qualitative and quantitative data, they must be completed and collected immediately following the test execution.  The Test Lead also maintains a list of DRs that identify all issues encountered during testing (see Section 7.6.4). 

### **7.5.3.3 OPERATIONAL TEST POST-TEST REVIEWS AND TEST STATUS REPORTING** 

The OT Test Lead should hold reviews at appropriate intervals during a test activity, such as: 

1. Reviews of test case results at the end of each day of testing 

2. Reviews at the end of a test-case group 

3. Reviews at the end of a test activity 

4. Final Post-Test Review 

These reviews are all held prior to the OT Caucus.  Their main focus is to get field and test personnel to clarify any issues that are not fully documented and to hold initial 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-12 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

discussions on any impacts on operational effectiveness or suitability.  The development engineers responsible for troubleshooting issues should attend to ensure that they fully understand the issues.  The OT Test Lead generates briefing minutes and assigns action items. 

The reviews may include the following: 

1. Review of test results, including a summary of verified requirements 

2. The status of test objectives and success criteria 

3. Review of issues in the respective logs of the OT Test Lead and observers 

4. Review of problems for accuracy, completeness, and recommended dispositions 

5. Review of blue-line deviations from the test procedures (changes to test procedures made during formal test conduct) 

6. Recommendations for retesting or regression testing 

Test status reports are generated following the completion of each of the above reviews. These reports summarize the results of testing, highlight significant findings, and provide an assessment of whether the objectives were met.  They also record DRs and comments made against the system documentation.  The contents of the OT Post-Test Reviews and Test Status Reports are used to support development of the OT Quicklook Test Report and Final Test Report. 

- NOTE:  Refer to the V&V Repository for the Test Status Report template. 

### **7.5.4 OPERATIONAL TEST DISCREPANCY REPORTING** 

DRs are generated for all issues discovered during OT.  DRs are also generated prior to OT for all issues discovered that impact operational requirements but are not being addressed and need to be evaluated during OT.  A DR must contain enough detail to document the issue and facilitate corrective action.  Such details include, but are not necessarily limited to, the following: 

   1. Unique DR identifier 

   2. Project or system identification 

   3. Requirement(s) impacted, including reference to COI/MOE/MOS/MOP affected 

   4. Description of the issue 

   5. Priority of the problem (see Section 6.3.7) 

   6. Impact of the problem 

   7. Name or number of the test case 

   8. Test step at which the discrepancy occurred 

   9. Test configuration and system states; including date(s) and time(s) 

   10. Supporting records and data (e.g., logs, screen saves, system records, system reports, test tool data, plots, etc.) 

   11. Associated resolution upon closure 

   12. Originator 

- NOTE:  Refer to the V&V Repository for the Discrepancy Report form. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-13 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

The OT Test Director and test team must conduct DR reviews on a regular basis to ensure accurate descriptions, determine validity and disposition priorities, and assess proposed resolutions.  To facilitate efficient tracking of issues discovered during OT, the OT Test Director maintains a DR database.  DRs are tracked until dispositions are documented for each and are closed out when the OT Test Director and the relevant stakeholders are satisfied that the issue has been resolved or mitigated.  All DRs that require corrective action by the contractor are raised to PTR status.  DRs that have been raised to PTRs are not closed out as DRs until corrective action has been implemented by the contractor and verified by the FAA. 

### **7.5.5 OPERATIONAL TEST CAUCUS** 

The OT Caucus is held after the completion of formal testing.  It is chaired by the OT Test Director and is conducted to present and review all findings and test results related to the operational effectiveness and suitability of the system.  At a minimum, participants include representatives from the OT test team and the field team(s). 

The focus of the caucus is to gain concurrence on the operational impact and criticality of all DRs and PTRs.  In preparation for the caucus, all OT DRs and PTRs are entered into an OT Problem Traceability Matrix.  At the caucus, the matrix is reviewed to assess the impact of DRs and PTRs on COIs, MOEs, MOSs, MOPs, and CPRs, and to determine their operational criticality.  All DRs that require corrective action by the contractor are raised to PTR status.  PTRs are assigned initial priorities to assist with resolution plans. At the caucus, each COI must be addressed based on the criticality of the problem(s) impacting it.  Figure 7-2 shows the process flow for determining the degree to which COIs and program requirements are met. 

The following standard practices and activities must be considered for the conduct of the OT Caucus: 

1. The assessment of COIs must focus on operational impacts that: 

   - a. Ensure that adverse conditions are clearly linked to operational issues 

   - b. Clearly identify the specific operational functions, procedures, or services that are interrupted, delayed, or degraded 

   - c. Indicate suitable workarounds, or if workarounds are not feasible 

2. Every issue must be well supported by references to the established CPRs, and COIs.  The DRs are related to COIs through their constituent MOPs, MOEs and MOSs in the OT Problem Traceability Matrix.  The matrix shows whether each COI is fully met, partially met, or not met due to significant issues.  It can also indicate when a COI is limited, due to less significant issues, but not enough to prevent the system from being operationally effective or suitable. (See Glossary for COI status definitions of Yes, Ltd (Limited), and No.) 

3. In addition to issues specifically impacting COIs, discuss and document general issues and concerns that the OT participants found to affect operational suitability and effectiveness.  Ensure that these issues and concerns have sufficient justification to be documented as an operational impact (i.e., impact or degradation to operational functions or services). 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-14 

### **<u>TEST & E</u> VALUATION H ANDBOOK** 



**Figure 7-2.  Operational Test: Critical Requirements Path** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-15 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

4. The caucus should not make programmatic decisions (such as milestone, deployment, scheduling, or staffing decisions). 

   - a. The OT Caucus should only provide supporting information for programmatic decisions. 

   - b. The caucus can address site specific considerations that support site deployment decisions or Key Site planning. 

5. The OT Caucus should review the established OT Exit Criteria, as indicated in Section 7.5.6, and report the status of any outstanding items. 

6. The OT Caucus ensures that the caucus activities provide sufficient time for stakeholders from different functional areas to collaborate on operational issues, to provide a comprehensive and holistic assessment of operational impacts. 

An OT Caucus Summary Report is produced to document the status of each COI, MOE, MOS, MOP, and CPR for the system under test.  This report supports resolution of critical PTRs prior to operational deployment.  This report and the PTR resolution plans provide the framework for any regression testing that may be necessary to resolve outstanding critical PTRs.  The Caucus Summary report is the artifact that provides data that goes into the Quicklook and Final reports. 

NOTE:  Refer to the V&V Repository for the OT Problem Traceability Matrix and OT Caucus Summary Report templates. 

### **7.5.6 OPERATIONAL TEST REGRESSION TESTING** 

OT regression testing is conducted to verify the integrity of solutions to DRs/PTRs. Additionally, regression testing is performed to ensure that these solutions have not introduced any new problems or issues, and to support validation of the system’s readiness for operational use.  Regression testing may require the participation of the OT field team(s).  Regression testing must: 

1. Ensure the functionality of corrective actions 

2. Demonstrate that the corrective actions do not impact other system functionality 

3. Re-run OT test procedures that were impacted by the problem 

4. Re-run OT test procedures that may be impacted by the fix 

5. Follow the same processes required for formal OT 

6. Be documented in an OT Caucus Summary Report, an OT Quicklook Test Report, and/or the OT Final Test Report 

## **7.6 OPERATIONAL TEST REPORTING** 

OT test reporting is comprised of the following reports: 

1. Interim Assessment Report(s) 

2. Quicklook Test Report(s) 

3. Final Test Report 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-16 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **7.6.1 OPERATIONAL TEST INTERIM ASSESSMENT REPORT** 

The OT IAR is an optional reporting mechanism that provides management with an assessment of the current state and maturity of the system by identifying system capabilities and limitations as tested for that reporting period.  OT IARs are developed following specific milestones, whether issues exist or not, as defined in the TEMP.  If exercising the option of the OT IAR, it must be provided to the TSB and ITT for their review and comment. 

The OT IAR provides sufficient data to support resolution plans and program decisions. Additionally, the OT IAR assists in the planning for future test activities and support planning for system implementation and deployment.  Specifically, the OT IAR: 

1. Provides the status of critical performance criteria defined in the TEMP 

2. Analyzes issues based on their impact on COIs and CPRs 

3. Provides early operational reporting for the following: 

   - a. DT 

   - b. Pre-formal OT conduct 

   - c. Formal OT conduct 

4. Highlights critical system issues which may impact the following operational milestones: 

   - a. Initial Operational Capability (IOC) 

   - b. ISD 

   - c. Operational Readiness Dates at field sites 

5. Provides support for programmatic decision-making (including scheduling, test planning, site deployment, and site acceptance testing) 

6. Supports operations and maintenance planning 

7. Provides input to the OT Quicklook Test Report and the OT Final Test Report 

The OT Test Director must provide the draft OT IAR to the TSB and the ITT for review and comment prior to electronically distributing the final document to the respective T&E Senior Manager, the Program Manager, the T&E First-Line Supervisor, and the TSB. 

Refer to Appendix E, Figure E-12, for the complete OT IAR review, endorsement, and/or approval cycle. 

NOTE:  Refer to the V&V Repository for the OT IAR template. 

### **7.6.2 OPERATIONAL TEST QUICKLOOK TEST REPORT** 

The OT Quicklook Test Report is developed following the completion of formal OT to provide a preliminary assessment of operational readiness.  This report is provided in advance of the more detailed Final Test Report that requires more analysis and time to complete.  The report contains preliminary results and, therefore, is not intended to support programmatic or operational milestone decisions. 

The OT Quicklook Test Report documents the preliminary results of all formal testing and the resolution plans of any issues discussed at the OT Caucus.  It expands upon the content provided through the OT Caucus Summary Report.  General descriptions of the 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-17 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

system’s performance and functional and operational limitations are included in the Quicklook Test Report.  If the resolution of program issues delays delivery of the OT Final Test Report, an OT Quicklook Test Report may be required after each major OT regression test. 

The OT Quicklook Test Report includes the following: 

1. An executive summary 

2. Background information on the testing 

3. A summary of test activities, including test article configuration 

4. Results from the Caucus Summary Report 

5. A synopsis of preliminary test results 

6. Preliminary conclusions, including a preliminary determination of operational readiness 

7. OT Issues Matrix as an appendix 

It is critical that the draft OT Quicklook Test Report be provided to the ITT and the TSB for their review and comment in time to support problem resolution and IOC/ISD preparation activities.  The approved OT Quicklook Test Report should be delivered within 15 business days from the completion of the test.  The approved OT Quicklook Test Report must be electronically distributed to the respective T&E Senior Manager, the Program Manager, the T&E First-Line Supervisor, the Director of Test Service Organization (or equivalent), and the TSB. 

The OT Quicklook Test Report is preliminary and is not intended to support programmatic or operational milestone decisions.  However, if directed by the PMO to use the report in this manner (for example, National Deployment, IOC, ISD) or in lieu of a final report, then consult the additional guidance provided in the OT Quicklook Report template, which includes endorsement by the TSB and signature of the Director of Test Service Organization (or equivalent). 

Refer to Appendix E, Figure E-13, for the complete OT Quicklook Test Report review, endorsement, and/or approval cycle. 

NOTE: Refer to the V&V Repository for the OT Quicklook Test Report template and an OT Quicklook Test Report sample. 

### **7.6.3 OPERATIONAL TEST FINAL TEST REPORT** 

The OT Final Test Report presents specific findings related to the operational effectiveness and suitability of the system.  The report: 

1. Contains an executive summary which summarizes the test results 

2. Addresses the resolution of all COIs 

3. Assesses operational readiness of the system, (operational effectiveness and suitability) 

4. Characterizes the operational capabilities and limitations of the system based on system performance against the CPRs 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-18 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

5. Documents the methods used in, and results of, the detailed analyses of test data. 

6. Identifies and assesses PTRs and issues that impact critical capabilities and benefits 

7. Updates the status of problems highlighted in the OT Quicklook Test Report 

8. Provides status of exit criteria as defined in the OT Test Plan 

9. Includes test descriptions, results, conclusions, and recommendations 

10. Identifies technical or operational risk areas 

11. Includes all approved deviations and waivers generated as a result of testing 

Conclusions regarding operational effectiveness and suitability are based on the combined results of all operational tests.  Operational readiness is assessed on the basis of operational effectiveness and suitability performance in accordance with COIs and CPRs.  In addition, the report addresses the risks or system limitations associated with shortfalls in meeting mission needs, operational requirements, and safety requirements. Identification and assessment of any new safety hazards should also be provided. 

The OT Final Test Report is used to support an ISD or other deployment decision and must include a very clear statement regarding whether or not the system is Operationally Ready (effective and suitable).  The following examples illustrate such clear unambiguous language. 

Example 1: “The OT test team found the system not operationally ready because COI 3.0 was not answered satisfactorily, and CPR 5.0 was not successfully met, due to Issue xx which was rated Priority 1.” 

Example 2: “The OT test team found the system operationally ready because all COIs were satisfactory answered and CPRs were successfully met.  All issues found during testing were rated Priority 3 or below.” 

For large or high-risk test programs, the OT Test Director must conduct an OT Final Test Report Briefing to the ITT prior to delivering a draft Final Test Report for review. Additionally, the OT Test Director must ensure that the report has been peer-reviewed (see Section 1.9) prior to submission to management for review/endorsement/approval. The OT Final Test Report requires: 

1. Endorsement of the TSB, the T&E First Line Supervisor, and the respective T&E Senior Manager 

2. Signature of the OT Test Director 

3. Approval of the Director of Test Service Organization (or equivalent) 

The Director of Test Service Organization (or equivalent) approves the final version of the report based on earlier endorsements and approvals, and an OT Final Test Report Outbrief by the OT Test Director. 

The approved OT Final Test Report should be delivered within 60 business days from the completion of the test.  The approved OT Final Test Report is delivered to the TSB and the Program Manager.  The AMS requires the OT Final Test Report as part of the entrance criteria to the ISD.  The Director of Test Service Organization (or equivalent) 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-19 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

provides an OT Final Test Report Outbrief, as required, to the Assistant Administrator for Next Generation (NextGen) Air Transportation System, ANG -1, prior to the ISD milestone. 

Refer to Appendix E, Figure E-14, for the complete OT Final Test Report review, endorsement, and/or approval cycle. 

NOTE:  Refer to the V&V Repository for the OT Final Test Report, the OT Final Report Director’s Briefing Template, and samples. 

## **7.7 TRANSITION TO IN-SERVICE M ANAGEMENT** 

Test support is often required during the transitional period from OT to ISM to correct PTRs and other performance issues.  This test support is handled through service-level agreements between the DT/OT test teams and the ISM organization, or via a Project Scope Agreement with the PMO. 

## **7.8 FIELD F AMILIARIZATION SUPPORT** 

The main focus of FF is to familiarize field users with the new system, service, or capability.  It is not intended to provide formal verification and validation of the system, service, or capability.  This section only addresses processes to be followed by the T&E organization in support of FF.  Site FF is the responsibility of the facility personnel at each operational site and is the final activity to achieve facility IOC.  If requested by the PMO, the test organization provides support services for FF, including the development of plans, procedures, and briefing materials.  The guidance for FF conduct and planning is contained in the AMS T&E guidance document.  FF is a formal T&E activity. 

### **7.8.1 FIELD FAMILIARIZATION SUPPORT PLANNING** 

FF support usually consists of running test procedures that go beyond the usual site system verification and baseline testing.  The general approach is to conduct activities that allows the facility to gain confidence in the system and attain a higher level of handson familiarization.  The level and type of FF support is determined through coordination with the PMO, AT and Tech Ops site representatives to identify specific areas that require T&E capabilities.  Once the test organization’s role is determined, an FF Support Plan is developed that details the activities.  The FF Support Plan should clearly identify who generates and maintains the FF artifacts such as daily status reports and site final report. The plan must be provided to the TSB for their review and comment prior to final delivery. FF support consists of the following activities: 

1. Conduct initial planning meetings with operational and in-service management organizations to gain insight into operational concerns 

2. Meet with field sites to gain the desired type of faults for system familiarization 

3. Create an FF support team from assessing familiarization needs for the site and define roles for the FF support team 

4. Develop a support schedule and status tracking matrix 

5. Develop a resource allocation matrix 

6. Assess engineering resources required for test case development and support 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-20 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

7. Define FF support team training requirements 

8. Define FF test tools as required 

9. Develop and document test case procedures 

10. Conduct dry run test cases 

11. Develop schedules to track all FF-related activities 

12. Distribute the FF Support Plan to the PMO and the site(s) 

Refer to Appendix E, Figure E-15, for the complete Field Familiarization Support Plan review, endorsement, and/or approval cycle. 

NOTE:  Refer to the V&V Repository for the FF Support Plan template. 

### **7.8.2 FIELD FAMILIARIZATION SUPPORT PREPARATION** 

Test procedures are developed, and a dry run is conducted based on the process specified in the FF Support Plan.  These procedures are packaged and delivered to the Site Test Directors so that they may select specific test procedures for execution. 

FF support preparation is performed in the following sequence: 

1. Schedule resources and tools for test case development and dry runs 

2. Conduct test case dry runs on new system releases 

3. Conduct site preparation meetings/briefings 30 business days prior to the start of site FF 

4. Participate in training activities on system overview and architecture, computerbased instruction, test training, operational evaluations, etc. 

5. Develop and maintain an FF database as central repository for FF-related documents and data storage 

NOTE: Refer to the V&V Repository for FF Test Procedures and FF Test Case Format samples. 

### **7.8.3 FIELD FAMILIARIZATION SUPPORT CONDUCT** 

The following standard processes must be considered for the conduct of FF support activities: 

1. Ensure required test equipment, tools, and documentation are delivered to the site 

2. Conduct a site kick-off meeting at the start of FF site activities 

3. Conduct Pre-Test Briefings prior to each individual test 

4. Conduct FF testing 

5. Provide support to updating site-specific procedures, handbooks, and guidance documents (as required) 

6. Conduct Post-Test Reviews at the completion of each individual test 

7. Conduct a wrap-up meeting at the completion of FF site activities 

8. Perform regression testing on issues identified by the site (as required) 

9. Assist in PTR verification and analysis (as required) 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-21 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

10. Generate Test Status Report(s) and submit them daily to the Program Manager, Test Directors, and Site Test Director 

### **7.8.4 FIELD FAMILIARIZATION REPORTING** 

The site FF support team tracks all site issues surfaced during the test activities and maintains these issues in a database.  A final report for each site is generated to document the activities and summarize any issues.  Reports and database information are distributed to the PMO, TSB, and site representatives. 

NOTE: Refer to the V&V Repository for FF Report and FF Status Tracking Matrix samples. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

7-22 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

## **8 TEST AND EVALUATION SUPPORT TO IN-SERVICE MANAGEMENT** 

T&E support to ISM consists of various T&E activities performed by test teams in support of program maintenance and upgrade activities under the responsibility of the secondlevel maintenance organizations.  These T&E activities can be categorized according to the following types of ISM program activities: 

1. Major program upgrade support 

2. Minor program upgrade support 

3. Program maintenance support 

The following sections define each of these ISM program activities and describe the T&E support provided by the  test team if tasked by the PMO or the second-level maintenance organization to provide T&E services.  Additionally, it should be noted that the specific level of T&E service support may differ from program to program and tailoring may be required. 

## **8.1 M AJOR PROGRAM UPGRADE SUPPORT** 

Major program upgrades to operational systems or services are defined as those upgrades that require new or modified program requirements, a new or modified vendor contract, and   corresponding DT and OT test programs to verify and validate the upgrade prior to its implementation.  For these types of upgrades, the test team will be responsible for developing a TEMP, DT oversight, and OT planning, conduct, and reporting.  As such, the applicable T&E processes, methods, and standards defined in Sections 4 through 7 and 9 of this Handbook will be followed, to include the use of the Test Planning, DT and OT Process Conformance Checklists contained in Appendices A through C.  If there is an ISD identified, then the program must be considered as major, but not all major ISM programs have an ISD. 

NOTE:  Refer to the V&V Repository for the ISM TEMP, the OT Test Plan, and the OT Final Test Report templates. 

## **8.2 M INOR PROGRAM UPGRADE SUPPORT** 

Minor program upgrades to operational systems or services are defined as those upgrades resulting from PTR fixes or NCPs/case files for which there is no need for a new or modified vendor contract.  In these instances, the second-level maintenance organization or the vendor implements and test the upgrade, while the test team will only be responsible for OT planning, conduct, and reporting.  As such, in the same manner as the T&E support provided to major program upgrades as defined in Section 8.1, the applicable T&E processes, methods, and standards defined in Sections 7 and 9 of this Handbook will be followed. 

## **8.3 SPECIAL SUPPORT ACTIVITIES** 

In addition to the more formalized T&E support for major and minor program upgrades, the test team may be requested to provide T&E support not defined in this Handbook, as SSAs, for program maintenance activities being performed by the second-level 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

8-1 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

maintenance organization.  For these activities, the test team provides T&E services in a supporting role to the second-level maintenance organization.  As such, the T&E processes, methods, and standards established by the second-level maintenance organization will be followed in lieu of those prescribed by this Handbook.  However, for all T&E activities performed in support of ISM program maintenance, it is recommended that the test team applies, where possible, the fundamental practices for quality T&E as defined in Section 1.5. 

NOTE:  Refer to the V&V Repository for the SSAs PDD. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

8-2 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

## **9 TEST PREPARATION AND DEPLOYMENT DECISION SUPPORT** 

This section contains test preparation and deployment decision support processes that cross AMS lifecycle phases. 

## **9.1 TEST C APABILITY ACCREDITATION** 

Accreditation is the official determination that a model or simulation (or other test capability) is acceptable for a specific purpose.  Accreditation is required for every test capability that is being used to verify and validate requirements.  DT and OT Test Directors are responsible for identifying all DT and OT accreditation requirements, including proposed accreditation methods, in the TEMP.  These proposed accreditation requirements and methods will be approved in conjunction with the overall TEMP approval process (see Section 5.2). 

When test capability accreditation is required, accreditation plans and procedures must be detailed in a standalone Accreditation Plan, or in DT/OT test plans.  Results from accreditation testing must be documented in an Accreditation Record prior to the start of system, service, or capability testing. 

The approval process for the Accreditation Plan and Record is detailed in Appendix E. Figure 9-1 depicts the logical flow of the accreditation process.  The following sections provide additional information on the process. 

### **9.1.1 ACCREDITATION DEFINITIONS** 

The following terms and definitions are essential to understanding the Accreditation 

Process: 

1. Accreditation:  The formal certification that a test capability is acceptable for a specific application 

2. Test Capability:  Assets that are used in conjunction with the system/service under test or a representation of the system/service under test to generate data to address test measures.  [Test capabilities include testbeds, simulated environments (including files and interfaces), instrumentation and test tools (including data collection and analysis), and modeling capabilities] 

3. Accreditation Verification:  The formal process of determining that a test capability accurately represents the contractor's conceptual description and specifications 

4. Accreditation Validation:  The formal process of determining the degree to which a test capability provides an accurate and complete representation of the test capability’s intended purpose (e.g., real world system loading, capacity loading, emulation of operational environments, etc.) 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

9-1 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



**Figure 9-1.  Test Capability Accreditation Process** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

9-2 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **9.1.2 ACCREDITATION TESTING** 

Accreditation tests must ensure that the test capability achieves its intended purpose in supporting a T&E activity.  The level of accreditation verification and validation to be performed will be driven by the required test capability performance, functionality, and fidelity necessary to support fulfillment of the objectives of a test activity or an individual test case.  Examples of the test capabilities typically accredited, and types of accreditation are as follows: 

1. Testbeds – A testbed is a stand-alone or distributed environment created for testing purposes.  It may consist of a combination of specialized hardware, software, real or simulated environmental conditions.  Verification of the testbed includes ensuring that interfaces and components of the testbed function as designed and are free of defects.  Validation of the testbed involves ensuring that the environment and associated stimulus provide sufficient representation of the conditions required for the test objectives. 

2. Simulated environments include the following: 

   - a. Simulation Files (Scenarios/Scripts) – Simulation files or software scenarios are used to automate procedures, system load, specific complex situations, etc.  Verification of simulations ensures that the simulation performs as scripted and is reliable, repeatable, and free of defects.  Simulations are validated to ensure that they are realistic, comprehensive for the operational environment being simulated, and sufficient for the intended use. 

   - b. Simulated Interfaces – One or more interfaces are typically simulated when live data or other system interfaces are not available or practical. Verification of the simulated interface includes ensuring that it conforms to the Interface Control Document (or other interface requirements). Validation of the interface should ensure that all the appropriate messages, data, timing, and content are sufficiently emulated by the simulated interface. 

3. Instrumentation and Test Tools – Instrumentation and test tools are equipment items that include data collection and analysis tools, drivers, oscilloscopes, meters, analyzers, and probes.  Instrumentation and test tools may be COTS or developmental items.  Verification of the instrumentation and test tools ensures that they are performing as designed.  Validation of the instrumentation and test tools ensure that they are meeting the needs for the test.  Calibration may be performed to accomplish the accreditation.  COTS items may use the vendor artifacts and documentation for verification and validation. 

4. Modeling – Modeling is a physical, mathematical, or otherwise logical representation of a system, entity, or process.  Typically, modeling is used to test and evaluate future real-world capabilities without actually implementing them.  Verification of a model ensures that the model is fully functional, reliable, and accurately processing/reporting data.  Validation of a model focuses on ensuring that the model encompasses all relevant variables, is representative of intended environments, and sufficiently emulates the real-world capabilities that are identified in the test case. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

9-3 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **9.1.3 ACCREDITATION PROCESS** 

Test capabilities that require accreditation are identified during test design and are documented in the TEMP and test plans.  Accreditation Plans are developed (the Accreditation Procedures are a part of the Accreditation Plan rather than a separate document) as other test plans are being developed.  This provides the opportunity to explore alternative test approaches or modifications to the overall test process. Additionally, Accreditation Plans may be either standalone documents referenced in the test plans, or they may be included as part of the test plans.  The prime contractor (for DT activities) or the OT Test Director (for OT activities) is responsible for the development of the respective Accreditation Plan(s).  For DT, the DT test team conducts an early informal review of the plan(s) to ensure that they are in agreement with the contractor’s accreditation strategy and to provide any other initial comments.  Subsequently, the DT test team and the TSB review the revised plan(s) for technical sufficiency prior to the DT Test Director’s recommendation of approval by the CO.  For OT, the TSB endorses the Accreditation Plan(s) prior to final approval by the respective T&E Senior Manager. 

The FAA witnesses all test capability accreditation activities conducted by the prime contractor for DT and conducts the test capability accreditation activities for OT.  The accreditation analysis and results from these activities should be completed and approved prior to the commencement of the simulation effort, requiring the use of the test capability(ies). 

Results of the accreditation process are appended to the Accreditation Plan, which then become the Accreditation Record.  This record provides information on the risks associated with using the test capability, and recommendations on whether to proceed. For DT, the prime contractor prepares the Accreditation Record, and the DT test team conducts an early informal review of the record to ensure that they are in agreement with the contractor’s accreditation results and to provide any other initial comments. Subsequently, the DT test team and the TSB review the revised record prior to the DT Test Director’s approval recommendation to the CO and COR.  For OT, the OT Test Director prepares the Accreditation Record, the TSB reviews the record, and the T&E First-Line Supervisor endorses the record prior to final approval by the respective T&E Senior Manager or appointed representative. 

CM of test capabilities and archiving of all Accreditation Records is the responsibility of the prime contractor (for DT) or the OT Test Director (for OT). 

Refer to Appendix E, Figure E-9, for the complete DT Accreditation Record review, endorsement and/or approval cycle, and Figure E-16 for the complete OT Accreditation Record review, endorsement and/or approval cycle.  For DT and OT Accreditation plans, refer to Figures E-6 and E-10, OT Test Plans Review, Endorsement and/or Approval Cycle, which also applies to Accreditation Plans. 

### **9.1.4 ACCREDITATION GUIDANCE** 

Accreditation activities for new test capabilities generally consist of the following steps: 

1. Describe the function and features of the test capability being accredited as well as the inputs and outputs. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

9-4 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

2. Determine the intended use of the capability during testing. 

3. Determine the test capability accreditation criteria.  (This may include documents such as the user manual, specification and design document or may include subject matter expertise.) 

4. Using known inputs, perform accreditation testing to exercise the capability, verifying and validating the functions and features according to the intended use for the test. 

5. Compare the outputs of the accreditation testing against the accreditation criteria for the test capability and document the results. 

In lieu of accreditation, an approved documented artifact (e.g., a prior Accreditation Record, test logs, as-run authenticated test procedures, test data, etc.) is required for established capabilities used in past testing or previously accredited capabilities. However, if the test capability or environment has changed, then the test capability requires re-accreditation in the new test environment. 

The Accreditation Plan must describe the methods used to verify and validate the test capability and must also identify any supporting artifacts.  Once a test capability has been accredited, it must be placed under CM in accordance with the CM Plan and monitored to ensure that the accreditation standards are maintained.  The Accreditation Plan must document the conditions under which the test capability requires a re-accreditation process.  Examples of such conditions include changes to the test capability algorithms, inputs, or outputs. 

NOTE:  Refer to the V&V Repository for the Test Capability Accreditation template and the CM PDD. 

## **9.2 IN-SERVICE REVIEW CHECKLIST AND DEPLOYMENT DECISION PLANNING** 

Deployment planning is part of a continuous In-Service Review (ISR) process that begins early in the lifecycle management process, usually during the development of requirements.  A tailored ISR Checklist is used to ensure that all deployment and implementation issues are resolved prior to the ISD.  This checklist will be used to: integrate checklist issues with other emerging issues (such as PTRs from program tests and evaluation); develop action plans for resolution of checklist and other issues; and document decisions and the results of issue resolution and mitigation. 

The service organization is responsible for developing, maintaining, and facilitating the ISR Checklist.  T&E support for the ISR checklist is provided by test POCs and FAA SMEs, who tailor checklist items, provide action plans and status, and approve the Test Section of the ISR Checklist from the AMS Investment Analysis phase until the ISD.  The test POC is the individual that provides a response to the checklist items.  An FAA SME is a representative from the office to be contacted to provide expertise and additional information about a checklist item's intent and concurs with the closure of each checklist item.  The test POC may also be the DT or OT Test Director, or an assigned test lead. The FAA SME for test is the service organization test lead, which may be the DT or OT Test Director, or both. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

9-5 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

## **9.3 TEST NAS CHANGE PROPOSALS** 

Test NCPs are typically required for temporary configuration changes to existing baselined systems, including the installation of prototypes. The current version of FAA Order 1800.66, _Configuration Management Policy_ , defines the Configuration Control Board approval process for test NCPs.  FAA Order 6032.1, _NAS Modification Program,_ provides additional guidance on test NCPs.  The current version of NCP approval process is lengthy; therefore, sufficient lead-time and preparation is necessary.  In addition to the information referenced on the NCP, the case file documentation for a test modification must include the following: 

1. The general method for accomplishing the modification, including: 

   - a. A description of system or system modification to be tested 

   - b. A description of connections and interfacing systems 

   - c. Descriptive diagrams as required 

   - d. An installation plan 

2. The applicable _PRD_ or requirement statement(s) 

3. A test plan and specific test procedures, including: 

   - a. Test objectives 

   - b. Evaluation plan 

   - c. Test steps 

   - d. Expected or desired results 

   - e. Exit criteria 

   - f. Anticipated duration of test 

4. A description of removal plan 

5. An estimate of associated costs 

6. A complete schedule of all planned tasks and activities 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

9-6 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

## **Appendix A.  Acronyms and Glossary** 

## **Acronyms** 

AMS Acquisition Management System APB Acquisition Program Baseline 

- AT Air Traffic 

- ATC Air Traffic Control 

- CDR Critical Design Review 

- CDRL Contract Data Requirements List 

- CI Configuration Item 

- CM Configuration Management 

- CMMI Capability Maturity Model Integration 

- CMTP Contractor Master Test Plan 

- CO Contracting Officer 

- COI Critical Operational Issue 

- ConOps Concept of Operations 

- COR Contracting Officer's Representative 

- COTS Commercial Off-the-Shelf 

- CPR Critical Performance Requirement 

- CRD Concept and Requirements Definition 

- CSCI Computer Software Configuration Item 

- DID Data Item Description 

- DMC Document Management and Control 

- DR Discrepancy Report 

- DR&A Data Reduction and Analysis 

- DT Development Test(ing) 

- ECP Engineering Change Proposal 

- EMC Electromagnetic Compatibility 

- EMI Electromagnetic Interference 

- FAA Federal Aviation Administration FAT Factory Acceptance Test(ing) FCA Functional Configuration Audit 

- FF Field Familiarization 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

A-1 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

- FIA Final Investment Analysis FID Final Investment Decision fPRD final Program Requirements Document FQT Functional Qualification Test(ing) fTEMP final TEMP GA Government Acceptance GFE Government Furnished Equipment GFI Government Furnished Information GFP Government Furnished Property HB Handbook HF Human Factors I&I Installation and Integration IIA Initial Investment Analysis IA Investment Analysis IAR Interim Assessment Report IARD Investment Analysis Readiness Decision IBR Integrated Baseline Review IID Initial Investment Decision IMS Integrated Master Schedule iTEMP initial TEMP IOA Independent Operational Assessment IOC Initial Operational Capability iPRD initial Program Requirements Document ISCM Information System Continuous Monitoring ISD In-Service Decision ISM In-Service Management ISO International Organization for Standardization ISPD Implementation Strategy and Planning Document ISR In-Service Review ITDP Integration and Test Development Plan ITT Integrated Test Team JRC Joint Resources Council KSN Knowledge Services Network 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

A-2 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

- MOE Measure of Effectiveness MOP Measure of Performance MOS Measure of Suitability NAS National Airspace System NCP NAS Change Proposal NDI Non-Developmental Item NextGen Next Generation Air Transportation System OCD Operational Capability Demonstration OCT Operational Capability Test OGB Operations Governance Board OT Operational Test(ing) PAT Production Acceptance Test(ing) PBSA Performance-Based Service Acquisition PCA Physical Configuration Audit PDD Process Description Document PDR Preliminary Design Review PMO Program Management Office POC Point of Contact pPRD preliminary Program Requirements Document PRD Program Requirements Document pTEMP preliminary TEMP PTR Program Trouble Report PWS Performance Work Statement QA Quality Assurance QMS Quality Management System QRO Quality Reliability Officer RMA Reliability, Maintainability, and Availability SASP Service Analysis and Strategic Planning SAT Site Acceptance Testing(ing) SEM FAA Systems Engineering Manual SI Solution Implementation SIR Screening Information Request SME Subject Matter Expert 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

A-3 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

- SOO Statement of Objectives SoS System of Systems SOW Statement of Work SSA Special Support Activities T&E Test and Evaluation TBD To Be Determined Tech Ops Technical Operations TEMP Test and Evaluation Master Plan TRR Test Readiness Review TRRG Test Roles and Responsibilities Guide TSB Test Standards Board TWG Test Working Group V&V Verification and Validation VRTM Verification Requirements Traceability Matrix WBS Work Breakdown Structure WJHTC William J. Hughes Technical Center 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

A-4 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

## **Glossary** 

### **TERM** 

### **DEFINITION** 

|Accreditation|Formal certification that a test capability is acceptable<br>for a specific application.|
|---|---|
|Adaptation|Unique site-dependent data/functions required by the<br>operational program to provide the flexible capability<br>necessary for individual site performance determined<br>during implementation.|
|Blue-line changes|Changes made to test procedures during formal test<br>conduct.|
|Critical Operational Issue<br>(COI)|A key operational effectiveness or operational suitability<br>issue that must be examined during operational test to<br>determine the system’s capability to perform its mission.|
|COI status is assessed as:|Yes – COI/CPR fully met under all test cases (No<br>significant issues impacting COI/CPR)<br>Ltd (Limited) – COI/CPR could not be met under all test<br>cases/conditions; ability to meet COI/CPR is limited (one<br>or more significant issues impacting COI/CPR)<br>No – COI/CPR not met (serious shortfalls affecting<br>COI/CPR)|
|Contractor|Private company with responsibility for designing and<br>producing a system, service, or capability.|
|Critical Performance<br>Requirements|Program requirements identified in the Program<br>Requirements Document as essential to the successful<br>performance of the system, service, or capability in<br>meeting the program’s mission needs.  Special<br>emphasis is placed upon the evaluation of Critical<br>Performance Requirements to ensure the timely<br>assessment of system, service, or capability capabilities<br>and to promote program success.|
|Development Testing|Primary objective is to demonstrate that all specified<br>technical and performance requirements for a system,<br>service, or capability have been met.|
|Dry Run|Complete end-to-end execution of test procedures using<br>formal test configurations and accredited scenarios,<br>simulations, and/or test tools (see Section 6.3.1).|



VVSPT-A2-PDD-013 v5.0 

12/18/2020 

A-5 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **TERM** 

### **DEFINITION** 

Endorsement A recommendation for approval or disapproval of a work product with supporting comments.  Endorsement can be accomplished via email, endorsement letter, or a written or digital signature on the signature page of the document by the endorser(s). 

Enterprise Level National Airspace System Requirements that may Capabilities involve more than one system to implement.  Changes may be required in multiple Federal Aviation Administration systems, Air Traffic Control procedures and avionics systems developed by industry. Verification and Validation of Enterprise Level capabilities may require multiple systems to reach specified states of development and may be performed by a dedicated Enterprise Level Capability Test Team. Field Familiarization (FF) Tests conducted at each site by Air Traffic and Technical Operations personnel to verify that the site is ready to switch over to the new system. Initial Operational The declaration by site personnel that the system is Capability ready for conditional operational use in the NAS and denotes the end of field familiarization at that site. Measure of Effectiveness First-level, qualitative decomposition of an operational (MOE) effectiveness component associated with a COI. Measure of Performance Quantitative values that characterize MOEs or MOSs. (MOP) These values are measurable by a test process. Measure of Suitability First-level, qualitative decomposition of an operational (MOS) suitability component associated with a COI. Operational Effectiveness The degree to which a system, service, or capability accomplishes its mission when used by representative personnel in the expected operational environment. Operational Readiness Operational readiness encompasses operational effectiveness and operational suitability. [AMS 2.6.1] Later test and evaluation examines performance and operational readiness (suitability and effectiveness) in support of decision-makers at the production, deployment, and in-service decisions.  [AMS 4.4.2] 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

A-6 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

|**TERM**|**DEFINITION**|
|---|---|
|Operational Readiness<br>Date|Operational readiness is attained when site operational<br>personnel are satisfied the solution can support full and<br>sustained air transportation operations.  The milestone<br>occurs after completion of the joint acceptance and<br>inspection process when the site official signs the facility<br>log designating the new solution as the primary means<br>for air transportation operations.|
|Operational Suitability|The degree to which a system, service, or capability<br>intended for field use satisfies its availability,<br>compatibility, transportability, interoperability, reliability<br>maintainability, safety, Human factors, logistics<br>supportability, documentation, personnel, and training<br>requirements.|
|Operational Testing|Primary objective is to examine performance and<br>determine operational readiness (effectiveness and<br>suitability) of a new or modified system for use in the<br>NAS and that the NAS infrastructure is ready to accept<br>the system.|
|Prime Contractor|The private company or organization that has an<br>established contract with the FAA to provide a system,<br>service, or capability.|
|Procedure|Subordinate to a process.  A set of activities or steps<br>taken to achieve a given purpose.  Any specific<br>combination of machines, tools, methods, materials,<br>and/or people employed to develop a work Product.<br>Could be used by multiple persons in one group either<br>separately, interleaved, recursively, or concurrently.<br>Some activities transform inputs into outputs needed for<br>other activities.|
|Red-line Changes|Changes made to test procedures during dry run<br>conduct.|
|Scrum|An Agile development methodology emphasizing<br>functional software, flexibility to change along with<br>emerging business realities, and exercising<br>communication and collaboration.|
|Subcontractor|A private company or organization whose contract is not<br>directly with the FAA but rather with a prime contractor.|



VVSPT-A2-PDD-013 v5.0 

12/18/2020 

A-7 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **TERM** 

### **DEFINITION** 

|Subsystem Specification|A contractor-produced document that decomposes<br>requirements from the government-furnished system<br>specification into lower-level specifications that apply to<br>components of the system to be developed.  The<br>subsystem specification documents must show<br>traceability to the system specification.|
|---|---|
|System Specification|The specification describes the physical, functional, or<br>performance requirements of a system, service, or<br>capability to be obtained from a contractor and contains<br>verifiable criteria for determining whether or not the<br>requirements are met. The system specification must<br>show traceability to the Program Requirement<br>Document.|
|Test Activity|A category of test hierarchy between Test Phase and<br>Test Case Group, with an identifiable title and reporting<br>requirements.|
|Testbed|A stand-alone or distributed environment created for<br>testing purposes.  It may consist of a combination of<br>specialized hardware, software, real or simulated<br>environmental conditions, and may be a component of a<br>larger test environment.|
|Test Capability|A resource or method used to verify or validate<br>requirements.  This may include testbed(s), simulations,<br>simulated interfaces, modeling, scripts, test equipment,<br>etc.  Test capabilities need to be accredited before they<br>are used in test activities.|
|Test Case|A subset of test procedures that specify a) one or more<br>system, service, or capability requirements to be verified<br>and validated; b) the resources required to execute the<br>test case; c) the specific steps that must be taken to<br>perform the test case.  Identified by paragraph number<br>in a Test Procedures document.|
|Test Case Group|A collection of test cases linked by a common purpose,<br>such as to verify a specific set of system, service, or<br>capability requirements.  A group may consist of a<br>similar set of test cases, performed under a range of<br>differing conditions.  Identified by paragraph number in a<br>Test Procedures document.|



VVSPT-A2-PDD-013 v5.0 

12/18/2020 

A-8 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **TERM** 

### **DEFINITION** 

|Test Environment|The hardware, software, interface, and support<br>configuration necessary to meet the test objectives (e.g.,<br>data, testbeds, simulators, test instrumentation, test<br>tools, etc.).|
|---|---|
|Test Event|The conduct of a Test Activity, or portion of a Test<br>Activity, where data is collected for the record.|
|Test Methods|Analysis (A):  Verification that is accomplished through<br>use of techniques (including but not limited to charts,<br>graphs, diagrams, mathematical models) to prove that<br>an item meets specified requirements.|
||Demonstration (D):  Verification that is accomplished by<br>operation, adjustment, or reconfiguration of items<br>performing their designed functions under specific<br>scenarios.<br>Inspection (I):  Verification that is accomplished by a<br>visual examination of the item, reviewing descriptive<br>documentation, and comparing the appropriate<br>characteristics with predetermined standards to<br>determine conformance to requirements without the use<br>of laboratory equipment or procedures.<br>Test (T):  Verification that is accomplished, with or<br>without instrumentation, through systematic exercising<br>of the application item under appropriate conditions with<br>the collection, analysis, and evaluation of quantitative<br>data.|
|Test Phase|Highest level subdivision in a test program (e.g., Test<br>and Evaluation Program Planning, Development Test,<br>Operational Test).|
|Test processes|A general term for methods that may be used or<br>procedures which may be followed to conduct test.|
|Test Procedure|A guiding document that details the steps to be taken.|
|Test Program|All of the identified activities that are required to perform<br>Verification and Validation of a National Airspace<br>System or a National Airspace System Enterprise Level<br>Capability.|



VVSPT-A2-PDD-013 v5.0 

12/18/2020 

A-9 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **TERM** 

### **DEFINITION** 

Test Scenario Simulations or scripted input developed to exercise combinations of operational factors that influence system performance. 

Test Steps A subset of a test case that directs test personnel to perform actions, and document responses. Test Tools Support equipment (hardware/software) that allows for the verification and validation of capabilities, functions, fixes and performance. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

A-10 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

## **Appendix B.  Test Planning Process Conformance Checklist** 

(See T&E Handbook, Section 1.7, T&E Standards Conformance, regarding checklists.) 



<!-- Start of picture text -->
Test Program:<br>T&E Team(s):<br>T&E First Line Supervisor:<br>DT Test Director:<br>OT Test Director:<br>Version  1 : ____ Initial  ____ Revision  ____ Checklist Complete<br>Review Signatures: Date:<br>_____________________________  ____________<br>T&E First Line Supervisor<br>_______________________________  ____________<br>DT Test Director<br>______________________________  ____________<br>OT Test Director<br>_______________________________  ____________<br>TSB Representative<br><!-- End of picture text -->

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

B-1 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **A P P E N D I X B. T E S T P L AN N I N G P R O C E S S C ON F O R M AN C E C H E C K L I S T** 

### **Test Program Name: Version Date** 

**2** 

|**Action**<br>**ID**|**Action**|**TSB Role**|**T&E HB**<br>**Ref. Sec.**|**Tailoring Change(s)**<br>**w/ Justification (if used)**<sup>**3**</sup>|**Target**<br>**Date**<sup>**4**</sup>|**Completion**<br>**Date**<sup>**5**</sup>|**Status/**<br>**Comments/**<br>**Artifacts**<sup>**6**</sup>|
|---|---|---|---|---|---|---|---|
|TP1|Participate in early system, service, or<br>capability engineering and implementation<br>reviews|Monitor|5.1 1.|||||
|TP2|Provide test strategy briefings to the<br>Program Office|Monitor|5.1.7.b.|||||
|TP3|Review the PRD for:<br>- Requirement completeness<br>- Definition of NAS operational<br>interfaces<br>- Requirement testability<br>- COI completeness and testability<br>- Identification of CPRs<br>- Test program structure|Monitor|5.1. 2.<br>5.1. 3.<br>5.1. 4.<br>5.1. 5.<br>5.1. 6.<br>5.1. 7.|||||
|TP4|Write the T&E section of the PRD, include<br>essential FAA and contractor tests, and<br>follow the review and approval cycle for<br>submission into the PRD|Monitor|5.1.7.c.<br>Fig. E-1|||||



VVSPT-A2-PDD-013 v5.0 

12/18/2020 

B-2 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **A P P E N D I X B. T E S T P L AN N I N G P R O C E S S C ON F O R M AN C E C H E C K L I S T** 

### **Test Program Name: Version Date** 

|**Action**<br>**ID**|**Action**|**TSB Role**|**2: **<br>**T&E HB**<br>**Ref. Sec.**|**Tailoring Change(s)**<br>**w/ Justification (if used)**<sup>**3**</sup>|**Target**<br>**Date**<sup>**4**</sup>|**Completion**<br>**Date**<sup>**5**</sup>|**Status/**<br>**Comments/**<br>**Artifacts**<sup>**6**</sup>|
|---|---|---|---|---|---|---|---|
|TP5|Form (with the Program Office) and<br>participate in the ITT, beginning with ISPD<br>and TEMP planning|Monitor|5.3,<br>5.2,<br>7.3.2|||||
|TP6|Write the T&E section of the ISPD, include<br>test strategy, test schedule and test<br>resource requirements, and follow the<br>review and approval cycle for submission<br>into the ISPD|Monitor|5.3,<br>Fig. E-2|||||
|TP7|Review, witness and document any early<br>evaluations (e.g., prototype tests, user<br>demos, OCDs, OCTs)|Monitor|4|||||
|TP8|Write the preliminary, initial and final TEMP,<br>utilizing the Test Design Process below:<br>- Identify and assess requirements<br>- Identify and decompose COIs into MOEs,<br>MOSs and MOPs<br>- Identify CPRs<br>- Define DT and OT test activities<br>- Develop the TEMP VRTM<br>- Identify Test Capability Requirements<br>- Define test schedule<br>- Update the APB (if required)<br>- Document the test design in the TEMP|Review|5.2.3<br>5.2.3.1<br>5.2.3.2<br>5.2.3.3<br>5.2.3.4<br>5.2.3.5<br>5.2.3.6<br>5.2.3.7<br>5.2.3.8<br>5.2.3.9|||||



VVSPT-A2-PDD-013 v5.0 

12/18/2020 

B-3 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **A P P E N D I X B. T E S T P L AN N I N G P R O C E S S C ON F O R M AN C E C H E C K L I S T** 

### **Test Program Name: Version Date** 

||||**2: **|||||
|---|---|---|---|---|---|---|---|
|**Action**<br>**ID**|**Action**|**TSB Role**|**T&E HB**<br>**Ref. Sec.**|**Tailoring Change(s)**<br>**w/ Justification (if used)**<sup>**3**</sup>|**Target**<br>**Date**<sup>**4**</sup>|**Completion**<br>**Date**<sup>**5**</sup>|**Status/**<br>**Comments/**<br>**Artifacts**<sup>**6**</sup>|
|TP9|Provide a briefing to the Program Manager<br>for concurrence on the T&E approach prior<br>to submitting the preliminary, initial and final<br>TEMP for Program Manager review and<br>approval|Monitor|5.2|||||
|TP10|Tailor and approve the Test Section of the<br>ISR Checklist|Monitor|9.2|||||
|TP11|Identify if there is a need for test NCPs in<br>the TEMP.  If so, provide the required<br>NCP/case file documentation in accordance<br>with the current versions of FAA Orders<br>1800.66 and 6032.1|Monitor|9.3|||||



VVSPT-A2-PDD-013 v5.0 

12/18/2020 

B-4 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **A P P E N D I X B. T E S T P L AN N I N G P R O C E S S C ON F O R M AN C E C H E C K L I S T** 

### **Test Program Name:** 

### **Version Date** 

|**Action**<br>**ID**|**Action**|**TSB Role**|**2: **<br>**T&E HB**<br>**Ref. Sec.**|**Tailoring Change(s)**<br>**w/ Justification (if used)**<sup>**3**</sup>|**Target**<br>**Date**<sup>**4**</sup>|**Completion**<br>**Date**<sup>**5**</sup>|**Status/**<br>**Comments/**<br>**Artifacts**<sup>**6**</sup>|
|---|---|---|---|---|---|---|---|
|TP12|If required, develop test program<br>accreditation requirements (prime contractor<br>for DT, OT Test Director for OT) and<br>document in the TEMP:<br>- For DT, review the prime contractor’s<br>Accreditation Plan(s) and follow the DT<br>Accreditation Record review and approval<br>cycle prior to providing a final approval<br>recommendation to the CO; and for OT,<br>develop Accreditation Plan(s) and follow the<br>OT Accreditation Record review and<br>approval cycle<br>- Witness prime contractor accreditation<br>activities for DT, and/or conduct<br>accreditation activities for OT. Provide<br>analysis and results for approval no later<br>than 30 business days prior to testing<br>- For DT, review the prime contractor’s<br>Accreditation Plan and follow the DT<br>Accreditation Record review and approval<br>cycle prior to providing a final approval<br>recommendation to the CO.  For OT, write<br>an Accreditation Plan and follow the OT<br>Accreditation Record review and approval<br>cycle<br>- Archive the Accreditation Plans(s),<br>analysis, and Accreditation Record(s)|Review|9.1,<br>9.1.3,<br>Fig. E-9,<br>Fig. E-16|||||



VVSPT-A2-PDD-013 v5.0 

12/18/2020 

B-5 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **A P P E N D I X B. T E S T P L AN N I N G P R O C E S S C ON F O R M AN C E C H E C K L I S T** 

### **Test Program Name: Version Date** 

**2** 

|**Action**<br>**ID**|**Action**|**TSB Role**|**T&E HB**<br>**Ref. Sec.**|**Tailoring Change(s)**<br>**w/ Justification (if used)**<sup>**3**</sup>|**Target**<br>**Date**<sup>**4**</sup>|**Completion**<br>**Date**<sup>**5**</sup>|**Status/**<br>**Comments/**<br>**Artifacts**<sup>**6**</sup>|
|---|---|---|---|---|---|---|---|
|TP13|Follow the review and approval cycle for all<br>versions of the TEMP that require approval<br>signatures|Review|5.2,<br>Fig. E-3|||||
|TP14|Update the TEMP at major milestones when<br>the ISPD or the program baseline has been<br>significantly modified, or when the program<br>is significantly changed or restructured|Review|5.2,<br>5.2.2|||||



- Note 1: Initial – Fill out a Checklist upon notification/assignment to a new T&E project, with anticipated action tailoring included, then date and sign. Revision – Update Checklist each time a changed, newly anticipated or actual but not previously anticipated tailored action is required, dated and signed for each revision. Checklist Complete – Finalize Checklist when the associated program phase is complete and all actions have been addressed, then date and sign. 

- Note 2: Each signed and dated version (Initial, Revisions, and Checklist Complete) of this checklist will be maintained by the DT Test Director in either a hard copy or in an electronic copy with a scanned signature page.  Each “working copy” of this checklist can be maintained electronically on the DT Test Director’s PC.  All signed and dated versions of this checklist will be maintained for a period of two (2) years beyond the completion of the OT Checklist and in accordance with the ANG-E Document Management and Control (DMC) Process Description Document (PDD). 

- Note 3: <u>Tailoring</u> – Identify any required change(s) to the Action, and provide justification for each specific change (Section 1.6 of this T&E Handbook can be used to provide justifications related to tailoring the T&E process). Leave blank if no tailoring is required. 

- Note 4: <u>Target Date – Provide at least the month and year of the anticipated completion of the Action.  Revise only when a major program schedule change has occurred.  Leave</u> blank if the Action already occurred prior to the completion of the Initial version of the checklist. 

- Note 5: <u>Completion Date – Provide the actual completion date of the Action.  If the Action was completed prior to the completion of the Initial version of the checklist, provide at least</u> the year of the Action completion or leave blank if unknown.  If the Action is completed after the completion of the Initial version of the checklist, provide the full date of the Action completion (month/day/year).  For Actions that have multiple items to complete, provide completion dates for each item and explain in the Status/Comments column. 

- Note 6: <u>Status/Comments – Provide any supporting information for the Action.  If the Action was completed prior to the completion of the Initial version of the checklist and the actual</u> date of completion is unknown, enter “Action occurred prior to the implementation of this T&E process” in this column. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

B-6 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

## **Appendix C.  Development Test Process Conformance Checklist** 

(See T&E Handbook, Section 1.7, T&E Standards Conformance, regarding checklists.) 

Test Program: 



<!-- Start of picture text -->
T&E Team(s):<br>T&E First Line Supervisor:<br>DT Test Director:<br>OT Test Director:<br>Version  1 : ____ Initial  ____ Revision  ____ Checklist Complete<br>Review Signatures: Date:<br>_____________________________  ____________<br>T&E First Line Supervisor<br>_______________________________  ____________<br>DT Test Director<br>_______________________________  ____________<br>TSB Representative<br><!-- End of picture text -->

VVSPT-A2-PDD-013 v5.0 

C-1 

12/18/2020 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **APPENDIX C. DT PROCESS CONFORMANCE CHECKLIST** 

### **Test Program Name:** 

### **Version Date** 

|**Action**<br>**ID**|**Action**|**TSB Role**|**2: **<br>**T&E HB**<br>**Ref. Sec.**|**Tailoring Change(s)**<br>**w/ Justification (if used)**<sup>**3**</sup>|**Target**<br>**Date**<sup>**4**</sup>|**Completion**<br>**Date**<sup>**5**</sup>|**Status/**<br>**Comments/**<br>**Artifacts**<sup>**6**</sup>|
|---|---|---|---|---|---|---|---|
|DT1|Support development of the FAA System<br>Specification, and ensure that all test-related<br>inputs are peer-reviewed prior to submission|Monitor|5.4|||||
|DT2|Support development of the SIR proposal<br>and SOW/PWS/SOO requirements,<br>ensuring that adequate test requirements<br>and test activities are included, and that<br>these inputs are peer-reviewed prior to<br>submission|Monitor|5.5,<br>6.1.3.1|||||
|DT3|Review/evaluate the contractor proposals|Monitor|5.6|||||
|DT4|Coordinate with the CO and COR to provide<br>test-related contract support|N/A|6.1.3|||||
|DT5|After confirming that they have undergone<br>internal contractor peer reviews, review and<br>comment on contractor specifications<br>(system level and subsystem level) and<br>other test-related CDRL documents|Monitor|6.1.3.2,<br>6.1.3.3|||||
|DT6|Provide status and action plans for ISR<br>Checklist test-related items|Monitor|9.2|||||
|DT7|Participate in and provide test expertise to<br>system engineering, hardware, and software<br>meetings and reviews|Monitor|6.1.4|||||



VVSPT-A2-PDD-013 v5.0 

C-2 

12/18/2020 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **APPENDIX C. DT PROCESS CONFORMANCE CHECKLIST** 

### **Test Program Name:** 

### **Version Date** 

|**Action**<br>**ID**|**Action**|**2**<br>**TSB Role**|**:**<br>**T&E HB**<br>**Ref. Sec.**|**Tailoring Change(s)**<br>**w/ Justification (if used)**<sup>**3**</sup>|**Target**<br>**Date**<sup>**4**</sup>|**Completion**<br>**Date**<sup>**5**</sup>|**Status/**<br>**Comments/**<br>**Artifacts**<sup>**6**</sup>|
|---|---|---|---|---|---|---|---|
|DT8|Review the CMTP (including the DT VRTM)<br>and follow the review and approval cycle<br>prior to providing an approval<br>recommendation to the CO|Review|6.1.3.2,<br>6.2.2,<br>6.2.3,<br>Fig. E-5|||||
|DT9|Participate in TWG meetings with the<br>Contractor Test Manager for DT test<br>program planning and issues resolution|N/A|6.2|||||
|DT10|Determine the verification method for any<br>COTS/NDI hardware, software, and<br>firmware|Monitor|6.2.1.1|||||
|DT11|Witness accreditation of DT test capabilities|N/A|6.2.1.10,<br>9.1|||||
|DT12|Participate in system training from the<br>contractor and T&E process training as<br>needed, and maintain training records as<br>required|Monitor|6.2.1.12|||||
|DT13|Review the contractor’s DT Test Plan(s) and<br>follow the review and approval cycle prior to<br>providing an approval recommendation to<br>the CO|Review|6.2.5,<br>Fig. E-6|||||
|DT14|Review the contractor’s DT Test Procedures<br>and follow the review and approval cycle<br>prior to providing an approval<br>recommendation to the CO|Monitor|6.2.6,<br>Fig. E-7|||||



VVSPT-A2-PDD-013 v5.0 

C-3 

12/18/2020 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **APPENDIX C. DT PROCESS CONFORMANCE CHECKLIST** 

### **Test Program Name:** 

### **Version Date** 

||||**2: **<br>||||**Status/**|
|---|---|---|---|---|---|---|---|
|**Action**<br>**ID**|**Action**|**TSB Role**|**T&E HB**<br>**Ref. Sec.**|**Tailoring Change(s)**<br>**w/ Justification (if used)**<sup>**3**</sup>|**Target**<br>**Date**<sup>**4**</sup>|**Completion**<br>**Date**<sup>**5**</sup>|<br>**Comments/**<br>**Artifacts**<sup>**6**</sup>|
|DT15|Ensure that all DT entrance criteria have<br>been met prior to entering formal DT|Monitor|6.2.7|||||
|DT16|Witness DT dry run testing prior to each<br>formal DT test activity|Monitor|6.3,<br>6.3.1|||||
|DT17|Participate in a contractor conducted TRR<br>prior to each formal DT test activity|Monitor|6.3,<br>6.3.2|||||
|DT18|Participate in Pre-Test Briefings prior to<br>each test, and review and approve any<br>planned test deviations|Monitor|6.3.3|||||
|DT19|Witness DT Software Testing|Monitor|6.2.1.2|||||
|DT20|Witness DT Hardware Testing|Monitor|6.2.1.3|||||
|DT21|Witness FAT|Monitor|6.2.1.4|||||
|DT22|Monitor FQT|Monitor|6.2.1.5|||||
|DT23|Witness DT I&I Testing|Monitor|6.2.1.6|||||
|DT24|Witness DT System Testing|Monitor|6.2.1.7|||||
|DT25|Witness Production Acceptance Testing<br>(PAT)|Monitor|6.2.1.8|||||
|DT26|Witness SAT<br>(Coordinate with each facility prior to SAT)|Monitor|6.2.1.9|||||



VVSPT-A2-PDD-013 v5.0 C-4 

12/18/2020 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **APPENDIX C. DT PROCESS CONFORMANCE CHECKLIST** 

### **Test Program Name:** 

### **Version Date** 

|**Action**<br>**ID**|**Action**|**TSB Role**|**2: **<br>**T&E HB**<br>**Ref. Sec.**|**Tailoring Change(s)**<br>**w/ Justification (if used)**<sup>**3**</sup>|**Target**<br>**Date**<sup>**4**</sup>|**Completion**<br>**Date**<sup>**5**</sup>|**Status/**<br>**Comments/**<br>**Artifacts**<sup>**6**</sup>|
|---|---|---|---|---|---|---|---|
|DT27|During all formal DT test execution:<br>- Sign off/initial all test procedure<br>changes/redlines/deviations<br>- Ensure that anomalies are properly<br>documented in the contractor’s test log<br>- Sign off on the test log and obtain copies<br>of the test log and as-run test procedures at<br>the completion of testing|Monitor|6.3.4|||||
|DT28|Participate in DT Post-Test Reviews after<br>each test, and review and confirm results|Monitor|6.3.5|||||
|DT29|Prepare, distribute to the DT test team, and<br>enter into the test status database a Test<br>Status Report for each dry run and formal<br>test run|Monitor|6.3.6|||||
|DT30|Review the contractor’s PTR database,<br>including:<br>- Review and approve the PTR database<br>design<br>- Review and concur on PTR priorities<br>- Review and concur on PTR corrective<br>actions and proposed regression testing|Monitor|6.3.7|||||
|DT31|Approve the extent of and witness any DT<br>Regression Testing|Monitor|6.3.8|||||



VVSPT-A2-PDD-013 v5.0 

C-5 

12/18/2020 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **APPENDIX C. DT PROCESS CONFORMANCE CHECKLIST** 

### **Test Program Name: Version Date** 

**2** 

|**Action**<br>**ID**|**Action**|**TSB Role**|**T&E HB**<br>**Ref. Sec.**|**Tailoring Change(s)**<br>**w/ Justification (if used)**<sup>**3**</sup>|**Target**<br>**Date**<sup>**4**</sup>|**Completion**<br>**Date**<sup>**5**</sup>|**Status/**<br>**Comments/**<br>**Artifacts**<sup>**6**</sup>|
|---|---|---|---|---|---|---|---|
|DT32|Review the contractor’s DT Test Report and<br>follow the review and approval cycle prior to<br>providing an approval recommendation to<br>the CO|Review|6.4,<br>Fig. E-8|||||
|DT33|Support the FCA, PCA, and GA processes<br>with test expertise and verification|Monitor|6.1.3.4|||||
|DT34|Ensure that all DT exit criteria have been<br>met prior to exiting DT|Monitor|6.2.8|||||



- Note 1: Initial – Fill out Checklist out upon notification/assignment to a new T&E project, with anticipated action tailoring included, then date and sign. Revision – Update Checklist each time a changed, <u>newly anticipated or actual but not previously anticipated tailored action is required; dated and signed for each revision.</u> Checklist Complete – Finalize Checklist when the associated program phase is complete and all actions have been addressed, then date and sign. 

- Note 2: Each signed and dated version (Initial, Revisions, and Checklist Complete) of this checklist will be maintained by the DT Test Director in either a hard copy or in an electronic copy with a scanned signature page.  Each “working copy” of this checklist can be maintained electronically on the DT Test Director’s PC.  All signed and dated versions of this checklist will be maintained for a period of two (2) years beyond the completion of the OT Checklist and in accordance with the ANG-E Document Management and Control (DMC) Process Description Document (PDD). 

VVSPT-A2-PDD-013 v5.0 

C-6 

12/18/2020 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

- Note 3: <u>Tailoring</u> – Identify any required change(s) to the action and provide justification for each specific change (Section 1.6 of this T&E Handbook can be used to provide justifications related to tailoring the T&E process).  Leave blank if no tailoring is required. 

- Note 4: <u>Target Date – Provide at least the month and year of the anticipated completion of the Action.  Revise only when a major program schedule change has occurred.  Leave</u> blank if the Action already occurred prior to the completion of the Initial version of the checklist. 

- Note 5: <u>Completion Date – Provide the actual completion date of the Action.  If the Action was completed prior to the completion of the Initial version of the checklist, provide at least</u> the year of the Action completion or leave blank if unknown.  If the Action is completed after the completion of the Initial version of the checklist, provide the full date of the Action completion (month/day/year). For Actions that have multiple items to complete, provide completion dates for each item and explain in the Status/Comments column. 

- Note 6: <u>Status/Comments – Provide any supporting information for the Action.  If the Action was completed prior to the completion of the Initial version of the checklist and the actual</u> date of completion is unknown, enter “Action occurred prior to the implementation of this T&E process” in this column. 

VVSPT-A2-PDD-013 v5.0 

C-7 

12/18/2020 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

## **Appendix D.  Operational Test Process Conformance Checklist** 

(See T&E Handbook, Section 1.7, T&E Standards Conformance, regarding checklists.) 

Test Program: 



<!-- Start of picture text -->
T&E Team(s):<br>T&E First Line Supervisor(s):<br>DT Test Director:<br>OT Test Director:<br>Version  1 : ____ Initial  ____ Revision  ____ Checklist Complete<br>Review Signatures: Date:<br>_____________________________  ____________<br>T&E First Line Supervisor<br>_______________________________  ____________<br>OT Test Director<br>_______________________________  ____________<br>TSB Representative<br><!-- End of picture text -->

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

D-1 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **APPENDIX D. OT PROCESS CONFORMANCE CHECKLIST** 

### **Test Program Name:** 

### **Version Date** 

|**Action**<br>**ID**|**Action**|**TSB Role**|**2: **<br>**T&E HB**<br>**Ref. Sec.**|**Tailoring Change(s)**<br>**w/ Justification (if used)**<sup>**3**</sup>|**Target**<br>**Date**<sup>**4**</sup>|**Completion**<br>**Date**<sup>**5**</sup>|**Status/**<br>**Comments/**<br>**Artifacts**<sup>**6**</sup>|
|---|---|---|---|---|---|---|---|
|OT1|Work with the ITT to define personnel and<br>resource requirements for OT, including<br>assigning test leads|Monitor|7.3.1|||||
|OT2|Support development of the FAA System<br>Specification from an operational<br>perspective|Monitor|5.4|||||
|OT3|Support development of the SIR proposal<br>and SOW/PWS/SOO requirements,<br>ensuring that adequate OT support<br>requirements are included, and that these<br>inputs are peer-reviewed prior to<br>submission|Monitor|5.5,<br>7.3.3|||||
|OT4|Evaluate contractor proposals from the OT<br>perspective|Monitor|5.6|||||
|OT5|Provide OT test-related contract support,<br>including inputs to the SOW/PWS/SOO and<br>participation in specification, CDRL, and<br>program reviews|N/A|5.5.2,<br>7.3.3|||||
|OT6|Provide status and action plans for ISR<br>Checklist test-related items|Monitor|9.2|||||
|OT7|Participate in system training from the<br>contractor and T&E process training as<br>needed, and maintain training records as<br>required|Monitor|7.3.4|||||



VVSPT-A2-PDD-013 v5.0 

12/18/2020 

D-2 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **APPENDIX D. OT PROCESS CONFORMANCE CHECKLIST** 

### **Test Program Name:** 

### **Version Date** 

|**Action**<br>**ID**|**Action**|**TSB Role**|**2: **<br>**T&E HB**<br>**Ref. Sec.**|**Tailoring Change(s)**<br>**w/ Justification (if used)**<sup>**3**</sup>|**Target**<br>**Date**<sup>**4**</sup>|**Completion**<br>**Date**<sup>**5**</sup>|**Status/**<br>**Comments/**<br>**Artifacts**<sup>**6**</sup>|
|---|---|---|---|---|---|---|---|
|OT8|Coordinate early during the T&E Planning<br>and Support phase with OT field<br>participants|Monitor|7.3.5|||||
|OT9|Plan and perform accreditation of OT test<br>capabilities|Monitor|7.3.6,<br>9.1|||||
|OT10|Participate in DT TWG meetings with the<br>Contractor Test Manager and DT Test<br>Director for test program planning and<br>resolution of issues that may affect OT|Monitor|6.2|||||
|OT11|Prior to OT, generate DRs for all issues<br>discovered that impact operational<br>requirements but are not being addressed<br>and need to be evaluated during OT|Monitor|7.5.4|||||
|OT12|Develop the OT Test Plan (including the OT<br>VRTM) and follow the review and approval<br>cycle prior to final distribution|Review|7.4.1,<br>7.4.2,<br>Fig. E-10|||||
|OT13|Meet with the ITT and ensure that all OT<br>entrance criteria have been met prior to<br>entering the OT phase|Monitor|7.4.5,<br>7.5|||||



VVSPT-A2-PDD-013 v5.0 

12/18/2020 

D-3 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **APPENDIX D. OT PROCESS CONFORMANCE CHECKLIST** 

### **Test Program Name:** 

### **Version Date** 

|**Action**<br>**ID**|**Action**|**TSB Role**|**2: **<br>**T&E HB**<br>**Ref. Sec.**|**Tailoring Change(s)**<br>**w/ Justification (if used)**<sup>**3**</sup>|**Target**<br>**Date**<sup>**4**</sup>|**Completion**<br>**Date**<sup>**5**</sup>|**Status/**<br>**Comments/**<br>**Artifacts**<sup>**6**</sup>|
|---|---|---|---|---|---|---|---|
|OT14|Collect, analyze, and report (using the OT<br>IAR) at specific milestones on system<br>performance, requirements, issues, and<br>risks having an operational impact during<br>system development, DT and OT<br>- Generate optional IARs and follow the<br>review and approval cycle prior to<br>distribution<br>- Electronically distribute completed IARs to<br>the respective T&E Senior Manager,<br>Program Manager, T&E First-Line<br>Supervisor, and TSB|Review|5.2.3.10,<br>7.6.1,<br>Fig. E-12|||||
|OT15|Generate the OT Test Procedures,<br>including:<br>- Develop the draft OT Test Procedures<br>(including checkout and debugging) and<br>follow the review and approval cycle<br>- Dry run the OT Test Procedures (dry runs<br>should include OT field participants)|Optional<br>Review|7.4.3,<br>Fig. E-11|||||
|OT16|Maintain an OT Test Procedures Status<br>Matrix during OT Test Procedure<br>development, and generate a Test Status<br>Report at the conclusion of each test activity<br>(checkout, debug, and dry run) and provide<br>it to the ITT|Monitor|7.4.3.1|||||



VVSPT-A2-PDD-013 v5.0 

12/18/2020 

D-4 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **APPENDIX D. OT PROCESS CONFORMANCE CHECKLIST** 

### **Test Program Name:** 

### **Version Date** 

||||**2: **<br>||||**Status/**|
|---|---|---|---|---|---|---|---|
|**Action**<br>**ID**|**Action**|**TSB Role**|**T&E HB**<br>**Ref. Sec.**|**Tailoring Change(s)**<br>**w/ Justification (if used)**<sup>**3**</sup>|**Target**<br>**Date**<sup>**4**</sup>|**Completion**<br>**Date**<sup>**5**</sup>|**Comments/**<br>**Artifacts**<sup>**6**</sup>|
|OT17|Develop OT user-evaluation questionnaires<br>and submit them to the appropriate union(s)<br>for approval prior to use during formal OT|Monitor|7.4.3.2|||||
|OT18|Coordinate all required logistical activities<br>for OT prior to the TRR|N/A|7.4.4|||||
|OT19|Conduct the OT TRR prior to the start of<br>formal OT activities|Monitor|7.5.2|||||
|OT20|Conduct an OT Pre-Test Briefing prior to the<br>start of each OT test|N/A|7.5.3.1|||||
|OT21|During all formal OT test executions:<br>- Maintain a test log<br>- Collect completed questionnaires (if used)<br>immediately following the test execution<br>- Generate DRs for all issues/anomalies<br>encountered during the testing|Monitor|7.5.3.2,<br>7.5.4|||||
|OT22|Conduct an OT Post-Test Review at the<br>conclusion of each formal OT test|N/A|7.5.3.3|||||
|OT23|Generate a Test Status Report at the<br>conclusion of each formal OT test|Monitor|7.5.3.3|||||
|OT24|Conduct DR reviews on a regular basis and<br>maintain the DR database|N/A|7.5.4|||||



VVSPT-A2-PDD-013 v5.0 

12/18/2020 

D-5 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **APPENDIX D. OT PROCESS CONFORMANCE CHECKLIST** 

### **Test Program Name:** 

### **Version Date** 

||||**2: **<br>||||**Status/**|
|---|---|---|---|---|---|---|---|
|**Action**<br>**ID**|**Action**|**TSB Role**|**T&E HB**<br>**Ref. Sec.**|**Tailoring Change(s)**<br>**w/ Justification (if used)**<sup>**3**</sup>|**Target**<br>**Date**<sup>**4**</sup>|**Completion**<br>**Date**<sup>**5**</sup>|<br>**Comments/**<br>**Artifacts**<sup>**6**</sup>|
|OT25|Generate an OT Problem Traceability Matrix<br>to identify the COIs, MOEs, MOSs, and<br>CPRs impacted by the open DRs and PTRs|Monitor|7.5.5|||||
|OT26|Conduct an OT Caucus after the completion<br>of formal OT testing, including:<br>- Review the OT Problem Traceability Matrix<br>to assess the operational impact of open<br>DRs and PTRs<br>- Generate an OT Caucus Summary Report<br>to document the status of each COI, MOE,<br>MOS, and CPR, and to support the<br>resolution of critical PTRs|Monitor|7.5.5|||||
|OT27|Generate an OT Quicklook Test Report,<br>including:<br>- The draft report and follow the review and<br>approval cycle prior to distribution<br>- Electronic distribution of the approved OT<br>Quicklook Test Report to the respective<br>T&E Senior Manager, Program Manager,<br>T&E First-Line Supervisor, Technical Center<br>Director, and TSB within 15 business days<br>from test completion|Review|1.8.5.,<br>1.9,<br>7.6.2,<br>Fig. E-13|||||
|OT28|Conduct OT Regression Testing to verify<br>the integrity of solutions to DRs/PTRs|Monitor|7.5.6|||||
|OT29|Ensure that all OT exit criteria have been<br>met prior to exiting OT|Monitor|7.4.6|||||



VVSPT-A2-PDD-013 v5.0 

12/18/2020 

D-6 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **APPENDIX D. OT PROCESS CONFORMANCE CHECKLIST** 

### **Test Program Name:** 

### **Version Date** 

|**Action**<br>**ID**|**Action**|**TSB Role**|**2: **<br>**T&E HB**<br>**Ref. Sec.**|**Tailoring Change(s)**<br>**w/ Justification (if used)**<sup>**3**</sup>|**Target**<br>**Date**<sup>**4**</sup>|**Completion**<br>**Date**<sup>**5**</sup>|**Status/**<br>**Comments/**<br>**Artifacts**<sup>**6**</sup>|
|---|---|---|---|---|---|---|---|
|OT30|Generate an OT Final Test Report that<br>includes:<br>- For large or high-risk programs, conduct<br>an OT Final Test Report Out-Brief to the ITT<br>prior to delivering the draft report for review<br>- Follow the OT Final Test Report review<br>and approval cycle prior to final distribution,<br>including an OT Final Test Report Out-Brief<br>to the Director of Test Service Organization<br>(or equivalent), if required.<br>- Deliver the approved OT Final Test Report<br>within 60 business days from test<br>completion to the TSB, and the Program<br>Manager, to support the ISD process|Review|7.6.3,<br>Fig. E-14|||||
|OT31|Provide an OT Final Test Report Out-Brief,<br>as required, to the ANG Assistant<br>Administrator for NextGen, ANG-1, prior to<br>the ISD milestone<br>(Director of Test Service Organization (or<br>equivalent) function)|Monitor|7.6.3|||||
|OT32|If required, provide test support to the ISM<br>organization during the transitional period<br>from OT to ISM|Monitor|7.7|||||
|OT33|If required, develop an FF Support Plan and<br>provide it to the TSB for review and<br>comment prior to final delivery to the<br>Program Office and site representatives|Review|7.8,<br>7.8.1,<br>Fig. E-15|||||



VVSPT-A2-PDD-013 v5.0 

12/18/2020 

D-7 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

### **APPENDIX D. OT PROCESS CONFORMANCE CHECKLIST** 

### **Test Program Name: Version Date** 

**2** 

|**Action**<br>**ID**|**Action**|**TSB Role**|**T&E HB**<br>**Ref. Sec.**|**Tailoring Change(s)**<br>**w/ Justification (if used)**<sup>**3**</sup>|**Target**<br>**Date**<sup>**4**</sup>|**Completion**<br>**Date**<sup>**5**</sup>|**Status/**<br>**Comments/**<br>**Artifacts**<sup>**6**</sup>|
|---|---|---|---|---|---|---|---|
|OT34|If required, develop and dry run FF test<br>procedures|Monitor|7.8.1,<br>7.8.2|||||
|OT35|If required, participate in FF testing,<br>including all activities associated with formal<br>testing|Monitor|7.8.3|||||
|OT36|If required, generate and distribute to the<br>Program Office, TSB, and site<br>representatives a final FF Report for each<br>site to document the activities and<br>summarize any issues encountered during<br>FF testing|Review|7.8.4|||||



- Note 1: Initial – Fill out Checklist upon notification/assignment to a new T&E project, with anticipated action tailoring included, then date and sign. Revision – Update Checklist each time a changed, newly anticipated or actual but not previously anticipated tailored action is required, date and sign for each revision. Checklist Complete – Finalize Checklist when the associated program phase is complete and all actions have been addressed, then date and sign. 

- Note 2: Each signed and dated version (Initial, Revisions, and Checklist Complete) of this checklist will be maintained by the OT Test Director in either a hard copy or in an electronic copy with a scanned signature page.  Each “working copy” of this checklist can be maintained electronically on the OT Test Director’s PC.  All signed and dated versions of this checklist will be maintained for a period of two (2) years beyond the completion of the OT Checklist and in accordance with the ANG-E Document Management and Control (DMC) Process Description Document (PDD). 

- Note 3: <u>Tailoring</u> – Identify any required change(s) to the Action, and provide justification for each specific change (Section 1.6 of this T&E Handbook can be used to provide justifications related to tailoring the T&E process).  Leave blank if no tailoring is required. 

- Note 4: <u>Target Date – Provide at least the month and year of the anticipated completion of the Action.  Revise only when a major program schedule change has occurred.  Leave</u> blank if the Action already occurred prior to the completion of the Initial version of the checklist. 

- Note 5: <u>Completion Date – Provide the actual completion date of the Action. If the Action was completed prior to the completion of the Initial version of the checklist, provide at least</u> the year of the Action completion or leave blank if unknown. If the Action is completed after the completion of the Initial version of the checklist, provide the full date of the Action completion (month/day/year). For Actions that have multiple items to complete, provide completion dates for each item and explain in the Status/Comments column. 

- Note 6: <u>Status/Comments – Provide any supporting information for the Action.  If the Action was completed prior to the completion of the Initial version of the checklist and the actual</u> date of completion is unknown, enter “Action occurred prior to the implementation of this T&E process” in this column. 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

D-8 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

## **Appendix E.  Test and Evaluation Work Products and Review Process Cycles** 

The following table identifies the major work products associated with each phase of the T&E process, along with a reference to their associated review and approval cycle flow diagrams contained in this Appendix. 

**Table E-1.  T&E Work Products** 

|**Test Phase**|**Work Product**|**TSB**<br>**Early**<br>**Review**<br>**Cycle**<sup>1</sup>|**TSB Final**<br>**Review**<br>**Required**<sup>2</sup>|**TSB**<br>**Endorsement**<br>**Required**<sup>3</sup>|**Flow**<br>**Diagram**<br>**Number**|
|---|---|---|---|---|---|
||PRD T&E Section|X|X||E-1|
|**T&E**|ISPD T&E Section|X|X|X|E-2|
|<br>**Program**<br>**Planning**|TEMP (Requires Director of Test<br>Service Organization (or equivalent)<br>Approval)|X|X|X|E-3|
||T&E Inputs to: Specification; SIR,<br>SOW||||E-4|
||CMTP||X||E-5|
||DT Test Plan||X||E-6|
|**Development**<br>**Test (DT)**|DT Test Procedures|T<br>th|SB’s role is to<br>e test team a|monitor<br>ctivity|E-7|
||DT Test Report||X||E-8|
||DT Accreditation Record||X||E-9|
||OT Test Plan|X|X|X|E-10|
||OT Test Procedures|TS|B reviews as|needed|E-11|
|**Otil**|OT IAR||X||E-12|
|**peraona**<br>**Test (OT)**|OT Quicklook Test Report||X||E-13|
||OT Final Test Report (Requires<br>Director of Test Service<br>Organization (or equivalent)<br>Approval)|X|X|X|E-14|



> 1 An early review is recommended for the purpose of identifying major work system, service, or capability deficiencies. This is typically accomplished by the project’s TSB POC and one other TSB member. It is recommended that the TSB Early Review start in parallel with the Peer Review but be complete prior to Comment Workoff and Tech Edit. 

> 2 The completed review results in a “tabling” meeting in which the TSB determines the level of conformance to established standards and the TSB’s position, if endorsable. Consult the TSB Work Product Review and Endorsement Guide regarding the number of reviewers to include that is commensurate with the priority level of the program. 

> 3 Endorsement is defined as a recommendation for approval or disapproval of a work product with supporting comments. Endorsement can be accomplished via email, endorsement letter, or a written or digital signature on the signature page of the document by the endorser(s). 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

E-1 

**<u>TEST & E</u> VALUATION H ANDBOOK** 

|FF Support Plan|X|X|E-15|
|---|---|---|---|
|OT Accreditation Record|X|X|E-16|



The following pages contain diagrams of the process flow cycles for reviewing and approving the test work products identified in the Handbook.  The processes in the diagrams may be tailored to meet program needs.  A process may be restarted if major revisions are required based on reviews or major program changes. 

The following terminology is presented below for use in understanding the flow diagrams: 

- <u>Signature:  On specified documents, written or digital signature(s) are required by</u> the responsible author(s) of the document [normally the Test Director(s)] on the signature page. 

- <u>Review:  A Review is defined as an assessment of a draft or final draft document</u> to provide comments and input.  The outcome of a review results in the delivery of a revised draft or a final document.  A Peer Review is a structured type of review which involves a methodical examination of a completed draft document.  Peer Reviews are conducted in accordance with the Peer Review PDD to ensure the quality of the work product.  Peer Reviews are conducted by unbiased subject matter experts who have independence from the development and approval of the document.  Peer reviewers use knowledge, experience, established standards and known best practices to provide editorial and technical comments. 

- <u>Endorsement:  Endorsement is defined as a recommendation for approval or</u> disapproval of a work product with supporting comments.  Endorsement can be accomplished via email, endorsement letter, or a written or digital signature on the signature page of the document by the endorser(s).  Note: The TSB endorses work products via TSB Endorsement Position Papers. 

- <u>Approval:  For DT work products, approval is defined by the provision of an</u> approval recommendation from the DT Test Director to the CO after all appropriate FAA authorities have reviewed and endorsed the document.  For OT work products, approval is defined by the written or digital signature on the signature page of the document by the designated authority after his/her review and approval of the document. 

The following symbology definitions are presented for use in understanding the connector lines between the blocks in the flow diagrams: 

- <u>Solid line:</u> Mandatory path for activity to follow 

- `o` <u>Dashed line:</u> Recommended path for activity to follow 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

E-2 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



### **Figure E-1.  Program Requirements (Test & Evaluation Section) Review, Endorsement and/or Approval Cycle** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

E-3 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



### **Figure E-2.  Implementation Strategy and Planning Document (Test & Evaluation Section) Review, Endorsement and/or Approval Cycle** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

E-4 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



**Figure E-3.  Preliminary, Initial, and Final Test and Evaluation Master Plan Review, Endorsement and/or Approval Cycle** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

E-5 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



**Figure E-4.  Test & Evaluation Input Review Cycle for FAA System Specification, Screening Information Request, Proposal Requirements, and Statements of Work Review Endorsement and/or Approval Cycle** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

E-6 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



### **Figure E-5.  Contractor Master Test Plan Review, Endorsement and/or Approval Cycle** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

E-7 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



### **Figure E-6.  Development Test Plan Review, Endorsement and/or Approval Cycle (Also used for Development Test Accreditation Plan)** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

E-8 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



### **Figure E-7.  Development Test Procedures Review, Endorsement and/or Approval Cycle** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

E-9 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



### **Figure E-8.  Development Test Report Review, Endorsement and/or Approval Cycle** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

E-10 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



**Figure E-9.  Development Test Accreditation Record Review, Endorsement and/or Approval Cycle** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

E-11 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



### **Figure E-10.  Operational Test Plan Review, Endorsement and/or Approval Cycle (Also used for Operational Test Accreditation Plan)** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

E-12 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



### **Figure E-11.  Operational Test Procedures and Test Capability Procedures Review, Endorsement and/or Approval Cycle** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

E-13 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



### **Figure E-12.  Operational Test Interim Assessment Report Review, Endorsement and/or Approval Cycle** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

E-14 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



### **Figure E-13.  Operational Test Quicklook Test Report Review, Endorsement and/or Approval Cycle** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

E-15 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



**Figure E-14.  Operational Test Final Test Report Review, Endorsement and/or Approval Cycle** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

E-16 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



### **Figure E-15.  Field Familiarization Support Plan Review, Endorsement and/or Approval Cycle** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

E-17 

**<u>TEST & E</u> VALUATION H ANDBOOK** 



**Figure E-16.  Operational Test, Accreditation Test, Accreditation Record Review, Endorsement and/or Approval Cycle** 

VVSPT-A2-PDD-013 v5.0 

12/18/2020 

E-18 


