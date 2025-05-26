# COIT13240 Project Report

## 1. CSV Secure File Sync Design

- Uses AES in CBC mode for encryption
- Key size: 128-bit static key for demo
- File sent via HTTP POST to server
- Server saves `.enc` file for future analysis
- Diffie-Hellman key exchange to be added (future enhancement)

## 2. Secure Web App Design

- Apache HTTP server deployed on Linux
- `secure.conf` uses TLS 1.3, strong ciphers
- `insecure.conf` allows deprecated protocols (e.g., TLS 1.0)
- Browser tested with Firefox and Lynx
- Packet captures show differences in certificate and cipher negotiation

## 3. Tools Used

- Python Cryptography (Hazmat)
- Flask for file server
- Apache for HTTPS site
- Wireshark for traffic capture

## 4. Packet Analysis

See `/packet_analysis/sample_test.txt` for summaries.

## 5. Security Considerations

- AES CBC is secure if key and IV are managed safely
- Upload endpoint is simple, could be enhanced with HTTPS + auth
- Apache insecure config demonstrates real-world misconfigurations

## 6. Contribution Summary

- [Your Name] – CSV Client + Report + Testing
- [Teammate] – Web Server Config + Testing + Slides

## 7. Reflection

This project deepened our understanding of practical encryption, secure server setups, and how small changes in configuration can expose vulnerabilities. We learned how to handle Python Hazmat securely and practiced setting up HTTPS on cloud servers.

