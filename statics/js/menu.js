<script>
	function showLeftMenu(){
		var circleBtObj = document.getElementById('circleBt');
		var leftMenuObj = document.getElementById('hideMenuBodyId');
		circleBtObj.style['display'] = "none";
		leftMenuObj.style['transform'] = "translate(0px, 0px)";

		leftMenuObj.style['msTransform'] = "translate(0px, 0px)";
		leftMenuObj.style['mozTransform'] = "translate(0px, 0px)";
		leftMenuObj.style['webkitTransform'] = "translate(0px, 0px)";
		leftMenuObj.style['oTransform'] = "translate(0px, 0px)";
	}

	function closeLeftMenu() {
		var circleBtObj = document.getElementById('circleBt');
		var leftMenuObj = document.getElementById('hideMenuBodyId');

		circleBtObj.style['display'] = "block";
		leftMenuObj.removeAttribute("style");
	}
</script>