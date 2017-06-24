# eNode



**Table of Contents**   
1. [Intro](#id1)
2. [Hardware](#id2)
3. [Software](#id3)
4. [Measure Direction Hack](#id4)
5. [Build Examples](#id5)


## Intro <a name="id1"></a>


**eNode** is a device based on ESP8266 and PZEM-004 that measures energy and/or temperature and delivers data to a MQTT broker and/or Emoncms. eNode is modular meaning you can start with a simple energy module a go up to a true 3-phase energy monitoring system, along with temperature detecton of up to 10 digital temperature sensors. Data is delivered through WiFi and configuration is done in it's own web page.


**Energy meter:**
  - Based on cheap Peacefair PZEM-004
  - Very accurate readings 
  - Energy direction possible with chip hack on first PZEM-004
  - up to 3 independent PZEM-004 per device
  - Volt, Ampere, RealPower

**Temperature meter:**
  - Based on cheap 1-wire DS18B20
  - up to 10 DSB20 digital 1-wire temperature sensors
  - Device addresses managed on the setup page

**Relay:**
  - MQTT controlled relay

**ESP8266**:
  - Easily configurable from web page
  - Delivers JSON formatted data to local/remote MQTT broker
  - Delivers data to local/remote Emoncms server
  - change refresh rate on demand





## Hardware <a name="id2"></a>

![Diagram](https://lh3.googleusercontent.com/e1DfGtuDOHP26ks97AbndyLBgnwTMQKkRq1iP9G3FVU9LVAItQy7oaT_N-G7u__ev1GwVheDQIT4FdfuTnYpeKXaBWdDkA-Hj8ABVrYQ7QMdZP-GNQVgKgIZV3G8cNY5jdXc4YkYQd31Ctxp7K26qBiDRz4ZabsLqoIqF-QRPAuusCwKpMDkOfXJpcTv5HSq1SGEhRiZfV27RDVZdenaQrf8q9VUYIf4BUmCWjhxIJC1U6ZtEUwBSjWuHwkXcHHz6rmBRi3fKQBbwzb-dS2X5vKwRFRTGck66H-jditREWfmHFMf6BCmInn1MypB31J1s-ZQw4ebJIZ6oqXXh0--bvhL2EViN4wZUSxpBGHI4pFWAHldrGt7cl5b3iP5ghdcrpyl_w1NgX3jell0uDbApxBli3oddDuJjr3MQ4tzG6eesagyHrXWTDTiqZRIb3pDDu4VGP2OkHRZExDRy51eAxpFR7kU23HwMWZw4Ci6SZus5xKCGuj209lCABqcidIjQKZ2Awd-2vVLVbmPZj4l4tqY5NSWbmggXl-4GVQazypX6jQOZ-DEINfM9rfzj-htv0cOkbhY2tOMi4pY2BtTZRiEv9_nZx-naJPWyDYqxS8sP8nqco0HUnkyBUIFP9x8XNTziEaPBNI6KZZIySMj9g4nM099wvj332Jgw2SMNg=w1369-h613-no)



Qty | Item | Function
:---: | :---: | ---:
1 | wemos D1 mini | `node`
1 | PSU 230VAC to 5VDC | `node`
1 | DC/DC 5V to 3.3VDC | `node`
3 | PZEM-004 | `Energy`
3 | R=510OHM | `Energy`
10 | DS18B20 | `Temperature`
1 |  R=4.7K OHM | `Temperature`
1| D1 relay shield|` Relay`


## Software <a name="id3"></a>

- Load Arduino's `WebUpdater` example sketch to the ESP8266
- Upload the appropriate firmware located on the `/bin` folder to the ESP8266
- Access eNode at `SSID:APRENODE / PASSWORD:12345678` / `http://1.1.1.1`
- Configure `local WiFi settings`, `enode name` and reboot
- Navigate to `http://<eNode name>.local` or `http://<eNode IP address>`
- make sure all temperatures sensors are correctly mapped on the sensor positions
- make sure to indicate the correct number of energy sensors
- check direction if you have a hacked PZEM
- Configure `MQTT broker` and/or `Emoncms` account
- enjoy!


## Measure Direction Hack <a name="id4"></a>

![](https://lh3.googleusercontent.com/7oKvPvdqY3lP6zBprZ33XxJ7tKCSPjcxN2w-OqwHl_1SzNu80wvdnXQUsuom1qUd44zljcSAKoW6R_QD6Fw6dyNdrQpZGyCAt7fK76CRAaeEPu2qT8z-xMeqMLAlgMNtwaDBF7miqPXhsgoQ-rWaterlj8KB61w-i8nbBX3sqG_NviRIJFRPZu4y5Mk5QQHA83q366xY_NipzpD8CfSDKwin57H3Htds_hMZ-07q1bP9mxqiQBRQqcq6nFyu7SyfzQPI7FPg7txX6qM7KTZdOb53coQP14PXP9ZpZgZd6tcLpuRveteLxfdhUHiUXz74R1f_4OeA_25O--yq3BcZT_W89wb5o-ZRAX4VKxyWw7SOmyMhGib1QK7HJxYOTOWC5yf9IasuEWV_vbtsjChd_gD7Al2RD4akmTF-P8RQy6oLgGEKNINEdbHCTc4NhU0PtUVe3b90hhll2i0vlXHoQQ_Dcv1H4UQkiork0te3gWIpN9IEScdoKep3nyKpx4NwDmuup3uilXumtjUWld5qL1ifNlgKCKj39EcPMyswWAbB7pGrEsRqt0L_xvEW9gpEuPkjH6MUEL-biGVslIl6hkCvgLHb1iIcVd2EOjmNMurGXLUkB2KS3h3Vw4LIQRWzvFUrmJfLbP9hZKorvSnoDPO2MfHhwYYeXgx2m2J11w=w800-h402-no)


## Build examples <a name="id5"></a>

### Single Energy meter with energy direction

![](https://lh3.googleusercontent.com/SBM5yHYrzJLQoWducXGPkJP71SLBFISQ5Ax2F3FiR5YQkcBkk9DWqZR7r-aBd-BZTT0_eq0TYaBDuSUKMblybQ1whlfn3Ab3sCUCO7kJJBTG1XEwTd10mAaM5Kt19AUJTuHebA=w950-h633-no)

![](https://lh3.googleusercontent.com/WklSgATVuYcM-uWvbv1qg55E02CUx65vQSYuu0rdVQBsc_ANtl6Y6VnednGCHvuDDJgTBmnBIoNl83vk3QXxfgnidPhTsvpPO1Nfrsi9RKvS4Sm8AGlZYS1ETrLe2WTAgLPpQQ=w1410-h737-no)


![](https://lh3.googleusercontent.com/sQ2G_MfHBDJgZtr_T6JmCbHzPJ0tjJ65jIqNFqcfjtzA-GOI7atpoX9LF5F_NyfGG5sIVLVW3Nkw8zpwZKXFduHe-lHJWSzEFdfq6-6qOtMNwXWco8yAiiEJuRivfRRX5k9SPA=w880-h282-no)

`by RJSC/APR`

### Solar water heating monitor


![](https://lh3.googleusercontent.com/tFdkEL8ua9Wu-ubJ4VFyz7GXtDTRZISQmi7aNZxGzFM9dd4C9nc-lPJ7kovtw_w76qnt8mhJZDld6FUdZHhbYR3bouUoOmFnFZkJbu6Rh54rfo9W-EXe-QJ2BJDxecN_b1-HZA=w1328-h984-no)

![](https://lh3.googleusercontent.com/Kjry__9ISTqjh2ymNkWo4btD8tX7F3stuvma9M4x7LwTNFgYzQmJqs2DiBaSt-pQffBzdvVn0nI350bkH2Aqf5yRAR9vJB3h2svWvKawNcxoNPndNSPwJWIe42NDbmDsqRYE08M12syY_pv3VL2G-PPUdXZyL_r6GJhh7iEqjDezaxl9XUeGF0C-X1hd9y4akavBKDe3x1xT68up4fHglX50_l_TwaPRCqHTwuepshVV3g_xHVBbBUXYxs4NbQx2tErrwVcrVc06Amq0Xr83xBYMaYryKFXGyLaUwywLwX6nKcr_E7pjjDc4HKWna7fptINRo2Kogf8YSM7B7FS8uqWZWj4PNQTM-MLdvERkYrDsJ59aRyHOM3zvodYx_slDjbMGSV729nK-kb0rnlKCJKJRXfCu9QzY1018_9JTrLhnrs7LUdj7Fi3H1ZNxpK1sll6PyvNQsjW9F7ay96g96UJS0nEMErjKvyz0o51kNf6hbr7TrYjSqanpGFAlLul7qiGtQN4qS4lbKXC3eYXnzYSXC4K_I3Q_dJBr69Pts08EzVOP7mi-EpeAWN9xfLinLKdoh5XTjeeG8xYyTPUV6usZgaobb_HFlQEpZCUhx9lwcjSTtBouWsaBVpsSNCkuG-6yxpKl9Vq1EMJ-XqV_Ibn2vaVTxCK52D354MRPVw=w485-h595-no)

`by APR`

### Single phase three point energy monitor + temperature sensors

![](https://lh3.googleusercontent.com/4TNofhn6XgbDWfB5Vy3fTMXBU3eEpPv2qGJiVXg1k4DyR8OhXb2wOtKr4gcQeAQeleT3dPNV570MK0fLHa-kvDiBpPCPHQ1jlnRBKeh3T-RfHlDuuAf3nAbqd7GbyfxLXktaCLOHvIaoJIxw0o1gRKzi8zrWWMfRKDp_w5OOR9E_Ef1yowT-bYkWTb8O1x2bqKBu7daBMgCKWSajoPW56bwUEElp0Pimn__CEJhloVevcrBVTbUvX2vT5eRQLaEzuvTROKQfC6l61Kbq5vJt9II_r3Fm93tIobBpjRM8qxEeMqzAtfvg7BwKWEmJrDm3m5KdPq6NxQMzqH7BsAbtotoalLiwUjF1K2GAqCDm480BRhQUqan4z-B6decHaWXQLtsFMyFh5-eusepbKKfI7bKsgj5StnvsV3N3nvQS2O0fgSi8zK3108sZEY-twaVZniZYedR79ZL3voSYmo_MW7FJ7h5RFXyswgGEgAr8bX2Xfi-I6wjTi4eQnswHMQaJ-rYFSrjEyni7zLfDID_Bv5G13PR63rlV0t8DUF-xwj4hSQzlnqvXMJnbflh2sbKkCSjsmZPPJIzkCHcxf2WURH2OeTVeaXtm7Btp2DsukpKweB2CTfTkaB4N_6oAwnWrqPrfVzG6a5Z6qtISHKcLM-J4iT7XSjnvOaEihi87dA=w648-h398-no)

![](https://lh3.googleusercontent.com/BZc7rxPkAizcA1MsoeSc3NuljXX6Rqzd766DGI7KEyPS6lk3bBi1ucrndeq2XFWTVcvZD72FCnDQ_jWR7vsf9b-HAef6bJuMdAJttUEG477DciE-uiFghomssKOI_40PhTXIjA=w433-h611-no)


`by APR`

### Three phase energy monitor

![](https://lh3.googleusercontent.com/lFx36pi3UEKvuJ2qYbtpFguBMdYHqDalrTyzYfMpJ6QEauFbN-FWTpCJb194URD0lFQuWnGRnPC9IVhM5hSQ8yW8yQG-qlcrPBA66at3fiLVNvpbyO8huPWIYGTkMBnIUtYm26PdR9uXiSEnjsl6J3pTGLOXD3ml4gpfDrUmTph6azpmuIuNogqD2aMiltb1xnjmrVW3IDMPG1lK0KD9EJCVmErBsmYO3THbocai0WbOm3nji5eVqjMjkVsnjNoq_8od44LKuXhRD6S3FyLAqMB2GhAaUMylOFMy1MYeswpV7-FJw6sxn5e6gVUjuuaassgb3GWwPzze9O-ix8DL3ow3HKpH5pxjQYOYonMsn6K4eaxno-wSZ3GFVay60ObxO_I9V-RbAVaF-ieE-dpDuLT7op7GzPBqxVaTbWEzweHOx6JiKF7nHEP6MrgxTVsdSkAHLDXw40UQI87A6i_EFgcIFeDXB6wZjHaYlRTB4G5hzbTIQXfr1oMywXrgVoNg-lMF1Hbzr8PgEdc1Fvtg_a4B4i8Tox6E8Ee9m8OVgw1mYuK419F-nFMuEBJt653Rfelz7v62tjP8Q1Evh7JaqDNR1K7sApte8ZGQa6a8c6ByLQwHckGxCVd8prbtLd_P8Zj8hNyJYykLXaHcxQ3f4LAbJzDnS46oUPKVWOXxDA=w480-h381-no)

![](https://lh3.googleusercontent.com/ub1PWoaaYFy7tjcKP3NMdjfcyy_1T3PzNMXWeNUh8XpMcnB6ppoux2o6ybINCb4YF8XOSAphxR3O-HAuFZyPVMpFlR26gftC5yqBesEXUbeBBvcPuQkCpGI4ImhlGNvRg_m8OSMk-2CEeb1wDeSex2sZFVybTSMVCFF0ratgtHhD9epSYo7Md6rKOOtR8SV6LqBSfAYKs2PjodtQtcLszY12ylb-NCLoY16C8IbbuLZuldwpNfwxwNEtC-55Uw9VtjsAD9dzvq-irZ3mqy67_wZcrr9Ba3PcNmUIolCeKH3Ry_ekCXQxMrn9nWhP8n70v14QbpR1aziz_AA6AsDeUHO8lunCqm24vMBvTeQNdQtcX0GkIiHel2F0WToG-pQCrgfuFMyIWGsGt13sPomGboG-IujlZO54pHCLRaJ-bQqArJtUP2TmK4V8lkNpKYEqL4XX_XK1IRpRqgT1X4UyhYEWZl6jFa6ADeu04gfg4iUS4OnU6Fsd6haVlp8jgq0nCm0c_rgZ50uGIzRNJjAIpZ5W48es9Srv1oHxDoQD6tCr60NMMRVPOOmjf-KCu1hWtSlrYn3Tp6TDLjI9LXhOhOqL_22RNCXkMU66JwiDXSMH-uoCmMPCMAGNCajNoBmUYvSLqzq45ZKzjAxlD8vBD79QBKptlcAn_e-jzTnR1g=w891-h635-no)

![](https://lh3.googleusercontent.com/SUtMuaYU9_C3L_J5VXKRoV2fLkUczk4VWAK_2BkKCeZveySMP-O4PEoQfYTDmTc43nil9ksVKdBbtjha8XoHf9IM3jX4muXXrghlTB1ynkGXtvvozB0KwNmbgyj4eRnWnqw9peWqxRMZABj9JrK1kGGYFE9ZvnnwFKE67_AycxmfGPepkMzeZRhMMdHIqfvkKvWynmy5cuIO9h5ADgGohU12Vowu8rLaJRkbKPfH6gQ4_Q_b4LcYZMJ-rcqfVG1OQcSr_ujL_DZzEjFp-IYaf1LCgKV1iOnYgqOmAJGR_13pU9VCijQSDh79NSgmFe4qQMk_5WqnwvHUR8REejvtnBPS5P8r_EGHO6s8NSbiZkeL0qppSdtgiFmgBy_ZGi8jhdN-fVDd83VaQY8ef1O5eTySVcSmW0dxyY3Sqj8i7trMEFXI9eRlPiZ1nK0OxpZqpmOGiwQnE2uqyO_8xstDdI2m0DcMa_r2anpgCGhtHBVExrtsEmGMDPaVxPwD8Qs1IDpKUaRLPs84aDwdWDnNMQBenOknIfgHP8ejUs-y2qzb9tZSKxbvFvtr0T6pucy8PVGK2zF3eN9M-pwvOXczWfWgQZaHdOroAkVuQuorKf0O1vSOMIBtng4-EHqeOqJ6NTSJXSP4HoK6FQCvU0iwrmNJr7xy8cZjmSZUQH_Atw=w472-h370-no)

![](https://lh3.googleusercontent.com/QeJ8_gS_vmSckQ2ZBuxvGNdT9uxHebwZyh364rR8FHZ3sgE6eujNlqYSh17tU7QitzIPzth_RtqV2tyLFnoq-_BQtpi-LL50eNbTqHphKlMxQh5xG7rPd_EwH4cyoz_E0b2d1iYBURK02n_uLU5wlgHnf62ou8vlJuOPQXtkhGTOSa2TI4yjJbd28SVJ9JxTYWnV6MSzD_9VzrmoQDelTw3cnSCSzI3w94WWsd0tdGuGCbkNClzOpsxJSL6FHArSmO0beChDl-OvW2VGb8FCRbK30v3fLIJdXdgtJOiRbj6-hFC5SGCcVW9Sl_4dpx19-k78MQryEiURxKDorgoJwIzx-rDmAOLA_yscJKjS09nMSgHunlyVPAX6uvgaD5XaH1d49AoArGhDe0gp_JlY-2R4cOoyf05p1gS2exxl2WN_YjQ18eQatBh1Kr0gq6whNqvlVUHdA9xzFtyvHaBxEOGZb02GhRgDr3waGkKuwcUT5rXbsAb-g7wEMcu_-M2-uvc2-xJC-Ya-GvYkIIDyLPCFltUy-54OE1YJKopCNo_U1ZUNYBXD7HEawd_BlMqZDU1SfFigiU7SKT6F3-95CtO8Ul1ZaK-Am4Y03IMSJgaR_VIJ0CwyDIB3LTVVD6KnSq8SJzUlLMHFDE7K68w72KpnWXfQkEypGe7THrEvAA=w1366-h584-no)



`by RJSC`





### Single energy monitor with current direction detection (Xtreme edition)

Warning: this is a compact frugal build with no isolation between the ESP8266 and the mains!

![](https://lh3.googleusercontent.com/zfVH0FW_7isSsE43hgIIo6f_JBsGgUXJCjxrxWLMo9KzeSGNXmJbXRO4RChQ1zv0pUpSGDVIzW3gx8e_N2TZf6j66NkIwnR4qVug30acyMBYPGMEUF1ar9Ci0hbgLZ6fg5D2MRU_DF9y-MaG_llzDVRl19ps4LB46WDk1M-UUd5KvY436vjlVwYPYPaIKdk6fVHm2JZNhST9ZDNntbOlfEtbIdEvYicy2oHPAQBEfSaMjf9eGmu25gXo_WEGvkmHto9O9tMzB-TmMHatnd_2SCe8ZILOp2jdOkt3AIDxnhF2Xb6QTZ9538DBG6-JK5r3Pj7W8y25ymSas8aMmABAn2mtC8qbI9IXEoxzgIZ01dNfGc_22I8cCs6Scq-ZH4vGY28awb01GOqBUb0_C8xYjLLskUdqw5QaWXRqiIe4m9nBR04XnIN_FyvXmSFc6X2uNwnQp21m0dHTebDJ1ISJb16l88E898zaz_DFmGrvJXQa8HM_j5BBrJAwfj72C54Ly0UeeGiI0joAWHoJUN71vnFCPml9xXQVn7KhUEjlkHbc8hlPWdgoo_rE8-hlyoswUdbUfKz5aqinh8MIAkxXFnz8GfJTX1amsAfeV6NM6awHoys6owQIPjQMyfkkpLwHEY2oCZ6SsAuGUQCcAnDiW2FW6TYSEOgv76it26hMAA=w782-h363-no)

![](https://lh3.googleusercontent.com/mMYq36Ngz_BdnH_Tc_D1jCMxPggqqar46_g5UEC1OIMj1TxcqbUo42uABXASkviCf-BxGsrGYiaJRexvZfFzlh4uxsM0jiOeKqV86nZtRlNJdAaXVJ9A_xzYIOi7sIl4dPjXgiQ7eIK_s34soG31cO8FIx1WucoC4XdQtDD6LqEoa31MztCHwKqSXh1vZC9mvCKYtvrktMi5FJ9dldUXNQ-K3EQCmXJZmKoQLEANr3P89PGg8cBoQKim8xPoNjhWIurOA3BCVv3-D5EDZqC7YiTauBQGyCE_h4KnIqDC3D_M-77w9k-ZT2YpFcALUzpNu1H2SWvxAyjUSJWxvgn6kOcKvrfMCKQvV9bKFMbIyTZVFg-z_HMdm3o16JAHdDUw-cCQjGVoffTwtUQ0Jm4nFKi92cez0abz2rxarfsUG1SEMBmXiURlIrtGJlKLA94ia9Q4CYeUi2AaS7yi_XK2MWCiPMD7wENgC_qqVw1b0pzK70quHQyoimmVpBgibCxDQT2Oywa7B-W5sOQsqbjLM17nnv9UvIbubx_NsJX7H1VUQOG1oGqaLCb3TBKlAi0oEOWXnszF2sBfFiof7LYpGz3oRSTs2x6tw_1NKLNkn6CXrKkRxwqK3dMRYJUW7x_gUaikC6cPqSrKLopSko32DVhdX5jrXZVIC-yHzEwtfg=w782-h348-no)

![](https://lh3.googleusercontent.com/v8S4-ADFeqpWfXBl0sVnBg0W3_lTEPHlxwk3R8cSesZJzsmoB7lOYjI1B-CLbNvr1PrIKuEotIOAbISVBfFGEk0c0O7BcypL5m8_0P_t9jv9j6ap1tJ6lvdtuBJJnRN27nkMnagQMKCCn24Xty61UQvvz1Ydtf1lZkHXew7_RbWIPMbhPvYCh8JrGM7wFLaxIT9ZpBPkaAhOe95YMYKozrMRlEunXybv4W4kqYP0oIeCrRw0N8LfbrlfbRklFZUTWak-EAELOwzbn5QDgHVrfmYqlGSnVsWURScK-WXomCyyaP06fCW0k4aQe7iIbTFktYkKDazrOSzSkwUXY5M5TbRZqhiMHDJAeihRkMt_X9o-5FeFC8LDPlmeeZgup66F1FJCcE4RxRwusxnQ86wvwh26Bc6a6BzXtWEaEouoiEU5zNyiU8KdEGrELJ8yDxiinwQEoeCPtI00aeySg9sKn3hi6eCoCkBHDx3SImiZ3aCESdcGHU5fypgerGp84aVUNw5O8cqaUdjhI5_r1jFQMcOEnqivfZ0bygEGSxsR0N5jg3x6hMazJRJLDzw4amDQZmvgcOtSzRy8ERYKPg_gWKJLhne6zT251-uXYRxpulYStXH-mH5XhYkXRJi7ZWfgq0Gfd4cnoAyrr0-j7GDbLDtL8TYLAa39zkB2up9Srw=w503-h398-no)


`by RJSC`



## Donate

Donate if you enjoy the firmware and would like to see this project develop.

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.me/APREBELO)
