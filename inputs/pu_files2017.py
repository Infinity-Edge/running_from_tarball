#!/usr/bin/env python

mixFiles = [
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/000CB8F1-EB0F-E811-8204-0025905B8598.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/002E2FCA-260E-E811-9F0D-0025905B85EE.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/006F7072-530C-E811-9697-0025905A6070.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/008E6D1A-1F0E-E811-AE20-0CC47A7C35E0.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/021F2CF1-280E-E811-A934-0025905A48B2.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0227C855-540C-E811-97D2-008CFAFBFC72.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0255CD47-7A0C-E811-9432-0CC47A4D76A0.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/025D57F6-1710-E811-9604-008CFAF71FB4.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0269DF9D-6C0C-E811-A3E0-0025905A610A.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/026BF25A-680C-E811-9BFB-0CC47A7C35B2.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/02806BFD-1C0E-E811-9C16-0025905A60E4.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/02B9226D-7D0C-E811-ABE2-0CC47A74527A.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/02C20BF0-EB0F-E811-A48D-0025905A60DA.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/02CA2CD5-7C0C-E811-845C-008CFAF73DD8.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/02F5FBA6-2C0E-E811-9276-7CD30AD0A7B6.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/04115B01-B50D-E811-87AA-0CC47A78A446.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/04782B0E-160E-E811-BC87-0CC47A7C3472.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/048B4171-2A0E-E811-A355-0025905A610C.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/048F5F18-540C-E811-A1E7-0025905A6132.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/049558CB-180E-E811-9B6E-0025905A48E4.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/04F17A47-7A0C-E811-B2E3-0CC47A4D76A0.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0619E8E3-1510-E811-A1BF-7CD30AD09D2A.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/061C17BD-160E-E811-AB3E-0025905B8572.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/063B31EA-520C-E811-992D-0025905A60F8.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/065F51F0-EB0F-E811-9175-0025905A608E.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/068DF657-690C-E811-B294-0242AC130002.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/069A47F1-EB0F-E811-AF21-0CC47A7C35A4.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/069B262B-5D0C-E811-8916-0CC47A78A3EC.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/06A6DCF5-EB0F-E811-8CE5-0CC47A4C8E22.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/06D69BED-EB0F-E811-901C-0025905A48E4.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/08032231-270E-E811-AA2A-0025905B85EE.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/08108399-660C-E811-8D10-0242AC130002.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0824EE93-180E-E811-986D-0025905A6126.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/085D9D55-660C-E811-A971-0CC47A4C8E96.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/08838F40-DA0D-E811-A69F-0025905A6084.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/08B693B2-870C-E811-876C-008CFAFBEC34.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0A04F2BA-ED0D-E811-A357-0CC47A78A3E8.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0A13738D-640C-E811-ABE1-0025905A60F2.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0A193E2B-EF0D-E811-867A-0CC47A4C8E64.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0A38475F-670C-E811-81F1-0242AC130002.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0A5A4DC1-1C0E-E811-94B2-0CC47A4D767E.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0A6B46FF-1F0E-E811-8A45-0025905B8596.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0A81DC02-EC0F-E811-B6D4-0025905A60B4.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0AC1ADF6-EB0F-E811-80DC-0025905B8564.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0AF53ADE-DB0D-E811-8A80-0025905A6064.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0C1A5D63-E00D-E811-AAD7-0CC47A4C8E86.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0C444CE0-210E-E811-83FD-0CC47A4D7614.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0C6668AA-610C-E811-B55F-0CC47A4C8E66.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0C6ED778-240E-E811-8754-0CC47A4C8E5E.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0C7E102F-950C-E811-893A-0025905B85DC.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0C8BC409-630C-E811-B20C-0025905B85A0.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0CA4FAF1-EB0F-E811-8B5C-0025905B85DC.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0CBC3130-5D0C-E811-AED2-0CC47A4C8E5E.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0CE00EF7-EB0F-E811-A77B-0025905A60B8.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0CF7E530-DA0D-E811-ABD8-0025905A6138.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0E63DCF9-EB0F-E811-B757-003048FFD7A4.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0E977B0E-1A0E-E811-A294-0CC47A7C3404.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0EAAD509-6D0C-E811-B7B7-0025905B860C.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0EBCE4AC-670C-E811-B5A3-0242AC130002.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0EC5ACE5-240E-E811-BCAA-0025905B8576.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0EDF26F7-EB0F-E811-9481-0CC47A4D7698.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/0EE38EEA-EB0F-E811-93DB-0025905B8568.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/102E70C1-940C-E811-8AE6-0CC47A7C347E.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/1081EAF5-8D0C-E811-BC4F-0CC47A4D7654.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/108DA907-5C0C-E811-9371-0CC47A7C3472.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/10AB85D0-890C-E811-AB86-0CC47A7C3432.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/10B8145C-BB0D-E811-A00F-0CC47A4C8F12.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/10CDC4D2-670C-E811-8826-0CC47A4C8EE2.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/10D7598E-290E-E811-BA75-0CC47A4D76A0.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/10DADE9B-680C-E811-8610-0CC47A4D764C.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/10E07552-8D0C-E811-806B-0CC47A7C34C4.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/10F0F25C-2B0E-E811-82F7-0CC47A4D768C.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/1222410A-7B0C-E811-8512-0025905A60FE.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/129659AA-BB0D-E811-878E-0025905B8572.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/12ED50CC-220E-E811-B818-0025905A60A6.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/14129F3E-650C-E811-9664-3417EBE50720.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/141FB0FA-EB0F-E811-9575-0025905B8600.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/142AA464-950C-E811-AAA2-0242AC130002.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/142F30ED-EB0F-E811-B58B-0CC47A7C3432.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/14388647-540C-E811-A624-0025905A60D0.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/1438BC80-670C-E811-88E4-008CFAFBEC34.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/14448762-680C-E811-9CBE-0242AC130002.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/1446410B-F30D-E811-BADD-0CC47A4D76C6.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/1457BE4A-1B0E-E811-BFE4-0025905B85A0.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/14917F2A-560C-E811-A765-0025905A48F2.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/149782A5-EE0D-E811-A50B-0CC47A78A4BA.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/14E5A7BE-1910-E811-BEA8-0CC47A74527A.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/165B8EED-EB0F-E811-A395-0CC47A4D764A.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/166A01F3-290E-E811-9C47-0CC47A78A436.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/166AA22D-780C-E811-AF49-7CD30AD08E0C.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/166C57FA-EB0F-E811-8B07-0CC47A4D76A0.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/168CEB1D-7C0C-E811-B7F7-0025905B8582.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/16D3E8C3-1C0E-E811-8910-0025905B8576.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/181E8DC3-1C0E-E811-8DA1-0025905B8590.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/1829D9FA-EB0F-E811-856A-003048FFD722.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/1839B26C-670C-E811-8E1D-0025905A608A.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/18448CEF-680C-E811-81F9-0242AC130002.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/184AD63B-E90D-E811-9720-0CC47A4D7670.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/1862575D-BB0D-E811-88EF-0CC47A4D7616.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/186E524A-690C-E811-AE90-0242AC130002.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/189F99F6-EB0F-E811-8F0F-0CC47A4C8F0A.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/18E2D1F3-EB0F-E811-B21C-0025905B85B2.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/18E72AE5-F30D-E811-9EFC-0025905A605E.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/18FEEA7B-1C0E-E811-B1D9-0025905B8572.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/1A01BBF8-EB0F-E811-BCCF-0CC47A4C8EB6.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/1A3EA4F5-EB0F-E811-9CF9-0025905B85FE.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/1A71712D-5D0C-E811-B019-0CC47A7C357E.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/1A80C6FA-EB0F-E811-818C-0CC47A7C3424.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/1A89403A-7D0C-E811-AC41-008CFAFBE7DE.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/1ABA79EC-8D0C-E811-A684-0242AC130002.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/1C04DF6C-280E-E811-BD80-0242AC130002.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/1C260896-6F0C-E811-80B7-3417EBE6453D.root',
'/store/mc/RunIISummer17PrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/MCv2_correctPU_94X_mc2017_realistic_v9-v1/20000/1E1C4BEA-240E-E811-AEA2-7845C4F9321B.root' ]

