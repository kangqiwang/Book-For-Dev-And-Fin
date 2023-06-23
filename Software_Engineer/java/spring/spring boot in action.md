## Spring Boot

spring offers a container, often referred to as the spring application context, that creates and manages application components. these components, or beans are wired together inside the spring application context to make a complete application.

the act of wiring beans together is based on pattern known as dependency injection(DI)

on top of its core container, spring and a full porfolio of related libraries offer a web framework, a variety of data persistence options, a scurity framework, integration with other systems, runtime monitoring, microservice support, a reactive programming model, and many other features

the core spring framework

spring boot

spring data

spring security

spring integration and spring batch

spring cloud

spring native


| Annotation      | Description                      |
| --------------- | -------------------------------- |
| @RequestMapping | General-purpose reuqest handling |
| @GetMapping     | Handles HTTP GET requests        |
| @PostMapping    | Handles HTTP Post requests       |
| @PutMapping     | handles HTTP PUT requests        |
| @DeleteMapping  | handles HTTP DELETE requests     |
| @PatchMapping   | handles HTTP Patch requests      |

## validating form input

@Data

@NotBlank(message = "City is required")

@CreditCardNumber(message = "Not a valid credit card number")

@Digits(integer = 3, fraction=0,message="Invalid CVV")

The @Valid annotation tells Spring MVC to perform validation on submitted Taco object after it's bound to the submitted form data

e.g 

``` java
@PostMapping public String processOrder(@Valid TacoOrder order, Errors errors,       SessionStatus sessionStatus) {
       if (errors.hasErrors()) 
       {
          return "orderForm";   
      }   
    log.info("Order submitted: {}",order);  

    sessionStatus.setComplete();
    return "redirect:/"; 
    } 

```


## template library
1. Template
2. FreeMarker
3. Groovy templates
4. JavaServer Pages(JSP)
5. Mustache
6. Thymeleaf

under /WEB-INF folder


## Spring Data

define persistence data class 
e.g.

```java
package tacos; 
import javax.persistence.Entity; 
import javax.persistence.Id;
import lombok.AccessLevel; 
import lombok.AllArgsConstructor; 
import lombok.Data; 
import lombok.NoArgsConstructor; 

@Data 
@Entity 
@AllArgsConstructor 
@NoArgsConstructor(access=AccessLevel.PRIVATE, force=true)

public class Ingredient {   

@Id   
private String id;
private String name;
private Type type;

public enum Type {WRAP, PROTEIN, VEGGIES, CHEESE ,SAUCE   } 
        
        
} 
```

customizing repositories

- IsAfter, After, IsGreaterThan, GreaterThan 
- IsGreaterThanEqual, GreaterThanEqual 
- IsBefore, Before, IsLessThan, LessThan 
- IsLessThanEqual, LessThanEqual 
- IsBetween, Between 
- IsNull, Null 
- IsNotNull, NotNull
- IsAfter, After, IsGreaterThan, GreaterThan 
- IsGreaterThanEqual, GreaterThanEqual 
- IsBefore, Before, IsLessThan, LessThan 
- IsLessThanEqual, LessThanEqual 
- IsBetween, Between 
- IsNull, Null 
- IsNotNull, NotNull


```java
@Query("Order o where o.deliveryCity='Seattle'") List<TacoOrder> 
```

### MongoDB

- @Id—Designates a property as the document ID (from Spring Data Commons) 
- @Document—Declares a domain type as a document to be persisted to MongoDB 
- @Field—Specifies the field name (and, optionally, the order) for storing a property in the persisted document 
- @Transient—Specifies that a property is not to be persisted

```java
@Data @AllArgsConstructor 
@NoArgsConstructor(access=AccessLevel.PRIVATE, force=true) 
@Document(collection="ingredients") public class Ingredient { ... } 

```


## Spring Security

### configuring authentication

```java

@Configuration
public class SecurityConfig {
    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}

```
- BcryptPasswordEncoder - applies bcrypt strong hashing encryption
- NoOpPasswordEncoder - applies no encoding
- Pbkdf2PasswordEncoder—Applies PBKDF2 encryption
- SCryptPasswordEncoder—Applies Scrypt hashing encryption
- StandardPasswordEncoder—Applies SHA-256 hashing encryption 




### configuring authentication



# Qestion

## explain dependency injection

dependency injection is a design patternn that allows us to remove the dependnecy of a class on another class. this makes our code loosely coupled and easier to test

e.g

``` java
@Service
public class AccountService {

    @Autowired
    private Connection connection;

    public void saveAccount(Account account) {
        // ...
    }
}
```


when Spring starts up, it will look for all the classes annotated with @Service, it will create an instance of the class and jnject all the dependencies annotated with @Autowired.

benefits:

- loose coupling
- testability
- scalability




