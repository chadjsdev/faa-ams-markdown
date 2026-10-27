---
title: "vandvguidelines"
source_url: https://fast.faa.gov/docs/vandvguidelines.pdf
source_type: pdf
converted: 2026-10-27
---
# **FAA AMS LIFECYCLE** 

# **VERIFICATION AND VALIDATION** 

# **GUIDELINES** 

**Version 4.0** 



**January 2023** 

###### **TABLE OF CONTENTS** 

|**1**<br>**INTRODUCTION ................................................................................................................................ 1**|
|---|
|1.1<br>SCOPE................................................................................................................................................. 1|
|1.2<br>V&V TERMS ANDDEFINITIONS......................................................................................................... 1<br><br>|
|_1.2.1_<br>_V&V Terms ............................................................................................................................... 1_|
|_1.2.2_<br>_V&V Definitions ....................................................................................................................... 2_|
|1.3<br>V&V PHILOSOPHY............................................................................................................................. 3|
|_1.3.1_<br>_V-Model Implementation .......................................................................................................... 5_|
|_1.3.2_<br>_Agile Acquisition/Shift-Left Principles In V&V ....................................................................... 6_|
|**2**<br>**V&V IMPLEMENTATION GUIDANCE ......................................................................................... 8**|
|2.1<br>V&V PLANNING................................................................................................................................. 8|
|2.2<br>PERFORMINGV&V ............................................................................................................................. 8<br><br>|
|_2.2.1_<br>_V&V of Work Products ............................................................................................................ 9_|
|_2.2.2_<br>_V&V of Products and Product Components .......................................................................... 10_|
|2.3<br>V&V REPORTING............................................................................................................................. 12|
|2.4<br>V&V DECISIONSUPPORT................................................................................................................. 12|
|**3**<br>**V&V APPROACH IN THE AMS LIFECYCLE ............................................................................ 14**|
|3.1<br>V&VINSERVICEANALYSIS& STRATEGICPLANNING.................................................................... 17|
|3.2<br>CONCEPT ANDREQUIREMENTSDEFINITION..................................................................................... 20|
|3.3<br>V&VININVESTMENTANALYSIS..................................................................................................... 24|
|_3.3.1_<br>_Initial Investment Analysis ..................................................................................................... 25_|
|_3.3.2_<br>_Final Investment Analysis ...................................................................................................... 30_|
|3.4<br>V&VINSOLUTIONIMPLEMENTATION............................................................................................. 37|
|3.5<br>V&VININ-SERVICEMANAGEMENT................................................................................................ 43|
|**APPENDIX A -  ACRONYMS ................................................................................................................... 49**|
|**APPENDIX B - VERIFICATION AND VALIDATION CHECKLISTS .............................................. 51**|
|**APPENDIX C - DEFINITIONS ................................................................................................................. 60**|



##### **LIST OF FIGURES** 

|Figure 1.  Work Product/Product Component/Product Relationships ................................. 2|
|---|
|Figure 2.  Basic Application of V&V .................................................................................. 4|
|Figure 3.  V-Model .............................................................................................................. 6|
|Figure 4.  AMS Lifecycle Primary V&V Activities .......................................................... 15|
|Figure 5.  AMS Rational Model for V&V ........................................................................ 17|



##### **LIST OF TABLES** 

|Table 1.  V&V in Service Analysis & Strategic Planning ................................................ 18|
|---|
|Table 2.  V&V in Concept and Requirements Definition ................................................. 21|
|Table 3.  V&V in Initial Investment Analysis ................................................................... 26|
|Table 4.  V&V in Final Investment Analysis .................................................................... 31|
|Table 5.  V&V in Solution Implementation ...................................................................... 39|
|Table 6.  V&V in In-Service Management ....................................................................... 45|



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

i 

## **1 INTRODUCTION** 

### **1.1 Scope** 

This document provides general guidance in the application of Verification and Validation (V&V) policies across the Federal Aviation Administration (FAA) Acquisition Management System (AMS) lifecycle by defining terminology, illustrating how to accomplish V&V, and describing its application in each phase of the AMS lifecycle as defined in the FAA Acquisition Management Policy.  Guidance is also provided for V&V planning, performing, and reporting to support of decision activities. 

- Section 1 defines the scope of the document, key V&V terms, and the V&V philosophy. 

- Section 2 provides V&V implementation guidance including planning, performance, reporting and decision support. 

- Section 3 defines essential work products, product components, and products and their responsible stakeholders for each decision point and phase of the AMS lifecycle. 

This document will be updated as better practices are identified and new lessons are learned.   The latest version is available on the FAA Acquisition System Toolset (FAST) website.  Additionally, the V&V Practice Toolkit contains templates and samples, advice for Subject Matter Experts (SMEs), and additional resources can be found on the FAA Acquisition Practices website. 

### **1.2 V&V Terms and Definitions** 

V&V is a disciplined approach to assess products, along with associated product components and work products throughout the lifecycle of a system, service, enterprise capability, facility, or operational change.  The conduct of V&V ensures that a quality product is built and that it satisfies operational requirements and service needs.  The order and significance of verification versus validation may change throughout the lifecycle based on the state of the mission definition, operational concept, requirements, product development, and product. 

#### **1.2.1 V&V Terms** 

V&V is performed on government and contractor work products, product components, and products and is required to be done by government and contractor organizations. Work products, product components, and products may be subject to V&V more than once during their lifecycle if modifications or additional levels of V&V are required.  The definitions of work product, product component, and product are: 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

1 

- 1) Work Product.  A work product represents, defines, or directs the final product.  A work product can include documents, processes, procedures, designs, descriptions, specifications, simulations, models, prototypes, and contracts. 

- 2) Product Component.  A product component is a lower-level part, element, or module of the product.  Product components are integrated to produce the product.  There may be multiple levels of product components. 

- 3) Product.  The final or end system, service, enterprise capability, facility, or operational change that is intended for delivery to a customer or end user. 

Figure 1 depicts the relationship between work products, product components, and products.  The early phases of the AMS lifecycle will generate several work products which must be verified and validated, such as the solution concept of operations and program requirements document that define and direct the development of product components and the final product.  Likewise, as product components become available, they too must be verified and validated before being integrated into the final product. The final product must be verified and validated before it is accepted into the operational environment. 



**Figure 1.  Work Product/Product Component/Product Relationships** 

#### **1.2.2 V&V Definitions** 

Verification ensures a product is built right according to specifications, while validation ensures the right product is built to fulfill its intended use.  More formally, verification and validation are defined as follows*: 

- 1) Verification.  Confirmation that selected work products meet their specified requirements.  This includes verification of the product (system, service, enterprise capability, or operational change) and intermediate work products 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

2 

against all applicable requirements.  Verification is inherently an incremental process since it occurs throughout the development lifecycle of the work products, beginning with initial requirements, progressing through subsequent changes, and culminating in the verification of the completed product. 

- 2) Validation.  Confirmation that a product or end product component will fulfill its intended purpose and user needs when placed in its intended environment.  The methods employed to accomplish validation are applied to selected work products and the product and product components.  The work products should be selected based on which are the best predictors of how well the product and product components will satisfy the intended purpose and user needs.  Validation can apply to all aspects of a product in its intended environments, such as operation, training, manufacturing, maintenance, or support services. 

*Note: _Capability Maturity Model Integration_<sup>_®_</sup> _(CMMI_<sup>_®_</sup> _) for Development, Version 1.2_ , Carnegie Mellon Software Engineering Institute, Pittsburgh, PA, August 2006.  The V&V definitions are consistent with Capability Maturity Model<sup>®</sup> Integration (CMMI<sup>®</sup> ).  CMMI<sup>®</sup> is an internationally recognized model for development and acquisition.  It is the best-practices model used by the Government Accountability Office as the basis for quality audits and process assessments.  V&V and Quality Assurance (QA) are complimentary processes with different purposes and objectives.  V&V focuses on ensuring that requirements are met, the overall project focuses on user/mission needs, and risk is managed.  On the other hand, QA focuses on ensuring that established processes are followed in producing the product. 

### **1.3 V&V Philosophy** 

V&V is systemically applied across the AMS lifecycle to support the FAA in creating the best products for the agency and its stakeholders National Airspace System (NAS) and non-NAS systems, services, and capabilities.  V&V supports key decisions and ensures that the developed product will fulfill mission needs and specification requirements. These products may be systems, services, capabilities, operational changes, or facilities. V&V improves a program’s overall efficiency and effectiveness and its management across the AMS lifecycle.  It is a systematic activity that supports decision-making and risk management. 

The EA is a major V&V source criterion and should be verified and validated in accordance with this guidelines document.  The EA defines the operational and technical framework for all capital assets of the FAA.  It describes the agency’s current and target architectures, as well as the transition strategy for moving from the current to the target architecture.  The V&V of critical work products and products are premised on the EA, which supports the FAA Strategic Initiatives, NAS Requirements Documents, and NAS Segment Implementation Plan (NSIP).  The EA infrastructure roadmaps are fully integrated plans of new initiatives (or upgrades to existing investments already in the field), which enhance visualization of new investments and their contribution to the NAS, including linkages to benefits, requirements, and other elements affecting the NAS.  The EA also supports the sizing and scoping of investments in terms of complexity (e.g., number of interfaces, stakeholders impacted, etc.).  Therefore, it is used to verify and validate critical work products such as needs, requirements, concepts of use, and 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

3 

strategies.  Finally, the EA is updated and refined based on the results and knowledge acquired from the conduct of V&V. 

