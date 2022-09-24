package tech.topskills.bankaccount.controllers;

import org.junit.jupiter.api.Test;
import org.springframework.ui.Model;
import org.springframework.validation.support.BindingAwareModelMap;

import static org.junit.jupiter.api.Assertions.*;

class HelloControllerTest {

    @Test
    void sayHello() {
        HelloController controller = new HelloController();
        Model model = new BindingAwareModelMap();
        String response = controller.sayHello("Tester", model);
        assertAll(
                () -> assertEquals("Tester", model.asMap().get("user")),
                () -> assertEquals("hello", response)
        );
    }
}