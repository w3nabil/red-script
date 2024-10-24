
# NOMB

NOMB is a mass mail tool developed using only the most basic knowledge of Python. It was part of my "Is Hacking All About Practice?" research project.  

# Gmail Email Address and Spam Detection Observations

## 1. Use of the `+` String in Gmail Addresses

### Observation:
Gmail offers a flexible feature for handling email aliases using the `+` symbol. For instance, if your primary email address is `contact@gmail.com`, you can receive emails sent to variations like `contact+support@gmail.com` or `contact+newsletter@gmail.com`, all of which will land in the same inbox (`contact@gmail.com`). 

### Hypothesis:
During mass email testing with NOMB, I observed that sending large volumes of emails to `contact@gmail.com` directly could flag the sender as spam. However, if the emails are sent to variations like `contact+support@gmail.com` or `contact+examplespam@gmail.com`, Gmail might treat these as unique addresses, thereby avoiding immediate detection by spam filters. This approach appears similar to how businesses send promotional emails to different departments or campaigns via alias addresses.

### Analysis:
While this method may help bypass superficial spam detection during testing, Gmail’s algorithms take into account more than just the recipient address. Gmail uses:
- **Behavioral analysis**: Repeatedly sending emails with alias variations might eventually trigger spam detection based on volume and frequency.
- **Content inspection**: Gmail evaluates email content (subject and body) to detect spam patterns.
- **Recipient feedback**: Gmail adjusts its spam filters based on whether users mark emails as spam, delete them, or ignore them.

Although this technique might initially reduce spam flags, Gmail's sophisticated spam detection processes go beyond simple alias handling and will likely detect mass-mailing behavior over time.

---

## 2. Subject Line Variation to Bypass Spam Detection

### Observation:
Gmail also analyzes the subject lines of emails to determine whether they are spam. By altering the subject line for each email, my massmail script can generate what appear to be unique emails. For example, by sending 100 emails with 100 different subjects, the system may treat these as individual, distinct messages.

### Hypothesis:
By appending random characters or digits to the subject (e.g., "Offer 1A23", "Offer 2B34", etc.), the goal was to evade spam filters. This would result in each email appearing as separate in the recipient's inbox, allowing the system to treat them as different messages, potentially bypassing certain spam detection algorithms.

### Analysis:
While changing the subject line may prevent initial grouping by Gmail, this tactic is not a long-term solution for avoiding spam detection. Gmail also assesses:
- **Content consistency**: If the body of the email remains similar or spammy (e.g., containing promotional links, repetitive text, or flagged keywords), Gmail’s algorithm may flag the emails despite different subject lines.
- **Sender reputation**: Gmail tracks sender behavior. If the mass emails result in low engagement (few clicks or opens) or are marked as spam, the sender’s reputation degrades, increasing the likelihood that future emails are flagged as spam.
- **Behavioral learning**: Gmail’s filters learn from user feedback and interaction patterns over time, meaning that altering the subject alone is not sufficient for long-term success in evading detection.

In conclusion, while subject line randomization may momentarily break Gmail's spam grouping, the system’s comprehensive spam detection considers content quality, sender behavior, and recipient interaction, making it a weak long-term strategy for bypassing spam filters.

---

## Conclusion:
Relying on `+` string variations or altering subject lines may offer short-term evasion, but Gmail’s advanced filters will ultimately detect consistent spamming behavior. Both techniques should be used cautiously and responsibly during the testing phases.

---

### Tested on:

| Mail Provider | Result | Last checked |
|---------------|--------|--------------|
| GMAIL | ✅ | *Thu Oct 24 2024 19:00:00 GMT+0000* |
| iCloud | ✅ | *Thu Oct 24 2024 19:00:00 GMT+0000* |
| ProtonMail | ✅ | *Thu Oct 24 2024 19:00:00 GMT+0000* |
| Yahoo | ❌ | *Thu Oct 24 2024 19:00:00 GMT+0000* |
| Outlook | ✅ | *Thu Oct 24 2024 19:00:00 GMT+0000* |

### Contributing

Contributions are welcome! 

To get started:
- Fork the repository
- Create a new branch for your feature or bug fix
- Submit a pull request

Feel free to reach out if you have any questions. Thank you for helping improve this project!