Senior management makes decisions regarding the progress and status of an investment initiative at critical milestones (decision points) to ensure that transition throughout the AMS lifecycle is based on knowledge and acceptable risk.  In support of decisionmaking, V&V reduces risk by ensuring the information used to make the decision is accurate and dependable.  Each decision point requires the development of verified and validated work products that provide information about the progress and status of the service or product being developed. 

Figure 2 depicts a generic flow of how V&V is applied.  Current work products, products and product components are verified against requirements and validated against needs, as identified in previous work products, products, and product components.  For example, a system specification is verified against the required standards and templates that define content and format.  The system specification would be validated against the needs in the program requirements document, a higher-level specification that defines mission needs in the form of operational requirements.  The results of V&V support key program decisions and risk mitigation.  Each work product then becomes the basis for V&V of future work products (or the final product).  This process emphasizes work products developed early in the AMS lifecycle such as gap analyses, solution concept of operation documents, and requirements documents.  These work products must be validated to ensure the right product is built. 



**Figure 2.  Basic Application of V&V** 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

4 

#### **1.3.1 V-Model Implementation** 

The V-Model shown in Figure 3 illustrates that the Verification and Validation disciplines are performed throughout all phases of the AMS Lifecycle.  V&V supports key decisions and ensures that the developed product will fulfill mission needs and specification requirements.  V&V improves a program’s overall efficiency and effectiveness and its management across the AMS lifecycle. 

V&V is essential during all phases of the AMS Lifecycle as new NAS and non-NAS products, systems, services, and enterprise capabilities are developed. 

1. The arrows on the left side of the “V” focus on work products such as concepts of operation, requirements, specifications, and system architectural design. 

2. The primary V&V on the left side of the “V” is to support strategic planning and ensure key decisions are made with thoroughly vetted documentation.  The loopback arrows signify the V&V against criteria in previous work products. 

3. The right side of the “V” focuses on the test and evaluation of systems, services and capabilities throughout the development and implementation cycle. 

4. The primary V&V on the right side of the “V” is to ensure that the concept of operations, requirements, architecture integration, and design specifications are validated and verified and that systems, services and capabilities are effective and suitable for implementation into FAA operations. 

5. The arrows in the middle of the “V” represent the cross-referencing and correlation from the strategic planning side of the “V” to the testing and the integration into FAA operations.  Activities on the left side of the “V” should be conscious of the future needs required for integration into FAA operations. Activities on the right side need to remain aware of the initial driving operational concepts and requirements that originated on the left of the “V”. 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

5 



<!-- Start of picture text -->
V&V<br>Against<br>Criteria<br>V&V<br>Against<br>Criteria<br>V&V<br>Against<br>Criteria<br>V&V<br>Against<br>Criteria<br>Research for<br>Service Strategic Investment Solution In ‐ Service Feedback<br>Analysis Planning Analysis Implementation Management<br>Initial Final In ‐ Service<br>Investment Investment Decision<br>SHIFT LEFT V&V with evolving and maturing system and service capabilities in the NAS<br>8/29/2022<br><!-- End of picture text -->

**Figure 3.  V-Model** 

#### **1.3.2 Agile Acquisition/Shift-Left Principles In V&V** 

Acquisition programs may apply Agile principles to optimize programmatic implementation by applying small batches of work and fast learning cycles.  Agile acquisition is a strategy for providing multiple, rapid deliveries of incremental capabilities for operational use and evaluation. A combination of Agile principles, acquisition policies, and Program Office operations will enable the rapid delivery of systems, services, and capabilities. A primary tenet of agile acquisition is the understanding that work products (i.e., concepts, requirements, specifications, systems) are fluid and continually maturing.  To do this, Program Office; engineering; users; development; and V&V/T&E stakeholders must work across disciplines to achieve a common goal.  They iteratively define, prototype, and change program scope and requirements.  Beginning with an approach and iteratively building, testing, and demonstrating capabilities in close coordination with users.  For instance, an operational tester may collaborate with developers earlier, during the concepts of operation and requirements phase, and continue to collaborate through all of T&E. Agile acquisition principles look for iterative and adaptive product development with early and continual V&V of concepts, requirements, developed elements and integrated systems. Agile 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

6 

acquisition continually performs verification and validation to ensure that new features and capabilities work as intended when delivered and deployed. 

Shift-Left is a practice intended to find and prevent defects early in the acquisition process. It is commonly known that major defects are introduced early in the acquisition process but do not surface until later when they are more costly and challenging to resolve. The idea is to improve quality by moving tasks to the left as early in the lifecycle as possible.  This shifting to the left creates opportunities to V&V work products as soon as possible. Testers are engaged on program office teams early in the lifecycle to detect and resolve defects and issues when they are less costly and more easily addressed. 

Early and often V&V will reduce the chances of deficiencies in fielded systems.  This approach supports the start of the acquisition effort sooner with an acceptable level of immature concepts and requirements.  Structured V&V and T&E as depicted in Figure 3, will support the iterative maturity levels needed to effectively advance the acquisition to set program goals.  By adopting agile acquisition principles, programs can optimize the acquisition lifecycle and foster cost-effective, knowledge-driven outcomes through effective V&V and T&E activities. 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

7 

## **2 V&V IMPLEMENTATION GUIDANCE** 

### **2.1 V&V Planning** 

V&V planning is required for all acquisition programs and must be incorporated into the appropriate phase and program planning documents throughout the product’s lifecycle. These planning documents include, but are not limited to, the plan for Concept and Requirements Definition, plans for initial and final Investment Analysis, the Implementation Strategy and Planning Document (ISPD), the TEMP, the Program Management Plan, the System Engineering Management Plan, and the Quality Assurance Plan.  These planning documents must incorporate the V&V planning elements listed below as they apply to each document: 

- 1) Description of Verification methods 2) Description of Validation methods 3) Identification of work products, product components, and products to be verified and/or validated 

- 4) Identification of processes, standards, and criteria to be used for verification and validation at each phase of the investment initiative, such as: 

   - a) Systems Engineering Manual 

   - b) Concept Development and Validation Guidelines 

   - c) Test and Evaluation Handbook 

- 5) Identification of measures and reports required to track and document V&V events and activities 

- 6) Definition of roles and responsibilities for V&V events and activities 7) Identification of independent stakeholder(s) or reviewer(s) to perform V&V (Note: An independent stakeholder or reviewer is not directly involved in the development of the work product, product component or product being verified and validated) 

- 8) Description of tools, models, prototypes, laboratories, and simulators required to support V&V events and activities 

- 9) Identification of training required for successful completion of V&V events and activities 

Further planning guidance can be found at the following websites: 

- 1) FAA Acquisition System Toolset (FAST) website. 

- 2) ANG-E Test and Evaluation (T&E) Portal. 

### **2.2 Performing V&V** 

V&V is performed by independent stakeholders or reviewers, as identified in Tables 1 through 6, that are not directly involved with developing of the work product, product component or product being verified and validated.  While performing V&V, all independent stakeholders and reviewers must be cognizant of the validity of V&V activities performed (or missed) on prerequisite work products, product components, and 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

8 

products.  If inconsistencies or conflicts are found with the validity of previous V&V activities, or if it is determined that a requisite V&V activity was not performed, these issues must be documented and resolved before proceeding. 

Critical technical documents that form the basis for future work products, product components, or products during a program’s lifecycle must be verified and validated before their use in all subsequent processes including the V&V process.  These critical technical documents include the NAS Concept of Operations, the NAS Requirements Document, the NAS Segment Implementation Plan, the National Air Research Plan, the NextGen Implementation Plan, and the Enterprise Architecture.  V&V of these critical technical documents is necessary to ensure a valid basis for programs, that no service gaps exist, and that programs align with the Agency’s overall goals.  The criteria used for the V&V of these documents are the FAA Strategic Initiatives document and all applicable standards associated with the document (i.e., manuals, handbooks, templates, and guidance documents). 

#### **2.2.1 V&V of Work Products** 

All major work products developed by a program or that are required by the acquisition category should be subject to formal and structured V&V in accordance with processes and standards described in this document.  A work product represents, defines, or directs product components and the product (system, service, capability, facility, or operational change).  This includes solution concepts of operation, processes, plans, procedures, designs, descriptions, requirements, specifications, models, prototypes, contracts, and other documents.  The scope of specific verification and validation activities for work products and the specific work products to undergo V&V will vary based on program complexity and available resources.  Section 3 of this document identifies the minimum set of work products (if required for the acquisition) that must undergo V&V during the AMS lifecycle. 

##### **<u>Verification</u>** 

Work product verification ensures that standards, templates, or other requirements that define their content and purpose are properly followed. 

The primary verification methods for work products are listed below.  The verification of a specific work product will use one or more of these methods to ensure the work product’s consistency, completeness, and correctness.  Definitions and descriptions of these methods can be found in Appendix C. 

##### **<u>Work Product Verification Methods</u>** 

- Inspections 

- Peer reviews 

- Audits 

- Checklists 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

9 

##### **<u>Validation</u>** 

Work product validation ensures that the work product supports the development of an operationally effective and suitable product. 

The primary validation methods for work products are listed below.  The validation of a specific work product will use one or more of these methods to ensure that they support the product’s intended use.  Definitions and descriptions of these methods can be found in Appendix C. 

##### **<u>Work Product Validation Methods</u>** 

- Discussions with users 

- User surveys 

- Functional presentations 

- Walk-throughs/dry runs 

- Inspections 

- Peer reviews 

- Audits 

- Analyses 

- Checklists 

- Testing 

- Demonstrations 

- Modeling 

- Storyboarding 

#### **2.2.2 V&V of Products and Product Components** 

