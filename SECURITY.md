# Security policy

This portfolio contains lab/reference code and evidence. It does not promise a
production support service or compliance certification. Only the current
development line is in scope until a supported-version policy accompanies an
actual release.

Do not open a public issue containing tokens, private keys, real passwords,
personal/customer data, sensitive host logs, kubeconfigs, cloud credentials, IaC
state/plans, or backup archives. If GitHub private vulnerability reporting is
enabled for the verified repository, use that channel. If it is unavailable,
open a minimal issue requesting a private contact route without the sensitive
details. Do not assume an email address or reporting endpoint exists.

Reports should identify the affected repository and revision, scope, reproducible
synthetic steps, expected/observed behavior, and likely impact. Avoid testing
against systems or accounts you do not own. A safe minimal fixture is preferable
to real credentials or private data. No response-time guarantee is offered.

Public evidence is reviewed/redacted. Required publishing checks scan staged
files and outgoing Git history in addition to `.gitignore`. Secret fixtures must
be explicitly synthetic and narrowly controlled. If a real secret is exposed,
stop publication, revoke/rotate it with the owner's authorization, and plan
remediation; deleting one working-tree file does not remove Git history.

By default, CI has read-only permissions. Third-party actions use verified full
commit pins. Untrusted PR code must not run with secrets, privileged workflow
context, or privileged self-hosted runners. Trusted jobs receive only necessary
permissions. No account-wide setting changes are implied by this policy.

Cloud resources, billable services, container publishing, host configuration
changes, and public service exposure are disabled under the current task scope.
The operations toolkit is read-only; future destructive exercises require
explicit lab identifiers, validated ownership, dry run, confirmation, and bounded
cleanup. Never weaken sandboxing, TLS, firewalls, SELinux/AppArmor, or security
checks to obtain a passing demo.
