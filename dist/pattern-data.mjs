export const patterns = [
  {
    "id": "edge",
    "title": "CloudFront, WAF & S3",
    "services": [
      "cloudfront",
      "waf",
      "s3"
    ],
    "cue": "Temukan titik pemeriksaan request. Di mana file asli disimpan?",
    "src": "./assets/patterns/edge.png",
    "source": "https://github.com/aws-samples/serverless-patterns/tree/main/cloudfront-waf-s3-cdk",
    "original": "https://raw.githubusercontent.com/aws-samples/serverless-patterns/main/cloudfront-waf-s3-cdk/CloudFront-WAF-S3.png",
    "alt": "A viewer request is checked against WAF rules at CloudFront; the distribution serves site files from its S3 origin."
  },
  {
    "id": "serverless",
    "title": "HTTP API to DynamoDB",
    "services": [
      "api-gateway",
      "lambda",
      "dynamodb"
    ],
    "cue": "Ikuti request dari endpoint sampai tabel. Komponen mana menjalankan logika aplikasi?",
    "src": "./assets/patterns/serverless.png",
    "source": "https://github.com/aws-samples/serverless-patterns/tree/main/apigw-http-api-lambda-dynamodb-python-cdk",
    "original": "https://raw.githubusercontent.com/aws-samples/serverless-patterns/main/apigw-http-api-lambda-dynamodb-python-cdk/docs/architecture.png",
    "alt": "An HTTP API invokes Lambda. The function reaches a DynamoDB table through a VPC endpoint."
  },
  {
    "id": "fanout",
    "title": "SNS fan-out to SQS",
    "services": [
      "sns",
      "sqs"
    ],
    "cue": "Perhatikan percabangan setelah topic. Mengapa setiap subscriber memiliki antreannya sendiri?",
    "src": "./assets/patterns/fanout.png",
    "source": "https://github.com/aws-samples/serverless-patterns/tree/main/sns-sqs-fanout",
    "original": "https://raw.githubusercontent.com/aws-samples/serverless-patterns/main/sns-sqs-fanout/images/architecture.png",
    "alt": "An SNS topic branches into three SQS queues. The example uses separate subscriptions for all, temperature, and humidity messages."
  },
  {
    "id": "athena",
    "title": "Querying S3 with Athena & Glue",
    "services": [
      "s3",
      "athena",
      "aws-glue",
      "glue-data-catalog"
    ],
    "cue": "Bedakan lokasi file data dengan lokasi metadata tabel.",
    "src": "./assets/patterns/athena.png",
    "source": "https://github.com/aws-samples/serverless-patterns/tree/main/athena-glue-s3-sam",
    "original": "https://raw.githubusercontent.com/aws-samples/serverless-patterns/main/athena-glue-s3-sam/images/architecture.png",
    "alt": "Athena, Glue, and an S3 Express One Zone directory bucket are shown together in this example of querying stored files."
  },
  {
    "id": "containers",
    "title": "Routing requests to ECS",
    "services": [
      "application-load-balancer-alb",
      "ecs"
    ],
    "cue": "Telusuri batas antara routing HTTP dan container yang menangani request.",
    "src": "./assets/patterns/containers.png",
    "source": "https://github.com/aws-samples/serverless-patterns/tree/main/alb-ecs-java-sam",
    "original": "https://raw.githubusercontent.com/aws-samples/serverless-patterns/main/alb-ecs-java-sam/images/architecture.png",
    "alt": "An Application Load Balancer sends requests to an ECS service. A separate arrow from ECR shows where the container image comes from."
  },
  {
    "id": "auth",
    "title": "Machine-to-machine authorization",
    "services": [
      "cognito-user-pools",
      "api-gateway"
    ],
    "cue": "Cari langkah untuk mendapatkan token dan langkah yang memakai token.",
    "src": "./assets/patterns/auth.png",
    "source": "https://github.com/aws-samples/serverless-patterns/tree/main/cognito-m2m-oauth-apigw-cdk",
    "original": "https://raw.githubusercontent.com/aws-samples/serverless-patterns/main/cognito-m2m-oauth-apigw-cdk/src/image/arch.png",
    "alt": "A machine client obtains a token through the authorization flow before it calls the protected API."
  },
  {
    "id": "batch",
    "title": "From event to batch job",
    "services": [
      "eventbridge",
      "aws-batch"
    ],
    "cue": "Perhatikan siapa mendeteksi event, lalu siapa mengerjakan job.",
    "src": "./assets/patterns/batch.png",
    "source": "https://github.com/aws-samples/serverless-patterns/tree/main/eventbridge-batch-sam",
    "original": "https://raw.githubusercontent.com/aws-samples/serverless-patterns/main/eventbridge-batch-sam/images/eventbridge-batch-sam.png",
    "alt": "An EventBridge rule sends matching events to an AWS Batch job."
  },
  {
    "id": "firehose",
    "title": "Streaming CloudWatch metrics",
    "services": [
      "cloudwatch",
      "amazon-data-firehose"
    ],
    "cue": "Ikuti jalur metric stream. Bedakan sumber telemetry dengan layanan delivery.",
    "src": "./assets/patterns/firehose.png",
    "source": "https://github.com/aws-samples/serverless-patterns/tree/main/cloudwatch-metric-streams-firehose-terraform",
    "original": "https://raw.githubusercontent.com/aws-samples/serverless-patterns/main/cloudwatch-metric-streams-firehose-terraform/images/pattern.png",
    "alt": "A CloudWatch metric stream passes metrics to Amazon Data Firehose, which delivers them to S3."
  },
  {
    "id": "stream",
    "title": "A DynamoDB change triggers processing",
    "services": [
      "dynamodb-streams",
      "dynamodb",
      "lambda"
    ],
    "cue": "Temukan perubahan item, stream record, dan fungsi pemrosesnya.",
    "src": "./assets/patterns/stream.png",
    "source": "https://github.com/aws-samples/serverless-patterns/tree/main/dynamodb-streams-lambda-dynamodb",
    "original": "https://raw.githubusercontent.com/aws-samples/serverless-patterns/main/dynamodb-streams-lambda-dynamodb/images/architecture.png",
    "alt": "An item change produces a DynamoDB Streams event. A Lambda function processes the event and writes to another DynamoDB table."
  },
  {
    "id": "bedrock",
    "title": "Orchestrating model calls",
    "services": [
      "step-functions",
      "amazon-bedrock"
    ],
    "cue": "Bedakan state machine yang mengatur urutan dengan model yang menghasilkan respons.",
    "src": "./assets/patterns/bedrock.png",
    "source": "https://github.com/aws-samples/serverless-patterns/tree/main/stepfunctions-bedrock-sam",
    "original": "https://raw.githubusercontent.com/aws-samples/serverless-patterns/main/stepfunctions-bedrock-sam/image/architecture.png",
    "alt": "A Step Functions state machine invokes an Amazon Bedrock model."
  },
  {
    "id": "doc",
    "title": "Document extraction with Textract",
    "services": [
      "textract",
      "lambda"
    ],
    "cue": "Temukan layanan yang membaca dokumen. Apa peran Lambda di sekitarnya?",
    "src": "./assets/patterns/doc.png",
    "source": "https://github.com/aws-samples/serverless-patterns/tree/main/textract-lambda-cdk-dotnet",
    "original": "https://raw.githubusercontent.com/aws-samples/serverless-patterns/main/textract-lambda-cdk-dotnet/Images/pattern.png",
    "alt": "An incoming S3 object triggers a Lambda function that calls Textract and writes results to an output bucket."
  },
  {
    "id": "observability",
    "title": "X-Ray service map",
    "services": [
      "x-ray",
      "api-gateway",
      "lambda",
      "dynamodb"
    ],
    "cue": "Ikuti satu request melintasi layanan. Service map ini adalah observasi dari contoh aplikasi.",
    "src": "./assets/patterns/observability.png",
    "source": "https://github.com/aws-samples/serverless-patterns/tree/main/apigw-lambda-dynamodb-xray",
    "original": "https://raw.githubusercontent.com/aws-samples/serverless-patterns/main/apigw-lambda-dynamodb-xray/docs/xray-service-map.png",
    "alt": "The X-Ray service map shows a traced path from the client through API Gateway and Lambda to DynamoDB."
  }
];
