## Send-message-decoupling
### Decouple Amazon Pinpoint multi channel message sending process via APIGate way and SQS

![Screenshot](images/Send-message-decoupling.png)

#### Description 
Customers may be unable to send multichannel messages via Amazon Pinpoint using other campaign management systems or current applications if they are unable to integrate directly with Amazon Pinpoint. This is primarily due to AWS's use of SIGv4 authentication. Also, when clients migrate their multi channel message payload from an existing provider to Amazon Pinpoint, they must change all APIs to Amazon Pinpoint standards, which is a significant amount of  effort.

Customers can use this solution to decouple Amazon Pinpoint from their applications and drive multi-channel interaction.

Use cases(s)
* Minimal changes to the existing application code.
* Integrating Pinpoint with other Engagement products such as SFMC, AMC, Clevertap, Webengage, and others 
* No pathways to login with AWS using IAM role-based authentication or SIGv4 authentication 
* Scalability - Sending larger API payloads (> 100 recipients) as part of a single API call

#### AWS CloudFormation Link
[CF Template](api-gateway-sqs-integration.template)
