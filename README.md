# RTFRC Project
Code Repository for Real Time Face Recognition Challenge at MIET, Meerut.  
Team Name: **_Learners and Visionaries_**  
Team Members: 
1. Siddharth Goel (Team Leader)
2. Kunal Yadav
3. Pulkit Kaushik (Left due to unforeseen circumstances)
4. Prashant Agarwal (Left due to unforeseen circumstances)

The RTFRC is an ongoing challenge at Meerut Institute of Engineering & Technology, Meerut.
We are required to build a Real Time Face Recognition module to recognize the college students/employees from non-college people.

To be successful in the challenge, minimum _94% accuracy_ is needed.

For the project, following technologies have been selected:
1. **AWS Rekognition** -> For the Face Recognition services. Selected due to high accuracy at a fraction of cost.  
2. **NodeJS** -> For the Back-End functionality of the onsite module. Will communicate with the Rekognition API to send images and receive the results. 
3. **Python** -> For on-site image capturing. Will be developing a motion detection program to detect and capture images whenever motion occurs.
4. **MySQL** -> Fulfills the needs for the database.  

## Week 1 
Selecting the best possible tools for the job and modifying the approach to ensure maximum accuracy.  
  
## Week 2 
Created 3 Lambda functions. The first two of them will be used to train AWS Rekognition, and the third one will be used to search for faces in a given image.
  
**rtfrcAddPeopleToDynamoDB** - This lambda function takes information of people as a JSON document and stores it into a DynamoDB table.  
  
**rtfrcIndexPeopleFaces** - This lambda function is invoked when an image of a person (whose record has been stored in DynamoDB by the first lambda function) is uploaded to a S3 bucket. The image is analyzed by AWS Rekognition and a "FaceId" is generated corresponding to the face of the person.
This "FaceId" is then stored in the DynamoDB with the record of the corresponding person.  
  
**rtfrcRecognizeFacesInImages** - This lambda function is invoked when an image is added to another S3 bucket. The image is analyzed by AWS Rekognition and the faces in the image are indexed.  
The indexed faces are then searched in the Rekognition collection which has been prepared by analyzing people's images using the second lambda function.  
Matching faces are stored in another DynamoDB table along with FaceId of the matched person. Using this FaceId and the DynamoDB table used in second lambda function we can find out the person who was in this image.  
The indexed faces of the current image are then removed from Rekognition collection to avoid high costs.  
  
## Towards the Last Leg of the competition  
  
**Created  a basic Face Detection Script using OpenCV and HaarCascade**    
The script is basic and Haar Cascade is used since it is more accurate than LMB Cascade. 
The Script detects face(s) that are in the range/scope of camera/webcam.  
The Script also saves those frames with faces to the desired location.   
