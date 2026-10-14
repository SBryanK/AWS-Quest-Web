import json,re
from pathlib import Path
ROOT=Path(__file__).parent
categories=[]
def add(id,title,question,memory,color,source,rows):
    services=[]
    for line in rows.strip().splitlines():
        if not line.strip():continue
        name,cue,use,compare,lesson,group=line.split('|')
        services.append(dict(id=re.sub(r'[^a-z0-9]+','-',name.lower()).strip('-'),name=name,cue=cue,use=use,compare=compare,lesson=lesson,group=group))
    categories.append(dict(id=id,title=title,question=question,memory=memory,color=color,source=source,services=services))
add('identity','Identity & governance','Siapa boleh melakukan apa?','IAM = izin · STS = izin sementara · Identity Center = login karyawan · Cognito = login pelanggan.','#2878a0','security-services', '''
IAM|Permission book · buku izin|Atur siapa boleh melakukan action pada resource, dengan conditions.|Identity policy grants; boundary dan SCP membatasi. Explicit deny yang berlaku menang.|l002|Identity & access
STS|Temporary badge · kartu sementara|Dapatkan temporary AWS credentials melalui role assumption atau federation.|STS menerbitkan session credentials; IAM mendefinisikan izin dan trust.|l004|Identity & access
IAM Identity Center|Staff entrance · pintu karyawan|Satu akses workforce ke banyak AWS accounts dan business apps.|Untuk workforce; Cognito ditujukan bagi identitas pengguna aplikasi.|l009|Identity & access
Cognito user pools|App login · direktori pelanggan|Sign-up, sign-in dan tokens untuk pengguna aplikasi.|User pool menghasilkan tokens; identity pool memberi temporary AWS credentials.|l005|Identity & access
Cognito identity pools|Token → AWS credentials|Tukar identitas yang dipercaya menjadi credentials AWS dengan izin role.|Bukan pengganti direktori user pool; kedua komponen dapat dipakai bersama.|l005|Identity & access
Organizations|Account family · keluarga akun|Kelompokkan accounts dalam OUs, consolidated billing dan organization policies.|Billing gabungan tidak menyatukan resource atau otomatis memberi akses antar-account.|l007|Govern accounts
SCPs|Permission ceiling · pagar organisasi|Batasi maximum permissions bagi principal member accounts yang tercakup.|SCP tidak memberi izin. Pengecualian scope, termasuk management account, perlu dipahami.|l008|Govern accounts
Control Tower|Landing zone · standar awal|Siapkan dan govern multi-account environment dengan controls dan Account Factory.|Control Tower memakai layanan seperti Organizations; bukan pengganti seluruh policy design.|l010|Govern accounts
Resource Access Manager (RAM)|Share resources · berbagi infrastruktur|Bagikan supported resources, misalnya subnets, ke accounts lain.|Resource sharing bukan berarti berbagi semua isi account atau menyalin resource.|l011|Govern accounts
AWS Managed Microsoft AD|Managed real AD · domain dikelola|Butuh Microsoft Active Directory dan integrasi atau trust yang didukung.|AWS mengelola domain controllers; AD Connector hanya proxy ke AD yang sudah ada.|l006|Directory Service
AD Connector|Directory proxy · jembatan AD|Teruskan directory requests ke on-premises Microsoft AD.|Tidak menyimpan direktori mandiri; membutuhkan konektivitas ke AD asal.|l006|Directory Service
Simple AD|Basic directory · kebutuhan dasar|Butuh directory berbasis Samba dengan subset fitur kompatibel AD.|Bukan full Microsoft AD; jangan pilih bila membutuhkan fitur atau trust yang tidak didukung.|l006|Directory Service
''')
add('security','Security & encryption','Bagaimana melindungi dan menemukan ancaman?','WAF = request web · Shield = DDoS · Inspector = celah · GuardDuty = ancaman · Macie = data sensitif.','#ae4b40','security-services','''
KMS|Key manager · pengelola kunci|Kelola encryption keys, access policies dan integrasi enkripsi AWS.|KMS biasanya melindungi data key dalam envelope encryption; bukan tempat menyimpan password aplikasi.|l013|Encrypt & protect secrets
CloudHSM|Dedicated vault · HSM khusus|Butuh kontrol cryptographic users dan keys pada dedicated HSM cluster.|Lebih banyak kontrol dan tanggung jawab operasional daripada KMS.|l016|Encrypt & protect secrets
Secrets Manager|Rotate secrets · putar rahasia|Simpan secrets dan otomatiskan rotation untuk integrasi yang sesuai.|Parameter Store cocok untuk konfigurasi; rotation Secrets Manager tetap perlu setup dan dukungan target.|l014|Encrypt & protect secrets
SSM Parameter Store|Config shelf · rak konfigurasi|Simpan parameter hierarkis, termasuk SecureString dengan KMS.|Bukan layanan rotation database credential yang setara Secrets Manager.|l014|Encrypt & protect secrets
Certificate Manager (ACM)|TLS certificates · identitas endpoint|Provision dan manage certificates untuk integrations dan exportable use cases yang didukung.|Certificate untuk TLS berbeda dari KMS data encryption key. Exported renewals perlu didistribusikan.|l015|Encrypt & protect secrets
WAF|Web request filter · saringan HTTP|Filter HTTP(S) requests berdasarkan rules, IP, rate dan attack patterns.|Layer aplikasi; security groups memfilter koneksi jaringan, bukan SQL injection di request.|l019|Prevent & inspect
Shield|DDoS shield · tahan banjir|Lindungi availability dari DDoS; bedakan Standard dan Advanced.|Bukan pengganti WAF rules atau capacity/resilience design.|l019|Prevent & inspect
Firewall Manager|Policy across accounts|Kelola supported security policies secara terpusat lintas organization.|Pengelola kebijakan, bukan firewall inline yang memeriksa semua packet sendiri.|l019|Prevent & inspect
Network Firewall|VPC inspection · pemeriksaan trafik|Stateful/stateless inspection traffic VPC melalui firewall endpoints.|Route traffic melalui endpoint; membuat firewall saja tidak mengubah route otomatis.|l089|Prevent & inspect
Inspector|Find vulnerabilities · cari celah|Assess vulnerabilities pada supported workloads dan images.|Celah software berbeda dari suspicious behavior yang dicari GuardDuty.|l020|Detect & investigate
GuardDuty|Threat detector · cari perilaku aneh|Deteksi potensi ancaman dari sumber telemetry dan protections yang didukung.|Findings butuh investigation/response; tidak otomatis memblokir semua ancaman.|l020|Detect & investigate
Macie|Sensitive data · isi S3|Temukan data sensitif dalam supported S3 objects, seperti informasi pribadi.|Menemukan PII tidak otomatis menghapus atau meredaksinya.|l096|Detect & investigate
Security Hub|Findings hub · kumpulkan temuan|Centralize dan prioritize security findings serta posture checks.|CloudTrail mencatat activity; Security Hub merangkum findings dari berbagai sumber.|l021|Detect & investigate
Detective|Investigation graph · hubungkan bukti|Telusuri relationships dan konteks activity untuk investigasi security.|Memperdalam penyebab; bukan pengganti GuardDuty threat detection.|l021|Detect & investigate
''')
add('compute','Compute & containers','Di mana kode berjalan?','EC2 = mesin · ECS/EKS = pengatur · Fargate = kapasitas container · ECR = gudang image · Lambda = function.','#9b6518','compute-services','''
EC2|Virtual machine · mesin virtual|Butuh kontrol OS, instance type, networking dan software server.|Kontrol lebih besar berarti patching dan pengelolaan guest OS menjadi tanggung jawabmu.|l022|Run code
EC2 Auto Scaling|Fleet size · jumlah mesin|Maintain desired capacity dan sesuaikan jumlah instances dengan demand.|ASG menambah kapasitas; load balancer membagi traffic.|l023|Run code
Lambda|Event → function|Jalankan code on demand dari request atau event tanpa mengelola server.|Perhatikan invocation model, duration, concurrency dan idempotency; bukan server panjang tanpa batas.|l027|Run code
AWS Batch|Queue → finite jobs|Jadwalkan batch jobs dan provision compute sesuai kebutuhan job.|Batch menjadwalkan pekerjaan; Step Functions mengorkestrasi alur beberapa langkah.|l057|Run code
Elastic Beanstalk|Deploy app · platform aplikasi|Deploy web application pada supported platform dengan environment management.|Resource seperti EC2/ALB tetap ada dan dapat memerlukan konfigurasi; bukan Lambda.|l066|Run code
ECS|AWS container scheduler|Kelola container tasks dan services menggunakan orkestrasi AWS.|ECS adalah orchestrator; Fargate atau EC2 menyediakan compute.|l025|Containers
EKS|Managed Kubernetes|Butuh Kubernetes API dan ecosystem dengan managed control plane.|Managed control plane tidak berarti semua node dan add-ons bebas operasi.|l026|Containers
Fargate|Containers without hosts|Jalankan supported ECS tasks atau EKS pods tanpa mengelola EC2 hosts.|Fargate bukan image registry dan bukan orchestrator terpisah.|l025|Containers
ECR|Image registry · gudang image|Simpan, version dan distribusikan container images.|ECR menyimpan image; ECS/EKS menjalankan container dari image.|l025|Containers
ECS Anywhere|ECS on your servers|Kelola containers pada supported external infrastructure dengan ECS.|Host tetap milik dan dikelola customer; bukan Fargate di on-premises.|l026|Containers
EKS Anywhere|Kubernetes on your infrastructure|Buat dan operasikan Kubernetes di infrastructure sendiri dengan tooling EKS Anywhere.|Berbeda dari EKS regional control plane; pahami responsibility model.|l026|Containers
Outposts|AWS at your site|Butuh supported AWS infrastructure/services secara on-premises.|Bukan sekadar VPN ke Region; ada hardware, capacity dan connectivity planning.|l035|Hybrid & edge
Local Zones|AWS near a city|Tempatkan supported workloads lebih dekat ke pengguna metro-area.|Bukan CloudFront cache; ini kapasitas infrastructure yang terhubung ke parent Region.|l035|Hybrid & edge
Wavelength|Telecom edge · dekat jaringan seluler|Low-latency supported workloads dekat telecom network edge.|Cek lokasi dan operator; bukan layanan yang tersedia di semua AZ.|l035|Hybrid & edge
''')
add('network','Network & delivery','Bagaimana request mencapai tujuan?','Route 53 = nama · ALB/NLB = bagi traffic · CloudFront = cache edge · Global Accelerator = jalur global.','#3068ab','networking-services','''
VPC|Your network · jaringan virtual|Rancang subnets, routing dan security boundaries dalam satu Region.|Subnet berada pada satu AZ; membuat VPC tidak otomatis menyediakan internet access.|l082|Network foundation
Security groups|Stateful allow · pagar resource|Allow traffic yang diperlukan pada supported resources/interfaces.|Return traffic untuk connection yang diizinkan bersifat stateful; tidak ada explicit deny rules.|l083|Network foundation
Network ACLs|Stateless subnet rules|Allow/deny traffic di batas subnet dengan numbered rules.|Periksa arah request dan return, termasuk ephemeral ports.|l083|Network foundation
Internet gateway|Internet doorway · pintu internet|Sediakan jalur internet untuk resources dengan addressing dan routing yang sesuai.|Private IPv4 instance tanpa public IP tidak mendapat internet hanya dengan IGW route.|l083|Network foundation
NAT gateway|Private IPv4 egress|Biarkan private IPv4 resources memulai koneksi keluar melalui NAT.|Tidak membuka arbitrary inbound connection dari internet ke instance private.|l083|Network foundation
VPC peering|Two-network link|Hubungkan dua VPC dengan IP ranges yang kompatibel.|Tidak transitive; A–B dan B–C tidak otomatis memberi A–C.|l084|Connect networks
Transit Gateway|Routing hub · hub jaringan|Hub-and-spoke untuk banyak VPC serta hybrid attachments.|Route tables dan attachment propagation menentukan konektivitas; bukan otomatis semua saling akses.|l084|Connect networks
PrivateLink|Private service access|Expose atau konsumsi supported service melalui private endpoint.|Akses service berbeda dari full network connectivity melalui peering/TGW.|l085|Private service paths
Gateway endpoints|S3/DynamoDB route shortcut|Akses S3 atau DynamoDB melalui endpoint pada route table yang sesuai.|Berbeda dari interface endpoint dengan private ENIs dan security groups.|l085|Private service paths
Interface endpoints|Service through private ENIs|Akses supported services melalui private IP endpoint di subnets.|Perhatikan DNS, security groups, endpoint policies dan biaya; tidak semua service memakai gateway endpoint.|l085|Private service paths
Site-to-Site VPN|Encrypted network tunnel|Hubungkan on-premises network dengan AWS melalui IPsec tunnels.|VPN memberikan encrypted tunnel; dedicated link adalah peran Direct Connect.|l086|Hybrid access
Client VPN|Remote user tunnel|Akses private resources untuk individual remote users.|Bukan koneksi site-wide appliance seperti Site-to-Site VPN.|l086|Hybrid access
VPN CloudHub|VPN hub for branches|Komunikasi antar supported remote networks melalui hub VPN dan routing yang tepat.|Pahami BGP dan route requirements; jangan anggap semua tunnel otomatis saling terhubung.|l086|Hybrid access
Direct Connect|Dedicated network path|Dedicated connectivity ke AWS dengan VIF yang sesuai tujuan.|Bukan otomatis end-to-end encryption; rancang encryption dan redundant connections jika dibutuhkan.|l087|Hybrid access
Route 53|DNS decisions · memilih alamat|Domain/DNS hosting, routing policies dan health-based DNS responses.|DNS failover tidak mempromosikan database atau menyalin state aplikasi.|l031|DNS & discovery
Route 53 Resolver|Hybrid DNS bridge|Inbound: on-prem bertanya ke AWS. Outbound: AWS meneruskan query ke DNS lain.|Arah request DNS menentukan jenis endpoint; jangan terbalik.|l033|DNS & discovery
Cloud Map|Service discovery · cari endpoint|Registry untuk menemukan supported service instances dan attributes.|Discovery tidak sama dengan load balancing atau application health recovery.|l070|DNS & discovery
Application Load Balancer (ALB)|HTTP routing · Layer 7|Host/path routing untuk HTTP(S) applications dan integrations yang didukung.|Butuh TCP/UDP pass-through atau static IP per AZ? Evaluasi NLB.|l028|Load balancing
Network Load Balancer (NLB)|Transport flows · Layer 4|Traffic TCP/UDP/TLS dengan flow-based routing dan alamat statis per AZ.|Tidak melakukan host/path HTTP routing seperti ALB.|l028|Load balancing
Gateway Load Balancer (GWLB)|Fleet of appliances|Sisipkan dan scale virtual network appliances melalui GENEVE.|Traffic inspection appliances berbeda dari routing HTTP ke web servers.|l028|Load balancing
CloudFront|Edge cache · dekat pengguna|Deliver/cache HTTP(S) content melalui edge locations dan origin policies.|Global Accelerator tidak melakukan content caching; cache correctness tergantung cache key/TTL.|l042|Global & edge
Global Accelerator|Global static IPs|Anycast static IPs dan routing AWS global network untuk supported endpoints.|Memperbaiki jalur/routing; bukan CDN object cache.|l034|Global & edge
CloudFront Functions|Light edge logic|Manipulasi ringan viewer request/response seperti URL atau headers.|Runtime constraints berbeda dari Lambda@Edge; tidak memilih hanya karena sama-sama function.|l044|Global & edge
Lambda@Edge|Richer edge processing|Jalankan supported request/response logic pada CloudFront event stages.|Beda deployment, runtime limits dan trigger scope dari Lambda regional/CloudFront Functions.|l044|Global & edge
''')
add('storage','Storage & files','Apakah data berupa object, block, atau file?','S3 = object · EBS = disk · EFS = NFS bersama · FSx = filesystem khusus.','#387e4e','storage-services','''
S3|Object store · bucket + key|Simpan objects untuk data lake, backup, media atau static assets.|Bukan POSIX filesystem atau block disk; access pattern menentukan storage class.|l038|Objects
S3 Glacier classes|Archive · jarang diambil|Arsipkan objects dengan access frequency, retrieval time dan minimum-duration yang sesuai.|Glacier Instant, Flexible dan Deep Archive memiliki retrieval characteristics berbeda.|l073|Objects
S3 access points|Separate access doors|Berikan endpoint dan policy terpisah untuk akses bucket oleh aplikasi/tim.|Access point mengatur akses; tidak membuat copy data otomatis.|l018|Objects
S3 Multi-Region Access Points|One global S3 entry|Gunakan global access point untuk supported multi-Region bucket architecture.|Routing saja tidak mereplikasi objects; replication harus dikonfigurasi.|l018|Objects
S3 Object Lambda|Transform on read|Pola transform response S3 saat dibaca, misalnya redaction.|Ketersediaan untuk customer baru dibatasi; pelajari konsep tanpa mengasumsikan eligibility.|l018|Objects
S3 Transfer Acceleration|Faster long-distance upload|Gunakan edge network path untuk transfer S3 lintas jarak bila hasil pengujian menguntungkan.|Berbeda dari CloudFront content delivery; ukur biaya dan benefit pada lokasi nyata.|l039|Objects
EBS|Persistent block disk|Block volumes untuk EC2 dan supported workloads dalam scope AZ.|Berbeda dari shared NFS. Snapshot membantu recovery; volume bukan otomatis multi-AZ.|l036|Block & shared files
EC2 instance store|Local temporary disk|Butuh local low-latency scratch, cache atau replicated transient data.|Data tidak tahan pada semua lifecycle events; jangan jadikan satu-satunya copy penting.|l036|Block & shared files
EFS|Shared Linux NFS|Banyak supported compute clients mengakses shared filesystem.|EFS memakai NFS; Windows SMB/AD requirements sering mengarah ke FSx Windows.|l037|Block & shared files
FSx for Windows File Server|Windows SMB + AD|Shared Windows file workloads dengan SMB dan Active Directory.|Bukan NFS EFS atau HPC Lustre; protocol menjadi decisive constraint.|l040|FSx family
FSx for Lustre|Parallel HPC filesystem|High-throughput parallel processing seperti HPC/ML dengan data integration yang sesuai.|Pilih deployment durability yang cocok; filesystem performance bukan backup strategy.|l040|FSx family
FSx for NetApp ONTAP|NetApp in AWS|Butuh ONTAP capabilities, storage efficiencies dan supported file/block protocols.|ONTAP semantics berbeda dari sekadar Windows SMB share atau object bucket.|l040|FSx family
FSx for OpenZFS|ZFS filesystem|Butuh managed OpenZFS, NFS access dan ZFS snapshot/clone capabilities.|Jangan tertukar dengan Lustre parallel HPC atau ONTAP multiprotocol features.|l040|FSx family
Data Lifecycle Manager|Automate EBS snapshots|Otomatiskan lifecycle EBS snapshots dan EBS-backed AMIs.|AWS Backup mengelola backup lintas supported services dengan kebijakan lebih luas.|l036|Protection
AWS Backup|Central backup policy|Jadwalkan, retain dan govern recovery points lintas supported resources.|Backup tidak identik dengan continuous server replication melalui DRS.|l081|Protection
''')
add('database','Databases & caching','Bagaimana aplikasi menyimpan dan membaca state?','RDS/Aurora = relasional · DynamoDB = key-value · DocumentDB = dokumen · ElastiCache/DAX = cache.','#7a55a4','database','''
RDS|Managed relational engine|Relational database dengan engine dan operational features yang didukung.|Multi-AZ DB instance standby bukan read replica; Multi-AZ DB clusters memiliki readable standbys.|l048|Relational
RDS Proxy|Connection pool · hemat koneksi|Pool/manage koneksi aplikasi ke supported relational databases, termasuk spiky Lambda.|Membantu koneksi; tidak menghilangkan semua bottleneck query atau storage.|l048|Relational
Aurora|AWS relational architecture|MySQL/PostgreSQL-compatible database dengan storage dan compute architecture Aurora.|Compatibility bukan berarti semua fitur engine asal tersedia persis sama.|l049|Relational
Aurora Serverless|Elastic DB compute|Sesuaikan database compute pada supported Aurora configurations.|Pahami versi dan scaling configuration; jangan menghafal perilaku v1 untuk v2.|l050|Relational
Aurora Global Database|Regional replicas · global reads|Cross-Region reads dan disaster recovery dengan supported Aurora global setup.|Replication lag dan failover procedure tetap menentukan RPO/RTO.|l050|Relational
DynamoDB|Key-value at scale|Predictable key-based access pada managed NoSQL tables.|Desain partition/sort keys dari access patterns; tidak memerlukan relational joins.|l046|NoSQL & search
DynamoDB Streams|Table changes · jejak perubahan|Tangkap item-level changes untuk downstream processing.|Change stream bukan backup jangka panjang; perhatikan retention dan consumer handling.|l046|NoSQL & search
DAX|DynamoDB read cache|Kurangi latency untuk supported DynamoDB read patterns dengan cache.|Tidak mempercepat setiap write atau menyediakan relational caching universal.|l046|NoSQL & search
DocumentDB|MongoDB-compatible documents|Document workloads memakai supported MongoDB-compatible APIs.|Compatibility perlu diuji; jangan menganggap semua MongoDB versions/features didukung.|l060|NoSQL & search
OpenSearch Service|Search & index · cari cepat|Full-text search, indexing dan log analytics.|Bukan pengganti universal transactional database; source-of-truth dan reindex plan tetap dibutuhkan.|l047|NoSQL & search
Timestream for LiveAnalytics|Time-series analytics|Time-stamped measurements dan analytical queries untuk existing eligible customers.|Ditutup untuk customer baru sejak 20 Jun 2025; evaluasi current alternatives untuk proyek baru.|l060|NoSQL & search
ElastiCache|Hot data in memory|Cache frequent reads, supported sessions atau data structures untuk mengurangi backend load.|Redis OSS/Valkey/Memcached capabilities berbeda; cache invalidation dan durability harus dirancang.|l045|Caching
''')
add('integration','Events & integration','Apakah perlu antrian, broadcast, atau workflow?','SQS = antre · SNS = sebarkan · EventBridge = cocokkan event · Step Functions = urutkan langkah.','#b05a29','application-integration','''
SQS|Work queue · satu pekerjaan|Buffer pekerjaan dan decouple producer dari consumers.|Consumers berbagi queue bersaing memproses; bukan setiap consumer mendapat salinan sendiri.|l052|Messages & events
SNS|Fan-out · satu ke banyak|Publish event ke subscribers; gabungkan dengan queues untuk independent buffering.|Pub/sub berbeda dari work queue; perhatikan topic type, retries dan delivery guarantees.|l054|Messages & events
EventBridge|Event router · cocokkan pola|Route events berdasarkan isi, source dan rules ke targets.|Bukan workflow state machine; orchestration panjang lebih cocok Step Functions.|l064|Messages & events
Amazon MQ|Keep broker protocols|Migrasikan aplikasi yang perlu supported ActiveMQ/RabbitMQ compatibility.|Pilih karena protocol compatibility; SQS/SNS menawarkan model API berbeda.|l053|Messages & events
Step Functions|Stateful workflow · alur kerja|Orkestrasi steps, branches, waits, retry, timeout dan human callback.|Standard/Express mempunyai semantics berbeda; side effects tetap butuh idempotency.|l051|APIs & workflows
API Gateway|Managed API front door|Expose REST/HTTP/WebSocket APIs dengan supported auth, throttling dan integrations.|API type memengaruhi fitur dan limits. API keys bukan pengganti authentication.|l029|APIs & workflows
AppSync|GraphQL with resolvers|API GraphQL yang mengambil data dari supported sources dengan resolvers.|GraphQL schema/resolvers berbeda dari generic REST proxy.|l030|APIs & workflows
''')
add('analytics','Data & analytics','Bagaimana data masuk, diolah, dan dianalisis?','Streams = tahan event · Firehose = antar data · Flink = hitung live · Glue = siapkan · Athena = SQL di S3.','#187f82','analytics','''
Kinesis Data Streams|Replayable event stream|Ingest ordered-per-shard records dan izinkan independent consumers/replay.|Beda queue: consumer melacak posisi; partition key menentukan distribution/order scope.|l055|Streaming
Amazon Data Firehose|Delivery pipe · antar data|Buffer, transform sesuai dukungan, lalu deliver ke storage/analytics destinations.|Bukan pengganti replayable stream dengan custom independent consumers.|l055|Streaming
Managed Service for Apache Flink|Stateful live processing|Windows, aggregations dan event-time processing pada streaming data.|Mengolah stream; Firehose terutama mengantarkan data.|l055|Streaming
Amazon MSK|Managed Kafka|Kafka-compatible streaming untuk existing Kafka producers/consumers.|Kafka compatibility menjadi alasan; operations dan partition planning tetap relevan.|l056|Streaming
EMR|Big-data frameworks|Jalankan Spark/Hadoop dan supported big-data ecosystem.|Lebih banyak framework/control daripada query SQL langsung memakai Athena.|l058|Prepare & catalog
AWS Glue|ETL + metadata|Integrasi data, transformation jobs dan metadata/catalog discovery.|Crawler mengidentifikasi metadata; bukan otomatis memperbaiki semua kualitas data.|l058|Prepare & catalog
Glue Data Catalog|Schema directory · katalog data|Bagikan metadata schema, locations dan partitions ke analytics tools.|Metadata catalog bukan penyimpanan seluruh data mentah.|l058|Prepare & catalog
AWS Data Exchange|Subscribe to datasets|Temukan dan akses datasets pihak ketiga melalui supported delivery methods.|Data subscription berbeda dari memindahkan own files dengan DataSync.|l041|Prepare & catalog
Athena|SQL over S3|Ad-hoc SQL pada supported S3 datasets tanpa mengelola cluster.|Partition dan columnar formats memengaruhi data scanned; beda operational transactional DB.|l061|Query & visualize
Redshift|Data warehouse|Analytical SQL pada warehouse dengan compute/storage model yang sesuai.|OLAP analytics berbeda dari OLTP application database seperti RDS.|l059|Query & visualize
Redshift Spectrum|Warehouse queries reach S3|Query supported external S3 data melalui Redshift.|Beda Athena: Spectrum terkait Redshift query environment.|l059|Query & visualize
QuickSight|BI dashboards · tampilkan insight|Buat dashboards dan business visualizations dengan supported data connections.|SPICE menyimpan imported data; refresh dan row-level security perlu konfigurasi.|l061|Query & visualize
''')
add('operations','Observe & operate','Siapa mengubah apa, apa yang rusak, dan bagaimana memperbaikinya?','CloudTrail = aktivitas · CloudWatch = kesehatan · Config = konfigurasi · X-Ray = perjalanan request.','#547a32','management-governance','''
CloudTrail|Who did what? · audit API|Audit AWS account activity dan supported management/data events.|Bukan semua application/SQL logs; event types dan logging scope perlu diaktifkan sesuai kebutuhan.|l012|Observe
CloudWatch|Metrics + alarms|Monitor metrics, dashboards, alarms dan operational signals.|Metrics/alarm berbeda dari audit identitas pada CloudTrail.|l062|Observe
CloudWatch Logs|Application log desk|Collect, retain dan query logs; gunakan filters/subscriptions untuk downstream processing.|Log retention tidak otomatis unlimited/free; destination permissions tetap penting.|l063|Observe
CloudWatch Synthetics|Synthetic visitor · uji dari luar|Canaries menguji endpoint atau user journey secara berkala.|Berbeda dari tracing actual requests yang dilayani aplikasi.|l062|Observe
AWS Config|Configuration timeline|Record supported resource configurations dan evaluate compliance rules.|Compliance detection tidak otomatis remediation; atur remediation action bila dibutuhkan.|l020|Observe
X-Ray|Request trace · ikuti perjalanan|Lacak request lintas instrumented components untuk menemukan latency/errors.|Perlu instrumentation/sampling; trace bukan pengganti seluruh metrics dan logs.|l065|Observe
AWS Health|AWS events affecting you|Lihat service/account events dan planned changes yang relevan.|Berbeda dari aplikasi sendiri down sementara AWS service sehat.|l065|Operate
Systems Manager|Fleet operations · kelola mesin|Manage supported nodes, patches, automation, inventory dan remote operations.|Node registration, IAM dan network endpoints tetap diperlukan.|l070|Operate
Session Manager|Shell without inbound SSH|Akses supported managed nodes dengan IAM dan SSM connectivity.|Tidak berarti otomatis merekam semua port-forwarded/SSH content.|l070|Operate
Run Command|Commands to a fleet|Jalankan perintah pada targeted managed nodes.|Bukan interactive shell; bedakan dari Automation runbooks multi-step.|l070|Operate
Fault Injection Service (FIS)|Controlled failure · uji ketahanan|Jalankan eksperimen fault dengan targets, safeguards dan stop conditions.|Bukan menjalankan chaos tanpa batas; tetapkan hypothesis dan recovery evidence.|l080|Operate
EC2 Instance Connect|Short-lived SSH key|Kirim SSH public key sementara untuk supported EC2 connection methods.|Key delivery tidak menggantikan network path atau security rules untuk SSH.|l021|Operate
''')
add('devops','Build & deploy','Bagaimana perubahan mencapai produksi?','Commit = simpan code · Build = test/package · Pipeline = koordinasi · Deploy = rilis · Formation = infrastructure.','#865177','developer-tools','''
CodeCommit|Git source repository|Simpan source dalam AWS-managed Git repositories.|CodeCommit tidak compile atau deploy. Penerimaan customer baru dibuka kembali pada Nov 2025.|l093|CI/CD stages
CodeBuild|Build & test · buat artifact|Compile, test dan package source sesuai build specification.|Bukan pipeline coordinator dan bukan layanan tanpa semua timeout/quota.|l093|CI/CD stages
CodePipeline|Release conductor · koordinator|Hubungkan source, build, approval dan deployment stages.|Build dilakukan oleh action/service yang terhubung, misalnya CodeBuild.|l093|CI/CD stages
CodeDeploy|Application rollout|Otomatiskan supported rolling, blue/green atau traffic-shifting deployment.|Tidak menggantikan provisioning infrastructure dengan CloudFormation.|l067|CI/CD stages
CloudFormation|Infrastructure templates|Declare dan manage resources melalui stacks, updates dan rollback behavior.|Drift detection hanya pada supported properties; external changes tetap perlu diatasi.|l068|Infrastructure & images
CloudFormation StackSets|Stacks across accounts|Deploy stack instances lintas accounts dan Regions.|StackSets mengelola distribution; bukan sharing existing resource seperti RAM.|l068|Infrastructure & images
CDK|Code → infrastructure|Gunakan programming language untuk define constructs yang synthesize CloudFormation.|CDK bukan aplikasi runtime; hasilnya masih mengikuti deployment lifecycle infrastructure.|l069|Infrastructure & images
SAM|Serverless templates|Abstraksi infrastructure dan tooling untuk serverless applications.|Dibangun di atas CloudFormation; bukan pengganti Lambda compute engine.|l069|Infrastructure & images
Service Catalog|Approved products · katalog standar|Berikan approved infrastructure products dengan governance constraints.|Catalog untuk provisioning products berbeda dari marketplace third-party datasets.|l069|Infrastructure & images
EC2 Image Builder|Golden image pipeline|Build, test dan distribute AMIs/container images secara repeatable.|Image baru tidak otomatis memperbarui instances yang sudah berjalan; butuh rollout.|l097|Infrastructure & images
''')
add('cost','Cost & capacity planning','Bagaimana mengendalikan pemakaian dan biaya?','Explorer = analisis · Budgets = batas/alert · CUR = rincian · Optimizer = ukuran · Savings = komitmen.','#926c20','aws-cost-management','''
Cost Explorer|Explore the bill|Analyze historical costs/usage dan forecasts dengan grouping/filtering.|Analisis biaya berbeda dari budget alert atau permission untuk menghentikan resource.|l074|See & control spend
AWS Budgets|Budget thresholds · pengingat biaya|Pantau cost/usage/reservation budgets dan optional actions yang dikonfigurasi.|Bukan real-time hard spending cap; data billing dan action timing mempunyai delay.|l074|See & control spend
Cost and Usage Report (CUR)|Detailed billing rows|Analisis terperinci billing/usage pada report data dan tooling yang sesuai.|Lebih granular daripada dashboard; perlu pipeline/query dan pemahaman billing fields.|l071|See & control spend
Cost allocation tags|Label the spend|Kelompokkan eligible costs berdasarkan activated tags seperti cost center.|Tagging resource saja tidak menjamin tag langsung aktif untuk semua billing reports.|l071|See & control spend
Compute Optimizer|Rightsize · ukuran yang pas|Gunakan recommendations berbasis utilization untuk supported resources.|Recommendation perlu dicek terhadap peak demand, constraints dan performance goals.|l074|Optimize capacity
Trusted Advisor|Best-practice checks|Tinjau supported recommendations untuk cost, security, performance dan resilience.|Cakupan checks bergantung layanan/support; bukan exhaustive architecture review.|l071|Optimize capacity
Service Quotas|Know your limits|Lihat quotas dan minta increase untuk batas yang adjustable.|Hard quota tidak otomatis bisa dinaikkan; scope account/Region/service penting.|l071|Optimize capacity
Savings Plans|Commit eligible spend|Tukar commitment penggunaan per jam dengan discount pada eligible usage.|Bukan capacity reservation; flexibility bergantung plan type dan commitment tetap dibayar.|l072|Purchase models
Reserved Instances|Match billing attributes|Dapatkan billing benefit untuk eligible usage sesuai reservation attributes.|Regional vs zonal EC2 reservations berbeda; jangan menganggap semua RI selalu menjamin kapasitas.|l024|Purchase models
Spot Instances|Spare capacity · boleh terputus|Gunakan discounted interruptible EC2 capacity untuk fault-tolerant jobs.|Checkpoint dan recovery penting; jangan mengandalkan satu Spot pool untuk critical singleton.|l024|Purchase models
''')
add('migration','Migration & recovery','Memindahkan file, database, atau server?','DataSync = file online · DMS = database · MGN = pindah server · DRS = pulihkan server · Backup = recovery points.','#93623b','migration-services','''
DataSync|Online data transfer|Transfer files/objects dari supported storage ke AWS atau antarlokasi yang didukung.|Bukan database CDC; DMS menangani supported database data migration.|l041|Transfer data
Transfer Family|Managed file protocols|Managed SFTP/FTPS/FTP/AS2 workflows sesuai protocol/endpoints yang didukung.|Berbeda dari DataSync agent-driven transfer; pilih berdasarkan client protocol dan workflow.|l041|Transfer data
S3 File Gateway|File access → S3 objects|Expose supported file shares dengan local caching dan object storage di S3.|NFS/SMB interface di gateway tidak membuat S3 menjadi native POSIX filesystem.|l076|Storage Gateway family
FSx File Gateway|Cached FSx access|Pola cached on-premises access ke FSx Windows pada materi lama.|Layanan ditutup untuk customer baru; cek lifecycle sebelum memilih untuk desain baru.|l076|Storage Gateway family
Volume Gateway|iSCSI volumes + cloud backup|Integrasikan block storage on-premises dengan cached/stored volume model.|Semantics block volume berbeda dari file shares atau virtual tapes.|l076|Storage Gateway family
Tape Gateway|Virtual tapes · backup lama|Integrasikan backup software yang kompatibel dengan virtual tape library.|Bukan general-purpose file server; gunakan untuk tape-oriented backup workflow.|l076|Storage Gateway family
Snowball / Snow family|Ship data · kirim perangkat|Pola offline bulk transfer atau edge processing saat jaringan tidak memadai.|Produk dan eligibility berubah; Snowball Edge dibatasi bagi existing customers sejak Nov 2025.|l077|Transfer data
Database Migration Service (DMS)|Database rows + CDC|Full load dan ongoing change replication untuk supported databases.|Tidak otomatis menyelesaikan semua schema/application incompatibility.|l078|Migrate databases & servers
Schema Conversion Tool (SCT)|Translate the schema|Assess dan convert supported database schema/code antar-engines.|Schema conversion berbeda dari memindahkan rows dan ongoing changes.|l078|Migrate databases & servers
Application Migration Service (MGN)|Rehost servers|Replicate supported source servers dan cut over workloads ke AWS.|Tujuan utamanya migration; DRS mempertahankan recovery capability untuk disaster scenarios.|l080|Migrate databases & servers
Elastic Disaster Recovery (DRS)|Standby server recovery|Continuous replication dan launch recovery instances saat disaster/drill.|Replication bisa ikut menyalin kerusakan logis; tetap rancang backup dan recovery points.|l080|Migrate databases & servers
Application Discovery Service|Inventory & dependencies|Kumpulkan informasi source environment untuk migration planning.|Discovery memberi evidence; bukan melakukan server cutover sendiri.|l080|Plan migration
Migration Hub|Migration tracking|Track progress dan coordinate supported migration tools/workstreams.|Bukan satu engine yang memindahkan semua jenis workload.|l080|Plan migration
Migration Evaluator|Build the business case|Estimasi migration economics dari inventory dan utilization evidence.|Projected savings bergantung assumptions; bukan guarantee setelah go-live.|l080|Plan migration
''')
add('ai','AI & machine learning','Apakah input berupa teks, suara, gambar, atau dokumen?','Rekognition = lihat · Transcribe = dengar→teks · Polly = teks→suara · Textract = baca form · Comprehend = makna teks.','#895caa','machine-learning','''
Amazon Bedrock|Foundation models · GenAI|Bangun generative AI applications dengan supported models dan managed capabilities.|RAG menambah context saat inference; fine-tuning mengubah model behavior melalui training.|l090|Build models & retrieval
SageMaker AI|ML development lifecycle|Build, train dan deploy ML dengan managed tooling dan infrastructure.|Untuk custom ML lifecycle; Bedrock berfokus pada penggunaan foundation models dan GenAI capabilities.|l092|Build models & retrieval
Kendra|Enterprise search|Cari informasi dalam enterprise content melalui supported connectors/search.|Search/retrieval bukan otomatis menghasilkan jawaban generatif yang selalu benar.|l092|Build models & retrieval
Personalize|Recommendations · pilihan personal|Bangun personalized recommendations dari interaction/catalog data yang sesuai.|Berbeda dari general text generation atau BI dashboard.|l092|Build models & retrieval
Rekognition|Images & video · lihat|Analyze supported visual content, labels atau moderation tasks.|OCR structured forms/tables lebih cocok Textract; cek capabilities sesuai use case.|l091|Images & documents
Textract|Documents → structured data|Extract text, forms dan tables dari supported documents.|Bukan semantic NLP classifier; Comprehend bekerja pada teks untuk meaning/entity analysis.|l092|Images & documents
Transcribe|Speech → text|Ubah audio speech menjadi transcript dengan supported features/languages.|Arah kebalikan Polly; transcription tidak sama dengan translation.|l091|Speech & language
Polly|Text → speech|Buat spoken audio dari text dengan voices/SSML yang didukung.|Tidak mentranskripsikan rekaman suara; itu tugas Transcribe.|l091|Speech & language
Translate|Language → language|Terjemahkan text antar supported languages.|Tidak mengubah audio ke text tanpa transcription step.|l091|Speech & language
Comprehend|Text → meaning|Analyze supported entities, sentiment dan NLP signals dari teks.|Textract mengekstrak text dari document image; Comprehend menganalisis text.|l091|Speech & language
Comprehend Medical|Clinical text entities|Extract supported medical information dari clinical text.|Domain/language support terbatas dan hasil perlu validasi; bukan diagnosis otomatis.|l091|Speech & language
Lex|Conversational interface|Bangun voice/text bot dengan intents dan conversational flows.|Lex menangani interaction; Connect menyediakan contact-center experience.|l091|Speech & language
''')
add('workplace','Users, devices & media','Bagaimana layanan mencapai orang dan perangkat?','WorkSpaces = desktop · AppStream = aplikasi · Device Farm = uji device · IoT Core = pesan device · SES = email.','#4d7287','end-user-computing','''
Amazon Connect|Cloud contact center|Rancang customer contact flows dan agent/customer interactions.|Lex adalah conversational bot; Connect menghubungkan pengalaman contact center yang lebih luas.|l094|People & communication
Amazon SES|Application email|Kirim transactional/bulk email dengan identity, reputation dan feedback handling.|Email delivery berbeda dari SNS event fan-out atau campaign journey orchestration.|l096|People & communication
Amazon Pinpoint|Audience campaigns|Kenali pola segments, campaigns dan journeys yang dibahas slide lama.|AWS mengakhiri support 30 Oct 2026; cek migration guidance dan AWS End User Messaging.|l096|People & communication
WorkSpaces|Managed desktops|Berikan virtual desktop experience bagi workforce dengan supported options.|Berbeda dari streaming satu aplikasi; persistence dan DR bergantung deployment.|l095|Desktop & testing
AppStream 2.0 / WorkSpaces Applications|Stream applications|Berikan remote application/non-persistent desktop access melalui supported clients.|AppStream 2.0 kini bernama WorkSpaces Applications; bedakan dari persistent desktop requirement.|l095|Desktop & testing
Device Farm|Test on devices|Uji mobile/web applications pada supported real devices dan browsers.|Testing platform, bukan virtual desktop untuk karyawan.|l095|Desktop & testing
IoT Core|Device message hub|Authenticate/connect devices dan route messages melalui pub/sub serta rules.|Offline buffering, downstream failures dan device lifecycle tetap perlu didesain.|l097|Devices & media
Kinesis Video Streams|Camera video pipeline|Ingest/store supported video streams untuk playback atau processing.|Raw video berbeda dari small structured events di Kinesis Data Streams.|l094|Devices & media
''')
D={'title':'AWS Service Memory Map','updated':'2026-10-11','scope':'Services and major features taught in the 101-lesson course. Grouping is for memorization, not an AWS architecture or an exhaustive catalog of every AWS product.','categories':categories}
# Tie every card back to the course and give service aliases searchable expansions.
gloss=json.loads((ROOT/'dist/glossary.json').read_text())
for cat in categories:
 cat['source']='https://docs.aws.amazon.com/whitepapers/latest/aws-overview/'+cat['source']+'.html'
 for s in cat['services']:
  candidates=[g for g in gloss if g['term'].lower()==s['name'].lower() or s['name'].startswith(g['term']+'|')]
  s['expansion']=candidates[0]['expansion'] if candidates else ''