As defined previously in Paragraph 1.2.1, a product is a system (hardware and/or software), service, capability, facility, or operational change intended for delivery to a customer or end user.  Product components are lower-level elements of the product, which are integrated to produce the final product.  V&V is performed on both products and product components.  Verification ensures that products or product components have been built properly to the specifications delineated in supporting work products. Validation ensures that product components and final integrated products are operationally effective and suitable to end users and maintainers.  The scope of verification and validation activities for products and product components will vary based on the program’s complexity and available resources. 

V&V of products and product components is primarily accomplished via Test and Evaluation (T&E).  While V&V efforts performed by T&E personnel occur in all phases of the AMS lifecycle, T&E of products and product components primarily occurs in Solution Implementation and In-Service Management.  During Solution Implementation, T&E is divided into three major activities:  Development Test (DT), Operational Test (OT), and Independent Operational Assessment (IOA). 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

10 

DT supports verification objectives, ensuring the product or product component under test meets all specified technical and performance requirements.  Additionally, for final products, DT verifies that the product is fully integrated and stable and has no adverse effect on the rest of the NAS.  DT is conducted by the product or product component developer and witnessed by FAA witnessed. 

The verification of a specific product or product component uses one or more of the primary verification methods listed below.  Definitions and descriptions of these methods can be found in Appendix C. 

##### **<u>Product and Product Component Verification Methods</u>** 

- Inspections 

- Peer reviews 

- Audits 

- Analyses 

- Checklists 

- Testing 

- Demonstrations 

- Simulations 

- Accreditation 

OT and IOA support validation objectives, ensuring that major product components and the final product are operationally effective and suitable for use in the NAS and that the NAS infrastructure is ready to accept the product.  OT is performed by the OT Test Director and OT test team with Air Traffic (AT), Technical Operations, and second-level maintenance personnel. Other participants may include representatives of other FAA organizations and/or external entities (e.g., airlines, cargo carriers, military, and private industry) as required.  For designated products, an IOA is led by a program manager from the Independent Safety Assessment Team and provides decision-makers with an independent determination of operational readiness in support of deployment decisions (such as an in-service decision). 

The validation of a specific product or major product component will use one or more of the primary validation methods listed below.  Definitions and descriptions of these methods can be found in Appendix C. 

##### **<u>Product and Product Component Validation Methods</u>** 

- Discussions with users 

- User evaluation questionnaires 

- Functional presentations 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

11 

- Inspections 

- Peer reviews 

- Audits 

- Analyses 

- Checklists 

- Testing 

- Demonstrations 

- Simulations 

### **2.3 V&V Reporting** 

V&V reporting supports AMS decision points and should be factored into the entrance criteria for these major decisions.  Quality V&V reporting promotes informed decisionmaking and contributes to the overall effectiveness and efficiency of the program.  V&V reports also support performance measurement and analysis by providing quantitative and qualitative results against the program’s technical performance criteria. 

The following practices are essential to quality V&V reporting: 

- 1) V&V events must be documented, and the corresponding documentation must be controlled and archived to ensure that historical records are kept. 

- 2) V&V reporting should consider that specific decision-making events, risk management, and work products will be based on the information contained in the report. 

- 3) V&V reporting on the quality of work products should identify how well the work product supports the development of an operationally effective and suitable product. 

- 4) V&V reporting of the results of test and evaluation activities (contained in final test reports) should identify how well the product or product component is built and to what degree it fulfills operational needs. 

- 5) The report should at a minimum contain the following: 

   - a. Introduction 

   - b. Purpose – Objectives of the V&V event 

   - c. Criteria – Source criteria that are used as a basis for the V&V event 

   - d. V&V Approach – Description of the V&V event 

   - e. V&V Participants 

   - f. V&V Results 

   - g. Recommendations 

### **2.4 V&V Decision Support** 

The performance of structured V&V before planned decision points, such as Concept and Requirements Definition Readiness Decision (CRDRD); Investment Readiness Decision (IARD); Initial Investment Decision (IIA); Final Investment Decision (FID); and InService Decision (ISD), reduces the risk of defects in a work product, product components, or product that supports these decisions by ensuring completeness and 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

12 

quality.  Structured V&V aids decision-makers, such as the Joint Resources Council, the Acquisition Executive Board, and designated in-service decision authorities by providing assessments of critical work products for each acquisition management phase and by discovering risk levels (both technical and non-technical) that affect program success. For example, V&V applied against program planning documentation may uncover inconsistencies within the document and its predecessor documents which could lead to increased risk, increased cost, and schedule delays. The tables in section 3 identify for each decision point what work products are subject to V&V, the criteria to be used to V&V the work products, and the stakeholders responsible for the V&V of the work products. 

The following practices are essential to V&V decision support: 

- 1) V&V events and results should be formally identified in plans as entrance criteria for associated decision points. 

- 2) V&V events and their results should be scheduled and planned well in advance of decision points. 

- 3) V&V results must be consistently applied so that decision-makers have reliable data and information for making sound and low-risk decisions based on the maturity and quality of work products. 

- 4) V&V results must support the objectives of the associated decision point before accepting/approving results. 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

13 

## **3 V&V APPROACH IN THE AMS LIFECYCLE** 

The AMS lifecycle is comprised of the following phases: 

- Service Analysis & Strategic Planning (SASP) 

- Concept & Requirements Definition (CRD) 

- Investment Analysis (IA) 

- Solution Implementation (SI) 

- In-Service Management (ISM) 

In addition to these formal phases, Research for Service Analysis (RSA) is a separate activity that precedes and/or is conducted during the early phases of the AMS lifecycle. RSA matures and validates new concepts and technologies for potential investment and deployment in the NAS.  RSA may also provide information that supports SASP, CDR, IA, and the early stages of SI.  The independent stakeholders and reviewers responsible for the V&V of RSA activities are the same as those for SASP, CRD, IA, and SI. 

The V&V process incorporates common tools and techniques for verifying and validating work products, product components, and products.  This V&V process ensures the quality of work products, product components, and products which are the outputs of each AMS phase necessary to make informed decisions and provides the basis for the next AMS phase.  However, the specific items undergoing V&V and the independent stakeholders and reviewers responsible for conducting V&V vary depending on the phase or activity of the AMS lifecycle. 

All critical work products, product components, and products, including those used as V&V criteria, are subject to systematic V&V by various program disciplines during every activity/phase of the lifecycle.  Each functional discipline plans, executes, and reports on V&V in accordance with AMS and standardized integrated processes maintained by the respective organization. 

While both verification and validation activities occur throughout the AMS lifecycle, Figure 4 depicts only the primary emphasis of V&V between the major decision points. For the complete set of minimum required V&V activities by lifecycle, see Tables 1-6. 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

14 



**Figure 4.  AMS Lifecycle Primary V&V Activities** 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

15 

Five primary management documents are required to support critical decision points early in the acquisition lifecycle.  They are essential for planning, management, and control of the entire acquisition lifecycle and are subject to formal and structured V&V. These documents and their purpose are provided below: 

1. Acquisition Program Baseline - Establishes the performance, cost, and schedule baselines for an investment program segment 

2. Program Requirements Document - Defines the operational framework and performance requirements an investment program must achieve 

3. Business Case - Summarizes results of the business case analysis and provides the analytical and quantitative basis for investment decisions 

4. Implementation Strategy and Planning Document - Defines overall implementation strategy and planning for an investment program 

5. Program Management Plan - Defines how the service team will manage the investment program to execute the strategy in the ISPD 

Appendix B provides four checklists to aid in the V&V of the PRD, APB, ISPD, and PMP.  Each checklist identifies the key elements in each document that must be verified or validated.  The methods used and the artifacts produced must be identified for each of these key elements.  These checklists provide authors with a structure that will help ensure that the documents accurately provide the information required for the approving authorities to make critical lifecycle decisions. 

The Investment Planning & Analysis office is responsible for verifying and validating the Business Case as described in the AFI Business Case Evaluation and Assessment Guideline.  The Investment Planning and Analysis Independent Evaluation Review (IER) satisfies the documentation and reporting requirements for the V&V of the Business Case. 

Figure 5 is a static representation of the AMS Relational Model (ARM). The ARM for V&V distills undocumented knowledge of AMS work product relationships into a simplified interactive visualization tool.  The ARM addresses the entire Acquisition Lifecycle from the initial concept to In-Service. This model is not a process flow but rather a contextual relationship diagram specifically focused on products where V&V strategies and practices can be applied during the lifecycle.  The model enables the user to trace an acquisition document back to its parent (driving) document(s) or forward to dependent related work products and into a thoroughly tested solution. The interactive ARM is available on the FAST. 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

16 



**Figure 5.  AMS Rational Model for V&V** 

### **3.1 V&V in Service Analysis & Strategic Planning** 

Service Analysis & Strategic Planning is the process used to determine what capabilities must be in place now and in the future to meet agency goals and the service needs of customers.  Results are captured in the “as is” and “to be” states of the EA, as well as the roadmaps for moving from the current state to the future state.  The responsible Line of Business includes the results in their business plans and service organizations describe them in their operating plans.  These activities develop the information necessary for determining which service shortfalls or new ideas for improving service delivery are approved for inclusion in agency strategic planning documents. 

The primary focus of V&V during SASP is to verify and validate the Preliminary Shortfall Analysis, the Concept & Requirements Definition Plan and the ISS Risk Factors Assessment. 

Table 1 identifies the following for Service Analysis & Strategic Planning: 

- The major decision points 

- The minimum required work products that must be verified and validated at the decision point 

- The criteria that each work product must be verified and validated against 

- The stakeholders responsible for each V&V activity 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

