package com.example.save_sync.savedata;

import java.sql.Date;
import lombok.Data;
import java.util.List;

@Data
public class Progress {

  private int currentFloor;
  private List<String> clearedRooms;
  private List<String> achievements;

}
