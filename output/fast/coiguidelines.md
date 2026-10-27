---
title: "coiguidelines"
source_url: https://fast.faa.gov/docs/coiguidelines.pdf
source_type: pdf
converted: 2026-10-27
---
# coiguidelines



### **FAA William J. Hughes Technical Center** 

# **Critical Operational Issue (COI) Guidelines** 

|Document #|VVSPT-C5-GDE-018|
|---|---|
|Version #|1.0|
|Version Date|January 28, 2022|



### **William J. Hughes Technical Center Atlantic City International Airport, New Jersey 08405** 

**CRITICAL O PERATIONAL I SSUE (COI) G UIDELINES** 

# **DOCUMENT VERSION CONTROL** 

|**VERSION**||**DESCRIPTION OFCHANGE**|**DATE**|
|---|---|---|---|
|1.0|Original||1/28/2022|



COI G U IDE L INE S 

1/28/2022 

II 

**COI G UIDELINES** 

# **Table of Contents** 

|1<br>Purpose .................................................................................................................... 1|
|---|
|2<br>Definitions ................................................................................................................. 1|
|3<br>COI Development ..................................................................................................... 2|
|3.1<br>Overview ......................................................................................................... 2|
|Figure 1.  COI Functional Areas ...................................................................................... 3|
|3.2<br>COI Structure .................................................................................................. 4|
|3.3<br>COI Checklist .................................................................................................. 4|
|4<br>COI Decomposition .................................................................................................. 5|
|4.1<br>Overview ......................................................................................................... 5|
|4.2<br>Responsibility .................................................................................................. 6|
|4.3<br>MOE, MOS, and MOP Structure ..................................................................... 7|
|5<br>COI Test Preparation, Statusing, and Reporting ...................................................... 8|
|5.1<br>COI Test Preparation ...................................................................................... 8|
|5.2<br>Status of COIs ................................................................................................. 8|
|5.3<br>COI Reporting ................................................................................................. 9|
|Appendix A — Acronym List .......................................................................................... 10|
|Appendix B — Examples of COIs ................................................................................. 11|
|Appendix C — VRTM Discussion and Examples .......................................................... 14|
|**List of Figures**|
|Figure 1. COI Functional Areas ....................................................................................... 3|
|Figure 2. COI Decomposition to Test Cases ................................................................... 6|
|**List of Tables**|
|Table 1. Definitions of COI Functional Areas .................................................................. 3|
|Table 2. Overall Responsibility of COI Decomposition Process ...................................... 7|



COI G U IDE L INE S 

1/28/2022 

II I 

**COI G UIDELINES** 

### **This page intentionally left blank.** 

COI G U IDE L INE S 

1/28/2022 

IV 

**COI G UIDELINES** 

## **1 PURPOSE** 

The purpose of this guide is to assist in the selection, review, and decomposition of Critical Operational Issues (COIs) contained in Section 7.7 of the Program Requirements Document (PRD).  As part of PRD development, COIs are established to focus testing of the system, service, or capability on criteria assessing its operational effectiveness and operational suitability.  COIs focus on the product’s capability to perform its mission, and COI content is based on the usability of the system, service, or capability being developed.  Finally, COIs are decomposed into usable measures to support Operational Testing (OT) and assessments.  This document provides guidance to assist in each of these three areas. 

## **2 DEFINITIONS** 

Critical Performance Requirements (CPRs), COIs, Measures of Effectiveness (MOEs), Measures of Suitability (MOSs), and Measures of Performance (MOPs) are elements that are essential to the evaluation of the operational effectiveness and suitability of systems, services, and capabilities.  These elements are defined as follows: 

1. CPRs — Program requirements identified in the PRD as essential to the successful performance of the system, service, or capability in meeting the program’s mission needs.  Special emphasis is placed on the evaluation of CPRs to ensure the timely assessment of system, service, or capability functionalities and to promote program success. 

2. COIs — Critical elements or operational objectives in the form of questions that must be examined during testing to determine the overall ability of the system, service, or capability to support mission accomplishment. 