17 

**<u>Table 1.  V&V in Service Analysis & Strategic Planning</u>**<sup>**1**</sup> 

|**Decision Point**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
|Concept and<br>Requirements<br>Definition<br>Readiness<br>Decision|Preliminary Shortfall<br>Analysis|Validation:<br>• Enterprise<br>Architecture<br>• NextGen<br>Implementation<br>Plan<br>• NAS Segment<br>Implementation<br>Plan<br>• FAA Strategic<br>Initiatives<br>• National Air<br>Research Plan<br>(NARP) (if<br>applicable)<br>• NAS ConOps|Lines of Business<br>(Mission<br>Support)/Service<br>Team (NAS),<br>Office of<br>Investment<br>Planning &<br>Analysis, and<br>Advanced<br>Concepts and<br>Technology<br>Development<br>Office|
|||Verification:<br>• Guidelines for<br>Service Analysis<br>Planning and<br>Concept and<br>Requirements<br>Definition<br>• Service Shortfall<br>Analysis<br>Guidance and<br>Templates<br>• AMS Policy||



> 1 Table 1 content is based on AMS policy as of the time this document was published.  Detailed guidelines for the SASP AMS lifecycle phase and document template exists and should be reviewed for current guidance. 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

18 

|Enterprise Architecture|Validation:|Enterprise|
|---|---|---|
|Change Notices,|• Shortfall|Architecture|
|Products, and|Analysis|Control Board|
|Amendments|• Service Needs<br>• Enterprise<br>Architecture<br>• Solution<br>Concept of<br>Operations<br>• NAS Segment<br>Implementation<br>Plan<br>• NAS<br>Requirements<br>Documents<br>• FAA Strategic<br>Initiatives|(NAS and Mission<br>Support) and<br>ANG Engineering<br>Services<br>FAA Enterprise<br>Architecture<br>Board|
||Verification:<br>• Templates for<br>Enterprise<br>Architecture<br>Change Notices,<br>Products, and<br>Amendments<br>• NAS Integrated<br>Systems<br>Engineering<br>Framework||
|Concept and<br>Requirements<br>Definition Plan|Validation:<br>• Enterprise<br>Architecture<br>• NextGen<br>Implementation<br>Plan<br>• NAS Segment<br>Implementation<br>Plan<br>Verification:<br>• Guidelines for<br>Service Analysis<br>Planningand|Lines of Business<br>(Mission<br>Support)/Service<br>Team (NAS)|



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

19 

|**Decision Point**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
|||Concept and<br>Requirements<br>Definition<br>• AMS Policy||
||ISS Risk Factors<br>Assessment|Validation<br>• FIPS-199<br>Security<br>Categorization<br>Table|Lines of Business<br>(Mission<br>Support)/Service<br>Team (NAS)|
|||Verification<br>• Information<br>Security<br>Guidance for<br>System<br>Acquisition<br>(ISGSA)||



### **3.2 Concept and Requirements Definition** 

Concept and Requirements Definition translates priority operational needs in the EA into preliminary requirements and a solution concept of operations for the capability needed to improve service delivery.  It also quantifies the service shortfall in sufficient detail for the definition of realistic preliminary requirements and an estimation of potential costs and benefits.  Finally, CRD identifies the most promising alternative solutions to satisfy the service need, one of which must be the alternative in the EA. 

The primary focus of V&V during CRD is to validate the preliminary program requirements, the concept of use, EA products and amendments, shortfall analysis, the initial investment analysis plan, and the Preliminary ISS Assessment to ensure that the existing or planned product properly addresses mission needs. 

Table 2 identifies the following for CRD: 

- The major decision points 

- The minimum required work products that must be verified and validated at the decision point 

- The criteria that each work product must be verified and validated against 

- The stakeholders responsible for each V&V activity 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

20 

|**Decision Point**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
|Investment<br>Analysis<br>Readiness<br>Decision|Solution Concept of<br>Operations<br>(Concept development<br>and validation focusing<br>on technical and<br>operational feasibility)|Validation:<br>• Enterprise<br>Architecture<br>• NextGen<br>Implementation<br>Plan<br>• NAS Segment<br>Implementation<br>Plan<br>• NAS<br>Requirements<br>Documents|Lines of Business<br>(Mission<br>Support)/Service<br>Team (NAS) and<br>ANG Engineering<br>Services|
|||Verification:<br>• Guidelines for<br>Service Analysis<br>Planning and<br>Concept and<br>Requirements<br>Definition<br>• Concept of<br>Operations<br>Guidance and<br>Template<br>• Preliminary ISS<br>Assessment||



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

21 

|**Decision Point**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
||preliminary Program<br>Requirements<br>Document|Validation:<br>• Enterprise<br>Architecture<br>• Solution Concept<br>of Operations<br>• NAS<br>Requirements<br>Documents|Lines of Business<br>(Mission<br>Support)/Service<br>Team (NAS) and<br>ANG Engineering<br>Services|
|||Verification:<br>• Program<br>Requirements<br>Document<br>template<br>• System<br>Engineering<br>Manual<br>• AMS Policy||
||Enterprise Architecture<br>products and<br>amendments|<br>Validation:<br>• Enterprise<br>Architecture<br>• Solution Concept<br>of Operations<br>• preliminary<br>Program<br>Requirements<br>Document<br>• NAS Segment<br>Implementation<br>Plan<br>• NAS<br>Requirements<br>Documents<br>• FAA Strategic<br>Initiatives|Enterprise<br>Architecture<br>Control Board<br>(NAS and<br>Mission Support)<br>and ANG<br>Engineering<br>Services|
|||Verification:<br>• NAS Integrated<br>Systems<br>Engineering<br>Framework||



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

22 

|**Decision Point**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
||Shortfall Analysis|Validation:<br>• Enterprise<br>Architecture<br>• NextGen<br>Implementation<br>Plan<br>• NAS Segment<br>Implementation<br>Plan<br>• FAA Strategic<br>Initiatives<br>• NARP (if<br>applicable)<br>• Operational<br>analysis report(s)<br>(if applicable)<br>• Preliminary<br>Shortfall<br>Analysis V&V<br>results (if<br>applicable)|Lines of Business<br>(Mission<br>Support)/Service<br>Team (NAS) and<br>ANG Engineering<br>Services|
|||Verification:<br>• Guidelines for<br>Service Analysis<br>Planning and<br>Concept and<br>Requirements<br>Definition<br>• Shortfall<br>Analysis<br>Guidance<br>• AMS Policy||



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

23 

|**Decision Point**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
||Initial Investment<br>Analysis plan|Validation:<br>• Solution Concept<br>of Operations<br>• preliminary<br>Program<br>Requirements<br>Document<br>• Enterprise<br>Architecture<br>Verification:<br>• Initial Investment<br>Analysis Plan<br>Guidance and<br>Template<br>• AMS Policy|Lines of Business<br>(Mission<br>Support)/Service<br>Team (NAS),<br>Office of<br>Investment<br>Planning and<br>Analysis AFI, and<br>ANG Engineering<br>Services|
|Investment<br>Analysis<br>Readiness<br>Decision|Preliminary ISS<br>Assessment|Validation<br>• FIPS-199<br>Security<br>Categorization<br>Table|Lines of Business<br>(Mission<br>Support)/Service<br>Team (NAS)|
|||Verification<br>• Information<br>Security<br>Guidance for<br>System<br>Acquisition<br>(ISGSA)||



**Table 2.  V&V in Concept and Requirements Definition**<sup>**2**</sup> 

### **3.3 V&V in Investment Analysis** 

IA is a flexible process tailored for the specific analysis to be performed.  Tailoring actions are approved by the Acquisition Executive or the Investment Decision Authority (IDA) and recorded in the appropriate plan and record of decision for Initial or Final Investment Analysis. 

> 2 Table 2 content is based on AMS policy as of the time this document was published. Detailed guidelines for the CRD AMS lifecycle phase and document template exists and should be reviewed for current guidance. 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

24 

#### **3.3.1 Initial Investment Analysis** 

Initial Investment Analysis evaluates alternative solutions to mission needs and provides realistic options to the IDA that satisfies FAA strategic and performance goals and achieves the best overall value for the FAA and its customers.  The main outputs are the initial PRD, initial ISPD, initial Business Case, preliminary Test and Evaluation Master Plan (TEMP), updated EA products and amendments, and plan for Final Investment Analysis. 

The primary focus of V&V during the Initial Investment Analysis is to validate the previously mentioned work products to ensure the selection of the best alternative for implementation. 

Table 3 identifies the following for Initial Investment Analysis: 

- The major decision points 

- The minimum required work products that must be verified and validated at the decision point 

- The criteria that each work product must be verified and validated against 

- The stakeholders responsible for each V&V activity 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

25 

##### **Table** **<u>3. V&V in Initial Investment Analysis</u>**<sup>**3**</sup> 

|**Decision Point**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
|Initial Investment<br>Decision|initial Program<br>Requirements<br>Document|Validation:<br>• Enterprise<br>Architecture<br>• Solution<br>Concept of<br>Operations<br>• Functional<br>Analyses<br>Products<br>• Results of<br>assessments<br>conducted<br>during Initial<br>Investment<br>Analysis<br>• NAS<br>Requirements<br>Documents<br>• preliminary<br>Program<br>Requirements<br>Document<br>V&V Results<br>• Initial ISS<br>assessment|Investment<br>Analysis Team<br>(includes all<br>specialists as<br>defined in AMS<br>Policy Section<br>2.5.1) and ANG<br>Engineering<br>Services|
|||Verification:<br>• Program<br>Requirements<br>Document<br>template<br>• System<br>Engineering<br>Manual<br>• AMS Policy<br>• ISGSA||



