import json
from pathlib import Path
P=(Path(__file__).resolve().parent/'dist')
raw='''IAM|Identity and Access Management|Mengatur siapa boleh melakukan action pada resource AWS.
Principal|Requesting identity|User, role session, atau service yang membuat request.
Policy|Permission document|Dokumen yang menyatakan allow/deny, actions, resources, dan conditions.
ARN|Amazon Resource Name|Identifier resource AWS; bucket ARN berbeda dari object ARN.
Least privilege|Minimum necessary permission|Berikan izin secukupnya untuk tugas yang benar-benar diperlukan.
Explicit deny|Stated prohibition|Larangan tertulis yang mengalahkan allow yang berlaku.
Implicit deny|No applicable allow|Ditolak karena tidak ada izin yang berlaku, berbeda dari explicit deny.
Trust policy|Role assumption policy|Policy role yang menentukan principal mana boleh assume role.
Permissions boundary|Identity permission ceiling|Batas maksimal izin user/role; tidak memberikan izin sendiri.
ABAC|Attribute-based access control|Izin ditentukan dengan attributes/tags, misalnya department yang sama.
RBAC|Role-based access control|Izin dikelompokkan berdasarkan peran pekerjaan.
STS|Security Token Service|Menerbitkan temporary AWS credentials, termasuk session token.
AssumeRole|Create a role session|Meminta temporary credentials untuk menjalankan izin role yang dipercaya.
ExternalId|Customer context for a third party|Nilai unik dari vendor untuk mencegah confused deputy; bukan password.
Confused deputy|Misused trusted intermediary|Pihak tepercaya ditipu agar memakai kewenangannya untuk customer yang salah.
Session tag|Temporary principal attribute|Tag pada role/federated session untuk evaluasi ABAC.
MFA|Multi-factor authentication|Membuktikan identitas dengan lebih dari satu faktor.
Federation|Trust an external identity provider|AWS menerima bukti login dari sistem identity lain.
IdP|Identity provider|Sistem yang mengautentikasi user dan menerbitkan bukti identity.
SAML|Security Assertion Markup Language|Standar federation assertions yang sering dipakai enterprise SSO.
OIDC|OpenID Connect|Identity layer berbasis OAuth 2.0, sering memakai ID tokens.
OAuth|Delegated authorization framework|Kerangka delegasi access; authentication biasanya ditambahkan melalui OIDC.
JWT|JSON Web Token|Token dengan claims dan signature yang perlu divalidasi dengan benar.
SSO|Single sign-on|Satu login untuk mengakses beberapa aplikasi/accounts sesuai izin.
Identity Center|AWS workforce access service|Mengatur workforce login dan account/application assignments.
Permission set|AWS account access template|Paket permissions yang diprovisikan untuk akses account melalui Identity Center.
Cognito user pool|Application user directory|Mengautentikasi app users dan menerbitkan tokens.
Cognito identity pool|Federated AWS credentials|Menukar identity yang didukung menjadi temporary AWS credentials.
AD|Active Directory|Directory Microsoft untuk users, computers, groups, dan domain services.
ADFS|Active Directory Federation Services|Menyediakan federation/SSO menggunakan identity enterprise.
DC|Domain controller|Server yang menyediakan layanan directory/authentication dalam AD domain.
Forest trust|Cross-forest authentication trust|Hubungan percaya antar-AD forests; tidak otomatis menyalin user objects.
LDAP|Lightweight Directory Access Protocol|Protocol untuk mengakses informasi directory.
OU|Organizational unit|Kelompok accounts dalam AWS Organizations untuk menerapkan controls.
SCP|Service control policy|Permission ceiling organisasi untuk principal member accounts yang tercakup.
RAM|Resource Access Manager / memory|Dalam governance: service berbagi resources. Dalam compute: random-access memory.
Landing zone|Governed AWS foundation|Struktur awal multi-account dengan identity, logging, network dan controls.
Account Factory|Standardized account provisioning|Membuat account menggunakan baseline yang disetujui dalam Control Tower.
Guardrail|Governance control|Control preventive, detective, atau proactive sesuai mekanismenya.
CloudTrail|AWS API audit events|Mencatat activity API; bukan semua application atau SQL logs.
Management event|Control-plane operation|Contoh: membuat subnet, mengubah policy, menjalankan instance.
Data event|Supported resource-level operation|Contoh: membaca object S3; perlu konfigurasi logging yang sesuai.
KMS|Key Management Service|Mengelola dan memakai cryptographic keys melalui AWS APIs/policies.
CMK|Customer master key, legacy term|Istilah lama; dokumentasi kini memakai KMS key/customer-managed key.
Envelope encryption|Encrypt data keys with another key|Data key mengenkripsi data; KMS key melindungi data key itu.
DEK|Data encryption key|Kunci yang langsung dipakai untuk mengenkripsi data.
AES|Advanced Encryption Standard|Algoritma symmetric encryption; satu secret key untuk operasi terkait.
RSA|Asymmetric cryptographic algorithm|Menggunakan pasangan public/private keys untuk operasi yang didukung.
ECC|Elliptic-curve cryptography|Keluarga cryptography berbasis kurva eliptik.
BYOK|Bring your own key|Memasukkan key material sendiri ke layanan yang mendukungnya.
HSM|Hardware security module|Perangkat khusus untuk menyimpan keys dan melakukan operasi cryptographic.
CloudHSM|Managed dedicated HSM service|AWS mengelola hardware; customer mengelola cryptographic users/keys.
Key policy|KMS resource policy|Menentukan siapa dapat memakai/mengelola KMS key sesuai evaluasi izin.
Key rotation|Change active key material|Mengganti material untuk operasi baru sambil mempertahankan decrypt data lama.
SSE-S3|S3-managed server-side encryption|S3 mengenkripsi object menggunakan keys yang dikelolanya.
SSE-KMS|KMS-backed server-side encryption|Server-side encryption yang memakai KMS dan izin key terkait.
SSE-C|Customer-provided server-side keys|Client menyuplai key untuk operasi S3 yang sesuai; wajib secure transport.
Client-side encryption|Encrypt before upload|Data dienkripsi oleh aplikasi sebelum dikirim ke storage service.
TLS|Transport Layer Security|Melindungi data dalam perjalanan dan memvalidasi peer sesuai konfigurasi.
SSL|Secure Sockets Layer|Istilah lama yang sering masih dipakai untuk menyebut TLS certificates.
SNI|Server Name Indication|Hostname pada TLS handshake untuk memilih certificate yang tepat.
mTLS|Mutual TLS|Client dan server menggunakan certificates untuk authentication dua arah.
CA|Certificate authority|Pihak yang menerbitkan dan menandatangani certificates.
ACM|AWS Certificate Manager|Mengelola certificates untuk integrasi dan exportable use cases yang didukung.
SAN|Subject Alternative Name|Daftar nama yang tercakup dalam certificate.
DNSSEC|DNS Security Extensions|Memvalidasi asal/integritas data DNS; tidak mengenkripsi HTTP traffic.
MITM|Man-in-the-middle|Penyerang menyisipkan diri di antara komunikasi pihak yang sah.
WORM|Write once, read many|Model retention yang melindungi data dari perubahan/deletion yang dilarang.
Object Lock|S3 version retention control|Melindungi object versions melalui retention dan/atau legal hold.
Governance mode|Bypassable-by-authorized retention|Retention dapat dibypass hanya melalui izin/proses yang sesuai.
Compliance mode|Strict protected retention|Retention yang tidak dapat dipersingkat selama masa perlindungan berlaku.
Presigned URL|Time-limited signed request|URL yang mendelegasikan operasi tertentu berdasarkan izin signer.
Access point|Named resource access entry|Endpoint/policy terpisah untuk akses terkontrol ke resource yang didukung.
MRAP|Multi-Region Access Point|Global access point untuk routing ke S3 buckets lintas Regions.
DDoS|Distributed denial of service|Traffic dari banyak sumber membebani layanan agar tidak tersedia.
WAF|Web Application Firewall|Memfilter HTTP requests berdasarkan rules Layer 7.
Web ACL|Web access control list|Kumpulan rules AWS WAF; berbeda dari subnet NACL.
SQLi|SQL injection|Input berbahaya yang mencoba mengubah query database.
XSS|Cross-site scripting|Script berbahaya dijalankan dalam konteks halaman yang dipercayai user.
Shield|AWS DDoS protection|Perlindungan DDoS dengan Standard dan kemampuan Advanced yang relevan.
SRT|Shield Response Team|Tim respons AWS untuk kemampuan Shield Advanced yang berlaku.
CVE|Common Vulnerabilities and Exposures|Identifier publik untuk vulnerability software tertentu.
Inspector|Workload vulnerability assessment|Mencari vulnerabilities pada workloads yang didukung.
GuardDuty|Threat detection|Mendeteksi perilaku mencurigakan dari telemetry yang didukung.
Config|Configuration history and compliance|Merekam konfigurasi resource dan mengevaluasi rules.
Security Hub|Security findings aggregation|Menggabungkan dan memprioritaskan findings dari sumber yang didukung.
Detective|Security investigation context|Membantu menganalisis hubungan dan akar suspicious activity.
EC2|Elastic Compute Cloud|Virtual servers dengan pilihan compute, networking dan storage.
AMI|Amazon Machine Image|Template software/configuration awal untuk membuat EC2 instance.
vCPU|Virtual central processing unit|Unit kapasitas CPU virtual; bukan selalu satu physical core.
Graviton|AWS Arm processors|CPU AWS yang memerlukan OS/binaries compatible dengan Arm.
Placement group|EC2 placement strategy|Mengatur cluster, spread, atau partition placement sesuai kebutuhan.
HPC|High-performance computing|Komputasi berat, sering paralel dan sensitif komunikasi antar-node.
ENA|Elastic Network Adapter|Interface enhanced networking pada EC2 yang mendukungnya.
EFA|Elastic Fabric Adapter|Networking untuk komunikasi HPC/ML antar-node berlatensi rendah.
MPI|Message Passing Interface|Standar komunikasi antar-process pada parallel computing.
SR-IOV|Single-root I/O virtualization|Teknik virtualisasi I/O untuk akses networking yang lebih efisien.
ASG|Auto Scaling group|Menjaga dan menyesuaikan jumlah EC2 instances sesuai konfigurasi.
Target tracking|Scale toward a metric target|Menambah/mengurangi capacity agar metric mendekati target.
Lifecycle hook|Pause an ASG lifecycle transition|Memberi waktu untuk bootstrap/cleanup sebelum transisi selesai.
Instance Refresh|Rolling ASG instance replacement|Mengganti instances agar memakai template/AMI terbaru secara terkontrol.
Warm-up|Time before capacity is ready|Waktu bootstrap dan stabilisasi sebelum instance dianggap siap scaling/traffic.
Spot|Interruptible spare compute capacity|Capacity diskon dengan kemungkinan interruption; workloads harus toleran.
RI|Reserved Instance|Model pembelian/discount dengan atribut dan scope tertentu.
Savings Plan|Usage-spend commitment discount|Commitment untuk eligible usage dengan pilihan fleksibilitas tertentu.
Dedicated Host|Customer-dedicated physical server|Kontrol host fisik yang membantu kebutuhan tenancy atau licensing.
Docker|Container tooling/platform|Membungkus aplikasi dan dependensinya dalam image.
Container image|Packaged application filesystem/config|Artifact yang dipakai untuk menjalankan container.
ECR|Elastic Container Registry|Registry untuk menyimpan dan mendistribusikan container images.
ECS|Elastic Container Service|Orchestrator AWS untuk menjalankan tasks/containers.
EKS|Elastic Kubernetes Service|Layanan managed Kubernetes control plane AWS.
Fargate|Managed container compute|Menjalankan containers yang didukung tanpa mengelola EC2 hosts.
Task definition|ECS execution specification|Deskripsi image, CPU, memory, networking, roles dan container settings.
Task role|Application AWS permissions|Role yang digunakan code di ECS task untuk mengakses AWS APIs.
Execution role|Platform task-start permissions|Izin ECS untuk actions seperti image pull, log delivery dan secret injection.
ENI|Elastic network interface|Interface network virtual dengan addresses dan security groups yang relevan.
awsvpc|ECS task networking mode|Memberi task network interface/private address tersendiri.
CSI|Container Storage Interface|Interface standar integrasi storage untuk container orchestration.
Pod|Kubernetes workload unit|Satu atau beberapa containers yang dijadwalkan bersama.
Lambda|Event-driven function compute|Menjalankan code berdasarkan invocation tanpa mengelola server biasa.
Concurrency|Simultaneous executions|Berapa executions sedang berjalan bersamaan, bukan requests/s.
Reserved concurrency|Function reservation and ceiling|Mencadangkan sekaligus membatasi concurrency sebuah function.
Provisioned concurrency|Pre-initialized Lambda environments|Capacity siap pakai untuk mengurangi latency startup yang relevan.
Cold start|Execution environment initialization|Waktu persiapan environment sebelum request diproses.
Synchronous|Caller waits for result|Pemanggil menunggu hasil operasi.
Asynchronous|Caller does not wait for completion|Pekerjaan dilanjutkan setelah penerimaan; hasil/retry ditangani terpisah.
ELB|Elastic Load Balancing|Keluarga managed load balancers AWS.
ALB|Application Load Balancer|Load balancer HTTP-aware dengan Layer 7 routing.
NLB|Network Load Balancer|Load balancer flows TCP/UDP/TLS yang didukung dengan static IP options.
GWLB|Gateway Load Balancer|Mengintegrasikan dan membagi traffic ke network appliances.
GENEVE|Generic Network Virtualization Encapsulation|Encapsulation yang digunakan GWLB untuk traffic appliances.
Target group|Registered backend group|Sekumpulan target dengan routing/health settings.
Cross-zone|Balance across AZ targets|Mengirim traffic dari load-balancer node ke targets lintas AZ.
Sticky session|Session affinity|Mengarahkan client ke target yang sama; bisa membuat load tidak seimbang.
Round robin|Cyclic target selection|Membagi pilihan target secara bergiliran.
Flow hash|Connection-based target selection|Hash atribut network flow memilih target selama koneksi.
API|Application programming interface|Kontrak cara program meminta layanan atau data.
REST|Representational state transfer|Gaya API berbasis resources dan operasi HTTP yang umum.
CORS|Cross-origin resource sharing|Mekanisme browser untuk mengizinkan membaca response lintas origin.
SigV4|AWS Signature Version 4|Mekanisme menandatangani AWS API requests dengan credentials.
Authorizer|Request authorization component|Memeriksa token/identity dan menghasilkan keputusan akses API.
API key|Client identification/metering token|Umumnya untuk identifikasi penggunaan; bukan pengganti authentication kuat.
Throttling|Limit request/execution rate|Pembatasan saat penggunaan melebihi kapasitas atau quota.
WebSocket|Persistent bidirectional connection|Koneksi untuk pesan dua arah antara client dan server.
GraphQL|Query language for APIs|Client meminta fields tertentu; resolvers mengambil data dari sources.
Resolver|DNS resolver / GraphQL field handler|Dalam DNS: mencari jawaban nama. Dalam GraphQL: mengambil nilai field.
TTL|Time to live|Batas waktu cache/retention sesuai konteks; tidak selalu deletion tepat waktu.
Alias record|Route 53 selected-target record|Record menuju target yang didukung, termasuk zone apex.
CNAME|Canonical name record|Memetakan hostname ke hostname lain; tidak dipakai pada zone apex.
A record|IPv4 address record|DNS record yang memetakan nama ke IPv4.
AAAA record|IPv6 address record|DNS record yang memetakan nama ke IPv6.
NS record|Name server record|Menentukan authoritative name servers suatu zone.
Hosted zone|DNS record container|Sekumpulan DNS records untuk domain dan subdomains.
Anycast|Same address advertised at multiple locations|Routing membawa client ke salah satu lokasi yang mengiklankan alamat sama.
EIP|Elastic IP address|Public IPv4 statis AWS yang bisa dihubungkan ke supported resources.
Outposts|AWS infrastructure on customer premises|Membawa layanan AWS tertentu ke lokasi customer.
Local Zone|AWS extension near a metro area|Lokasi layanan terpilih dekat pengguna dengan parent Region.
Wavelength|AWS infrastructure at telecom edge|Layanan terpilih untuk low-latency use cases pada jaringan operator.
EBS|Elastic Block Store|Persistent network block volumes dengan scope AZ.
EFS|Elastic File System|Managed shared NFS filesystem untuk workloads yang sesuai.
FSx|Managed filesystem family|Pilihan Windows, Lustre, ONTAP, OpenZFS dengan semantics berbeda.
NFS|Network File System|Protocol shared files yang umum pada Linux/Unix.
SMB|Server Message Block|Protocol shared files yang umum dalam Windows environments.
NTFS|New Technology File System|Filesystem Windows dengan permission/metadata semantics terkait.
POSIX|Portable Operating System Interface|Kumpulan interface/semantics Unix termasuk file operations.
iSCSI|SCSI over IP|Protocol block storage melalui IP network.
IOPS|I/O operations per second|Jumlah operasi storage per detik; berbeda dari byte throughput.
Throughput|Data/work per unit time|Banyak data atau pekerjaan yang diproses per detik.
Latency|Delay per operation|Waktu tunggu suatu operasi/request.
Snapshot|Point-in-time storage copy|Recovery point; consistency dan restore behavior bergantung service.
FSR|Fast Snapshot Restore|Fitur EBS untuk menghindari initialization penalty pada restore yang dikonfigurasi.
DLM|Data Lifecycle Manager|Otomasi lifecycle EBS snapshots dan EBS-backed AMIs.
Ephemeral|Not durable across lifecycle loss|Data bisa hilang saat instance/host lifecycle tertentu berakhir.
S3|Simple Storage Service|Object storage AWS dengan keys, metadata dan storage classes.
Bucket|S3 object container|Namespace/container object dengan policies dan settings sendiri.
Prefix|Beginning of an object key|Bagian awal key untuk organisasi, filtering dan distribusi akses.
CRR|Cross-Region Replication|Replikasi eligible S3 objects ke Region berbeda.
SRR|Same-Region Replication|Replikasi eligible S3 objects dalam Region yang sama.
RTC|Replication Time Control|Komitmen waktu replikasi S3 untuk eligible objects sesuai ketentuan layanan.
Multipart upload|Upload object in parts|Memecah transfer besar menjadi parts untuk parallelism/retry.
Byte-range GET|Read selected object bytes|Mengambil bagian tertentu dari object atau memparalelkan download.
IA|Infrequent access|Kelas/tier untuk data yang jarang diakses dengan trade-off retrieval.
Durability|Data survival probability/design|Kemampuan data tetap tersimpan, bukan frekuensi layanan dapat diakses.
Availability|Service accessibility|Seberapa sering layanan siap diakses dalam kondisi yang ditentukan.
SLA|Service-level agreement|Komitmen kontraktual layanan dengan kondisi/kompensasi tertentu.
CDN|Content delivery network|Jaringan edge untuk mendekatkan delivery/cache ke pengguna.
OAC|Origin Access Control|Mekanisme CloudFront untuk mengamankan akses ke supported origins seperti S3.
OAI|Origin Access Identity|Mekanisme legacy CloudFront untuk S3 origin access.
Cache hit|Requested data found in cache|Response dapat dilayani dari cache tanpa origin fetch terkait.
Cache miss|Requested data absent/stale in cache|Perlu mengambil dari origin atau backing data source.
Cache key|Identity of a cached response|Kombinasi atribut request yang membedakan cache entries.
Invalidation|Remove/expire cached content|Memaksa cache mengambil versi yang sesuai pada request berikutnya.
SPICE|Super-fast, Parallel, In-memory Calculation Engine|Engine in-memory QuickSight untuk imported datasets.
DAX|DynamoDB Accelerator|Cache untuk supported DynamoDB read patterns.
RDS|Relational Database Service|Managed relational databases dengan engine yang didukung.
OLTP|Online transaction processing|Banyak transaksi kecil yang mengubah/membaca data operasional.
OLAP|Online analytical processing|Query analitis/aggregations atas banyak data.
ACID|Atomicity, consistency, isolation, durability|Sifat transaksi database; detail isolation tetap perlu dipahami.
Partition key|Data distribution key|Key untuk menentukan penempatan/logical grouping data.
Sort key|Ordering key within a partition|Bagian key untuk urutan dan range access dalam partition.
GSI|Global secondary index|DynamoDB alternate key index, dapat ditambahkan kemudian.
LSI|Local secondary index|DynamoDB index dengan partition key sama dan sort key lain; saat table dibuat.
RCU|Read capacity unit|Unit kapasitas provisioned reads DynamoDB menurut ukuran/consistency.
WCU|Write capacity unit|Unit kapasitas provisioned writes DynamoDB menurut ukuran/transaction mode.
Strong consistency|Read latest successful relevant write|Read consistency yang lebih kuat dalam scope dukungan layanan.
Eventual consistency|Replicas converge over time|Read bisa sementara tertinggal sebelum perubahan tersebar.
Read replica|Read-serving data copy|Copy untuk scaling reads/DR sesuai engine dan replication behavior.
Multi-AZ|Across Availability Zones|Pola availability lintas AZ; readable standby bergantung jenis deployment.
PITR|Point-in-time recovery|Mengembalikan data ke waktu tertentu dalam recovery window yang didukung.
TDE|Transparent Data Encryption|Encryption database engine pada storage untuk engines yang mendukungnya.
RMAN|Oracle Recovery Manager|Tool Oracle untuk backup/recovery sesuai dukungan deployment.
RAC|Oracle Real Application Clusters|Teknologi clustering Oracle; tidak didukung pada RDS for Oracle standar.
RDS Proxy|Managed database connection proxy|Mengelola pooling/connections ke supported databases.
Writer endpoint|Endpoint to current database writer|Alamat untuk koneksi ke primary/writer yang berlaku.
Reader endpoint|Endpoint for eligible read replicas|Mendistribusikan connections ke eligible replicas, bukan tiap SQL statement.
State machine|Explicit workflow model|Definisi states, transitions, choices, retries, waits dan outcomes.
Callback token|Workflow completion reference|Token yang mengaitkan hasil async/human step dengan workflow yang menunggu.
Idempotency|Same request has no extra effect if repeated|Retry tidak membuat charge/order/action tambahan yang tidak diinginkan.
Backoff|Increase delay between retries|Mengurangi retry storm; jitter menyebarkan timing antar-clients.
Jitter|Randomized retry delay|Variasi waktu retry agar banyak clients tidak retry bersamaan.
SQS|Simple Queue Service|Durable queue untuk decoupling dan buffering pekerjaan.
SNS|Simple Notification Service|Publish/subscribe untuk fan-out ke subscribers yang didukung.
FIFO|First in, first out|Ordering dalam scope seperti message group, dengan deduplication rules terkait.
Visibility timeout|Temporary message hiding after receive|Waktu message tidak terlihat oleh consumers lain saat sedang diproses.
DLQ|Dead-letter queue|Tempat pesan gagal berulang/delivery failure untuk investigasi dan recovery.
Redrive|Move failed messages for reprocessing|Mengirim kembali pesan DLQ setelah masalahnya ditangani.
Long polling|Wait for messages before returning|Mengurangi empty polling responses pada queue.
Fan-out|One event to many consumers|Mengirim salinan event ke beberapa jalur pemrosesan independen.
Message group ID|FIFO ordering group|Messages dalam group yang sama mengikuti ordering scope.
MQ|Message queue/broker|Broker messaging dengan protocols/semantics engine tertentu.
AMQP|Advanced Message Queuing Protocol|Protocol messaging yang dipakai broker/client kompatibel.
MQTT|Publish/subscribe messaging protocol|Protocol ringan yang umum untuk IoT dan broker messaging.
STOMP|Simple Text Oriented Messaging Protocol|Protocol messaging berbasis frame teks.
Shard|Stream partition/capacity unit|Bagian Kinesis stream dengan ordered records dan capacity limits.
KPL|Kinesis Producer Library|Library producer untuk pengiriman records yang lebih efisien.
KCL|Kinesis Client Library|Library consumer untuk koordinasi/shard processing dan checkpointing.
Checkpoint|Recorded processing progress/state|Posisi/state untuk melanjutkan pemrosesan setelah restart/failure.
Firehose|Amazon Data Firehose|Managed delivery service ke supported storage/analytics destinations.
Flink|Apache stream-processing framework|Pemrosesan stream stateful, windows dan event-time computation.
MSK|Managed Streaming for Apache Kafka|Managed Kafka dengan compatible clients dan ecosystem.
Offset|Position in a log partition|Menandai posisi consumer untuk melanjutkan/replay events.
ETL|Extract, transform, load|Mengambil data, mengubahnya, lalu memuat ke destination.
ELT|Extract, load, transform|Memuat data terlebih dahulu lalu mentransformasi di target analytics platform.
EMR|Elastic MapReduce|Layanan untuk big-data frameworks seperti Spark/Hadoop.
HDFS|Hadoop Distributed File System|Distributed filesystem pada cluster Hadoop; perlu desain durability.
EMRFS|EMR filesystem integration with S3|Akses object S3 dari supported EMR workloads.
MPP|Massively parallel processing|Query/computation dibagi ke banyak processing units.
WLM|Workload management|Mengatur queue/prioritas/resources untuk beban query yang berbeda.
Parquet|Columnar data format|Membantu kompresi dan membaca kolom yang diperlukan saja.
ORC|Optimized Row Columnar|Format columnar untuk analytical workloads.
Data Catalog|Dataset metadata registry|Menyimpan schema, locations dan partitions; bukan semua data mentah.
SPF|Sender Policy Framework|DNS-based email sending authorization mechanism.
DKIM|DomainKeys Identified Mail|Signature email untuk validasi domain/signature integrity.
IaC|Infrastructure as code|Definisi infrastructure dalam templates/code yang dapat direview dan diulang.
Stack|CloudFormation managed resource group|Resource set yang dikelola melalui satu lifecycle stack.
StackSet|Multi-account/Region stack deployment|Menyebarkan stack instances ke banyak accounts/Regions.
Drift|Difference from declared configuration|Perbedaan actual resource state dari IaC expectation yang didukung.
SAM|Serverless Application Model|Abstraksi/tooling serverless yang dibangun di atas CloudFormation.
CDK|Cloud Development Kit|Menulis infrastructure dengan code lalu synthesize CloudFormation.
CI/CD|Continuous integration / delivery or deployment|Pipeline test, build dan release yang repeatable.
Canary deployment|Small initial traffic exposure|Menguji sebagian traffic sebelum meluaskan rollout.
Blue/green|Two deployment environments|Environment baru diuji lalu traffic dipindah, dengan rollback yang direncanakan.
Rolling deployment|Update in batches|Mengganti/update sebagian fleet secara bertahap.
SSM|AWS Systems Manager|Pengelolaan managed nodes, commands, patches, sessions dan automation.
Runbook|Operational procedure|Langkah-langkah operasi yang bisa manual atau diotomatisasi.
Maintenance window|Approved operating period|Jadwal menjalankan patch/maintenance dengan batas concurrency/errors.
Cloud Map|Service/resource discovery|Registry locations/attributes agar aplikasi menemukan endpoints.
RPO|Recovery point objective|Batas toleransi kehilangan data terbaru saat recovery.
RTO|Recovery time objective|Batas toleransi waktu pemulihan layanan.
DR|Disaster recovery|Persiapan dan proses mengembalikan layanan setelah kejadian besar.
Pilot light|Core-only recovery readiness|Komponen inti/data siap; aplikasi penuh masih perlu diaktifkan.
Warm standby|Reduced running recovery stack|Seluruh layanan berjalan pada capacity kecil dan dapat dibesarkan.
Active-active|Multiple serving sites|Lebih dari satu lokasi melayani traffic, dengan data coordination yang dirancang.
DMS|Database Migration Service|Memigrasikan/replicate supported database data termasuk CDC.
SCT|Schema Conversion Tool|Membantu assessment/konversi schema antar database engines.
CDC|Change data capture|Menangkap perubahan berkelanjutan setelah/seiring bulk data load.
MGN|Application Migration Service|Server rehosting ke AWS dengan replication dan cutover.
DRS|Elastic Disaster Recovery|Ongoing replication dan pemulihan supported servers ke AWS.
FIS|Fault Injection Simulator|Eksperimen failure terkontrol dengan stop conditions dan monitoring.
Cutover|Switch production to target|Memindahkan layanan/clients ke sistem baru setelah validasi.
Failover|Switch to recovery resource/site|Mengalihkan layanan dari komponen gagal ke alternatif siap pakai.
Failback|Return from recovery site|Mengembalikan layanan setelah primary dapat beroperasi lagi.
VTL|Virtual tape library|Interface tape virtual untuk backup software yang kompatibel.
VPC|Virtual Private Cloud|Network virtual regional tempat subnets, routes dan controls dikelola.
AZ|Availability Zone|Failure-isolation location dalam AWS Region; subnet berada dalam satu AZ.
CIDR|Classless Inter-Domain Routing|Notasi prefix alamat, misalnya /26 berarti 64 alamat IPv4 total.
IGW|Internet Gateway|Jalur internet untuk VPC dengan addressing/routing/controls yang sesuai.
NAT|Network address translation|Mengubah alamat/ports untuk supported egress/transit paths.
NACL|Network access control list|Stateless subnet firewall dengan ordered allow/deny rules.
Security group|Stateful allow-list firewall|Controls pada supported interfaces/resources; tidak punya explicit deny rules.
RFC 1918|Private IPv4 address ranges|10/8, 172.16/12 dan 192.168/16; bukan semua special-use ranges.
Longest prefix match|Most-specific route selection|Route dengan prefix paling panjang yang cocok dipilih.
Peering|Pairwise VPC connectivity|Koneksi VPC non-transitive yang memerlukan compatible CIDRs dan routes.
TGW|Transit Gateway|Hub routing untuk supported VPC/hybrid attachments dengan route tables.
PrivateLink|Private endpoint service access|Akses service melalui interface endpoints tanpa full VPC peering.
Gateway endpoint|Route-table endpoint for S3/DynamoDB|Private service path dalam VPC tanpa endpoint ENI untuk pattern ini.
Interface endpoint|Private service ENI endpoint|ENI dengan private addresses dan SG, plus optional private DNS.
VPN|Virtual private network|Encrypted tunnel connectivity sesuai protocol/design yang dipilih.
VGW|Virtual private gateway|AWS-side gateway untuk supported VPC hybrid connections.
CGW|Customer gateway|Representasi customer-side VPN gateway dan parameters.
BGP|Border Gateway Protocol|Pertukaran route antar autonomous systems; bukan encryption protocol.
ASN|Autonomous system number|Identifier routing system untuk BGP configuration.
IPsec|Internet Protocol Security|Kumpulan protocols untuk autentikasi/encryption pada VPN IP traffic.
DX|AWS Direct Connect|Dedicated connectivity ke AWS dengan virtual interfaces.
VIF|Virtual interface|Logical DX interface: public, private, atau transit sesuai tujuan.
LAG|Link aggregation group|Menggabungkan compatible physical links; shared failures masih mungkin.
MACsec|Media Access Control Security|Link-layer encryption untuk connections yang mendukungnya.
VLAN|Virtual local area network|Logical network segmentation pada link Layer 2.
North-south|Boundary-crossing traffic|Traffic masuk/keluar environment, misalnya ke internet/on premises.
East-west|Lateral workload traffic|Traffic antar-workloads/VPCs dalam architecture.
Flow Logs|Network-flow metadata|Catatan IP, ports, bytes dan action; bukan payload packet.
PII|Personally identifiable information|Data yang dapat mengidentifikasi individu.
PHI|Protected health information|Informasi kesehatan pribadi dalam konteks perlindungan yang relevan.
NLP|Natural language processing|Analisis/pemrosesan bahasa manusia oleh software/ML.
ASR|Automatic speech recognition|Mengubah suara percakapan menjadi text.
SSML|Speech Synthesis Markup Language|Markup untuk mengatur pronunciation/prosody speech synthesis.
FM|Foundation model|Model besar yang dapat dipakai/adaptasi untuk banyak tugas.
RAG|Retrieval-augmented generation|Mengambil konteks eksternal lalu memberikannya pada model saat menjawab.
Fine-tuning|Model adaptation through training|Training lanjutan untuk mengubah behavior/weights model yang didukung.
Inference|Use a trained model|Menjalankan model untuk menghasilkan prediction/response.
VDI|Virtual desktop infrastructure|Desktop yang berjalan di infrastructure remote.
IoT|Internet of Things|Perangkat yang mengirim/menerima data melalui network.
SFTP|SSH File Transfer Protocol|File transfer melalui SSH; berbeda dari FTPS.
FTPS|FTP over TLS|FTP dengan TLS untuk melindungi koneksi yang sesuai.
FTP|File Transfer Protocol|Protocol transfer legacy; tanpa TLS bukan encrypted transport.
CRUD|Create, read, update, delete|Empat jenis operasi data dasar.
JDBC|Java Database Connectivity|Interface Java untuk berkomunikasi dengan database.
ODBC|Open Database Connectivity|Interface standardized untuk koneksi/query database.
TCO|Total cost of ownership|Biaya total termasuk service, operasi, transfer, support dan migration.
Blast radius|Scope of failure impact|Seberapa luas kerusakan/akses yang terpengaruh oleh satu kegagalan.
Backpressure|Control upstream demand|Mengendalikan producer/consumer agar dependency tidak overload.
Stateless|No required local session state|Request dapat ditangani instance lain karena state penting disimpan terpisah.'''
glossary=[]
for line in raw.splitlines():
 t,e,d=line.split('|',2);glossary.append(dict(term=t,expansion=e,definition=d))
P.joinpath('glossary.json').write_text(json.dumps(sorted(glossary,key=lambda x:x['term'].lower()),ensure_ascii=False))
print(len(glossary),'glossary entries')
