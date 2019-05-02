Feature: login google

Scenario: login success
Given Access url Login
And Click button Sign In
When Fill Email
And Click Button Next
Then I should see element password