> 3 Table 3 content is based on AMS policy as of the time this document was published. Detailed guidelines for the Initial Investment Analysis AMS lifecycle phase and document template exists and should be reviewed for current guidance. 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

26 

|**Decision Point**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
||initial Business Case|Validation:<br>• Enterprise<br>Architecture<br>• Solution<br>Concept of<br>Operations<br>• Functional<br>Analyses<br>Products<br>• initial Program<br>Requirements<br>Document|Investment<br>Analysis Team<br>(includes all<br>specialists as<br>defined in AMS<br>Policy Section<br>2.5.1) and Office<br>of Investment<br>Planning and<br>Analysis|
|||Verification:<br>• Business Case<br>template<br>• AMS Policy||
||initial Implementation<br>Strategy and Planning<br>Document|Validation:<br>• Enterprise<br>Architecture<br>• initial Program<br>Requirements<br>Document<br>• initial Business<br>Case<br>• Solution<br>Concept of<br>Operations<br>Verification:<br>• Implementation<br>Strategy and<br>Planning<br>Document<br>template<br>• AMS Policy|Investment<br>Analysis Team<br>(includes all<br>specialists as<br>defined in AMS<br>Policy Section<br>2.5.1)|



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

27 

|**Decision Point**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
||preliminary Test and<br>Evaluation Master Plan|Validation:<br>• initial<br>Implementation<br>Strategy and<br>Planning<br>Document<br>• initial Program<br>Requirements<br>Document<br>• initial Business<br>Case<br>• Solution<br>Concept of<br>Operations|Investment<br>Analysis Team<br>(includes all<br>specialists as<br>defined in AMS<br>Policy Section<br>2.5.1), ANG-E<br>Test Standards<br>Board|
|||Verification:<br>• Test and<br>Evaluation<br>Handbook<br>• TEMP<br>template<br>• AMS Policy||



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

28 

|**Decision Point**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
||Enterprise Architecture<br>products and<br>amendments|Validation:<br>• Enterprise<br>Architecture<br>• Solution<br>Concept of<br>Operations<br>• initial Program<br>Requirements<br>Document<br>• NAS Segment<br>Implementation<br>Plan<br>• NAS<br>Requirements<br>Documents<br>• FAA Strategic<br>Initiatives|Enterprise<br>Architecture<br>Control Board<br>(NAS and Mission<br>Support) and ANG<br>Engineering<br>Services|
|||Verification:<br>• NAS Integrated<br>Systems<br>Engineering<br>Framework||



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

29 

|**Decision Point**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
||final Investment<br>Analysis plan|Validation:<br>• Enterprise<br>Architecture<br>• Solution<br>Concept of<br>Operations<br>• Functional<br>Analyses<br>Products<br>• initial Program<br>Requirements<br>Document<br>• Results of<br>assessments<br>conducted<br>during Initial<br>Investment<br>Analysis<br>Verification:<br>• Investment<br>Analysis Plan<br>template<br>• AMS Policy|Investment<br>Analysis Team<br>(includes all<br>specialists as<br>defined in AMS<br>Policy Section<br>2.5.1) and Office<br>of Investment<br>Planning and<br>Analysis.|



#### **3.3.2 Final Investment Analysis** 

Final Investment Analysis develops detailed plans and final requirements for the selected investment opportunity.  The principal outputs are program baseline work products, including final PRD, final BC, final ISPD, APB, Program Management Plan (PMP), initial TEMP, updated EA products and amendments, tailored In-Service Review (ISR) checklist and the Screening Information Request (SIR). 

The primary focus of V&V during the Final Investment Analysis is to validate the previously mentioned work products to mitigate risk and support the implementation of the best alternative. 

Table 4 identifies the following for Final Investment Analysis: 

- The major decision points 

- The minimum required work products that must be verified and validated at the decision point 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

30 

- The criteria that each work product must be verified and validated against 

- The stakeholders responsible for each V&V activity 

**<u>Table 4.  V&V in Final Investment Analysis</u>**<sup>**4**</sup> 

|**Decision Point**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
|Final Investment<br>Decision|final Program<br>Requirements<br>Document|Validation:<br>• Enterprise<br>Architecture<br>• Solution<br>Concept of<br>Operations<br>• Functional<br>Analyses<br>Products<br>• Results of<br>assessments<br>conducted<br>during Final<br>Investment<br>Analysis<br>• NAS<br>Requirement<br>Documents<br>• initial Program<br>Requirements<br>Document<br>V&V Results<br>• Final ISS<br>Assessment|Investment<br>Analysis Team<br>(includes all<br>specialists as<br>defined in AMS<br>Policy Section<br>2.5.1) and ANG<br>Engineering<br>Services|
|||Verification:<br>• Program<br>Requirements<br>Document<br>template<br>• System<br>Engineering<br>Manual<br>• AMS Policy||



> 4 Table 4 content is based on AMS policy as of the time this document was published. Detailed guidelines for the Final Investment Analysis AMS lifecycle phase and document template exists and should be reviewed for current guidance. 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

31 

|**Decision Point**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
||final Business Case|Validation:<br>• Enterprise<br>Architecture<br>• Solution<br>Concept of<br>Operations<br>• Functional<br>Analyses<br>Products<br>• final Program<br>Requirements<br>Document<br>• Results of<br>assessments<br>conducted<br>during Final<br>Investment<br>Analysis<br>• initial Business<br>Case V&V<br>Results|Investment<br>Analysis Team<br>(includes all<br>specialists as<br>defined in AMS<br>Policy Section<br>2.5.1) and Office<br>of Investment<br>Planning and<br>Analysis|
|||Verification:<br>• Business Case<br>Analysis<br>Guidelines<br>• AMS Policy||



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

32 

|**Decision Point**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
||Acquisition Program<br>Baseline|Validation:<br>• Enterprise<br>Architecture<br>• Solution<br>Concept of<br>Operations<br>• Functional<br>Analyses<br>Products<br>• final Program<br>Requirements<br>Document<br>• Business Case|Investment<br>Analysis Team<br>(includes all<br>specialists as<br>defined in AMS<br>Policy Section<br>2.5.1), Office of<br>Investment<br>Planning and<br>Analysis, and<br>Office of Budget<br>and Programs|
|||Verification:<br>• FAA<br>Acquisition<br>Baseline<br>Management<br>Standard<br>Operating<br>Procedure<br>• Acquisition<br>Program<br>Baseline<br>Template<br>• AMS Policy||
||Program Management<br>Plan|Validation:<br>• final ISPD<br>• final Program<br>Requirements<br>Document<br>• final Business<br>Case<br>Verification:<br>• Program<br>Management<br>Plan Template<br>• AMS Policy|Investment<br>Analysis Team<br>(includes all<br>specialists as<br>defined in AMS<br>Policy Section<br>2.5.1), Office of<br>Investment<br>Planning and<br>Analysis, and<br>Office of Budget<br>and Programs|



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

33 

|**Decision Point**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
||initial Test and<br>Evaluation Master Plan|Validation:<br>• final<br>Implementation<br>Strategy and<br>Planning<br>Document<br>• final Program<br>Requirements<br>Document<br>• final Business<br>Case<br>• Acquisition<br>Program<br>Baseline<br>• preliminary<br>Test and<br>Evaluation<br>Master Plan<br>V&V Results|Investment<br>Analysis Team<br>(includes all<br>specialists as<br>defined in AMS<br>Policy Section<br>2.5.1), ANG-E<br>Test Standards<br>Board|
|||Verification:<br>• Test and<br>Evaluation<br>Handbook<br>• TEMP template<br>• AMS Policy||



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

34 

|**Decision Point**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
||Updated Enterprise<br>Architecture products<br>and amendments|Validation:<br>• Enterprise<br>Architecture<br>• Solution<br>Concept of<br>Operations<br>• final Program<br>Requirements<br>Document<br>• NAS Segment<br>Implementation<br>Plan<br>• NAS<br>Requirements<br>Documents<br>• FAA Strategic<br>Initiatives|Enterprise<br>Architecture<br>Control Board<br>(NAS and<br>Mission Support)<br>and ANG<br>Engineering<br>Services|
|||Verification:<br>• NAS Integrated<br>Systems<br>Engineering<br>Framework||



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

35 

|**Decision Point**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
||final Implementation<br>Strategy and Planning<br>Document|Validation:<br>• Enterprise<br>Architecture<br>• final Program<br>Requirements<br>Document<br>• Business Case<br>• initial<br>Implementation<br>Strategy and<br>Planning<br>Document<br>V&V Results|Investment<br>Analysis Team<br>(includes all<br>specialists as<br>defined in AMS<br>Policy Section<br>2.5.1)|
|||Verification:<br>• Implementation<br>Strategy and<br>Planning<br>Document<br>template<br>• AMS Policy||
||Tailored In-Service<br>Review Checklist|Validation:<br>• Implementation<br>Strategy and<br>Planning<br>Document<br>• final Program<br>Requirements<br>Document<br>• Solution<br>Concept of<br>Operations|Investment<br>Analysis Team<br>(includes all<br>specialists as<br>defined in AMS<br>Policy Section<br>2.5.1)|
|||Verification:<br>• In-Service<br>Review<br>Checklist<br>template<br>• AMS Policy||



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

36 

