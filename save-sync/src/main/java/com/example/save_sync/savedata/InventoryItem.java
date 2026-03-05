package com.example.save_sync.savedata;

import java.sql.Date;
import lombok.Data;
import java.util.List;

@Data
public class InventoryItem {

  private String itemId;
  private String name;
  private int quantity;
  private boolean equipment;

}