3. MOEs — A first-level decomposition of the COI to an associated component of effectiveness.  Operational effectiveness addresses the degree to which a product accomplishes its mission when used by representative personnel in the expected operational environment.  MOEs include the following areas of evaluation: 

   - a. Accuracy 

   - b. Coverage 

   - c. Component performance 

   - d. System capacity 

   - e. Data timeliness 

4. MOSs — A first-level decomposition of the COI to an associated component of suitability.  Operational suitability addresses the degree to which a product intended for field use satisfies: 

   - a. Reliability, Maintainability, Availability (RMA) 

   - b. Compatibility 

COI G U IDE L INE S 

1/28/2022 

1 

**COI G UIDELINES** 

   - c. Transportability 

   - d. Interoperability 

   - e. Safety 

   - f. Human factors 

   - g. Logistics 

   - h. Supportability 

   - i. Training requirements 

   - j. Site adaptability 

   - k. Fault tolerance 

   - l. Security 

5. MOPs — Quantitative values or qualitative functionality statements, which are validated by a test process, that characterize and support evaluation of the COIs, MOEs, and MOSs. 

Note the difference between the definitions for the MOE/MOS and the MOP.  The MOE/MOS is a measure related to operations and is an indicator of task accomplishment, whereas the MOP is a measure related to the system, service, or capability and is an indicator of system technical performance or system characteristics. 

## **3 COI DEVELOPMENT** 

All CPRs must trace to the set of COIs that are developed.  COI development and operational requirements definition are done as part of the same process.  COIs are developed with the help of the user and test organizations to ensure the COIs are comprehensive.  The test team has a critical role in ensuring COIs are verifiable and testable.  For most systems, the high-level requirements can be addressed by the development of COIs in the form of questions, which are answered through evaluation of the subordinate MOEs, MOSs, and MOPs.  Typically, five COIs are recommended to address FAA systems, services, or capabilities, but a program may have more or less as required.  Based on the mission need, questions should be developed which, when answered, will determine whether the system can be used within the National Airspace System (NAS). 

## **3.1 OVERVIEW** 

A COI’s focus is on the product’s capability to perform its mission and the content is based on the use of the product.  COIs typically relate to: 

1. Operational effectiveness, which measures the degree to which a product satisfies mission requirements when used by representative personnel in the planned operational environment, and 

2. Operational suitability, which measures the degree to which a product meets its availability, operability, maintainability, safety, security, human factors, and support requirements. 

COI G U IDE L INE S 

1/28/2022 

2 

**COI G UIDELINES** 

All COIs must be addressed during OT and Independent Operational Assessment (IOA), if the program is designated for IOA, and resolved prior to the In-Service Decision (ISD). A COI is a critical element or operational objective examined during testing to determine the system’s overall capability to support mission accomplishment.  COIs are stated in the form of a question at a high level and usually cannot be answered directly from a single test or measurement. 

The functional areas addressed by COIs are depicted in Figure 1 and defined in Table 1. 



**Figure 1.  COI Functional Areas** 

**Table 1.  Definitions of COI Functional Areas** 

|**FUNCTIONAL AREA**|**DEFINITION**|
|---|---|
|NAS Integration|The system can be introduced into the NAS without degrading the<br>performance of existingsystems and operations.|
|Performance|Provides a measure characterizing a physical or functional attribute relating<br>to the execution of an operation or function.  Performance attributes<br>include quantity (how many or how much), quality (how well), coverage<br>(how much area, how far), timeliness (how responsive, how frequent), and<br>readiness (mission/operational readiness).  Performance is an attribute for<br>all systems, people, products, and processes including those for<br>development, production, verification, deployment, operations, support,<br>training, and disposal.|
|RMA|Reliability, Maintainability, and Availability are three attributes that<br>collectively affect both the utility and the lifecycle cost of a product or<br>system.  Reliability is the probability of failure-free performance of an item<br>over a specified timeframe.  Maintainability is the ability to perform<br>corrective or preventative maintenance tasks within a given time by<br>appropriately trained personnel.  Availability quantifies the likelihood that<br>the system or service is ready for use.|



COI G U IDE L INE S 

1/28/2022 

3 

**COI G UIDELINES** 

