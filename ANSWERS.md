# Answers

# CHALLENGE #1 - Test Design Challenge
## Test Strategy
Role-Based Access Control (RBAC) testing with positive and negative scenarios:

## Implementation considerations
- We can test on the UI level or API level
- API level testing is more reliable, faster, and less coupled to the UI
- A combination of both is preferred
- We test different HTTP VERBS (GET, POST, PUT, DELETE, or PATCH or anything else if used)
  - In UI, the meaning of these verbs is translated to actions
- For API testing, we refer to entities by their IDs (or UUID if used)
  - Name and other attributes can change, but the ID should be unique
- IDs can be used to check the relation between entities (foreign keys in DB)
<br />For example, a product can look like this:
```json
{
  "id": "1234-5678-9012-3456",
  "brand_id": "1234-5678-9012-3456",
  "product_list_id": "2345-6789-0123-4567"
}
```
- An ID should be unique within its entity type (e.g., a user ID is unique among users)
- But not withing other entities (e.g., a user ID can be the same as a product ID)


## Test Plans

### 1. Admin
**Positive Scenarios**
- Can `create` a new User
- Can `delete` a User
- Can `update` a User
- Can `list` all Users
- Can `get` a specific User
- Can `create` a new Brand
- Can `delete` a Brand
- Can `update` a Brand
- Can `list` all Brands
- Can `get` a specific Brand
- Can `create` a new Product List
- Can `delete` a Product List
- Can `update` a Product List
- Can `list` all Product Lists
- Can `get` a specific Product List
- Can `update` permission sets of a user

**Negative Scenarios**
- Should not be able to delete itself (not mentioned in the requirements, but increases security)

### 2. Brand Admin
**Pre-setup**
- Create 2 Brands (using the Brand Admin account)
- Create a Brand Admin account (using the Admin account) - Admin of Brand A

**Positive Scenarios**
- Can `create` a Product List within its Brand A
- Can `delete` a Product List within its Brand A
- Can `list` all Product Lists within its Brand A
- Can `get` a specific Product List within its Brand A
- Can `update` a Product List within its Brand A
- Can `create` a Product within its Brand A
- Can `list` all Products within its Brand A
- Can `get` a specific Product within its Brand A
- Can `delete` a Product within its Brand A
- Can `update` a Product within its Brand A
- Can `list` Products within its Brand A
- Can `get` a specific Product within its Brand A

**Negative Scenarios**
- Should not be able to `create` another Brand B
- Should not be able to `delete` another Brand B
- Should not be able to `update` another Brand B
- Should not be able to `list` all Product Lists within Brand B
- Should not be able to `get` a specific Product List within Brand B
- Should not be able to `create` another Product List within Brand B
- Should not be able to `delete` another Product List within Brand B
- Should not be able to `update` another Product List within Brand B
- Should not be able to `list` all Products within Brand B
- Should not be able to `get` a specific Product within Brand B
- Should not be able to `create` another Product within Brand B
- Should not be able to `delete` another Product within Brand B
- Should not be able to `update` another Product within Brand B
- Should not be able to `list` all Users
- Should not be able to `get` a specific User
- Should not be able to `create` a User
- Should not be able to `delete` a User
- Should not be able to `update` a User
- Should not be able to `list` users
- Should not be able to `get` a specific User

### 3. User
**Pre-setup**
- Create a User account (using the Admin account)
- Create a Brand (using the Admin account)

**Positive Scenarios**
- Can `get` a specific Brand
- Can `list` all Brands
- Can `get` a specific Product List
- Can `list` all Product Lists
- Can `get` a specific Product
- Can `list` all Products

**Negative Scenarios**
- Should not be able to `create` a Brand
- Should not be able to `delete` a Brand
- Should not be able to `update` a Brand
- Should not be able to `create` a Product List
- Should not be able to `delete` a Product List
- Should not be able to `update` a Product List
- Should not be able to `create` a Product
- Should not be able to `delete` a Product
- Should not be able to `update` a Product
- Should not be able to `create` a User
- Should not be able to `delete` a User
- Should not be able to `update` a User

### 4. Other Scenarios
- When a Brand is deleted, all its Product Lists and Products should be deleted
  - Depends on hard delete or soft delete
  - If hard delete: Depends on the "on delete" constraint (retain or cascade)
- When a Product List is deleted, all its Products should be deleted (hard delete or soft delete)
- If a product has `creator_id` or something like that:
  - Nothing should be done in case of a soft delete
  - Business decides what needs to be done in case of a hard delete (i.e: null or delete)