|**Decision Point**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
||Screening Information<br>Request, including:<br>• Statement of Work<br>• Contract Data<br>Requirements List/<br>Data Item<br>Descriptions<br>• System<br>Specification|Validation:<br>• final Program<br>Requirements<br>Document<br>• Implementation<br>Strategy and<br>Planning<br>Document<br>• initial Test &<br>Evaluation<br>Master Plan|Investment<br>Analysis Team<br>(includes all<br>specialists as<br>defined in AMS<br>Policy Section<br>2.5.1) and the<br>Contracting<br>Officer|
|||Verification:<br>• Statement of<br>Work template<br>• Templates for<br>DD Form 1423-<br>1 and DD Form<br>1664<br>• System<br>Specification<br>template<br>• AMS Policy||



### **3.4 V&V in Solution Implementation** 

The overarching goal of SI is to satisfy user requirements and achieve the benefit targets in the Business Case.  Plans and baselines from the Final Investment Analysis are revalidated and updated, if necessary, after/before contract award – typically through the FAA Integrated Baseline Review (IBR) process – to ensure they can realistically serve as the management construct for program implementation.  SI involves the following seven major activities: 

- 1) Finalize program planning 

- 2) Obtain the solution 

- 3) Verify operational readiness 

- 4) Prepare for In-Service Decision 

- 5) Update planning for ISM 

- 6) In-Service Decision 

- 7) Deploy solution at all sites 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

37 

The primary focus of V&V during Solution Implementation is to verify and validate products and product components and their associated work products that serve as the artifacts of these activities.  Developmental and operational testing are the primary methods used to verify and validate the product and product components.  To support these tests, plans, procedures, and reports are generated which must be verified and validated to ensure test results provide accurate and complete data to support the InService Decision.  In addition to the primary V&V activities, technical milestones such as the Preliminary Design Review (PDR) and Critical Design Review (CDR) also represent key opportunities for the conduct of a structured V&V of the system/service allocated and product baselines respectively. 

Table 5 identifies the following for SI: 

- The major decision points 

- The minimum required work products, product components, and products that must be verified and validated at each decision point 

- The criteria that each work product, product component, or product must be verified and validated against 

- The stakeholders responsible for each V&V activity 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

38 

**<u>Table 5.  V&V in Solution Implementation</u>**<sup>**5**</sup> 

|**Decision Points**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
|Contract Award|Contract including:<br>• Updated Statement<br>of Work<br>• Updated Contract<br>Data Requirements<br>List/ Data Item<br>Descriptions<br>• Updated System<br>Specification|Validation:<br>• Final Program<br>Requirements<br>Document<br>• Implementation<br>Strategy and<br>Planning<br>Document<br>• Results from<br>negotiations<br>with contractor|Service Team<br>(including<br>functional<br>organizations<br>such as systems<br>engineering, test<br>and evaluation,<br>etc.) and<br>Contracting<br>Officer|
|||Verification:<br>• Statement of<br>Work template<br>• Templates for<br>DD Form<br>1423-1 and DD<br>Form 1664<br>• System<br>Specification<br>template||



> 5 Table 5 content is based on AMS policy as of the time this document was published. Detailed templates and guidance for the SI AMS lifecycle exist and should be reviewed for current direction. AMS Lifecycle Verification and Validation Guidelines                             January 2023 

39 

|**Decision Points**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
||final Test and<br>Evaluation Master Plan|Validation:<br>• final<br>Implementation<br>Strategy and<br>Planning<br>Document<br>• final Program<br>Requirements<br>Document<br>• final Business<br>Case<br>• Acquisition<br>Program<br>Baseline<br>• Updated<br>Statement of<br>Work<br>• Updated<br>Contract Data<br>Requirements<br>List/ Data Item<br>Descriptions<br>• initial Test and<br>Evaluation<br>Master Plan<br>V&V Results|Investment<br>Analysis Team<br>(includes all<br>specialists as<br>defined in AMS<br>Policy Section<br>2.5.1), ANG-E<br>Test Standards<br>Board|
|||Verification:<br>• Test and<br>Evaluation<br>Handbook<br>• TEMP<br>template<br>• AMS Policy||



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

40 

|**Decision Points**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
|Product<br>Demonstration<br>Decision (if required)|Contract Specifications<br>(Decomposed from the<br>FAA System<br>Specification)|Validation:<br>• FAA System<br>Specification<br>• Contract<br>Verification:<br>• Statement of<br>Work<br>• Data Item<br>Description<br>from contract<br>for<br>specifications|Service Team<br>(including<br>functional<br>organizations<br>such as systems<br>engineering, test<br>and evaluation,<br>etc.)|
||Design Documents|Validation:<br>• Contractor<br>System<br>Specification<br>• Contract<br>Verification:<br>• Data Item<br>Description<br>from contract<br>for design<br>documents|Service Team<br>(including<br>functional<br>organizations<br>such as systems<br>engineering, test<br>and evaluation,<br>etc.)|



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

41 

|**Decision Points**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
|Product<br>Acceptance/Contractor<br>Acceptance and<br>Inspection (CAI)<br>Production Decision<br>(if required)<br>In-Service Decision|System/Service<br>_Note: Major V&V_<br>_activities include DT, OT,_<br>_and IOA_|Validation:<br>• Final Program<br>Requirements<br>Document<br>including<br>Critical<br>Operational<br>Issues and<br>Critical<br>Performance<br>Requirements<br>• Solution<br>Concept of<br>Operations<br>Verification:<br>• System<br>Specification<br>and/or lower-<br>level<br>specifications<br>• Safety Risk<br>Management<br>Document<br>|Service Team<br>(including<br>functional<br>organizations<br>such as systems<br>engineering, test<br>and evaluation,<br>etc.) and ATO<br>Office of Safety<br>and Technical<br>Training|
|||• Contract||
||Safety Risk<br>Management<br>Document or System<br>Safety Assessment<br>Report|Validation:<br>• Prior safety<br>assessments<br>• Solution<br>Concept of<br>Operations<br>• Final Program<br>Requirements<br>Document<br>Verification:<br>• FAA Safety<br>Management<br>System(SMS)|Service Team<br>(including<br>functional<br>organizations<br>such as systems<br>engineering, test<br>and evaluation,<br>etc.) and ATO<br>Office of Safety<br>and Technical<br>Training|



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

42 

|**Decision Points**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
||System Security<br>Authorization|Validation:<br>• Plan of Actions<br>and Milestones<br>(POA&M)<br>Verification:<br>•<br>Security<br>Authorization<br>Handbook<br>•<br>AMS Policy|Service Team<br>(including<br>functional<br>organizations<br>such as systems<br>engineering, test<br>and evaluation,<br>Information<br>Systems<br>Security<br>Manager, etc.)|
||Completed In-Service<br>Review Checklist|Validation:<br>Assess completed<br>checklist<br>Issues/Action<br>Plans/Remarks<br>against the<br>associated<br>checklist question<br>Verification:<br>• In-Service<br>Review<br>Checklist<br>Template<br>• AMS Policy|Service Team<br>(including<br>functional<br>organizations<br>such as systems<br>engineering, test<br>and evaluation,<br>etc.) and ATO<br>Office of Safety<br>and Technical<br>Training|



### **3.5 V&V in In-Service Management** 

The primary goal of ISM is to support the execution of the FAA mission of providing air traffic control and other services.  Systems, products, services, and facilities are operated, maintained, secured, and sustained in real-time to provide the level of service required by users and customers.  In addition, fielded products and services receive periodic monitoring and evaluation, and performance data is provided to ongoing MA and IA activities as the basis for revalidating the need to sustain deployed assets or taking other action to improve service delivery.  This includes configuration management, preventive and corrective maintenance, training, infrastructure support and logistics support, emergency sustainment actions, and the removal/disposal of obsolete assets.  Also included is the sustainment of flight inspection, aircraft certification, and regulatory requirements. 

The primary focus of V&V during ISM is to ensure that any modifications to the product meet new/modified requirements and that any new/modified requirements or operational 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

43 

concepts are valid.  It is essential to ensure the product continues to fulfill its intended purpose throughout its lifecycle.  Additionally, all major work products associated with product modifications are subject to V& V during ISM. 

Table 6 identifies the following for ISM: 

- The major decision points 

- The minimum required work products, product components, and products that must be verified and validated at each decision point 

- The criteria that each work product, product component, or product must be verified and validated against 

- The stakeholders responsible for each V&V activity 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

44 

**<u>Table 6.  V&V in In-Service Management</u>**<sup>**6**</sup> 

|**Decision**<br>**Points**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
|Decision to<br>Implement an<br>Improvement or<br>Change<br>Decision to<br>Deploy an<br>Improvement or<br>Change|Updates to Enterprise<br>Architecture products<br>and amendments|Validation:<br>• Enterprise<br>Architecture<br>• NAS Segment<br>Implementation<br>Plan<br>• NAS<br>Requirements<br>Documents<br>• Operational<br>Analysis Reports<br>Verification:<br>• NAS Integrated<br>Systems<br>Engineering<br>Framework|Service Team<br>(including functional<br>organizations such as<br>systems engineering),<br>Enterprise<br>Architecture Control<br>Board<br>(NAS and Mission<br>Support), and ANG<br>Engineering Services|
||NAS Change Proposals<br>(NCPs)/Changed<br>Requirements|Validation:<br>• Post<br>Implementation<br>Reviews<br>• Operational<br>Analyses<br>• Final Program<br>Requirements<br>Document<br>Verification:<br>• FAA Form 1800-<br>2 (Case File/NCP<br>Form)<br>• FAA Order<br>1800.66<br>Configuration<br>Management<br>Policy|Service Team<br>(including functional<br>organizations such as<br>systems engineering)|



> 6 Table 6 content is based on AMS policy as of the time this document was published. Detailed templates and guidance for the ISM AMS lifecycle exist and should be reviewed for current guidance. AMS Lifecycle Verification and Validation Guidelines                             January 2023 