|**FUNCTIONAL AREA**|**DEFINITION**|
|---|---|
|Supportability|The degree to which product design and planned logistics resources meet<br>product-use requirements.|
|Degraded Ops|The maintenance levels of service when elements of the underlying<br>technical infrastructure are unavailable.|
|Human Factors|A multi-disciplinary effort to generate and apply human performance<br>information to acquire safe, efficient, and effective operational systems.|
|Safety|Operation and maintenance of system functionality without imposing harm<br>or danger to the environment or users.|
|Security|The system functionality protects from risk of unauthorized access or<br>malicious activity during operations or maintenance of the system.|
|Adaptation|Modification to the system for operations that are specific to the sites in<br>which the system is installed.|
|Transition|Ability of the system to be integrated at a site and changeover from the<br>legacy system without affecting site operations.|
|Certification|The formal process of documenting the attestation and confirmation that<br>the system, service, or capability meets its required characteristics.|
|Training|The activity that analyzes, designs, develops, implements, and evaluates<br>artifacts necessary to operate and maintain the solution.|



## **3.2 COI STRUCTURE** 

The structure of a COI takes the following form: 

1. COIs are stated in the form of a question at a high level and usually cannot be answered directly from a single test or measurement. 

2. COIs do not have direct evaluation criteria (they are supported by one or more MOEs/MOSs and associated criteria). 

Key components of a properly structured COI statement are 

1. An interrogative word demanding a “yes” or “no” answer (e.g., “Does,” “Can,” or “Is”). 

2. Identification of the solution of concern. 

3. The capability of concern, such as robust voice and data communications. 

4. A set of applicable operational conditions.  An example would be “Does En Route Automation Modernization (ERAM) ensure safe operations of En Route Air Traffic Control (ATC) during peak demand?” 

## **3.3 COI CHECKLIST** 

Appendix B provides some of the best examples of COIs that have been presented in PRDs in recent years.  A checklist for developing COIs is provided below: 

- Are COIs specific to the tasks the system must perform? 

- Are all COIs consistent with the purpose of the OT? 

- Can the COIs, as stated, be answered through OT? 

COI G U IDE L INE S 

1/28/2022 

4 

**COI G UIDELINES** 

- Are new tactics or techniques necessary for the test, and are they properly factored into the COIs? 

- Have COIs been reviewed to ensure they do not overlap? 

- If more than one mission is envisioned for the system, do the COIs reflect the user's priorities? 

- Are COIs consistent with the existing or planned operations and maintenance concepts, tactics, techniques, and doctrine? 

- Have COIs, which were developed in the past, been reevaluated for compatibility with current program conditions? 

- Do COIs address areas of interface (interoperability) with other systems? 

- Are the COIs free from grammatical and spelling errors? 

## **4 COI DECOMPOSITION** 

## **4.1 OVERVIEW** 

Resolution of a COI cannot be accomplished by a single test or measurement.  Instead, multiple individual testable measurements provide the answer.  The results of the evaluations of these testable measures must be combined for full resolution of a COI. Therefore, each COI must be broken down into a complete set of testable measures. 

The test team provides an outline of the test program by decomposing the COIs from the PRD, first into MOEs and MOSs, and then into MOPs.  For each COI, there typically will be multiple MOEs/MOSs; and for each MOE/MOS, there are typically multiple MOPs. However, some MOEs/MOSs may not have an associated MOP.  In some programs, MOPs are further decomposed into individual Data Elements when multiple operational performance criteria are identified.  The test team’s completed COI decomposition is confirmed by the end-user during the test planning stage with the establishment of the test cases. 

Figure 2 shows the decomposition process.  MOPs that correspond to each CPR listed in the PRD must also be developed. 

COI G U IDE L INE S 

1/28/2022 

5 

**COI G UIDELINES** 



**Figure 2.  COI Decomposition to Test Cases** 

The Test and Evaluation Master Plan (TEMP) Verification Requirements Traceability Matrix (VRTM) provides a structured approach that ensures planned testing is comprehensive and complete.  It maps all COIs/MOEs/MOSs/MOPs and the program requirements into Test and Evaluation (T&E) phases [Development Test (DT) or OT] and associated test activities.  Appendix C provides a discussion and examples of VRTMs. 

