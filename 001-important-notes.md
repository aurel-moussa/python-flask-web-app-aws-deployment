### Flask
Flask is a micro web framework written in Python. 
It is classified as a microframework because of its minimal structure 
that provides an ecosystem of external components such as form validation, 
upload handling, authentications, etc., that can be mixed and matched as needed, 
focusing on including only what you need instead of providing a complete toolset. 
Companies that use the Flask framework include Pinterest and LinkedIn.

### AWS
Amazon Web Services (AWS) is a subsidiary of Amazon 
providing on-demand cloud computing platforms and APIs to individuals, 
companies, and governments, on a metered pay-as-you-go basis. 
These cloud computing web services provide a variety of basic abstract technical 
infrastructure and distributed computing building blocks and tools.  

### AECC
Amazon Elastic Compute Cloud (Amazon EC2), 
provides secure, resizable compute capacity in the cloud.
In simple terms cloud servers.

### Elastic Beanstalk
https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/MXOIG5R-TwKziBuUfp8C6Q_5a0d5f70c2fb4183bd31e921b9c7d5dd_aeb-architecture2.png?expiry=1660694400000&hmac=vtmG5j7mNM2iy_q8X_oodpri9_Mpu6eRgEQuqDe8BwQ
The environment is the heart of the application. 
In the diagram, the environment is shown within the top-level solid line. 
When you create an environment, Elastic Beanstalk provisions the resources required to run your application. 
AWS resources created for an environment include one elastic load balancer (ELB in the diagram), an Auto Scaling group, 
and one or more Amazon Elastic Compute Cloud (Amazon EC2) instances.

Every environment has a CNAME (URL) that points to a load balancer. 
The environment has a URL, such as myapp.us-west-2.elasticbeanstalk.com. 
This URL is aliased in Amazon Route 53 to an Elastic Load Balancing URL—something 
like abcdef-123456.us-west-2.elb.amazonaws.com—by using a CNAME record. 
Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service. 
It provides secure and reliable routing to your infrastructure. 
The domain name that you registered with your DNS provider will forward requests to the CNAME.

The load balancer sits in front of the Amazon EC2 instances, 
which are part of an Auto Scaling group. Amazon EC2 Auto Scaling automatically starts additional Amazon 
EC2 instances to accommodate increasing load on your application. 
If the load on your application decreases, Amazon EC2 Auto Scaling stops instances, 
but always leaves at least one instance running.

The Amazon EC2 instances shown in the diagram are part of one security group. 
A security group defines the firewall rules for your instances. 
By default, Elastic Beanstalk defines a security group, which allows everyone to connect using port 80 (HTTP). 
You can define more than one security group. For example, you can define a security group for your database server.

Environment properties are a set of name/value pair variables whose value is set outside the program, 
typically through a functionality built into the operating system or microservice. 
These are loaded during application initialization.