45 

|**Decision**<br>**Points**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
||Implemented changes<br>to the baseline<br>system/service<br>(supported by and<br>documented in plans,<br>procedures and reports)<br>_Note: Major V&V_<br>_activities include ISM DT_<br>_and OT activities (IOA if_<br>_applicable)_|Validation:<br>• Final Program<br>Requirements<br>Document<br>including Critical<br>Operational<br>Issues and<br>Critical<br>Performance<br>Requirements<br>• NAS Change<br>Proposal<br>• Functional<br>Description<br>Document|Service Team<br>(including functional<br>organizations such as<br>systems engineering)|
|||Verification:||
|||• System<br>Specification<br>and/or lower-<br>level<br>specifications<br>• Functional<br>Description<br>Documents<br>• Safety Risk<br>Management<br>Document<br>• Contract||



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

46 

|**Decision**<br>**Points**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
||System Support<br>Directives|Validation:<br>• System/service<br>procedures<br>Verification:<br>• FAA Order<br>1320.58A,<br>Instructions for<br>Writing Notices,<br>Maintenance<br>Technical<br>Handbooks, and<br>System Support<br>Directives|Service Team<br>(including functional<br>organizations such as<br>systems engineering)|



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

47 

|**Decision**<br>**Points**|**Work**<br>**Products/Product**<br>**Components/Products**<br>**Subject to V&V**|**V&V Criteria**|**Stakeholder**<br>**Responsible for**<br>**V&V**|
|---|---|---|---|
||Updates to the<br>Implementation<br>Strategy and Planning<br>Document|Validation:<br>• Enterprise<br>Architecture<br>• Solution Concept<br>of Operations<br>• Functional<br>Analyses<br>Products<br>• Updated Program<br>Requirements<br>Document<br>• Detailed strategy<br>for procuring,<br>implementing,<br>testing, and<br>supporting the<br>solution<br>• Final<br>Implementation<br>Strategy and<br>Planning<br>Document V&V<br>Results|Service Team<br>(including functional<br>organizations such as<br>systems engineering)|
|||Verification:<br>• Implementation<br>Strategy and<br>Planning<br>Document<br>template<br>• AMS Policy||



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

48 

## **APPENDIX A - ACRONYMS** 

|ACAT|Acquisition Categories|
|---|---|
|AMS|Acquisition Management System|
|ARM|AMS Rational Model|
|APB|Acquisition Program Baseline<br>|
|ATO|Air Traffic Organization|
|BC|Business Case|
|CAI|Contractor Acceptance and Inspection|
|CDR|Critical Design Review|
|CMMI<sup>®</sup>|Capability Maturity Model<sup>®</sup>Integration|
|CPR|Critical Performance Requirement|
|CRD|Concept and Requirements Definition|
|CRDRD|Concept and Requirements Definition Readiness Decision|
|DT|Development Test|
|EA|Enterprise Architecture|
|eV&V|Enterprise Verification and Validation|
|FAA|Federal Aviation Administration|
|FAST|FAA Acquisition System Toolset|
|FID|<br>Final Investment Decision|
|FPRD|Final Program Requirements Document|
|IA|Investment Analysis|
|IARD|Investment Analysis Readiness Decision|
|IBR|Integrated Baseline Review|
|IDA|Investment Decision Authority|
|IER|Independent Evaluation Review|
|IID|Initial Investment Decision|
|IOA|Independent Operational Assessment|
|ISD|In-Service Decision|
|ISGSA|Information Security Guidance for System Acquisition|
|ISM|In-Service Management|
|ISPD|Implementation Strategy and Planning Document|
|ISR|<br>In-Service Review|
|ISS|Information System Security|
|NARP|National Aviation Research Plan|
|NAS|National Airspace System|
|NCP|<br>NAS Change Proposal|
|NSIP|<br>NAS Segment Implementation Plan|



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

49 

|OT|Operational Test|
|---|---|
|PDR|Preliminary Design Review|
|PMP|Program Management Plan|
|POA&M|Plan of Actions and Milestones|
|PRD|Program Requirements Document|
|QA|Quality Assurance|
|RMA|Reliability Maintainability Availability|
|RSA|Research for Systems Analysis|
|SASP|Service Analysis & Strategic Planning|
|SI|Solution Implementation|
|SIR|Screening Information Request|
|SME|Subject Matter Expert|
|SMS|Safety Management System|
|T&E|Test and Evaluation|
|TEMP|Test and Evaluation Master Plan|
|TSB|Test Standards Board|
|V&V|Verification and Validation|



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

50 

## **APPENDIX B - VERIFICATION AND VALIDATION CHECKLISTS** 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

51 

## **PROGRAM REQUIREMENTS DOCUMENT VERIFICATION AND VALIDATION CHECKLIST** 

**Title of PRD: Document Revision: Lifecycle Phase:** 

##### **Document Date:** 

_Instructions:  Check the Acceptance box that best assesses the Criterion.  In the Comments block, cite sections that do not meet PRD requirements or elaborate on findings.  Estimate when counting requirements._ 

|**CRITERIA**|**ACCEPTANCE**|**COMMENTS**|
|---|---|---|
|**Compliance**|||
|1.<br>Does the PRD conform to the FAA<br>Template for the Program<br>Requirements?|☐YES<br>☐NO||
|2.<br>Do the requirements comply with the<br>International Council on Systems<br>Engineering (INCOSE) Guide for<br>Writing Requirements?|☐YES<br>☐NO|Est. %:<br>Req. Issues/Total Reqs.|
|3.<br>Are the identified Critical Performance<br>Requirements (CPRs) in accordance<br>with Appendix 1 of the PRD Template?|☐YES<br>☐NO|Est. %:<br>CPR Issues/Total CPRs|
|4.<br>Does the PRD include a VRTM in<br>accordance with Appendix 4 of the PRD<br>Template?|☐YES<br>☐NO||
|5.<br>Are the identified COIs in accordance<br>with the FAA WJHTC Test and<br>Evaluation Handbook, the PRD<br>Template and the PRD Canned<br>Requirements?|☐YES<br>☐NO||
|**Traceability/Relationships**|||
|6. <sup>Does the PRD provide traceability to the</sup><br>Target NAS Requirement Document?|☐YES<br>☐NO||
|7. <sup>Does the PRD provide traceability to the</sup><br>Functional Analysis Document?|☐YES<br>☐NO||
|8. <sup>Does the PRD align with the Shortfall</sup><br>Analysis Report?|☐YES<br>☐NO||
|9.<br>Does the PRD align with applicable<br>Operational Improvement(s) or related<br>increment(s)?|☐YES<br>☐NO||
|10. <sup>Does the PRD align with applicable</sup><br>SolutionConceptofOperations?|☐YES<br>☐NO||
|**Requirements Focus**|||
|11.<br>In relation to the program’s scope, does<br>the PRD sufficiently address the<br>following areas:|||
|a.<br>Functional?|☐YES<br>☐NO||
|b.<br>Data and Information?|☐YES<br>☐NO||
|c.<br>Performance?|☐YES<br>☐NO||
|d.<br>Reliability, Maintainability, and<br>Availability?|☐YES<br>☐NO||
|<br>e.<br>Physical Integration?|☐YES<br>☐NO||
|f.<br>Functional Integration?|☐YES<br>☐NO||
|g.<br>Human Factors?|☐YES<br>☐NO||



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

52 

||**CRITERIA**|**ACCEPTANCE**|**COMMENTS**|
|---|---|---|---|
||**Compliance**|||
|h.|Information System Security?|☐YES<br>☐NO||
|i.|System Safety?|☐YES<br>☐NO||
|j.|Configuration Management?|☐YES<br>☐NO||
|k.|Test and Evaluation?|☐YES<br>☐NO||
|l.|Implementation and Transition?|☐YES<br>☐NO||
|m.|In-Service Management?|☐YES<br>☐NO||



SUMMARY/RECOMMENDATION: 

|Reviewer|
|---|
|Organizational<br>code|
|Telephone|
|Email|
|Review Team|
|Date Completed|



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

53 

## **IMPLEMENTATION STRATEGY AND PLANNING DOCUMENT** 

## **VERIFICATION AND VALIDATION CHECKLISTIMPLEMENTATION STRATEGY AND PLANNING DOCUMENT** 

## **VERIFICATION AND VALIDATION CHECKLIST** 

**Title of ISPD:** 

**Document Revision:** 

**Document Date:** 

**Lifecycle Phase:** 

_Instructions:  Check the Acceptance box that best assesses the Criterion.  In the Comments block, cite sections that do not meet ISPD requirements or elaborate on findings._ 

|**CRITERIA**|**ACCEPTANCE**|**COMMENTS**|
|---|---|---|
|1.<br>Does the ISPD conform to the FAA<br>Template for the Implementation Strategy<br>and Planning Document?|☐YES<br>☐NO<br>||
|2.<sup>Are all sections of the ISPD consistent and</sup><br>cohesive in approach and direction?|☐YES<br>☐NO<br>||
|3.<sup>Is the comparative analysis of alternative</sup><br>solutions adequately documented?|☐YES<br>☐NO||
|4.<br>Does the program implementation strategy<br>align with FAA documentation in the<br>following:|||
|a.<br>FAA Strategic Plan?|☐YES<br>☐NO||
|b. Solution ConOps?|☐YES<br>☐NO||
|c.<br>Shortfall Analysis Report?|☐YES<br>☐NO||
|d. Program Requirements Document?|☐YES<br>☐NO||
|e.<br>NAS Segment Implementation Plan?|☐YES<br>☐NO<br>☐N/A||
|f.<br>Enterprise Architecture?|☐YES<br>☐NO<br>☐N/A||
|g. Target NAS Requirements Document?|☐YES<br>☐NO<br>☐N/A||
|5. Does the acquisition strategy:|||
|a.<br>Identify prospective sources?|☐YES<br>☐NO||
|b. Formulate a competition strategy?|☐YES<br>☐NO||
|c.<br>Determine source selection criteria?|☐YES<br>☐NO||
|d. Define prime and support contract<br>management processes?|☐YES<br>☐NO||
|<br>e.<br>Define an approach to establishing and<br>communicating acquisition goals and<br>success criteria to stakeholders and<br>prime contractor?|☐YES<br>☐NO||



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