## **4.2 RESPONSIBILITY** 

COI decomposition is accomplished early in OT planning in conjunction with development of the initial TEMP (iTEMP).  The test team’s job is to develop the MOEs, MOSs, and MOPs.  The test team works with users to reach agreement on the COI decomposition. 

The development and use of COIs is essential to the operational evaluation of new or modified systems.  Complete and testable COIs benefit sponsors, users, and testers.  The Program Management Organization (PMO) has primary responsibility for the development of the PRD that includes the COIs.  The test team’s involvement ensures that COIs are testable and user involvement ensures that user requirements are reflected properly.  The joint efforts of the PMO, end-user, and test organizations are necessary to verify overall operational readiness.  Table 2 shows the responsibilities for the decomposition process. 

COI G U IDE L INE S 

1/28/2022 

6 

**COI G UIDELINES** 

### **Table 2.  Overall Responsibility of COI Decomposition Process** 

|**COI**<br>**DECOMPOSED**<br>**ELEMENT**|**DOCUMENTEDIN: **|**AUTHOR**|**AGREEMENT**|**ROLE OFSERVICEORGANIZATION**|
|---|---|---|---|---|
|MOEs|Test Plans|Test<br>Team|PMO/Users|Ensure that COI decomposition<br>accurately reflects operational needs,|
|MOSs|Test Plans|Test<br>Team|PMO/Users|via agreement with test plans.|
|MOPs|Test Plans|Test<br>Team|PMO/Users||



## **4.3 MOE, MOS, AND MOP STRUCTURE** 

The MOEs, MOSs, and MOPs need to be written in quantitative or qualitative terms that are objective, quantifiable, and understandable.  They should not begin with verbs like “assess” or “evaluate.”  The data required to evaluate and assess them need to be measurable and collectible in test or answerable using modeling or simulation.  With welldefined tasks, many appropriate MOEs, MOSs, and related MOPs will be evident.  Data to answer an MOE and MOS are usually collected under realistic operational scenarios with representative users. 

The decomposition process can be divided into phases: 

1. First phase of decomposition: 

   - a. Define/refine MOEs/MOSs to ensure that all system capabilities and operations are covered. 

   - b. Identify the test objectives of the MOE/MOS and help define the test approach and structure. 

2. Second phase of decomposition: 

   - a. Identify specific system and operational details that need to be included in test procedures. 

   - b. Develop MOPs and the data collection and analysis methods that will ultimately provide the OT results. 

When developing MOEs, MOSs, and MOPs, refer to the following checklist: 

- MOEs and MOSs must be related to COIs. 

- MOPs must be linked to MOEs/MOSs. 

- MOEs, MOSs, and MOPs must be consistent with the system requirements. 

- MOEs, MOSs, and MOPs must be feasible and executable in terms of time, cost, and resources. 

- MOEs, MOSs, and MOPs must comprehensively address the COI regardless of complexity or potential limitation. 

- MOEs, MOSs, and MOPs must comprehensively consider all feasible use cases. 

COI G U IDE L INE S 

1/28/2022 

7 

**COI G UIDELINES** 

## **5 COI TEST PREPARATION, STATUSING, AND REPORTING** 

## **5.1 COI TEST PREPARATION** 

The decomposition of the COIs begins in the TEMP and OT VRTMs. 

1. TEMP VRTM 

As discussed in Section 4.2, during early TEMP development, the TEMP VRTM is generated with a mapping of COIs/MOEs/MOSs/MOPs and program requirements down to the test activity level for OT and to the DT phase, as appropriate.  Detail below the COI level must be considered preliminary and may need to be revised and expanded as OT planning progresses.  As the program progresses, additional information such as that included in the Implementation Strategy and Planning Document (ISPD), the Contractor Master Test Plan (CMTP), and the System Specification provides further details that must be incorporated into the VRTM. 

2. OT VRTM 

The purpose of the OT VRTM is to address all COIs, CPRs, and other program requirements to be verified and validated as part of the OT test program.  The TEMP VRTM provides the basis for developing the OT VRTM.  During OT Test Plan development, the OT VRTM is further refined from the TEMP VRTM to map the COIs/MOEs/MOSs/MOPs and applicable program requirements from the PRD and System Specification Document to the respective OT activities and test cases in which the MOPs and requirements will be verified and validated. 

