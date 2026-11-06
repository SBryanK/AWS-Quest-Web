"""Extract selected unmodified AWS SVG assets. Usage: python3 scripts/import_icons.py ICON_PACKAGE.zip"""
import json,re,sys,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
z=zipfile.ZipFile(sys.argv[1]); paths=[p for p in z.namelist() if not p.startswith('__MACOSX') and p.endswith('_48.svg') and '/Arch_' in p]
def norm(s):return re.sub(r'[^a-z0-9]','',re.sub(r'^(Amazon|AWS)[ -]','',s,flags=re.I).lower())
lookup={norm(Path(p).name.removeprefix('Arch_').removesuffix('_48.svg')):p for p in paths}
alias={
'iam':'Identity-and-Access-Management','sts':'Identity-and-Access-Management','cognito-user-pools':'Cognito','cognito-identity-pools':'Cognito','scps':'Organizations','resource-access-manager-ram':'Resource-Access-Manager','aws-managed-microsoft-ad':'Directory-Service','ad-connector':'Directory-Service','simple-ad':'Directory-Service',
'kms':'Key-Management-Service','ssm-parameter-store':'Systems-Manager','certificate-manager-acm':'Certificate-Manager','ecs':'Elastic-Container-Service','eks':'Elastic-Kubernetes-Service','ecr':'Elastic-Container-Registry','outposts':'Outposts-family',
'vpc':'Virtual-Private-Cloud','security-groups':'Virtual-Private-Cloud','network-acls':'Virtual-Private-Cloud','internet-gateway':'Virtual-Private-Cloud','nat-gateway':'Virtual-Private-Cloud','vpc-peering':'Virtual-Private-Cloud','gateway-endpoints':'Virtual-Private-Cloud','interface-endpoints':'PrivateLink','vpn-cloudhub':'Site-to-Site-VPN','route-53-resolver':'Route-53','application-load-balancer-alb':'Elastic-Load-Balancing','network-load-balancer-nlb':'Elastic-Load-Balancing','gateway-load-balancer-gwlb':'Elastic-Load-Balancing','cloudfront-functions':'CloudFront','lambda-edge':'Lambda',
's3':'Simple-Storage-Service','s3-glacier-classes':'Simple-Storage-Service-Glacier','ebs':'Elastic-Block-Store','ec2-instance-store':'EC2','fsx-for-windows-file-server':'FSx-for-WFS','data-lifecycle-manager':'Elastic-Block-Store',
'rds-proxy':'RDS','aurora-serverless':'Aurora','aurora-global-database':'Aurora','dynamodb-streams':'DynamoDB','dax':'DynamoDB','timestream-for-liveanalytics':'Timestream',
'sqs':'Simple-Queue-Service','sns':'Simple-Notification-Service','amazon-msk':'Managed-Streaming-for-Apache-Kafka','glue-data-catalog':'Glue','redshift-spectrum':'Redshift','quicksight':'Quick',
'cloudwatch-logs':'CloudWatch','cloudwatch-synthetics':'CloudWatch','aws-health':'Health-Dashboard','session-manager':'Systems-Manager','run-command':'Systems-Manager','fault-injection-service-fis':'Fault-Injection-Service','ec2-instance-connect':'EC2',
'cloudformation-stacksets':'CloudFormation','cdk':'Cloud-Development-Kit','sam':'Serverless-Application-Repository','cost-and-usage-report-cur':'Cost-and-Usage-Report','cost-allocation-tags':'Cost-Explorer','service-quotas':'Trusted-Advisor','reserved-instances':'Reserved-Instance-Reporting','spot-instances':'EC2',
'snowball-snow-family':'Snowball','database-migration-service-dms':'Database-Migration-Service','schema-conversion-tool-sct':'Database-Migration-Service','application-migration-service-mgn':'Application-Migration-Service','elastic-disaster-recovery-drs':'Elastic-Disaster-Recovery','migration-hub':'Application-Discovery-Service','amazon-ses':'Simple-Email-Service','appstream-2-0-workspaces-applications':'WorkSpaces'}
# Use a service-family image when this entry is a feature; labels disclose it.
family=set(alias)-{'iam','resource-access-manager-ram','kms','certificate-manager-acm','ecs','eks','ecr','outposts','vpc','s3','s3-glacier-classes','ebs','fsx-for-windows-file-server','timestream-for-liveanalytics','sqs','sns','amazon-msk','aws-health','fault-injection-service-fis','cdk','cost-and-usage-report-cur','reserved-instances','snowball-snow-family','database-migration-service-dms','application-migration-service-mgn','elastic-disaster-recovery-drs','amazon-ses'}
# Unrelated icon substitutes are deliberately avoided; custom concept glyphs instead.
for id in ['sam','service-quotas','migration-hub','appstream-2-0-workspaces-applications','cost-allocation-tags','schema-conversion-tool-sct','reserved-instances']:alias.pop(id,None)
resource_names={
  "sts": "AWS-Identity-Access-Management_AWS-STS",
  "aws-managed-microsoft-ad": "AWS-Directory-Service_AWS-Managed-Microsoft-AD",
  "ad-connector": "AWS-Directory-Service_AD-Connector",
  "simple-ad": "AWS-Directory-Service_Simple-AD",
  "ssm-parameter-store": "AWS-Systems-Manager_Parameter-Store",
  "internet-gateway": "Amazon-VPC_Internet-Gateway",
  "nat-gateway": "Amazon-VPC_NAT-Gateway",
  "network-acls": "Amazon-VPC_Network-Access-Control-List",
  "vpc-peering": "Amazon-VPC_Peering-Connection",
  "application-load-balancer-alb": "Elastic-Load-Balancing_Application-Load-Balancer",
  "network-load-balancer-nlb": "Elastic-Load-Balancing_Network-Load-Balancer",
  "gateway-load-balancer-gwlb": "Elastic-Load-Balancing_Gateway-Load-Balancer",
  "route-53-resolver": "Amazon-Route-53_Resolver",
  "cloudfront-functions": "Amazon-CloudFront_Functions",
  "s3-access-points": "Amazon-Simple-Storage-Service_General-Access-Points",
  "s3-multi-region-access-points": "Amazon-Simple-Storage-Service_S3-Multi-Region-Access-Points",
  "s3-object-lambda": "Amazon-Simple-Storage-Service_S3-Object-Lambda-Access-Points",
  "data-lifecycle-manager": "Amazon-Elastic-Block-Store_Amazon-Data-Lifecycle-Manager",
  "rds-proxy": "Amazon-RDS-Proxy-Instance",
  "dynamodb-streams": "Amazon-DynamoDB_Stream",
  "dax": "Amazon-DynamoDB_Amazon-DynamoDB-Accelerator",
  "glue-data-catalog": "AWS-Glue_Data-Catalog",
  "cloudwatch-logs": "Amazon-CloudWatch_Logs",
  "cloudwatch-synthetics": "Amazon-CloudWatch_Synthetics",
  "session-manager": "AWS-Systems-Manager_Session-Manager",
  "run-command": "AWS-Systems-Manager_Run-Command",
  "spot-instances": "Amazon-EC2_Spot-Instance",
  "s3-file-gateway": "AWS-Storage-Gateway_Amazon-S3-File-Gateway",
  "fsx-file-gateway": "AWS-Storage-Gateway_Amazon-FSx-File-Gateway",
  "volume-gateway": "AWS-Storage-Gateway_Volume-Gateway",
  "tape-gateway": "AWS-Storage-Gateway_Tape-Gateway"
}
resources={Path(p).name:p for p in z.namelist() if not p.startswith('__MACOSX') and p.endswith('_48.svg') and '/Res_' in p}
data=json.loads((ROOT/'dist/mindmap.json').read_text()); out={}; assets=ROOT/'dist/assets/aws';assets.mkdir(parents=True,exist_ok=True)
for c in data['categories']:
 for s in c['services']:
  id=s['id']; target=alias.get(id,s['name'])
  if id.startswith('s3-') and id not in alias:target='Simple-Storage-Service';family.add(id)
  if id in ['s3-file-gateway','fsx-file-gateway','volume-gateway','tape-gateway']:target='Storage-Gateway';family.add(id)
  p=lookup.get(norm(target)); item={'category':c['id'],'color':c['color'],'kind':'family' if id in family else 'service'}
  if id in resource_names:
   p=resources['Res_'+resource_names[id]+'_48.svg'];item['kind']='resource'
  if p:
   filename=Path(p).name; (assets/filename).write_bytes(z.read(p));item.update(src='./assets/aws/'+filename,label=filename.removeprefix('Arch_').removeprefix('Res_').removesuffix('_48.svg').replace('-',' ').replace('_',' / '))
  else:item.update(kind='concept',label=s['name']);print('Concept glyph:',id)
  out[id]=item
(ROOT/'dist/icon-catalog.mjs').write_text('// Generated by scripts/import_icons.py from the AWS Architecture Icons package.\nexport const icons = '+json.dumps(out,indent=2,ensure_ascii=False)+';\n')
print('entries',len(out),'unique official SVGs',len({v['src'] for v in out.values() if 'src' in v}))
