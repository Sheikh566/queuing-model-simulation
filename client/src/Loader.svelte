<script>

</script>

<div id="ui">
  <div class="dice">
      <ol class="dice_list">
          <li class="dice_list_item"></li>
          <li class="dice_list_item"></li>
          <li class="dice_list_item"></li>
          <li class="dice_list_item"></li>
          <li class="dice_list_item"></li>
          <li class="dice_list_item"></li>
      </ol>
  </div>
  <div class="dice">
      <ol class="dice_list">
          <li class="dice_list_item"></li>
          <li class="dice_list_item"></li>
          <li class="dice_list_item"></li>
          <li class="dice_list_item"></li>
          <li class="dice_list_item"></li>
          <li class="dice_list_item"></li>
      </ol>
  </div>
  <div class="dice">
      <ol class="dice_list">
          <li class="dice_list_item"></li>
          <li class="dice_list_item"></li>
          <li class="dice_list_item"></li>
          <li class="dice_list_item"></li>
          <li class="dice_list_item"></li>
          <li class="dice_list_item"></li>
      </ol>
  </div>
</div>

<style>
li {
	 list-style-type: none;
}
 ol {
	 margin: 0;
	 padding: 0;
}
 #ui {
	 position: absolute;
	 top: 60%;
	 left: 50%;
	 perspective: 600px;
}
 #ui .dice {
	 transform-style: preserve-3d;
}
 #ui .dice:nth-child(1) {
	 animation: rotate1 20000ms linear infinite;
}
 #ui .dice:nth-child(2) {
	 animation: rotate2 20000ms linear infinite;
}
 #ui .dice:nth-child(3) {
	 animation: rotate3 20000ms linear infinite;
}
 #ui .dice_list {
	 transform-style: preserve-3d;
	 transform: translateY(-75px) translateX(-75px);
}
 #ui .dice_list_item {
	 position: absolute;
	 width: 150px;
	 height: 150px;
	 border: 1px solid rgba(255, 255, 255, 0.6);
}
 #ui .dice_list_item:nth-child(1) {
	 background: rgba(121, 187, 7, 0.5);
	 animation: child1 3000ms ease-in-out infinite alternate;
}
 @keyframes child1 {
	 0% {
		 transform: translateZ(75px);
	}
	 100% {
		 transform: translateZ(-75px);
	}
}
 #ui .dice_list_item:nth-child(2) {
	 background: rgba(250, 167, 64, 0.5);
	 animation: child2 3000ms ease-in-out infinite alternate;
}
 @keyframes child2 {
	 0% {
		 transform: translateY(75px) rotateX(270deg);
	}
	 100% {
		 transform: translateY(-75px) rotateX(270deg);
	}
}
 #ui .dice_list_item:nth-child(3) {
	 background: rgba(79, 255, 123, 0.5);
	 animation: child3 3000ms ease-in-out infinite alternate;
}
 @keyframes child3 {
	 0% {
		 transform: translateX(75px) rotateY(-270deg);
	}
	 100% {
		 transform: translateX(-75px) rotateY(-270deg);
	}
}
 #ui .dice_list_item:nth-child(4) {
	 background: rgba(217, 52, 187, 0.5);
	 animation: child4 3000ms ease-in-out infinite alternate;
}
 @keyframes child4 {
	 0% {
		 transform: translateX(-75px) rotateY(-90deg);
	}
	 100% {
		 transform: translateX(75px) rotateY(-90deg);
	}
}
 #ui .dice_list_item:nth-child(5) {
	 background: rgba(158, 205, 93, 0.5);
	 animation: child5 3000ms ease-in-out infinite alternate;
}
 @keyframes child5 {
	 0% {
		 transform: translateY(-75px) rotateX(90deg);
	}
	 100% {
		 transform: translateY(75px) rotateX(90deg);
	}
}
 #ui .dice_list_item:nth-child(6) {
	 background: rgba(83, 77, 95, 0.5);
	 animation: child6 3000ms ease-in-out infinite alternate;
}
 @keyframes child6 {
	 0% {
		 transform: translateZ(-75px) rotateY(180deg);
	}
	 100% {
		 transform: translateZ(75px) rotateY(180deg);
	}
}
 @keyframes rotate1 {
	 0% {
		 transform: rotateX(0deg) rotateY(0deg);
	}
	 100% {
		 transform: rotateX(360deg) rotateY(1080deg);
	}
}
 @keyframes rotate2 {
	 0% {
		 transform: rotateX(0deg) rotateY(0deg) scale3d(0.7, 0.7, 0.7);
	}
	 100% {
		 transform: rotateX(360deg) rotateY(1080deg) scale3d(0.7, 0.7, 0.7);
	}
}
 @keyframes rotate3 {
	 0% {
		 transform: rotateX(0deg) rotateY(0deg) scale3d(0.4, 0.4, 0.4);
	}
	 100% {
		 transform: rotateX(360deg) rotateY(1080deg) scale3d(0.4, 0.4, 0.4);
	}
}
 
</style>