3. OT Test Plans and Procedures 

The formulation of OT plans and procedures considers operational conditions, measures, user stimuli, and scenarios that address the OT requirements identified in the OT VRTM.  The procedures must address COIs, MOEs, MOSs, and MOPs through their respective test cases. 

## **5.2 STATUS OF COIS** 

The OT Caucus is held after the completion of formal testing to assess and status the COIs.  It is chaired by the OT Test Director and is conducted to present and review all findings and test results related to the operational effectiveness and suitability of the system.  At a minimum, participants include representatives from the OT test team and the field team(s) from the user community. 

The focus of the caucus is to gain concurrence on the operational impact and criticality of all Discrepancy Reports (DRs) and Program Trouble Reports (PTRs).  In preparation for the caucus, all OT DRs and PTRs are entered into an OT Problem Traceability Matrix.  At the caucus, the matrix is reviewed to assess the impact of DRs and PTRs on COIs, MOEs, MOSs, MOPs, and CPRs, and to determine their operational criticality.  All DRs that require corrective action by the contractor are raised to PTR status.  PTRs are assigned initial priorities to assist with resolution plans.  At the caucus, each COI must be 

COI G U IDE L INE S 

1/28/2022 

8 

**COI G UIDELINES** 

addressed based on the criticality of the problem(s) impacting it.  The final status of the OT Caucus findings is documented in the OT Caucus Summary report. 

## **5.3 COI REPORTING** 

The OT Final Test Report presents specific findings related to the operational effectiveness and suitability of the system.  Conclusions regarding operational effectiveness and suitability are based on the combined results of all operational tests. Operational readiness is assessed on the basis of operational effectiveness and suitability performance in accordance with COIs and CPRs.  In addition, the report addresses the risks or system limitations associated with shortfalls in meeting mission needs, operational requirements, and safety requirements.  Identification and assessment of any new safety hazards should also be provided. 

COI G U IDE L INE S 

1/28/2022 

9 

**COI G UIDELINES** 

## **APPENDIX A — ACRONYM LIST** 

ATC Air Traffic Control CMTP Contractor Master Test Plan COI Critical Operational Issue CPR Critical Performance Requirement DR Discrepancy Report DT Development Test ERAM En Route Automation Modernization IOA Independent Operational Assessment ISD In-Service Decision ISPD Implementation Strategy and Planning Document iTEMP Initial Test and Evaluation Master Plan MOE Measure of Effectiveness MOP Measure of Performance MOS Measure of Suitability NAS National Airspace System OT Operational Test PMO Program Management Organization PRD Program Requirements Document PTR Program Trouble Report RMA Reliability, Maintainability, Availability T&E Test and Evaluation TEMP Test and Evaluation Master Plan VRTM Verification Requirements Traceability Matrix 

COI G U IDE L INE S 

1/28/2022 

10 

**COI G UIDELINES** 

## **APPENDIX B — EXAMPLES OF COIS** 

Table A-1 provides some of the best examples of Critical Operational Issues (COIs) that have been presented in Program Requirement Documents (PRDs) in recent years.  They focus on critical elements or operational objectives that must be examined during testing to determine a system’s overall capability to support mission accomplishment.  Each of the COIs focus on one or more specific functional areas that are defined in Section 3.1 of this document. 

**Table A-1. Best COIs** 

