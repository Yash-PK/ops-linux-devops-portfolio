# Explicit extension backlog

These are scoped future opportunities, not implemented skills. Activate an
extension only after its primary project's core gates pass, with a separate
acceptance checklist, supported dependency research, resource budget, security
boundary, and executed evidence. Prefer one primary implementation per capability.

| Extension | Candidate project | Meaningful acceptance before a coverage claim |
| --- | --- | --- |
| LDAP, FreeIPA, SSSD, Kerberos | Fleet automation | Disposable identity domain/client; positive and denied login; ticket lifecycle; offline behavior; scoped cleanup. |
| VPN connectivity | Network/storage lab | Isolated peers; authenticated tunnel; routing/DNS assertions; denied unauthenticated path; revocation and cleanup. |
| Proxmox or VMware provider | Network/storage lab | Authorized supported local provider; reproducible VM lifecycle; inventory-only teardown; architecture/license limits documented. |
| Additional local hypervisors | Fleet/network lab | Real tested provider integration; cloud-init and VM/systemd/reboot evidence. Listing a provider is insufficient. |
| Puppet or Salt | Fleet automation | Separate reproducible desired-state example; idempotence, invalid-state rejection, recovery; measured tradeoff against Ansible. |
| Rootless Podman | Container platform | Clean unprivileged job lifecycle, storage persistence, network/readiness behavior, and shutdown test. |
| Alternative cache/queue | Container platform | Compatibility/migration demonstration and outage semantics; no redundant unused service. |
| Messaging systems | Container platform | Verified broker/client combination, retries, acknowledgement, duplicate handling, and bounded failure/recovery. |
| Additional database | Container/recovery | Application use case, migrations, tests, and actual restore semantics. |
| AWS load balancing, RDS, EKS, DNS, S3, audit logging | Cloud foundation | Separate cost/auth gates and static/module checks; actual claims require authorized plan/apply evidence. |
| Azure or GCP | Cloud foundation | Native provider implementation and tests; IAM/network semantics explained; not renamed AWS configuration. |
| Serverless | Cloud foundation/delivery | Platform-specific runnable workload, event failure handling, observability, cost controls, and authorized deployment evidence. |
| Jenkins | Delivery | Jenkinsfile, Configuration as Code, isolated agents, reproducible execution, failed quality gate, and credential boundary. |
| GitLab CI | Delivery | Real pipeline execution on selected workload with equivalent gates and artifact/promotion evidence. |
| Maven/Gradle or Node.js workload | Delivery | A real tested service with supported locked dependencies and native build/release lifecycle. |
| Flux | Kubernetes/GitOps | Separate reconciliation/rollback/drift tests and a reasoned Argo CD comparison. |
| Service mesh | Kubernetes/GitOps | Concrete workload need, enforced policy or mTLS, telemetry, failure behavior, resource overhead, and cleanup. |
| Advanced scheduling/multinode failure | Kubernetes/GitOps | Explicit node topology; scheduling/drain/recovery assertions; distinguish local control plane from production resilience. |
| OpenSearch | Observability | Indexed workload logs, search/retention/security configuration, query evidence, and resource-aware teardown. |
| Alternative collector | Observability | Separately tested pipeline and concrete maintenance/resource tradeoff; avoid redundant collection. |
| OpenBao or Vault / External Secrets | DevSecOps policy | Least-privilege access, lease/rotation/revocation or sync tests, local failure behavior, and clean secrets handling. |
| WAL/PITR | Backup/recovery | Restore to a selected time with before/after record assertions and observed recovery measurements. |
| Velero | Backup/recovery | A tested backend/storage combination that restores application data consistently, not only Kubernetes objects. |
| Backstage | Golden path | Runnable resource-budgeted portal, catalog ownership, generated-service acceptance, and maintenance strategy. |
| Extended capstone | Capstone | Full pinned platform lifecycle with additional reversible faults and evidence-backed postmortem updates. |

All entries are `planned`. Additional alternatives can be added only with a
concrete use case and an explanation of the implementation and validation they
would require. Resource availability is not permission to provision cloud
resources, alter this host, subscribe to services, or expose a public endpoint.