updates={
 'application-migration-service-mgn':('Renamed','AWS Application Migration Service is now AWS Transform MGN; the slides retain the earlier name.','https://docs.aws.amazon.com/mgn/latest/ug/General-Questions-FAQ.html'),
 'amazon-pinpoint':('Lifecycle change','Support ends 30 October 2026. Messaging channel APIs continue under AWS End User Messaging.','https://docs.aws.amazon.com/pinpoint/latest/archguide/welcome.html'),
 'codecommit':('Availability update','New customer access reopened in November 2025.','https://docs.aws.amazon.com/codecommit/latest/userguide/history.html'),
 'appstream-2-0-workspaces-applications':('Renamed','AppStream 2.0 is now Amazon WorkSpaces Applications.','https://aws.amazon.com/workspaces/applications/'),
 'timestream-for-liveanalytics':('Existing customers','New customer access closed on 20 June 2025.','https://docs.aws.amazon.com/timestream/latest/developerguide/AmazonTimestreamForLiveAnalytics-availability-change.html'),
 'snowball-snow-family':('Check eligibility','Snowball Edge availability is restricted to existing customers.','https://aws.amazon.com/snowball/faqs/'),
 's3-object-lambda':('Check eligibility','Restricted to existing customers and selected partners from November 2025.','https://docs.aws.amazon.com/AmazonS3/latest/userguide/transforming-objects.html'),
 'fsx-file-gateway':('Existing customers','FSx File Gateway is no longer open to new customers.','https://docs.aws.amazon.com/filegateway/latest/filefsxw/what-is-file-fsxw.html')}
for cat in categories:
 for s in cat['services']:
  if s['id'] in updates:
   tag,note,url=updates[s['id']];s['update']={'tag':tag,'note':note,'url':url}
(ROOT/'dist/mindmap.json').write_text(json.dumps(D,ensure_ascii=False,indent=2))
print(len(categories),'categories;',sum(len(c['services']) for c in categories),'services and features')