|||||**FU **|**NCTI**|**ONA**|**LARE**||**AS**|||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**NO. **|**PROGRAMCOIS**|**NAS INTEGRATION**|**PERFORMANCE**<br>**RMA**|**SUPPORTABILITY**|**DEGRADEDOPS**|**HUMANFACTORS**|**SAFETY**<br>|**SECURITY**||**ADAPTATION**|**TRANSITION**|**CERTIFICATION**|**TRAINING**|
|1.|Can the TFDM system interface and operate effectively with<br>other NAS equipment and systems without degrading NAS<br>performance?|**X**|||**X**|||||||||
|2.|Is STARS suitable for the FAA and DoD ATC operational<br>environment?|**X**||||||||||||
|3.|Is the RMA of the ASR-11 suitable for incorporation into the<br>National Airspace System (NAS) when used in operational<br>environment with the available resources, logistics plan,<br>maintenance procedures, and personnel?||**X**|**X**|**X**|||||||||
|4.|Can NEXCOM equipment be used without disruption or<br>degradation to Air Traffic Control (ATC) operations?||||**X**|||||||||
|5.|Does the TFDM system provide Computer Human Interface<br>(CHI) that supports safe and effective operation and<br>maintenance of the system?|||||**X**||||||||
|6.|Do the procedures and human-system designs for ATC and<br>technical operations support safe and effective operations for<br>the users?||**X**|||**X**|**X**|||||||



COI G U IDE L INE S 

1/28/2022 

11 

**COI G UIDELINES** 

|**NO. **|**PROGRAMCOIS**|**NAS INTEGRATION**|**PERFORMANCE**<br>**RMA**|**FU **<br>**SUPPORTABILITY**|**NCTI**<br>**DEGRADEDOPS**|**ONALAREA**<br>**HUMANFACTORS**<br>**SAFETY**<br>**SECURITY**|**S**<br>**ADAPTATION**|**TRANSITION**|**CERTIFICATION**|**TRAINING**|
|---|---|---|---|---|---|---|---|---|---|---|
|7.|Does ERAM design and site adaptation procedures allow ERAM<br>to be transitioned and adapted safely and expeditiously to all<br>sites to which it will be deployed?|||||**X**|**X**|**X**|||
|8.|Are the TFDM operational and maintenance procedures and<br>policies in place to support effective and safe Surface CDM<br>operations?|||||**X**|||||
|9.|Does the system meet the applicable physical, information, and<br>personnel security orders imposed by the FAA?|||||**X**|||||
|10.|Does the system provide adequate mitigation of security risks to<br>the system and the NAS?|||||**X**|||||
|11.|Can the OCS be installed, optimized, and adapted to site<br>conditions in the ATCSCC?||||||**X**||||
|12.|Does the NVS provide the modularity and reconfigurability<br>necessary to accommodate varying site adaptation<br>requirements?||||||**X**||||
|13.|Does the TFDM system design and procedures allow the TFDM<br>system to be optimized, adapted to site-specific conditions, and<br>certified by available personnel without disruption or degradation<br>to ATC operations?||||**X**||**X**|**X**|||
|14.|Do the system design and procedures allow the components of<br>the ASSC system to be optimized, adapted to site conditions,<br>and certified by maintenance personnel?||||||**X**||**X**||
|15.|Does TFDM design allow transition from legacy systems without<br>interruption to ATC operations?|||||||**X**|||



COI G U IDE L INE S 

1/28/2022 

12 

**COI G UIDELINES** 

|**NO. **|**PROGRAMCOIS**|**NAS INTEGRATION**|**PERFORMANCE**|**RMA**|**FU **<br>**SUPPORTABILITY**|**NCTI**<br>**DEGRADEDOPS**|**ONA**<br>**HUMANFACTORS**|**LAREA**<br>**SAFETY**<br>**SECURITY**|**S**<br>**ADAPTATION**<br>**TRANSITION**|**CERTIFICATION**|**TRAINING**|
|---|---|---|---|---|---|---|---|---|---|---|---|
|16.|Are Air Traffic, Technical Operations, Pilot and Vehicle<br>Operators training in place to allow the RWSL system to be<br>effectively operated and maintained?||||||||||**X**|
|17.|Is the TFDM ATC and Technical Operations training and<br>documentation sufficient to safely and effectively operate and<br>maintain the TFDM system?||||||||||**X**|
|18.|Does the ASR-11 provide accurate and reliable weather data<br>suitable for safe aircraft routing by air traffic control?||**X**|||||||||
|19.|Does the ASSC system detect and aid in the prevention of<br>runway collisions?||**X**|||||||||
|20.|Does RWSL provide accurate time-sensitive airport movement<br>area data for pilots and vehicle operators?||**X**|||||||||
|21.|Does the TFDM system provide timely and accurate information<br>to meet ATC operational and performance requirements?||**X**|||||||||
|22.|Does the DME equipment, subsystems, and LRUs meet the<br>performance stability requirements for intended operations?||**X**|||||||||
|23.|Does ILS provide the integrity of signal necessary to meet CAT<br>I/II/III precision approach requirements?||**X**|||||||||
|24.|Does ILS provide the continuity of service necessary to meet<br>CAT I/II/III precision approach requirements?||**X**|||||||||
|25.|Does the ILS equipment, subsystems, and LRUs meet the<br>performance stability requirements for CAT I/II/III operations?||**X**|||||||||



