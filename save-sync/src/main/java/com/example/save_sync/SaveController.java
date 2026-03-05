package com.example.save_sync;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import com.example.save_sync.savedata.SaveData;

@RestController
public class SaveController {
  private final SaveRepository saveRepository;

  public SaveController(SaveRepository saveRepository) {
    this.saveRepository = saveRepository;
  }

  @PostMapping("/saves")
  public SaveData upload(@RequestBody SaveData savedata) {
    if (saveRepository.existsById(savedata.getPlayerName())) {
      return saveRepository.save(savedata);
    } else {
      return saveRepository.save(savedata);
    }
  }

  @GetMapping("/saves/{playerName}")
  public SaveData download(@PathVariable String playerName) {
    return saveRepository.findById(playerName).orElse(null);
  }
}