54 

||**CRITERIA**|**ACCEPTANCE**|**COMMENTS**|
|---|---|---|---|
|6.<br>Ha<br>an<br>go|s the program established management<br>d contract controls for clearly defined<br>als for:|||
|a.|Cost?|☐YES<br>☐NO||
|b.|Schedule?|☐YES<br>☐NO||
|c.|Technical performance?|☐YES<br>☐NO||
|d.|Prime contractors?|☐YES<br>☐NO||
|e.|Support contractors?|☐YES<br>☐NO||
|f.|Quality assurance?|☐YES<br>☐NO||
|7. Do<br>an|es the ISPD sufficiently address planning<br>d strategies for following areas:|||
|a.|Hardware and Software?|☐YES<br>☐NO||
|b.|RMA?|☐YES<br>☐NO||
|c.|Configuration Management?|☐YES<br>☐NO||
|d.|Interfaces?|☐YES<br>☐NO||
|e.|Human Factors?|☐YES<br>☐NO||
|f.|Safety?|☐YES<br>☐NO||
|g.|Security?|☐YES<br>☐NO||
|h.|Test and Evaluation?|☐YES<br>☐NO||
|i.|Production?|☐YES<br>☐NO||
|j.|Integrated Logistics Support|☐YES<br>☐NO||
|k.|Deployment Strategy (prior to and after<br>ISD)|☐YES<br>☐NO||



###### SUMMARY/RECOMMENDATION: 

|Reviewer|
|---|
|Organizational<br>code|
|Telephone|
|Email|
|ReviewTeam|
|Date Completed|



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

55 

## **PROGRAM MANAGEMENT PLAN VERIFICATION AND VALIDATION CHECKLIST** 

**Title of PMP:** 

**Document Revision:** 

##### **Document Date:** 

**Lifecycle Phase:** 

_Instructions:  Check the Acceptance box that best assesses the Criterion.  In the Comments block, cite sections that do not meet PMP requirements or elaborate on findings.  Estimate when counting requirements._ 

|**CRITERIA**|**ACCEPTANCE**|**COMMENTS**|
|---|---|---|
|1<br>PMP conforms to FAA guidelines and template for the<br>Program Management Plan|☐YES<br>☐NO||
|2<br>Ensure all sections of the PMP are consistent and cohesive<br>in approach and direction.|☐YES<br>☐NO||
|3<br>Program management structure for the following have<br>beendetermined:|||
|a. Organizational Breakdown Structure|☐YES<br>☐NO||
|b. Staffing Plan/Skills Matrix|☐YES<br>☐NO||
|c. Roles and Responsibilities|☐YES<br>☐NO||
|4<br>Program management approach for the following have<br>been determined:|||
|a. Program Management|||
|1). Program Planning and Control|☐YES<br>☐NO||
|2). Financial/Business Management|☐YES<br>☐NO||
|3). Schedule Management|☐YES<br>☐NO||
|4). Risk Management|☐YES<br>☐NO||
|5). Requirements Management|☐YES<br>☐NO||
|b. Contract Management|||
|1). Quality Assurance|☐YES<br>☐NO||
|2). Technical Data|☐YES<br>☐NO||
|c. Physical and Functional Integration Management|☐YES<br>☐NO||
|d. Integrated Logistics Support|☐YES<br>☐NO||
|e. Systems and Health Management|||
|<br>1). System Safety Management|☐YES<br>☐NO||
|2). Employee Health and Safety Management|☐YES<br>☐NO||
|f. Security and Privacy Management|☐YES<br>☐NO||
|g. Test and Evaluation Management|☐YES<br>☐NO||
|h. Deployment Management|☐YES<br>☐NO||
|i. Communication Management|☐YES||



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

56 

**<u><mark>CRITERIA ACCEPTANCE COMMENTS</mark></u>** ☐ NO 

SUMMARY/RECOMMENDATION: 

|Reviewer|
|---|
|Organizational<br>code|
|Telephone|
|Email|
|Review Team|
|Date Completed|



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

57 

## **ACQUISITION PROGRAM BASELINE VERIFICATION AND VALIDATION CHECKLIST** 

**Title of APB: Document Revision: Document Date: Lifecycle Phase:** 

_Instructions:  Check the Acceptance box that best assesses the Criterion.  In the Comments block, cite sections that do not meet APB requirements or elaborate on findings.  Estimate when counting requirements._ 

|**CRITERIA**|**ACCEPTANCE**|**COMMENTS**|
|---|---|---|
|1<br>APB conforms to FAA Template for the Acquisition<br>Program Baseline Document|☐YES<br>☐NO<br>||
|2<br>Ensure all sections of the APB are consistent and cohesive<br>in approach and direction. (This is especially important<br>when each section is authored by a different individual.)|☐YES<br>☐NO||
|3<br>Schedule, Cost, and Performance|||
|a. Schedule milestones have been selected from AMS<br>Policy or reworked with the approval of the<br>Capital Programs Formulation Group and the<br>Financial Services Organization.  All milestones<br>represent an accurate estimate of the program<br>schedule.|☐YES<br>☐NO||
|b. Costs estimates are accurately presented by fiscal<br>year and include costs for:|||
|1) Prime contract|☐YES<br>☐NO||
|2) Testing|☐YES<br>☐NO||
|3) Deployment|☐YES<br>☐NO||
|4) Site preparation|☐YES<br>☐NO||
|5) Installation|☐YES<br>☐NO||
|6) Headquarters and Field support contracts|☐YES<br>☐NO||
|c. Approved Critical Performance Requirements<br>obtained from the Program Requirements<br>Document|||
|1) Ensure Critical Performance Requirements<br>are identified and consistent with those in the<br>Program Requirements Document.|☐YES<br>☐NO||
|2) Requirements are clearly stated|☐YES<br>☐NO||
|3) Associate values for each requirement are<br>provided|☐YES<br>☐NO||



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

<u>SUMMARY/RECOMMENDATION:</u> Click or tap here to enter text. 

58 

|Reviewer|
|---|
|Organizational<br>code|
|Telephone|
|Email|
|ReviewTeam|
|Date Completed|



AMS Lifecycle Verification and Validation Guidelines                             January 2023 

59 

## **APPENDIX C - DEFINITIONS** 

Accreditation - The formal certification that a test capability is acceptable for a specific application. 

Analyses - This is a method of verification which consists of comparing hardware or software design with known scientific and technical principles, technical data, or procedures and practices to validate that the proposed design will meet the specified functional or performance requirements. 

Audits - (1) An independent examination of a work product or set of work products to assess compliance with specifications, standards, contractual agreements, or other criteria.  (2) To conduct an independent review and examination of system records and activities to test the adequacy and effectiveness of data security and data integrity procedures, to ensure compliance with established policy and operational procedures, and to recommend any necessary changes. 

Checklists - A list of items needed to be verified, checked, or inspected. 

Demonstrations - This is a method of verification where qualitative versus quantitative validation of a requirement is made during a dynamic test of the equipment.  Additional definitions applied to this term are:  (1) If a requirement is validated by test during first article qualification testing and the requirement has enough significance that it is "retested" during acceptance test, then this acceptance testing can be indicated in the VRTM as a Demonstration.  (2) In general, software functional requirements are validated by demonstration since the functionality must be observed through some secondary media. 

Discussions with Users – Self-explanatory. 

Functional Presentations – A presentation illustrating the hierarchical arrangement of functions and interfaces providing a complete representation of the system from a performance and behavioral perspective. 

Inspections - Is a method of verification to determine compliance with specification requirements and consists primarily of visual observations, or mechanical measurements of the equipment, physical locations, or technical examination of engineering-support documentation. 

Modeling - Construction of programs used to model the effects of a postulated environment for investigating the dimensions of a problem for the effects of algorithmic processes on responsive targets. 

Peer reviews - A peer review is a structured type of review that involves a methodical examination of a completed draft document for quality improvement purposes.  Peer reviews are conducted by unbiased subject matter experts (SME) who have independence from the development and approval of the work product, component product or product. 

Simulation - A model(s) that behaves or operates like a given system when provided a set of controlled inputs. 

Storyboarding - Is a graphic arrangement of illustrations or images displayed in sequence for the purpose of visualizing a story or concept. 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

60 

Testing - The process of operating a system or component under specified conditions, observing or recording the results, and making an evaluation of some aspect of the system or component. 

User Surveys – User surveys are a method of gathering information from individuals.  Surveys have a variety of purposes and can be conducted in many ways.  Surveys may be conducted to gather information through a printed questionnaire, over the telephone, by mail, in person, by diskette, or on the web. 

Walk-throughs/dry runs – Is a technique where the effects of a possible failure are intentionally mitigated by the conduct of a rehearsal of the process or procedure prior to performing the real one. 

AMS Lifecycle Verification and Validation Guidelines                             January 2023 

61 


