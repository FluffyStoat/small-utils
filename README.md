**Utility scripts for "Cuba-platform":**

1. Script for generating **"EntityAccess"** and **"EntityAttributeAccess"** for security role by template:
    ```
   @EntityAccess(entityClass = <name>.class, operations = {EntityOp.CREATE, EntityOp.READ, EntityOp.UPDATE, EntityOp.DELETE})
   
   @EntityAttributeAccess(entityClass = BusinessUser.class, modify = "*")
   ```

   **Example:**
   ```
   python roles_access_generate.py -d <path_to_dir> -o <output_file>
   ```
   **Result:**
   ```
   @EntityAccess(entityClass = CustomEntity.class, operations = {EntityOp.CREATE, EntityOp.READ, EntityOp.UPDATE, EntityOp.DELETE})
   
   @EntityAttributeAccess(entityClass = CustomEntity.class, modify = "*")
   ```
    
    