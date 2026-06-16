/* =====================================================================
   ACE7 SPICES — interactions
   ===================================================================== */
(function(){
  "use strict";

  /* ---------- header scroll state ---------- */
  var header=document.querySelector(".header");
  function onScroll(){ if(!header)return; header.classList.toggle("scrolled", window.scrollY>30); }
  window.addEventListener("scroll", onScroll, {passive:true}); onScroll();

  /* ---------- mobile drawer ---------- */
  var burger=document.querySelector(".burger");
  var drawer=document.querySelector(".drawer");
  if(burger&&drawer){
    burger.addEventListener("click",function(){
      var open=drawer.classList.toggle("open");
      burger.classList.toggle("open",open);
      burger.setAttribute("aria-expanded",open);
      document.body.style.overflow=open?"hidden":"";
    });
    drawer.querySelectorAll("a").forEach(function(a){
      a.addEventListener("click",function(){
        drawer.classList.remove("open");burger.classList.remove("open");
        document.body.style.overflow="";
      });
    });
  }

  /* ---------- scroll reveal ---------- */
  var reveals=document.querySelectorAll(".reveal");
  if("IntersectionObserver" in window && reveals.length){
    var io=new IntersectionObserver(function(entries){
      entries.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add("in"); io.unobserve(e.target); } });
    },{threshold:0.12,rootMargin:"0px 0px -8% 0px"});
    reveals.forEach(function(el){io.observe(el);});
  } else { reveals.forEach(function(el){el.classList.add("in");}); }

  /* ---------- count-up stats ---------- */
  var counters=document.querySelectorAll("[data-count]");
  if("IntersectionObserver" in window && counters.length){
    var co=new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(!e.isIntersecting)return;
        var el=e.target, target=parseFloat(el.getAttribute("data-count")),
            suffix=el.getAttribute("data-suffix")||"", dec=(target%1!==0)?1:0,
            start=null, dur=1400;
        function step(ts){
          if(!start)start=ts;
          var p=Math.min((ts-start)/dur,1), val=(target*(0.2+0.8*p));
          el.textContent=(p<1?val:target).toFixed(dec)+suffix;
          if(p<1)requestAnimationFrame(step);
        }
        requestAnimationFrame(step); co.unobserve(el);
      });
    },{threshold:0.5});
    counters.forEach(function(el){co.observe(el);});
  }

  /* ---------- image placeholder fallback ----------
     real <img> tags swap to a labelled placeholder if the file isn't present yet */
  document.querySelectorAll("img[data-ph]").forEach(function(img){
    function fallback(){
      if(img.dataset.failed)return; img.dataset.failed="1";
      var d=document.createElement("div");
      d.className="ph "+(img.getAttribute("data-ph-class")||"");
      d.innerHTML='<div class="ph__tag"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>'+
        '<span class="n">'+(img.getAttribute("data-ph")||img.alt)+'</span>'+
        '<span class="d">'+ (img.getAttribute("src")||"") +'</span></div>';
      if(img.parentNode)img.parentNode.replaceChild(d,img);
    }
    img.addEventListener("error",fallback);
    if(img.complete && img.naturalWidth===0) fallback();
  });

  /* ---------- tabs ---------- */
  document.querySelectorAll("[data-tabs]").forEach(function(group){
    var tabs=group.querySelectorAll(".tab");
    var panels=group.querySelectorAll(".tabpanel");
    tabs.forEach(function(tab){
      tab.addEventListener("click",function(){
        var t=tab.getAttribute("data-tab");
        tabs.forEach(function(x){x.classList.toggle("active",x===tab);});
        panels.forEach(function(p){p.classList.toggle("active",p.getAttribute("data-panel")===t);});
      });
    });
  });

  /* ---------- accordion ---------- */
  document.querySelectorAll(".acc__q").forEach(function(q){
    q.addEventListener("click",function(){
      var acc=q.closest(".acc"), ans=acc.querySelector(".acc__a"),
          open=acc.classList.toggle("open");
      q.setAttribute("aria-expanded",open);
      ans.style.maxHeight=open?ans.scrollHeight+"px":0;
    });
  });

  /* ---------- SHU / ASTA heat scale (red chilli page) ---------- */
  var heat=document.querySelector("[data-heatscale]");
  if(heat){
    var DATA={
      teja:{name:"Teja S17",shuPct:88,shu:"50,000 – 100,000",asta:"32 – 42",use:"Maximum heat · oleoresin · hot sauces"},
      "414":{name:"414 Hybrid",shuPct:55,shu:"30,000 – 50,000",asta:"32 – 42",use:"All-purpose heat + colour"},
      sannam:{name:"334 / S4 Sannam",shuPct:38,shu:"25,000 – 40,000",asta:"32 – 38",use:"Balanced curry & blends"},
      byadgi:{name:"Byadgi (Kaddi)",shuPct:16,shu:"8,000 – 15,000",asta:"60 – 130",use:"Deep colour · low heat · paprika-style"}
    };
    var mark=heat.querySelector(".heatscale__mark"),
        outShu=heat.querySelector("[data-out=shu]"),
        outAsta=heat.querySelector("[data-out=asta]"),
        outUse=heat.querySelector("[data-out=use]"),
        markName=mark.querySelector("b"), markVal=mark.querySelector("span");
    function setHeat(key){
      var d=DATA[key]; if(!d)return;
      mark.style.left=d.shuPct+"%";
      markName.textContent=d.name; markVal.textContent="~"+d.shu.split(" – ")[1]+" SHU max";
      outShu.textContent=d.shu; outAsta.textContent=d.asta; outUse.textContent=d.use;
      heat.querySelectorAll(".heatpicker button").forEach(function(b){
        b.classList.toggle("active",b.getAttribute("data-heat")===key);
      });
    }
    heat.querySelectorAll(".heatpicker button").forEach(function(b){
      b.addEventListener("click",function(){setHeat(b.getAttribute("data-heat"));});
    });
    setHeat("sannam");
  }

  /* ---------- harvest calendar ---------- */
  var cal=document.querySelector("[data-calendar]");
  if(cal){
    /* phase per crop per month index 0..11 (Jan..Dec); {phase, peak, label, note, specs} */
    var CAL={
      "Red Chilli — Guntur, AP":{
        color:"#C8102E",
        months:[
          {p:"harvest",peak:false}, {p:"harvest",peak:true}, {p:"harvest",peak:true}, {p:"process"},
          {p:"process"}, {p:"sow"}, {p:"sow"}, {p:"grow"},
          {p:"grow"}, {p:"grow"}, {p:"grow"}, {p:"harvest"}
        ],
        notes:{
          sow:{t:"Nursery & transplanting",n:"Seedlings raised in nurseries through the monsoon, then transplanted to the field across the Guntur belt as the rains ease.",s:[["Window","Jun – Jul"],["Crop type","Kharif / irrigated"]]},
          grow:{t:"Vegetative growth & flowering",n:"Plants build canopy, flower and set fruit. Green chillies form and begin colouring on the plant under the dry winter sun.",s:[["Window","Aug – Nov"],["Stage","Flower → fruit set"]]},
          harvest:{t:"Red-ripe harvest & picking",n:"Fully-ripened red chillies are hand-picked in successive rounds. Peak arrivals hit the Guntur Mirchi Yard — Asia's largest chilli market — in February–March.",s:[["Window","Dec – Mar"],["Peak","Feb – Mar"],["Method","Hand-picked, sun-dried"]]},
          process:{t:"Sorting, cold-milling & lab release",n:"Dried lots are colour- and defect-sorted, cold-press milled to spec, then lab-tested for SHU, ASTA, moisture, pesticide & aflatoxin before dispatch.",s:[["Window","Feb – Apr"],["Tested for","SHU · ASTA · AFL"]]}
        }
      },
      "Coriander — Rajasthan":{
        color:"#8FA31E",
        months:[
          {p:"grow"}, {p:"harvest",peak:true}, {p:"harvest",peak:true}, {p:"process"},
          {p:"process"}, {p:"none"}, {p:"none"}, {p:"none"},
          {p:"none"}, {p:"sow"}, {p:"sow"}, {p:"grow"}
        ],
        notes:{
          sow:{t:"Sowing (rabi crop)",n:"Coriander is sown across Rajasthan's Hadoti belt as the post-monsoon soil cools — the dry days and cool nights that concentrate the seed's essential oils.",s:[["Window","Oct – Nov"],["Crop type","Rabi / winter"]]},
          grow:{t:"Vegetative growth & flowering",n:"Plants develop foliage and flower through the cool winter, setting the bold, green-toned seed Rajasthan is known for.",s:[["Window","Dec – Jan"],["Stage","Flower → seed set"]]},
          harvest:{t:"Seed harvest",n:"Mature seed is harvested and threshed; arrivals build at Ramganj Mandi — among the world's largest coriander markets — through March–April.",s:[["Window","Feb – Mar"],["Peak","Mar"],["Grade","Eagle · Single · Scooter"]]},
          process:{t:"Cleaning, milling & lab release",n:"Seed is machine-cleaned to ≥99% purity, cold-press milled for powder, and lab-tested for volatile oil, moisture & admixture before dispatch.",s:[["Window","Mar – Apr"],["Tested for","Vol. oil · purity"]]}
        }
      },
      "Turmeric — Sangli & Salem":{
        color:"#D98E04",
        months:[
          {p:"harvest"}, {p:"harvest",peak:true}, {p:"harvest",peak:true}, {p:"process"},
          {p:"process"}, {p:"sow"}, {p:"sow"}, {p:"grow"},
          {p:"grow"}, {p:"grow"}, {p:"grow"}, {p:"grow"}
        ],
        notes:{
          sow:{t:"Planting (long-duration crop)",n:"Rhizomes are planted with the onset of the monsoon across the Sangli (Maharashtra) and Salem/Erode (Tamil Nadu) belts for an 8–9 month cycle.",s:[["Window","May – Jul"],["Cycle","~8–9 months"]]},
          grow:{t:"Rhizome development",n:"Underground rhizomes bulk up through the monsoon and post-monsoon months, building the curcumin that defines high-grade Indian turmeric.",s:[["Window","Aug – Dec"],["Builds","Curcumin %"]]},
          harvest:{t:"Digging & curing",n:"Mature turmeric is dug, boiled, sun-dried and polished. Sangli is one of Asia's largest turmeric trading hubs; Salem turmeric is prized for high curcumin.",s:[["Window","Jan – Mar"],["Peak","Feb – Mar"],["Cure","Boiled · dried · polished"]]},
          process:{t:"Grading, milling & lab release",n:"Cured fingers are graded, cold-press milled, and lab-tested for curcumin %, colour value and — critically — screened lead-chromate-free before dispatch.",s:[["Window","Feb – Apr"],["Tested for","Curcumin · Pb-free"]]}
        }
      }
    };
    var MONTHS=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"];
    var grid=cal.querySelector(".cal__grid");
    var detail=cal.querySelector(".cal__detail");
    var html='<div></div>';
    MONTHS.forEach(function(m){html+='<div class="cal__head">'+m+'</div>';});
    Object.keys(CAL).forEach(function(crop){
      var c=CAL[crop];
      html+='<div class="cal__crop"><i style="background:'+c.color+'"></i>'+crop+'</div>';
      c.months.forEach(function(cell,i){
        var cls=(cell.p&&cell.p!=="none")?(" "+cell.p):"";
        var peak=cell.peak?" peak":"";
        var dataPhase=(cell.p&&cell.p!=="none")?(' data-phase="'+cell.p+'" data-crop="'+crop+'" tabindex="0" role="button" aria-label="'+crop+', '+MONTHS[i]+'"'):"";
        html+='<div class="cal__cell'+cls+peak+'"'+dataPhase+'></div>';
      });
    });
    grid.innerHTML=html;

    function showDetail(crop,phase){
      var c=CAL[crop]; if(!c||!c.notes[phase])return;
      var n=c.notes[phase];
      var specs=n.s.map(function(s){return '<div><span>'+s[0]+'</span><b>'+s[1]+'</b></div>';}).join("");
      detail.innerHTML='<h4>'+n.t+'</h4><div class="ph-name" style="color:'+c.color+'">'+crop+'</div><p>'+n.n+'</p><div class="specs">'+specs+'</div>';
      detail.classList.add("show");
    }
    grid.querySelectorAll(".cal__cell[data-phase]").forEach(function(cell){
      function go(){ showDetail(cell.getAttribute("data-crop"),cell.getAttribute("data-phase")); }
      cell.addEventListener("click",go);
      cell.addEventListener("keydown",function(e){if(e.key==="Enter"||e.key===" "){e.preventDefault();go();}});
    });
    /* default open */
    showDetail("Red Chilli — Guntur, AP","harvest");
  }

  /* ---------- check items (inquiry form) ---------- */
  document.querySelectorAll(".checkitem").forEach(function(item){
    var input=item.querySelector("input");
    function sync(){item.classList.toggle("checked",input.checked);}
    input.addEventListener("change",sync);sync();
  });

  /* ---------- inquiry form (demo handler) ---------- */
  var form=document.querySelector("[data-inquiry]");
  if(form){
    form.addEventListener("submit",function(e){
      e.preventDefault();
      var success=document.querySelector(".form-success");
      // Build a structured mailto as a no-backend fallback
      var fd=new FormData(form);
      var lines=[];
      fd.forEach(function(v,k){ if(v) lines.push(k+": "+v); });
      var products=[];
      form.querySelectorAll(".checkitem input:checked").forEach(function(c){products.push(c.value);});
      if(products.length)lines.push("Products of interest: "+products.join(", "));
      var body=encodeURIComponent("New B2B inquiry via ace7spices.com\n\n"+lines.join("\n"));
      var subject=encodeURIComponent("Trade inquiry — "+(fd.get("company")||"new buyer"));
      form.style.display="none";
      if(success){
        success.classList.add("show");
        success.scrollIntoView({behavior:"smooth",block:"center"});
        var mailBtn=success.querySelector("[data-mailto]");
        if(mailBtn)mailBtn.setAttribute("href","mailto:support@ace7spices.com?subject="+subject+"&body="+body);
      }
    });
  }

  /* ---------- footer year ---------- */
  var yr=document.querySelector("[data-year]"); if(yr)yr.textContent=new Date().getFullYear();

})();
