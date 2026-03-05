package com.example.save_sync;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.save_sync.savedata.SaveData;

public interface SaveRepository extends JpaRepository<SaveData, String> {

}
