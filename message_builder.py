from datetime import date, timedelta

def flex(days, infos):
    num = len(infos)
    contents = [{
        "type": "bubble",
        "size": "kilo",
        "body": 
        {
            "type": "box",
            "layout": "vertical",
            "contents": 
            [
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": 
                    [
                        {
                            "type": "text",
                            "text": "GPSS",
                            "size": "md",
                            "weight": "bold",
                            "color": "#1f69b4",
                            "margin": "md",
                            "offsetStart": "md"
                        },
                        {
                            "type": "text",
                            "text": "Weekly Update",
                            "size": "xxl",
                            "weight": "bold",
                            "margin": "md",
                            "offsetStart": "md"
                        },
                        {
                            "type": "text",
                            "text": f"updated since {date.today() - timedelta(days=days)}",
                            "offsetStart": "md",
                            "size": "xs",
                            "color": "#8c8c8c"
                        }
                    ],
                    "margin": "xxl"
                },
                {
                    "type": "separator",
                    "margin": "xxl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": 
                    [
                        {
                            "type": "text",
                            "text": f"This update announced a total of {num} patents.",
                            "wrap": True
                        },
                        {
                            "type": "text",
                            "text": f"{min(11, num)} of them you may be interested in are shown. ",
                            "wrap": True
                        }
                    ] 
                    if num > 0 else 
                    [
                        {
                            "type": "text",
                            "text": "No patent annouced since last update.",
                            "wrap": True
                        }
                    ],
                    "margin": "xxl",
                    "spacing": "sm",
                    "paddingAll": "md"
                },
                {
                    "type": "separator",
                    "margin": "xxl"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": 
                    [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": 
                            [
                                {
                                    "type": "text",
                                    "text": "Show All New Updates",
                                    "margin": "md",
                                    "gravity": "top",
                                    "align": "center",
                                    "weight": "bold",
                                    "size": "sm"
                                }
                            ],
                            "borderColor": "#6F8FAF",
                            "borderWidth": "2px",
                            "cornerRadius": "md",
                            "margin": "xl",
                            "height": "40px",
                            "action": {
                                "type": "postback",
                                "label": "action",
                                "data": f"action=show_all&days={days}",
                                "displayText": "Show all new updates. Please wait."
                            },
                            "alignItems": "center",
                            "position": "relative",
                            "width": "80%"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": 
                            [
                                {
                                    "type": "text",
                                    "text": "Show Eariler Updates",
                                    "margin": "md",
                                    "gravity": "top",
                                    "align": "center",
                                    "weight": "bold",
                                    "size": "sm"
                                }
                            ],
                            "borderColor": "#6F8FAF",
                            "borderWidth": "2px",
                            "cornerRadius": "md",
                            "margin": "xl",
                            "height": "40px",
                            "action": {
                                "type": "postback",
                                "label": "action",
                                "data": f"action=show_early&days={days}",
                                "displayText": "Show earlier updates. Please wait."
                            },
                            "alignItems": "center",
                            "position": "relative",
                            "width": "80%"
                        }
                    ],
                    "margin": "xxl",
                    "spacing": "md",
                    "alignItems": "center",
                    "justifyContent": "center"
                }
            ]
        }
    }]
    for info in infos if num <= 11 else infos[:11]:
        contents.append({
            "type": "bubble",
            "size": "kilo",
            "hero": 
            {
                "type": "image",
                "url": info["image"],
                "size": "full",
                "aspectMode": "cover",
                "aspectRatio": "320:213"
            },
            "body": 
            {
                "type": "box",
                "layout": "vertical",
                "contents": 
                [
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": 
                        [
                            {
                                "type": "text",
                                "text": info["date"],
                                "align": "end",
                                "color": "#8c8c8c",
                                "size": "xs"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": 
                        [
                            {
                                "type": "text",
                                "text": info["title"],
                                "wrap": True,
                                "weight": "bold",
                                "size": "sm",
                                "flex": 5,
                                "maxLines": 5
                            }
                        ],
                        "height": "90px"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": 
                        [
                            {
                                "type": "text",
                                "text": info["content"],
                                "wrap": True,
                                "color": "#8c8c8c",
                                "size": "xs",
                                "flex": 5,
                                "maxLines": 12
                            }
                        ],
                        "height": "200px",
                    },
                    {
                        "type": "button",
                        "action": 
                        {
                            "type": "uri",
                            "label": "前往",
                            "uri": info["url"],
                            # "uri": "https://www.google.com.tw/",
                        },
                        "style": "link"
                    }
                ],
                "spacing": "sm",
                "paddingAll": "13px"
            }
        })
    return {
        "type": "carousel",
        "contents": contents
    }