COI G U IDE L INE S 

1/28/2022 

13 

**COI G UIDELINES** 

## **APPENDIX C — VRTM DISCUSSION AND EXAMPLES** 

The Program Requirements Document (PRD) contains all requirements for a program, whether they will be satisfied by a product development, procedure changes, or changes to external systems that may be controlled by stakeholders other than the FAA.  The PRD has each program’s set of Critical Operational Issues (COIs). 

The Operational Test (OT) Verification Requirements Traceability Matrix (VRTM) contains the final decomposition of COIs from the Test and Evaluation Master Plan (TEMP) allocated to OT activities. 

**Table B-1.  Brief Description of the OT VRTM Column** 

|**FIELD/COLUMN/ATTRIBUTE**|**TYPE**|**DESCRIPTION**|**EXAMPLEVALUES**|**TARGET**<br>**DOCUMENT**|
|---|---|---|---|---|
|COI/MOE/MOS/MOP Text|Text|The full text of the COI, MOE, MOS, and MOP|Does the system provide the<br>ability to capture and process<br>NAS data?|OT Plan|
|COI/MOE/MOS/MOP ID|Text|The COI number from the TEMP or a<br>decomposed MOE, MOS, or MOP number|COI 1|OT Plan|
|Related PRD Requirements|Text|Any related PRD requirements|PRD 221, PRD 124, PRD 514,<br>PRD 515|OT Plan|
|Related PRD Text|Text|The full text of the applicable PRD requirement||OT Plan|
|Related SSD Requirements|Text|Any related SSD requirements||OT Plan|
|CPR (N/A or #)|Text|If this OT VRTM item relates to a CPR, or child<br>requirement of a CPR, the number from the<br>CPR table in the PRD goes here; otherwise,<br>put“N/A.”|N/A<br>4|OT Plan|
|Activity ID|Text|The name of the activity or activities in the OT<br>program where the MOE/MOS/MOP will be<br>tested.  This column may have multiple entries,<br>in “sub rows,” for multiple activities that verify<br>the MOE/MOS/MOP, such as integration<br>testing, operational effectiveness, and<br>operational suitability testing (OE/OS), etc.<br>The remaining columns would likewise need to<br>have multiple corresponding entries.|NAS Integration Testing<br>Stability Testing<br>Op. Effectiveness Testing|OT Plan|



COI G U IDE L INE S 

1/28/2022 

14 

**COI G UIDELINES** 

|**FIELD/COLUMN/ATTRIBUTE**|**TYPE**|**DESCRIPTION**|**EXAMPLEVALUES**|**TARGET**<br>**DOCUMENT**|
|---|---|---|---|---|
|Test Case ID|Text|The identifier for the procedures section and<br>steps that will include this MOE/MOS/MOP.<br>This column may be broken down into multiple<br>columns to include Case Group, or Step, as<br>per the templates for OT plans and<br>procedures.|1.5.4.1|OT<br>Procedures|
|Verification Method|Text|The method(s) that will be used for verification<br>of the MOE/MOS/MOP, usually either Analysis,<br>Demonstration, Inspection, or Test|A, D, I, T|OT Plan|
|Run Date|Date|The proposed or actual date the test case was<br>executed|Any common date format|OT Report|
|Test Result|Text|The result of test case execution|COIs: Yes, No, Limited<br>MOEs, MOSs, MOPs: Untested,<br>Pass,Fail,Partial,Deferred|OT Report|



COI G U IDE L INE S 

1/28/2022 

15 


