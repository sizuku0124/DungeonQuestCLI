package com.example.save_sync.savedata;

import java.sql.Date;
import java.util.List;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import lombok.Data;

@Entity
@Data
public class SaveData {
  @Id
  private String playerName;
  private Date savedAt;
  private CharacterData character;
  private String inventory;
  private String progress;

  public String getPlayerName() {
    return playerName;
  }

  public void setPlayerName(String playerName) {
    this.playerName = playerName;
  }

  public Date getSavedAt() {
    return savedAt;
  }

  public void setSavedAt(Date savedAt) {
    this.savedAt = savedAt;
  }

  public String getInventory() {
    return inventory;
  }

  public void setInventory(String inventory) {
    this.inventory = inventory;
  }

  public String getProgress() {
    return progress;
  }

  public void setProgress(String progress) {
    this.progress = progress;
  }

  public CharacterData getCharacter() {
    return character;
  }

  public void setCharactor(CharacterData character) {
    this.character = character;
  }
}
